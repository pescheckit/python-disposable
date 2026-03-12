from importlib.resources import files

_domains: frozenset[str] | None = None


def _load() -> frozenset[str]:
    global _domains
    if _domains is None:
        data = files("disposable_email").joinpath("domains.txt").read_text(encoding="utf-8")
        _domains = frozenset(line.strip().lower() for line in data.splitlines() if line.strip())
    return _domains


def is_disposable(email_or_domain: str) -> bool:
    """Return True if the email address or domain is a known disposable/temporary email service."""
    domain = email_or_domain.split("@")[-1].strip().lower()
    return domain in _load()


def is_valid(email_or_domain: str) -> bool:
    """Return True if the email address or domain is NOT a known disposable/temporary email service."""
    return not is_disposable(email_or_domain)


def domain_count() -> int:
    """Return the number of known disposable domains in the bundled list."""
    return len(_load())
