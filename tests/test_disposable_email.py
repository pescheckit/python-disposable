import pytest
from disposable_email import is_disposable, is_valid, domain_count, get_domains


class TestDomainCount:
    def test_domain_count_is_positive(self):
        assert domain_count() > 0

    def test_domain_count_is_large(self):
        assert domain_count() >= 10_000

    def test_strict_domain_count_is_positive(self):
        assert domain_count(strict=True) > 0

    def test_strict_count_differs_from_normal(self):
        assert domain_count(strict=True) != domain_count()


class TestGetDomains:
    def test_returns_frozenset(self):
        assert isinstance(get_domains(), frozenset)

    def test_strict_returns_frozenset(self):
        assert isinstance(get_domains(strict=True), frozenset)

    def test_contains_known_disposable(self):
        assert "mailinator.com" in get_domains()

    def test_does_not_contain_legitimate(self):
        assert "gmail.com" not in get_domains()

    def test_strict_and_normal_are_different(self):
        assert get_domains() != get_domains(strict=True)


class TestIsDisposable:
    def test_known_disposable_domain(self):
        assert is_disposable("mailinator.com") is True

    def test_known_disposable_domain_guerrilla(self):
        assert is_disposable("guerrillamail.com") is True

    def test_known_disposable_domain_10minute(self):
        assert is_disposable("10minutemail.com") is True

    def test_known_legitimate_domain_gmail(self):
        assert is_disposable("gmail.com") is False

    def test_known_legitimate_domain_outlook(self):
        assert is_disposable("outlook.com") is False

    def test_known_legitimate_domain_yahoo(self):
        assert is_disposable("yahoo.com") is False

    def test_email_address_disposable(self):
        assert is_disposable("user@mailinator.com") is True

    def test_email_address_legitimate(self):
        assert is_disposable("user@gmail.com") is False

    def test_case_insensitive_domain(self):
        assert is_disposable("MAILINATOR.COM") is True

    def test_case_insensitive_email(self):
        assert is_disposable("User@MAILINATOR.COM") is True

    def test_empty_string(self):
        assert is_disposable("") is False

    def test_domain_with_whitespace(self):
        assert is_disposable("  mailinator.com  ") is True


class TestSubdomainStripping:
    def test_subdomain_of_disposable_is_disposable(self):
        assert is_disposable("mail.mailinator.com") is True

    def test_deep_subdomain_of_disposable_is_disposable(self):
        assert is_disposable("a.b.mailinator.com") is True

    def test_subdomain_of_legitimate_is_not_disposable(self):
        assert is_disposable("mail.gmail.com") is False


class TestStrictMode:
    def test_strict_false_by_default(self):
        # Default call should behave same as strict=False
        assert is_disposable("mailinator.com") == is_disposable("mailinator.com", strict=False)

    def test_strict_mode_accepts_email(self):
        assert is_disposable("user@mailinator.com", strict=True) is True

    def test_strict_mode_legitimate_domain(self):
        assert is_disposable("gmail.com", strict=True) is False


class TestIsValid:
    def test_valid_email_is_not_disposable(self):
        assert is_valid("user@gmail.com") is True

    def test_disposable_email_is_not_valid(self):
        assert is_valid("user@mailinator.com") is False

    def test_strict_valid(self):
        assert is_valid("user@gmail.com", strict=True) is True

    def test_strict_invalid(self):
        assert is_valid("user@mailinator.com", strict=True) is False

    def test_is_valid_is_inverse_of_is_disposable(self):
        domains = ["gmail.com", "mailinator.com", "guerrillamail.com", "outlook.com"]
        for domain in domains:
            assert is_valid(domain) is not is_disposable(domain)


class TestCaching:
    def test_repeated_calls_are_consistent(self):
        assert is_disposable("mailinator.com") == is_disposable("mailinator.com")

    def test_domain_count_is_stable(self):
        assert domain_count() == domain_count()

    def test_get_domains_returns_same_object(self):
        # Should return cached frozenset, not a new object each time
        assert get_domains() is get_domains()

    def test_get_domains_strict_returns_same_object(self):
        assert get_domains(strict=True) is get_domains(strict=True)
