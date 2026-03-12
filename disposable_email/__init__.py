from __future__ import annotations

from importlib.resources import files
from typing import Optional

_domains: Optional[frozenset[str]] = None
_domains_strict: Optional[frozenset[str]] = None


def _load(strict: bool = False) -> frozenset[str]:
    global _domains, _domains_strict
    if strict:
        if _domains_strict is None:
            data = files("disposable_email").joinpath("domains_strict.txt").read_text(encoding="utf-8")
            _domains_strict = frozenset(line.strip().lower() for line in data.splitlines() if line.strip())
        return _domains_strict
    else:
        if _domains is None:
            data = files("disposable_email").joinpath("domains.txt").read_text(encoding="utf-8")
            _domains = frozenset(line.strip().lower() for line in data.splitlines() if line.strip())
        return _domains


def _extract_domain(email_or_domain: str) -> str:
    """Extract and normalize domain, stripping subdomains if needed."""
    domain = email_or_domain.split("@")[-1].strip().lower()
    return domain


def _is_disposable_domain(domain: str, strict: bool = False) -> bool:
    """Check domain and progressively strip subdomains until a match is found."""
    domains = _load(strict)
    parts = domain.split(".")
    # Check from full domain down to second-level domain (e.g. a.b.c.com -> b.c.com -> c.com)
    for i in range(len(parts) - 1):
        candidate = ".".join(parts[i:])
        if candidate in domains:
            return True
    return False


def is_disposable(email_or_domain: str, strict: bool = False) -> bool:
    """Return True if the email address or domain is a known disposable/temporary email service.

    Args:
        email_or_domain: An email address (user@example.com) or bare domain (example.com).
        strict: If True, also flags greylisted domains (anonymous signup services).
    """
    domain = _extract_domain(email_or_domain)
    if not domain:
        return False
    return _is_disposable_domain(domain, strict=strict)


def is_valid(email_or_domain: str, strict: bool = False) -> bool:
    """Return True if the email address or domain is NOT a known disposable/temporary email service.

    Args:
        email_or_domain: An email address (user@example.com) or bare domain (example.com).
        strict: If True, also flags greylisted domains (anonymous signup services).
    """
    return not is_disposable(email_or_domain, strict=strict)


def get_domains(strict: bool = False) -> frozenset[str]:
    """Return the full set of known disposable domains.

    Args:
        strict: If True, returns the strict list (includes greylisted domains).
    """
    return _load(strict)


def domain_count(strict: bool = False) -> int:
    """Return the number of known disposable domains in the bundled list.

    Args:
        strict: If True, returns the count for the strict list.
    """
    return len(_load(strict))
