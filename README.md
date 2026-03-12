# python-disposable

A lightweight Python package to detect disposable/temporary email addresses. Bundles **72,000+ domains** from [disposable/disposable-email-domains](https://github.com/disposable/disposable-email-domains), updated daily — no network calls at runtime.

## Installation

```bash
pip install python-disposable
```

## Usage

### Basic check

```python
from disposable_email import is_disposable, is_valid

is_disposable("user@mailinator.com")  # True
is_disposable("user@gmail.com")       # False

# Works with bare domains too
is_disposable("guerrillamail.com")    # True

# Inverse
is_valid("user@gmail.com")            # True
```

### Strict mode

Strict mode also flags greylisted domains — services that allow anonymous signups but aren't purely disposable (e.g. some free email providers).

```python
is_disposable("example.com", strict=True)
is_valid("example.com", strict=True)
```

### Subdomain handling

Subdomains are automatically resolved to their parent domain.

```python
is_disposable("mail.mailinator.com")     # True
is_disposable("a.b.guerrillamail.com")   # True
```

### Get the full domain set

```python
from disposable_email import get_domains

domains = get_domains()              # frozenset of 72k+ domains
domains_strict = get_domains(strict=True)  # frozenset of strict list
```

### Domain count

```python
from disposable_email import domain_count

domain_count()              # 72170
domain_count(strict=True)   # 26468
```

## Django example

```python
from django import forms
from disposable_email import is_disposable

class RegisterForm(forms.Form):
    email = forms.EmailField()

    def clean_email(self):
        email = self.cleaned_data["email"]
        if is_disposable(email):
            raise forms.ValidationError("Disposable email addresses are not allowed.")
        return email
```

## API reference

| Function | Description |
|----------|-------------|
| `is_disposable(email_or_domain, strict=False)` | Returns `True` if the email/domain is disposable |
| `is_valid(email_or_domain, strict=False)` | Returns `True` if the email/domain is **not** disposable |
| `get_domains(strict=False)` | Returns the full `frozenset` of known disposable domains |
| `domain_count(strict=False)` | Returns the number of bundled domains |

## Data source

Domain lists are sourced from [disposable/disposable-email-domains](https://github.com/disposable/disposable-email-domains) and bundled at release time. The upstream list is updated daily via automated scraping of 40+ sources.

This package checks for upstream updates daily and opens a pull request automatically when new domains are available.

## License

MIT — see [LICENSE](LICENSE).
