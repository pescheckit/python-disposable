# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-08-16 02:37 UTC**.*  
*Last DNS snapshot: **2026-08-16T02:29:29+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 74,693 |
| `domains_strict.txt` | 74,724 |
| `domains_inferred.txt` (opt-in) | 0 |

## Reachability

Of **75,537** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 12,062 | 16.0% |
| A_ONLY | 1,971 | 2.6% |
| NXDOMAIN | 21,443 | 28.4% |
| NO_RECORDS | 288 | 0.4% |
| TIMEOUT | 39,773 | 52.7% |

**14,033 domains are mail-reachable today** (18.6%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `mail.wabblywabble.com` | 656 | 712 |  |
| `mail.wallywatts.com` | 656 | 712 |  |
| `route2.mx.cloudflare.net` | 528 | 537 | yes |
| `route1.mx.cloudflare.net` | 527 | 536 | yes |
| `route3.mx.cloudflare.net` | 527 | 536 | yes |
| `mx4.beavis99.com` | 508 | 509 |  |
| `mx4.beavis99.net` | 508 | 509 |  |
| `generator.email` | 427 | 563 |  |
| `tinyhost.shop` | 306 | 306 |  |
| `mx.emlhub.com` | 291 | 291 |  |
| `emailfake.com` | 265 | 302 |  |
| `park-mx.above.com` | 237 | 241 | yes |
| `aspmx.l.google.com` | 225 | 227 | yes |
| `aero4.unstablemail.com` | 220 | 220 |  |
| `alt1.aspmx.l.google.com` | 220 | 222 | yes |
| `srv4.unstablemail.com` | 220 | 220 |  |
| `alt2.aspmx.l.google.com` | 215 | 217 | yes |
| `mx.spymail.one` | 215 | 215 |  |
| `mx.emlpro.com` | 195 | 195 |  |
| `mx.emltmp.com` | 178 | 178 |  |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 656 | 712 |
| `mail.wallywatts.com` | 656 | 712 |
| `mx4.beavis99.com` | 508 | 509 |
| `mx4.beavis99.net` | 508 | 509 |
| `generator.email` | 427 | 563 |
| `tinyhost.shop` | 306 | 306 |
| `mx.emlhub.com` | 291 | 291 |
| `emailfake.com` | 265 | 302 |
| `aero4.unstablemail.com` | 220 | 220 |
| `srv4.unstablemail.com` | 220 | 220 |
| `mx.spymail.one` | 215 | 215 |
| `mx.emlpro.com` | 195 | 195 |
| `mx.emltmp.com` | 178 | 178 |
| `email.chatgpt.org.uk` | 176 | 176 |
| `mx.dropmail.me` | 174 | 174 |
| `mail.casadorock.com` | 165 | 165 |
| `mx.freeml.net` | 157 | 157 |
| `email.gravityengine.cc` | 150 | 150 |
| `mx37.m1bp.com` | 150 | 150 |
| `mx37.mb5p.com` | 150 | 150 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `78.47.124.133` | 1106 | 1106 |
| `94.130.108.80` | 1106 | 1106 |
| `91.196.52.205` | 593 | 766 |
| `116.202.9.167` | 501 | 550 |
| `46.101.111.206` | 501 | 550 |
| `142.132.166.12` | 495 | 545 |
| `188.166.111.252` | 495 | 545 |
| `162.159.205.23` | 442 | 449 |
| `162.159.205.24` | 442 | 449 |
| `162.159.205.25` | 442 | 449 |
| `162.159.205.17` | 427 | 435 |
| `162.159.205.18` | 427 | 435 |
| `162.159.205.19` | 427 | 435 |
| `162.159.205.11` | 419 | 426 |
| `162.159.205.12` | 419 | 426 |
| `162.159.205.13` | 419 | 426 |
| `13.223.25.84` | 365 | 365 |
| `54.243.117.197` | 365 | 365 |
| `188.245.74.208` | 363 | 364 |
| `195.201.18.63` | 331 | 332 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 213 |
| High-confidence disposable IPs | 425 |
| Promoted to `domains_inferred.txt` | 0 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**1655 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

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
| `0nes.net` | `park-mx.above.com` |
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


*… and 1,625 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
