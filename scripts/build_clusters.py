"""Build MX and IP cluster tables from resolution data.

Reads:
    disposable_email/data/resolution.sqlite (domain_resolution table)
    disposable_email/domains.txt        (treated as the "disposable" set)
    disposable_email/data/shared_infra.txt

Writes (to the same SQLite):
    mx_cluster  (mx_host, domain_count, disposable_count, is_shared_infra)
    ip_cluster  (ip,      domain_count, disposable_count, is_shared_infra)

A "cluster" here is just an MX host or IP, plus how many resolved domains
reference it. `disposable_count` is the subset of those domains that are
on the bundled disposable list.
"""
from __future__ import annotations

import argparse
import json
import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_DB = ROOT / "disposable_email" / "data" / "resolution.sqlite"
DEFAULT_DOMAINS = ROOT / "disposable_email" / "domains.txt"
DEFAULT_SHARED_INFRA = ROOT / "disposable_email" / "data" / "shared_infra.txt"

CLUSTER_SCHEMA = """
DROP TABLE IF EXISTS mx_cluster;
DROP TABLE IF EXISTS ip_cluster;

CREATE TABLE mx_cluster (
    mx_host          TEXT PRIMARY KEY,
    domain_count     INTEGER NOT NULL,
    disposable_count INTEGER NOT NULL,
    is_shared_infra  INTEGER NOT NULL
);

CREATE TABLE ip_cluster (
    ip               TEXT PRIMARY KEY,
    domain_count     INTEGER NOT NULL,
    disposable_count INTEGER NOT NULL,
    is_shared_infra  INTEGER NOT NULL
);

CREATE INDEX idx_mx_disposable ON mx_cluster(disposable_count);
CREATE INDEX idx_ip_disposable ON ip_cluster(disposable_count);
"""


def load_lines(path: Path) -> list[str]:
    if not path.exists():
        return []
    out = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if line and not line.startswith("#"):
            out.append(line.lower())
    return out


def is_shared(host: str, suffixes: list[str]) -> bool:
    """True if host ends with any suffix in the shared-infra list."""
    h = host.rstrip(".").lower()
    for s in suffixes:
        s = s.rstrip(".").lower()
        if h == s or h.endswith("." + s):
            return True
    return False


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--db", type=Path, default=DEFAULT_DB)
    parser.add_argument("--domains", type=Path, default=DEFAULT_DOMAINS)
    parser.add_argument("--shared-infra", type=Path, default=DEFAULT_SHARED_INFRA)
    args = parser.parse_args()

    if not args.db.exists():
        print(f"ERROR: {args.db} not found. Run resolve_domains.py first.", file=sys.stderr)
        return 1

    disposable_set = set(load_lines(args.domains))
    shared_suffixes = load_lines(args.shared_infra)

    print(f"Disposable list: {len(disposable_set)} domains", file=sys.stderr)
    print(f"Shared-infra suffixes: {len(shared_suffixes)}", file=sys.stderr)

    conn = sqlite3.connect(str(args.db))
    conn.executescript(CLUSTER_SCHEMA)

    mx_total: dict[str, int] = {}
    mx_disp: dict[str, int] = {}
    ip_total: dict[str, int] = {}
    ip_disp: dict[str, int] = {}

    rows = conn.execute(
        "SELECT domain, mx_hosts, ips FROM domain_resolution"
    ).fetchall()
    print(f"Resolution rows: {len(rows)}", file=sys.stderr)

    for domain, mx_json, ips_json in rows:
        is_disp = domain in disposable_set
        mx_hosts = json.loads(mx_json) if mx_json else []
        ips = json.loads(ips_json) if ips_json else []
        for h in set(mx_hosts):
            mx_total[h] = mx_total.get(h, 0) + 1
            if is_disp:
                mx_disp[h] = mx_disp.get(h, 0) + 1
        for ip in set(ips):
            ip_total[ip] = ip_total.get(ip, 0) + 1
            if is_disp:
                ip_disp[ip] = ip_disp.get(ip, 0) + 1

    mx_rows = [
        (host, total, mx_disp.get(host, 0), int(is_shared(host, shared_suffixes)))
        for host, total in mx_total.items()
    ]
    ip_rows = [
        (ip, total, ip_disp.get(ip, 0), 0)  # IP-level shared marking is left to ASN
        for ip, total in ip_total.items()
    ]

    conn.executemany(
        "INSERT INTO mx_cluster (mx_host, domain_count, disposable_count, is_shared_infra)"
        " VALUES (?, ?, ?, ?)",
        mx_rows,
    )
    conn.executemany(
        "INSERT INTO ip_cluster (ip, domain_count, disposable_count, is_shared_infra)"
        " VALUES (?, ?, ?, ?)",
        ip_rows,
    )
    conn.commit()

    shared_mx = sum(1 for r in mx_rows if r[3])
    print(f"Wrote {len(mx_rows)} MX clusters ({shared_mx} marked shared-infra)", file=sys.stderr)
    print(f"Wrote {len(ip_rows)} IP clusters", file=sys.stderr)
    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
