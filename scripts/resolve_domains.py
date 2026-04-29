"""Resolve every disposable domain to its MX hosts and mail IPs.

Output: disposable_email/data/resolution.sqlite

Strategy:
  - For each domain, query MX. If present -> resolve each MX host to A.
  - If domain has no MX, query A directly (RFC 5321 implicit MX fallback).
  - Categorize: MX_OK | A_ONLY | NXDOMAIN | NO_RECORDS | TIMEOUT | OTHER.
  - Skip domains already resolved within --max-age-days (resume support).

Run from repo root:
    python scripts/resolve_domains.py
    python scripts/resolve_domains.py --limit 200          # smoke test
    python scripts/resolve_domains.py --max-age-days 0     # force re-resolve all
"""
from __future__ import annotations

import argparse
import json
import sqlite3
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timedelta, timezone
from pathlib import Path

import dns.exception
import dns.resolver

ROOT = Path(__file__).resolve().parent.parent
DOMAINS_FILE = ROOT / "disposable_email" / "domains.txt"
DEFAULT_DB = ROOT / "disposable_email" / "data" / "resolution.sqlite"

NAMESERVERS = ["1.1.1.1", "1.0.0.1", "8.8.8.8", "9.9.9.9"]
DEFAULT_TIMEOUT = 5.0
DEFAULT_WORKERS = 50

SCHEMA = """
CREATE TABLE IF NOT EXISTS domain_resolution (
    domain      TEXT PRIMARY KEY,
    resolved_at TEXT NOT NULL,
    status      TEXT NOT NULL,
    mx_hosts    TEXT,
    ips         TEXT
);
CREATE INDEX IF NOT EXISTS idx_resolution_status ON domain_resolution(status);
"""


def make_resolver(timeout: float) -> dns.resolver.Resolver:
    r = dns.resolver.Resolver(configure=False)
    r.nameservers = NAMESERVERS
    r.lifetime = timeout
    r.timeout = timeout
    return r


def resolve_one(domain: str, resolver: dns.resolver.Resolver) -> tuple[str, list[str], list[str]]:
    """Resolve one domain. Returns (status, mx_hosts, ips)."""
    try:
        mx_answers = resolver.resolve(domain, "MX")
    except dns.resolver.NXDOMAIN:
        return "NXDOMAIN", [], []
    except dns.resolver.NoAnswer:
        try:
            a_answers = resolver.resolve(domain, "A")
            return "A_ONLY", [], sorted({rr.address for rr in a_answers})
        except dns.resolver.NoAnswer:
            return "NO_RECORDS", [], []
        except dns.resolver.NXDOMAIN:
            return "NXDOMAIN", [], []
        except (dns.exception.Timeout, dns.resolver.NoNameservers):
            return "TIMEOUT", [], []
        except Exception:
            return "OTHER", [], []
    except (dns.exception.Timeout, dns.resolver.NoNameservers):
        return "TIMEOUT", [], []
    except Exception:
        return "OTHER", [], []

    mx_hosts = sorted({str(r.exchange).rstrip(".").lower() for r in mx_answers if str(r.exchange).rstrip(".")})

    ips: set[str] = set()
    for host in mx_hosts:
        if not host:
            continue
        try:
            for rr in resolver.resolve(host, "A"):
                ips.add(rr.address)
        except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN,
                dns.exception.Timeout, dns.resolver.NoNameservers):
            continue
        except Exception:
            continue
    return "MX_OK", mx_hosts, sorted(ips)


def open_db(db_path: Path) -> sqlite3.Connection:
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(db_path))
    conn.executescript(SCHEMA)
    conn.commit()
    return conn


def load_skip_set(conn: sqlite3.Connection, max_age_days: int) -> set[str]:
    """Domains resolved within the last `max_age_days` days are skipped."""
    if max_age_days <= 0:
        return set()
    cutoff = datetime.now(timezone.utc) - timedelta(days=max_age_days)
    rows = conn.execute(
        "SELECT domain FROM domain_resolution WHERE resolved_at >= ?",
        (cutoff.isoformat(),),
    ).fetchall()
    return {r[0] for r in rows}


def load_domains(domains_file: Path, limit: int | None) -> list[str]:
    with open(domains_file, encoding="utf-8") as f:
        domains = [d.strip().lower() for d in f if d.strip() and not d.startswith("#")]
    if limit:
        domains = domains[:limit]
    return domains


def write_batch(conn: sqlite3.Connection, batch: list[tuple]) -> None:
    conn.executemany(
        "INSERT OR REPLACE INTO domain_resolution"
        " (domain, resolved_at, status, mx_hosts, ips) VALUES (?, ?, ?, ?, ?)",
        batch,
    )
    conn.commit()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--db", type=Path, default=DEFAULT_DB)
    parser.add_argument("--domains", type=Path, default=DOMAINS_FILE)
    parser.add_argument("--limit", type=int, default=None,
                        help="Only resolve first N domains (smoke test)")
    parser.add_argument("--workers", type=int, default=DEFAULT_WORKERS)
    parser.add_argument("--timeout", type=float, default=DEFAULT_TIMEOUT)
    parser.add_argument("--max-age-days", type=int, default=7,
                        help="Skip domains resolved within this many days (0 = re-resolve all)")
    parser.add_argument("--batch-size", type=int, default=500)
    args = parser.parse_args()

    domains = load_domains(args.domains, args.limit)
    conn = open_db(args.db)
    skip = load_skip_set(conn, args.max_age_days)
    todo = [d for d in domains if d not in skip]

    print(f"Loaded {len(domains)} domains; skipping {len(skip)} fresh; resolving {len(todo)}",
          file=sys.stderr)

    if not todo:
        print("Nothing to resolve.", file=sys.stderr)
        return 0

    resolver = make_resolver(args.timeout)
    started = time.monotonic()
    batch: list[tuple] = []
    counts: dict[str, int] = {}

    def task(domain: str):
        return domain, *resolve_one(domain, resolver)

    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = [pool.submit(task, d) for d in todo]
        for i, fut in enumerate(as_completed(futures), 1):
            domain, status, mx_hosts, ips = fut.result()
            counts[status] = counts.get(status, 0) + 1
            batch.append((
                domain,
                datetime.now(timezone.utc).isoformat(timespec="seconds"),
                status,
                json.dumps(mx_hosts) if mx_hosts else None,
                json.dumps(ips) if ips else None,
            ))
            if len(batch) >= args.batch_size:
                write_batch(conn, batch)
                batch = []
            if i % 1000 == 0:
                elapsed = time.monotonic() - started
                rate = i / elapsed if elapsed else 0
                print(f"  {i}/{len(todo)}  {rate:.1f}/s  {counts}", file=sys.stderr)

    if batch:
        write_batch(conn, batch)

    elapsed = time.monotonic() - started
    print(f"\nDone. Resolved {len(todo)} in {elapsed:.0f}s ({len(todo)/elapsed:.1f}/s)",
          file=sys.stderr)
    print(f"Status breakdown: {counts}", file=sys.stderr)
    print(f"Database: {args.db}", file=sys.stderr)
    conn.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
