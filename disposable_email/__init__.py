from __future__ import annotations

from importlib.resources import files
from typing import Optional

_cache: dict[tuple[bool, bool], frozenset[str]] = {}
_custom_cache: Optional[frozenset[str]] = None
_inferred_cache: Optional[frozenset[str]] = None


def _read_resource(name: str) -> str:
    return files("disposable_email").joinpath(name).read_text(encoding="utf-8")


def _parse(text: str) -> frozenset[str]:
    return frozenset(
        line.strip().lower()
        for line in text.splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    )


def _load_custom() -> frozenset[str]:
    global _custom_cache
    if _custom_cache is None:
        _custom_cache = _parse(_read_resource("domains_custom.txt"))
    return _custom_cache


def _load_inferred() -> frozenset[str]:
    """Load domains_inferred.txt. Empty frozenset if file absent."""
    global _inferred_cache
    if _inferred_cache is None:
        try:
            _inferred_cache = _parse(_read_resource("domains_inferred.txt"))
        except (FileNotFoundError, ModuleNotFoundError):
            _inferred_cache = frozenset()
    return _inferred_cache


def _load(strict: bool = False, inferred: bool = False) -> frozenset[str]:
    key = (strict, inferred)
    if key in _cache:
        return _cache[key]
    base = _parse(_read_resource("domains_strict.txt" if strict else "domains.txt"))
    result = base | _load_custom()
    if inferred:
        result = result | _load_inferred()
    _cache[key] = result
    return result


def _extract_domain(email_or_domain: str) -> str:
    return email_or_domain.split("@")[-1].strip().lower()


def _is_disposable_domain(domain: str, strict: bool = False, inferred: bool = False) -> bool:
    domains = _load(strict=strict, inferred=inferred)
    parts = domain.split(".")
    for i in range(len(parts) - 1):
        candidate = ".".join(parts[i:])
        if candidate in domains:
            return True
    return False


def is_disposable(email_or_domain: str, strict: bool = False, inferred: bool = False) -> bool:
    """Return True if the email address or domain is a known disposable/temporary email service.

    Args:
        email_or_domain: An email address (user@example.com) or bare domain (example.com).
        strict: If True, also flags greylisted domains (anonymous signup services).
        inferred: If True, also flags domains in `domains_inferred.txt` — domains that
            were not on the upstream disposable list but share mail infrastructure with
            5+ already-known disposable services. Higher recall, slightly higher
            false-positive risk than the curated list.
    """
    domain = _extract_domain(email_or_domain)
    if not domain:
        return False
    return _is_disposable_domain(domain, strict=strict, inferred=inferred)


def is_valid(email_or_domain: str, strict: bool = False, inferred: bool = False) -> bool:
    """Return True if the email address or domain is NOT a known disposable/temporary email service."""
    return not is_disposable(email_or_domain, strict=strict, inferred=inferred)


def get_domains(strict: bool = False, inferred: bool = False) -> frozenset[str]:
    """Return the full set of known disposable domains.

    Args:
        strict: If True, returns the strict list (includes greylisted domains).
        inferred: If True, additionally includes domains_inferred.txt.
    """
    return _load(strict=strict, inferred=inferred)


def domain_count(strict: bool = False, inferred: bool = False) -> int:
    """Return the number of known disposable domains in the bundled list."""
    return len(_load(strict=strict, inferred=inferred))
