"""Render docs/statistics.md from the resolution + cluster data.

Reads the SQLite produced by resolve_domains.py and build_clusters.py, plus the
bundled disposable lists, and emits a human-readable Markdown report.
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
DEFAULT_DOMAINS = ROOT / "disposable_email" / "domains.txt"
DEFAULT_STRICT = ROOT / "disposable_email" / "domains_strict.txt"
DEFAULT_INFERRED = ROOT / "disposable_email" / "domains_inferred.txt"
DEFAULT_OUT = ROOT / "docs" / "statistics.md"

TOP_N = 20


def load_lines(path: Path) -> set[str]:
    if not path.exists():
        return set()
    out: set[str] = set()
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip().lower()
        if line and not line.startswith("#"):
            out.add(line)
    return out


def pct(n: int, total: int) -> str:
    if not total:
        return "0%"
    return f"{n / total * 100:.1f}%"


def md_table(headers: list[str], rows: list[list[str]]) -> str:
    out = "| " + " | ".join(headers) + " |\n"
    out += "|" + "|".join(["---"] * len(headers)) + "|\n"
    for row in rows:
        out += "| " + " | ".join(str(c) for c in row) + " |\n"
    return out


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--db", type=Path, default=DEFAULT_DB)
    parser.add_argument("--domains", type=Path, default=DEFAULT_DOMAINS)
    parser.add_argument("--domains-strict", type=Path, default=DEFAULT_STRICT)
    parser.add_argument("--inferred", type=Path, default=DEFAULT_INFERRED)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()

    if not args.db.exists():
        print(f"ERROR: {args.db} not found.", file=sys.stderr)
        return 1

    disposable_set = load_lines(args.domains)
    strict_set = load_lines(args.domains_strict)
    inferred_set = load_lines(args.inferred)

    conn = sqlite3.connect(str(args.db))

    # === Reachability ===
    status_rows = conn.execute(
        "SELECT status, COUNT(*) FROM domain_resolution GROUP BY status"
    ).fetchall()
    status_counts = dict(status_rows)
    total_resolved = sum(status_counts.values())
    reachable = status_counts.get("MX_OK", 0) + status_counts.get("A_ONLY", 0)

    last_resolution = conn.execute(
        "SELECT MAX(resolved_at) FROM domain_resolution"
    ).fetchone()[0] or "n/a"

    # === Top disposable MX hosts ===
    top_mx = conn.execute(
        "SELECT mx_host, disposable_count, domain_count, is_shared_infra"
        " FROM mx_cluster"
        " WHERE disposable_count > 0"
        " ORDER BY disposable_count DESC, mx_host"
        " LIMIT ?",
        (TOP_N,),
    ).fetchall()

    top_mx_excluding_shared = conn.execute(
        "SELECT mx_host, disposable_count, domain_count"
        " FROM mx_cluster"
        " WHERE disposable_count > 0 AND is_shared_infra = 0"
        " ORDER BY disposable_count DESC, mx_host"
        " LIMIT ?",
        (TOP_N,),
    ).fetchall()

    top_ips = conn.execute(
        "SELECT ip, disposable_count, domain_count"
        " FROM ip_cluster"
        " WHERE disposable_count > 0"
        " ORDER BY disposable_count DESC, ip"
        " LIMIT ?",
        (TOP_N,),
    ).fetchall()

    # === Phase 3b: upstream domains whose only MX is on the shared-infra denylist ===
    suspect_rows = conn.execute(
        "SELECT dr.domain, dr.mx_hosts FROM domain_resolution dr"
        " WHERE dr.status = 'MX_OK' AND dr.mx_hosts IS NOT NULL"
    ).fetchall()
    shared_mx: set[str] = {
        r[0] for r in conn.execute(
            "SELECT mx_host FROM mx_cluster WHERE is_shared_infra = 1"
        )
    }
    upstream_on_shared = []
    for domain, mx_json in suspect_rows:
        if domain not in disposable_set:
            continue
        mx_hosts = json.loads(mx_json) if mx_json else []
        if mx_hosts and all(h in shared_mx for h in mx_hosts):
            upstream_on_shared.append((domain, mx_hosts[0]))
    upstream_on_shared.sort()

    # === Inferred candidates summary ===
    high_mx_count = conn.execute(
        "SELECT COUNT(*) FROM mx_cluster"
        " WHERE disposable_count >= 5 AND is_shared_infra = 0"
    ).fetchone()[0]
    high_ip_count = conn.execute(
        "SELECT COUNT(*) FROM ip_cluster"
        " WHERE disposable_count >= 5 AND is_shared_infra = 0"
    ).fetchone()[0]

    # === Render ===
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    md = []
    md.append("# Disposable Email Infrastructure — Statistics\n")
    md.append(f"*Generated automatically. Last build: **{now}**.*  ")
    md.append(f"*Last DNS snapshot: **{last_resolution}**.*\n")
    md.append("This document is regenerated nightly from the bundled "
              "[`resolution.sqlite`](../disposable_email/data/) snapshot.")
    md.append("It captures the live mail infrastructure of the disposable email domains "
              "shipped with this package.\n")

    md.append("## Domain list sizes\n")
    md.append(md_table(
        ["List", "Domains"],
        [
            ["`domains.txt` (default)", f"{len(disposable_set):,}"],
            ["`domains_strict.txt`", f"{len(strict_set):,}"],
            ["`domains_inferred.txt` (opt-in)", f"{len(inferred_set):,}"],
        ],
    ))

    md.append("## Reachability\n")
    md.append(f"Of **{total_resolved:,}** resolved domains:\n")
    rows = []
    for status in ("MX_OK", "A_ONLY", "NXDOMAIN", "NO_RECORDS", "TIMEOUT", "OTHER", "SERVFAIL"):
        c = status_counts.get(status, 0)
        if c:
            rows.append([status, f"{c:,}", pct(c, total_resolved)])
    md.append(md_table(["Status", "Count", "% of resolved"], rows))
    md.append(
        f"**{reachable:,} domains are mail-reachable today** "
        f"({pct(reachable, total_resolved)}). The remainder are historical: domains "
        f"that no longer resolve (NXDOMAIN) but are kept on the list because disposable "
        f"operators frequently re-register such names.\n"
    )

    md.append("## Top disposable mail backends (MX hosts)\n")
    md.append(f"Including shared infrastructure (Cloudflare/Google/etc.):\n")
    rows = [
        [f"`{host}`", str(disp), str(total), "yes" if shared else ""]
        for host, disp, total, shared in top_mx
    ]
    md.append(md_table(["MX host", "Disposable domains", "Total resolved", "Shared infra"], rows))

    md.append("\nWith shared infrastructure excluded (these are the *true* disposable "
              "mail backends):\n")
    rows = [
        [f"`{host}`", str(disp), str(total)]
        for host, disp, total in top_mx_excluding_shared
    ]
    md.append(md_table(["MX host", "Disposable domains", "Total resolved"], rows))

    md.append("\n## Top mail IPs by disposable domain count\n")
    rows = [
        [f"`{ip}`", str(disp), str(total)]
        for ip, disp, total in top_ips
    ]
    md.append(md_table(["IP address", "Disposable domains", "Total resolved"], rows))

    md.append("\n## Inferred candidates pipeline\n")
    md.append(md_table(
        ["Metric", "Value"],
        [
            ["High-confidence disposable MX hosts (≥5 disposables, not shared)", f"{high_mx_count:,}"],
            ["High-confidence disposable IPs", f"{high_ip_count:,}"],
            ["Promoted to `domains_inferred.txt`", f"{len(inferred_set):,}"],
        ],
    ))
    md.append("\nA candidate domain (sourced from Certificate Transparency logs) is "
              "promoted to `domains_inferred.txt` when its MX or IP intersects with one "
              "of the high-confidence disposable clusters above.\n")

    md.append("## Possible upstream false positives (phase 3b)\n")
    md.append(
        f"**{len(upstream_on_shared)} domains** in `domains.txt` resolve *only* to MX hosts "
        "on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email "
        "Routing, etc.). These may be legitimate businesses incorrectly listed upstream — "
        "or shell domains owned by disposable operators who happen to use mainstream mail. "
        "Review manually; this script does NOT auto-remove them.\n"
    )
    if upstream_on_shared:
        rows = [
            [f"`{d}`", f"`{mx}`"]
            for d, mx in upstream_on_shared[:30]
        ]
        md.append(md_table(["Listed disposable", "MX (shared infra)"], rows))
        if len(upstream_on_shared) > 30:
            md.append(f"\n*… and {len(upstream_on_shared) - 30:,} more. "
                      f"Full list available by querying the SQLite directly.*\n")

    md.append("\n---\n")
    md.append("*This file is auto-generated by `scripts/generate_stats.py`. "
              "Do not edit by hand.*\n")

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text("\n".join(md), encoding="utf-8")
    print(f"Wrote {args.out}", file=sys.stderr)
    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
