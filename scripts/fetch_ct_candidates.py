"""Fetch candidate disposable domains from Certificate Transparency logs.

Queries crt.sh for domains matching known disposable-email keywords,
extracts unique apex-ish names, and appends them to candidates.txt.
The infer_candidates.py step later resolves these and tests for
cluster overlap with the known-disposable infrastructure.

Run from repo root:
    python scripts/fetch_ct_candidates.py
    python scripts/fetch_ct_candidates.py --keywords trashmail tempmail
"""
from __future__ import annotations

import argparse
import json
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_DOMAINS = ROOT / "disposable_email" / "domains.txt"
DEFAULT_STRICT = ROOT / "disposable_email" / "domains_strict.txt"
DEFAULT_CANDIDATES = ROOT / "disposable_email" / "data" / "candidates.txt"

DEFAULT_KEYWORDS = [
    "tempmail", "tempemail", "temp-mail", "temp.mail",
    "trashmail", "trash-mail",
    "throwaway", "throw-away",
    "disposable",
    "burnermail", "burner-mail",
    "10minutemail", "10minute",
    "fakemail", "fake-mail",
    "guerrillamail",
    "mohmal",
    "mailnesia",
    "yopmail",
    "minutemail", "5minute", "30minute", "60minute",
    "spambox",
    "discardmail",
    "mailcatch",
]

CRT_SH_URL = "https://crt.sh/?q={q}&output=json"

# Conservative TLD allowlist for parsed names — drop entries with weird/unlikely TLDs
COMMON_TLDS = {
    "com", "net", "org", "io", "co", "me", "info", "biz", "us", "uk",
    "de", "fr", "nl", "es", "it", "ru", "pl", "br", "in", "cn", "jp",
    "tk", "ml", "ga", "cf", "gq",   # free TLDs heavily used by disposables
    "xyz", "online", "site", "website", "click", "link",
    "email", "mail", "live", "app", "dev", "tech", "fun", "top",
    "shop", "store", "blog", "art", "club", "page",
}


def load_excluded(*paths: Path) -> set[str]:
    out: set[str] = set()
    for path in paths:
        if not path.exists():
            continue
        for line in path.read_text(encoding="utf-8").splitlines():
            line = line.strip().lower()
            if line and not line.startswith("#"):
                out.add(line)
    return out


def load_existing_candidates(path: Path) -> set[str]:
    if not path.exists():
        return set()
    return load_excluded(path)


def query_crtsh(keyword: str, timeout: float, retries: int = 4,
                backoff_base: float = 3.0) -> list[dict]:
    """Query crt.sh with exponential backoff. Tolerates transient 502/timeouts."""
    pattern = f"%{keyword}%"
    url = CRT_SH_URL.format(q=urllib.parse.quote(pattern))
    req = urllib.request.Request(url, headers={"User-Agent": "python-disposable-osint/1.0"})
    last_err = None
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                data = resp.read().decode("utf-8", errors="replace")
            return json.loads(data) if data.strip() else []
        except urllib.error.HTTPError as e:
            last_err = e
            # 404 = no certs found; not retryable
            if e.code == 404:
                return []
            # 502/503/504/429 = transient; retry
            if e.code not in (502, 503, 504, 429):
                break
        except Exception as e:
            last_err = e
        if attempt < retries - 1:
            sleep_s = backoff_base * (2 ** attempt)
            print(f"  retry {attempt + 1}/{retries - 1} for {keyword!r} in {sleep_s:.0f}s ({last_err})",
                  file=sys.stderr)
            time.sleep(sleep_s)
    print(f"  crt.sh query for {keyword!r} failed after {retries} attempts: {last_err}",
          file=sys.stderr)
    return []


def normalize_name(name: str) -> str | None:
    """Lowercase, strip wildcard, strip whitespace, return apex-ish form."""
    n = name.strip().lower().lstrip("*.")
    if not n or " " in n or "/" in n:
        return None
    if n.startswith(".") or n.endswith("."):
        return None
    parts = n.split(".")
    if len(parts) < 2:
        return None
    tld = parts[-1]
    if not tld.isalpha() or len(tld) < 2:
        return None
    if tld not in COMMON_TLDS:
        return None
    return n


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--candidates-file", type=Path, default=DEFAULT_CANDIDATES)
    parser.add_argument("--domains", type=Path, default=DEFAULT_DOMAINS)
    parser.add_argument("--domains-strict", type=Path, default=DEFAULT_STRICT)
    parser.add_argument("--keywords", nargs="*", default=None,
                        help="Override keyword list (default: built-in)")
    parser.add_argument("--per-keyword-sleep", type=float, default=2.0,
                        help="Seconds between crt.sh queries (be polite)")
    parser.add_argument("--timeout", type=float, default=30.0)
    parser.add_argument("--max-per-keyword", type=int, default=2000,
                        help="Cap names extracted per keyword query")
    args = parser.parse_args()

    keywords = args.keywords or DEFAULT_KEYWORDS
    excluded = load_excluded(args.domains, args.domains_strict)
    existing = load_existing_candidates(args.candidates_file)

    print(f"Excluding {len(excluded)} known-disposable domains", file=sys.stderr)
    print(f"Existing candidates: {len(existing)}", file=sys.stderr)
    print(f"Querying crt.sh with {len(keywords)} keywords", file=sys.stderr)

    discovered: set[str] = set()
    for i, kw in enumerate(keywords, 1):
        rows = query_crtsh(kw, timeout=args.timeout)
        kw_count = 0
        for row in rows[: args.max_per_keyword]:
            name_value = row.get("name_value", "") or ""
            common_name = row.get("common_name", "") or ""
            for raw in name_value.split("\n") + [common_name]:
                norm = normalize_name(raw)
                if not norm:
                    continue
                if norm in excluded or norm in existing or norm in discovered:
                    continue
                discovered.add(norm)
                kw_count += 1
        print(f"  [{i}/{len(keywords)}] {kw!r}: {len(rows)} certs -> +{kw_count} new candidates",
              file=sys.stderr)
        if i < len(keywords):
            time.sleep(args.per_keyword_sleep)

    if not discovered:
        print("No new candidates discovered.", file=sys.stderr)
        return 0

    args.candidates_file.parent.mkdir(parents=True, exist_ok=True)
    if args.candidates_file.exists():
        body = args.candidates_file.read_text(encoding="utf-8")
        if body and not body.endswith("\n"):
            body += "\n"
    else:
        body = (
            "# Candidate domains discovered from Certificate Transparency logs.\n"
            "# These are NOT yet on the disposable list — infer_candidates.py\n"
            "# resolves each, checks for MX/IP cluster overlap with known\n"
            "# disposable infrastructure, and promotes hits to domains_inferred.txt.\n"
            "# Source: crt.sh keyword queries.\n"
        )

    body += "\n".join(sorted(discovered)) + "\n"
    args.candidates_file.write_text(body, encoding="utf-8")

    print(f"\nAppended {len(discovered)} new candidates to {args.candidates_file}",
          file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
