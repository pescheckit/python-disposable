# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-08-30 02:34 UTC**.*  
*Last DNS snapshot: **2026-08-30T02:16:34+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 74,915 |
| `domains_strict.txt` | 74,946 |
| `domains_inferred.txt` (opt-in) | 0 |

## Reachability

Of **75,828** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 13,674 | 18.0% |
| A_ONLY | 2,496 | 3.3% |
| NXDOMAIN | 23,563 | 31.1% |
| NO_RECORDS | 354 | 0.5% |
| TIMEOUT | 35,741 | 47.1% |

**16,170 domains are mail-reachable today** (21.3%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `mail.wabblywabble.com` | 762 | 824 |  |
| `mail.wallywatts.com` | 762 | 824 |  |
| `mx4.beavis99.com` | 618 | 619 |  |
| `mx4.beavis99.net` | 618 | 619 |  |
| `route2.mx.cloudflare.net` | 526 | 536 | yes |
| `route1.mx.cloudflare.net` | 525 | 535 | yes |
| `route3.mx.cloudflare.net` | 525 | 535 | yes |
| `generator.email` | 437 | 574 |  |
| `email.gravityengine.cc` | 369 | 369 |  |
| `email.chatgpt.org.uk` | 325 | 325 |  |
| `mx.emlhub.com` | 283 | 283 |  |
| `park-mx.above.com` | 283 | 288 | yes |
| `emailfake.com` | 262 | 299 |  |
| `aero4.unstablemail.com` | 256 | 256 |  |
| `srv4.unstablemail.com` | 256 | 256 |  |
| `aspmx.l.google.com` | 248 | 250 | yes |
| `alt1.aspmx.l.google.com` | 245 | 247 | yes |
| `alt2.aspmx.l.google.com` | 243 | 245 | yes |
| `tinyhost.shop` | 222 | 223 |  |
| `mx.spymail.one` | 221 | 221 |  |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 762 | 824 |
| `mail.wallywatts.com` | 762 | 824 |
| `mx4.beavis99.com` | 618 | 619 |
| `mx4.beavis99.net` | 618 | 619 |
| `generator.email` | 437 | 574 |
| `email.gravityengine.cc` | 369 | 369 |
| `email.chatgpt.org.uk` | 325 | 325 |
| `mx.emlhub.com` | 283 | 283 |
| `emailfake.com` | 262 | 299 |
| `aero4.unstablemail.com` | 256 | 256 |
| `srv4.unstablemail.com` | 256 | 256 |
| `tinyhost.shop` | 222 | 223 |
| `mx.spymail.one` | 221 | 221 |
| `mx.emltmp.com` | 192 | 192 |
| `mx.emlpro.com` | 187 | 187 |
| `mx.freeml.net` | 163 | 163 |
| `mx37.m1bp.com` | 163 | 163 |
| `mx37.mb5p.com` | 163 | 163 |
| `mx.dropmail.me` | 160 | 160 |
| `mail.casadorock.com` | 138 | 138 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `78.47.124.133` | 1146 | 1146 |
| `94.130.108.80` | 1146 | 1146 |
| `138.226.240.26` | 672 | 672 |
| `142.132.166.12` | 644 | 698 |
| `188.166.111.252` | 644 | 698 |
| `116.202.9.167` | 642 | 695 |
| `46.101.111.206` | 642 | 695 |
| `91.196.52.205` | 610 | 784 |
| `188.245.74.208` | 493 | 494 |
| `13.223.25.84` | 490 | 490 |
| `54.243.117.197` | 490 | 490 |
| `195.201.18.63` | 478 | 479 |
| `162.159.205.17` | 460 | 469 |
| `162.159.205.18` | 460 | 469 |
| `162.159.205.19` | 460 | 469 |
| `162.159.205.23` | 454 | 462 |
| `162.159.205.24` | 454 | 462 |
| `162.159.205.25` | 454 | 462 |
| `162.159.205.11` | 449 | 457 |
| `162.159.205.12` | 449 | 457 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 236 |
| High-confidence disposable IPs | 504 |
| Promoted to `domains_inferred.txt` | 0 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**1786 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

| Listed disposable | MX (shared infra) |
|---|---|
| `0-30-24.com` | `alt1.aspmx.l.google.com` |
| `0-mail.com` | `park-mx.above.com` |
| `0058.ru` | `alt1.aspmx.l.google.com` |
| `01g.cloud` | `alt1.aspmx.l.google.com` |
| `020307.xyz` | `route1.mx.cloudflare.net` |
| `0ak.org` | `mx00.ionos.com` |
| `0hcow.com` | `mxa.mailgun.org` |
| `0hio.net` | `aspmx1.migadu.com` |
| `0nce.net` | `route1.mx.cloudflare.net` |
| `0rg.fr` | `mx1.mail.ovh.net` |
| `0xmiikee.com` | `eforward1.registrar-servers.com` |
| `1-8.biz` | `mail.protonmail.ch` |
| `1-box.ru` | `mx.yandex.ru` |
| `10bir.com` | `route1.mx.cloudflare.net` |
| `10dkmail.net` | `smtp.google.com` |
| `10m.email` | `eforward1.registrar-servers.com` |
| `10mi.org` | `alt1.aspmx.l.google.com` |
| `10minemail.com` | `route1.mx.cloudflare.net` |
| `10minutemail.co.za` | `route1.mx.cloudflare.net` |
| `11cows.com` | `mxa.mailgun.org` |
| `123gmail.com` | `park-mx.above.com` |
| `12499aaa.com` | `eforward1.registrar-servers.com` |
| `129.in` | `park-mx.above.com` |
| `12storage.com` | `park-mx.above.com` |
| `13dk.net` | `route1.mx.cloudflare.net` |
| `14n.co.uk` | `14n-co-uk.mail.protection.outlook.com` |
| `14p.in` | `eforward1.registrar-servers.com` |
| `15qm-mail.red` | `eforward1.registrar-servers.com` |
| `189.email` | `route1.mx.cloudflare.net` |
| `1987.com` | `park-mx.above.com` |


*… and 1,756 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
