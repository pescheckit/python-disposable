# python-disposable

A Python package to check if an email address or domain belongs to a disposable/temporary email service.

Bundles **72,000+ domains** from [disposable/disposable-email-domains](https://github.com/disposable/disposable-email-domains), updated daily.

## Installation

```bash
pip install disposable-email-check
```

## Usage

```python
from disposable_email import is_disposable, is_valid, domain_count

# Check by email address
is_disposable("user@mailinator.com")  # True
is_disposable("user@gmail.com")       # False

# Check by domain only
is_disposable("guerrillamail.com")    # True

# Inverse check
is_valid("user@gmail.com")            # True
is_valid("user@10minutemail.com")     # False

# How many domains are bundled?
domain_count()  # 72170
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

## Updating the domain list

The bundled `domains.txt` is sourced from [disposable/disposable-email-domains](https://github.com/disposable/disposable-email-domains) and updated with each package release.

To update manually, run:

```bash
curl -sL https://raw.githubusercontent.com/disposable/disposable-email-domains/master/domains.txt \
  -o disposable_email/domains.txt
```

Then bump the version in `pyproject.toml` and re-publish.
