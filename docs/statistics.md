# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-07-30 03:18 UTC**.*  
*Last DNS snapshot: **2026-07-30T03:05:07+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 74,660 |
| `domains_strict.txt` | 74,691 |
| `domains_inferred.txt` (opt-in) | 0 |

## Reachability

Of **75,390** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 11,934 | 15.8% |
| A_ONLY | 1,966 | 2.6% |
| NXDOMAIN | 20,739 | 27.5% |
| NO_RECORDS | 301 | 0.4% |
| TIMEOUT | 40,450 | 53.7% |

**13,900 domains are mail-reachable today** (18.4%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `mail.wabblywabble.com` | 662 | 710 |  |
| `mail.wallywatts.com` | 662 | 710 |  |
| `route2.mx.cloudflare.net` | 516 | 525 | yes |
| `route1.mx.cloudflare.net` | 515 | 524 | yes |
| `route3.mx.cloudflare.net` | 515 | 524 | yes |
| `mx4.beavis99.com` | 496 | 497 |  |
| `mx4.beavis99.net` | 496 | 497 |  |
| `generator.email` | 411 | 547 |  |
| `tinyhost.shop` | 336 | 336 |  |
| `mx.emlhub.com` | 270 | 270 |  |
| `emailfake.com` | 263 | 304 |  |
| `park-mx.above.com` | 255 | 258 | yes |
| `aspmx.l.google.com` | 225 | 227 | yes |
| `alt1.aspmx.l.google.com` | 224 | 226 | yes |
| `alt2.aspmx.l.google.com` | 220 | 222 | yes |
| `aero4.unstablemail.com` | 216 | 216 |  |
| `srv4.unstablemail.com` | 215 | 215 |  |
| `email.chatgpt.org.uk` | 188 | 188 |  |
| `email.gravityengine.cc` | 186 | 186 |  |
| `eforward1.registrar-servers.com` | 183 | 186 | yes |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 662 | 710 |
| `mail.wallywatts.com` | 662 | 710 |
| `mx4.beavis99.com` | 496 | 497 |
| `mx4.beavis99.net` | 496 | 497 |
| `generator.email` | 411 | 547 |
| `tinyhost.shop` | 336 | 336 |
| `mx.emlhub.com` | 270 | 270 |
| `emailfake.com` | 263 | 304 |
| `aero4.unstablemail.com` | 216 | 216 |
| `srv4.unstablemail.com` | 215 | 215 |
| `email.chatgpt.org.uk` | 188 | 188 |
| `email.gravityengine.cc` | 186 | 186 |
| `mx.emltmp.com` | 172 | 172 |
| `mx.spymail.one` | 163 | 163 |
| `mx.emlpro.com` | 151 | 151 |
| `mx.dropmail.me` | 150 | 150 |
| `mail.casadorock.com` | 143 | 143 |
| `mx37.m1bp.com` | 137 | 137 |
| `mx37.mb5p.com` | 137 | 137 |
| `mx.freeml.net` | 126 | 126 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `78.47.124.133` | 932 | 932 |
| `94.130.108.80` | 932 | 932 |
| `91.196.52.205` | 566 | 747 |
| `142.132.166.12` | 501 | 543 |
| `188.166.111.252` | 501 | 543 |
| `116.202.9.167` | 483 | 524 |
| `46.101.111.206` | 483 | 524 |
| `162.159.205.23` | 405 | 413 |
| `162.159.205.24` | 405 | 413 |
| `162.159.205.25` | 405 | 413 |
| `162.159.205.17` | 404 | 412 |
| `162.159.205.18` | 404 | 412 |
| `162.159.205.19` | 404 | 412 |
| `13.223.25.84` | 400 | 400 |
| `54.243.117.197` | 400 | 400 |
| `162.159.205.11` | 394 | 402 |
| `162.159.205.12` | 394 | 402 |
| `162.159.205.13` | 394 | 402 |
| `188.245.74.208` | 373 | 374 |
| `195.201.18.63` | 358 | 359 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 206 |
| High-confidence disposable IPs | 448 |
| Promoted to `domains_inferred.txt` | 0 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**1677 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

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
| `12storage.com` | `park-mx.above.com` |
| `13dk.net` | `route1.mx.cloudflare.net` |
| `14n.co.uk` | `14n-co-uk.mail.protection.outlook.com` |
| `14p.in` | `eforward1.registrar-servers.com` |
| `15qm-mail.red` | `eforward1.registrar-servers.com` |
| `189.email` | `route1.mx.cloudflare.net` |
| `1987.com` | `park-mx.above.com` |


*… and 1,647 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
