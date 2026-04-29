"""Promote CT-log candidates to inferred-disposable based on cluster overlap.

Inference rule:
    A cluster (MX host or IP) is "high-confidence disposable" if:
        - disposable_count >= MIN_DISPOSABLE  (default 5)
        - is_shared_infra = 0                  (not on the curated denylist)

    A candidate domain is promoted to domains_inferred.txt if:
        - It has a resolution entry (MX_OK or A_ONLY)
        - At least one of its MX hosts OR IPs belongs to a
          high-confidence disposable cluster.
        - It is not already on domains.txt / domains_strict.txt.

Run order in the nightly pipeline:
    resolve_domains.py                                # upstream
    fetch_ct_candidates.py                            # CT logs -> candidates.txt
    resolve_domains.py --domains data/candidates.txt  # resolve candidates
    build_clusters.py                                 # build cluster tables
    infer_candidates.py                               # this script
"""
from __future__ import annotations

import argparse
import json
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_DB = ROOT / "disposable_email" / "data" / "resolution.sqlite"
DEFAULT_CANDIDATES = ROOT / "disposable_email" / "data" / "candidates.txt"
DEFAULT_DOMAINS = ROOT / "disposable_email" / "domains.txt"
DEFAULT_STRICT = ROOT / "disposable_email" / "domains_strict.txt"
DEFAULT_INFERRED = ROOT / "disposable_email" / "domains_inferred.txt"


def load_lines(path: Path) -> set[str]:
    if not path.exists():
        return set()
    out: set[str] = set()
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip().lower()
        if line and not line.startswith("#"):
            out.add(line)
    return out


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--db", type=Path, default=DEFAULT_DB)
    parser.add_argument("--candidates", type=Path, default=DEFAULT_CANDIDATES)
    parser.add_argument("--domains", type=Path, default=DEFAULT_DOMAINS)
    parser.add_argument("--domains-strict", type=Path, default=DEFAULT_STRICT)
    parser.add_argument("--out", type=Path, default=DEFAULT_INFERRED)
    parser.add_argument("--min-disposable", type=int, default=5,
                        help="Min disposables per cluster to call it 'disposable infra'")
    args = parser.parse_args()

    if not args.db.exists():
        print(f"ERROR: {args.db} not found.", file=sys.stderr)
        return 1
    if not args.candidates.exists():
        print(f"No candidates file at {args.candidates} — nothing to infer.", file=sys.stderr)
        # Still write an empty (or unchanged) inferred file so downstream tooling has it.
        if not args.out.exists():
            args.out.write_text(_header(0), encoding="utf-8")
        return 0

    candidates = load_lines(args.candidates)
    excluded = load_lines(args.domains) | load_lines(args.domains_strict)

    conn = sqlite3.connect(str(args.db))

    # Verify cluster tables exist
    cluster_tables = {
        r[0] for r in conn.execute(
            "SELECT name FROM sqlite_master WHERE type='table'"
        ).fetchall()
    }
    if "mx_cluster" not in cluster_tables or "ip_cluster" not in cluster_tables:
        print("ERROR: cluster tables missing. Run build_clusters.py first.", file=sys.stderr)
        return 1

    high_mx = {
        row[0] for row in conn.execute(
            "SELECT mx_host FROM mx_cluster"
            " WHERE disposable_count >= ? AND is_shared_infra = 0",
            (args.min_disposable,),
        )
    }
    high_ip = {
        row[0] for row in conn.execute(
            "SELECT ip FROM ip_cluster"
            " WHERE disposable_count >= ? AND is_shared_infra = 0",
            (args.min_disposable,),
        )
    }
    print(f"High-confidence disposable MX hosts: {len(high_mx)}", file=sys.stderr)
    print(f"High-confidence disposable IPs:      {len(high_ip)}", file=sys.stderr)

    # For each candidate, fetch its resolution and check overlap.
    promoted: list[tuple[str, str]] = []  # (domain, reason)
    placeholders = ",".join(["?"] * len(candidates)) if candidates else None
    rows = []
    if placeholders:
        rows = conn.execute(
            f"SELECT domain, mx_hosts, ips FROM domain_resolution"
            f" WHERE domain IN ({placeholders})",
            tuple(candidates),
        ).fetchall()

    for domain, mx_json, ips_json in rows:
        if domain in excluded:
            continue
        mx_hosts = set(json.loads(mx_json) if mx_json else [])
        ips = set(json.loads(ips_json) if ips_json else [])
        mx_hits = mx_hosts & high_mx
        ip_hits = ips & high_ip
        if mx_hits:
            reason = f"shared MX with disposables: {sorted(mx_hits)[0]}"
            promoted.append((domain, reason))
        elif ip_hits:
            reason = f"shared IP with disposables: {sorted(ip_hits)[0]}"
            promoted.append((domain, reason))

    promoted.sort()
    body = _header(len(promoted))
    for domain, reason in promoted:
        body += f"{domain}\n"

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(body, encoding="utf-8")

    print(f"\nPromoted {len(promoted)} candidates to {args.out}", file=sys.stderr)
    if promoted[:10]:
        print("First 10 promotions:", file=sys.stderr)
        for d, r in promoted[:10]:
            print(f"  {d}  ({r})", file=sys.stderr)

    conn.close()
    return 0


def _header(count: int) -> str:
    return (
        "# Inferred disposable email domains.\n"
        "#\n"
        "# These domains were NOT on the upstream disposable list, but their\n"
        "# mail infrastructure (MX host or IP) is shared with at least 5\n"
        "# already-known disposable services AND is not on the shared-infra\n"
        "# allowlist (Cloudflare Email Routing, Google Workspace, etc.).\n"
        "#\n"
        "# Source: scripts/infer_candidates.py\n"
        f"# Last updated: {datetime.now(timezone.utc).isoformat(timespec='seconds')}\n"
        f"# Count: {count}\n"
        "#\n"
        "# Use via:  is_disposable(\"x@example.com\", inferred=True)\n"
        "\n"
    )


if __name__ == "__main__":
    sys.exit(main())
