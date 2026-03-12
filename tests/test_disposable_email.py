import pytest
from disposable_email import is_disposable, is_valid, domain_count


class TestDomainCount:
    def test_domain_count_is_positive(self):
        assert domain_count() > 0

    def test_domain_count_is_large(self):
        # Sanity check: the bundled list should have at least 10k domains
        assert domain_count() >= 10_000


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
        # Empty input should not raise, just return False
        assert is_disposable("") is False

    def test_domain_with_whitespace(self):
        assert is_disposable("  mailinator.com  ") is True


class TestIsValid:
    def test_valid_email_is_not_disposable(self):
        assert is_valid("user@gmail.com") is True

    def test_disposable_email_is_not_valid(self):
        assert is_valid("user@mailinator.com") is False

    def test_is_valid_is_inverse_of_is_disposable(self):
        domains = ["gmail.com", "mailinator.com", "guerrillamail.com", "outlook.com"]
        for domain in domains:
            assert is_valid(domain) is not is_disposable(domain)


class TestCaching:
    def test_repeated_calls_are_consistent(self):
        result1 = is_disposable("mailinator.com")
        result2 = is_disposable("mailinator.com")
        assert result1 == result2

    def test_domain_count_is_stable(self):
        assert domain_count() == domain_count()
