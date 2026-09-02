# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-09-02 02:51 UTC**.*  
*Last DNS snapshot: **2026-09-02T02:51:22+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 75,248 |
| `domains_strict.txt` | 75,279 |
| `domains_inferred.txt` (opt-in) | 2 |

## Reachability

Of **76,175** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 15,034 | 19.7% |
| A_ONLY | 2,815 | 3.7% |
| NXDOMAIN | 25,759 | 33.8% |
| NO_RECORDS | 388 | 0.5% |
| TIMEOUT | 32,179 | 42.2% |

**17,849 domains are mail-reachable today** (23.4%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `mail.wabblywabble.com` | 839 | 903 |  |
| `mail.wallywatts.com` | 839 | 903 |  |
| `mx4.beavis99.com` | 662 | 663 |  |
| `mx4.beavis99.net` | 662 | 663 |  |
| `route2.mx.cloudflare.net` | 566 | 577 | yes |
| `route1.mx.cloudflare.net` | 565 | 576 | yes |
| `route3.mx.cloudflare.net` | 565 | 576 | yes |
| `generator.email` | 484 | 620 |  |
| `tinyhost.shop` | 475 | 475 |  |
| `email.chatgpt.org.uk` | 393 | 393 |  |
| `email.gravityengine.cc` | 381 | 381 |  |
| `park-mx.above.com` | 305 | 310 | yes |
| `mx.emlhub.com` | 290 | 290 |  |
| `emailfake.com` | 282 | 319 |  |
| `aspmx.l.google.com` | 277 | 279 | yes |
| `aero4.unstablemail.com` | 275 | 275 |  |
| `alt1.aspmx.l.google.com` | 275 | 277 | yes |
| `srv4.unstablemail.com` | 275 | 275 |  |
| `alt2.aspmx.l.google.com` | 272 | 274 | yes |
| `mx.spymail.one` | 234 | 234 |  |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 839 | 903 |
| `mail.wallywatts.com` | 839 | 903 |
| `mx4.beavis99.com` | 662 | 663 |
| `mx4.beavis99.net` | 662 | 663 |
| `generator.email` | 484 | 620 |
| `tinyhost.shop` | 475 | 475 |
| `email.chatgpt.org.uk` | 393 | 393 |
| `email.gravityengine.cc` | 381 | 381 |
| `mx.emlhub.com` | 290 | 290 |
| `emailfake.com` | 282 | 319 |
| `aero4.unstablemail.com` | 275 | 275 |
| `srv4.unstablemail.com` | 275 | 275 |
| `mx.spymail.one` | 234 | 234 |
| `mx.emlpro.com` | 202 | 202 |
| `mx.emltmp.com` | 201 | 201 |
| `mx.dropmail.me` | 174 | 174 |
| `mx.freeml.net` | 169 | 169 |
| `mx37.m1bp.com` | 168 | 168 |
| `mx37.mb5p.com` | 168 | 168 |
| `mail.casadorock.com` | 150 | 150 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `78.47.124.133` | 1235 | 1235 |
| `94.130.108.80` | 1235 | 1235 |
| `138.226.240.26` | 744 | 744 |
| `142.132.166.12` | 730 | 786 |
| `188.166.111.252` | 730 | 786 |
| `116.202.9.167` | 729 | 784 |
| `46.101.111.206` | 729 | 784 |
| `91.196.52.205` | 701 | 874 |
| `13.223.25.84` | 572 | 572 |
| `54.243.117.197` | 572 | 572 |
| `188.245.74.208` | 539 | 540 |
| `195.201.18.63` | 524 | 525 |
| `162.159.205.17` | 499 | 509 |
| `162.159.205.18` | 499 | 509 |
| `162.159.205.19` | 499 | 509 |
| `162.159.205.23` | 495 | 504 |
| `162.159.205.24` | 495 | 504 |
| `162.159.205.25` | 495 | 504 |
| `162.159.205.11` | 490 | 499 |
| `162.159.205.12` | 490 | 499 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 243 |
| High-confidence disposable IPs | 552 |
| Promoted to `domains_inferred.txt` | 2 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**1951 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

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


*… and 1,921 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
