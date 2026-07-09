# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-07-09 03:34 UTC**.*  
*Last DNS snapshot: **2026-07-09T03:21:40+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 74,454 |
| `domains_strict.txt` | 74,485 |
| `domains_inferred.txt` (opt-in) | 0 |

## Reachability

Of **75,095** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 11,877 | 15.8% |
| A_ONLY | 1,943 | 2.6% |
| NXDOMAIN | 19,970 | 26.6% |
| NO_RECORDS | 262 | 0.3% |
| TIMEOUT | 41,043 | 54.7% |

**13,820 domains are mail-reachable today** (18.4%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `mail.wabblywabble.com` | 638 | 676 |  |
| `mail.wallywatts.com` | 638 | 676 |  |
| `route1.mx.cloudflare.net` | 469 | 477 | yes |
| `route2.mx.cloudflare.net` | 469 | 477 | yes |
| `route3.mx.cloudflare.net` | 467 | 475 | yes |
| `mx4.beavis99.com` | 463 | 464 |  |
| `mx4.beavis99.net` | 463 | 464 |  |
| `generator.email` | 435 | 580 |  |
| `tinyhost.shop` | 356 | 356 |  |
| `email.gravityengine.cc` | 311 | 311 |  |
| `park-mx.above.com` | 280 | 282 | yes |
| `mx.emlhub.com` | 270 | 270 |  |
| `emailfake.com` | 219 | 264 |  |
| `aspmx.l.google.com` | 209 | 210 | yes |
| `alt1.aspmx.l.google.com` | 204 | 205 | yes |
| `alt2.aspmx.l.google.com` | 203 | 204 | yes |
| `aero4.unstablemail.com` | 190 | 190 |  |
| `srv4.unstablemail.com` | 190 | 190 |  |
| `mx.emltmp.com` | 176 | 176 |  |
| `mx.spymail.one` | 171 | 171 |  |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 638 | 676 |
| `mail.wallywatts.com` | 638 | 676 |
| `mx4.beavis99.com` | 463 | 464 |
| `mx4.beavis99.net` | 463 | 464 |
| `generator.email` | 435 | 580 |
| `tinyhost.shop` | 356 | 356 |
| `email.gravityengine.cc` | 311 | 311 |
| `mx.emlhub.com` | 270 | 270 |
| `emailfake.com` | 219 | 264 |
| `aero4.unstablemail.com` | 190 | 190 |
| `srv4.unstablemail.com` | 190 | 190 |
| `mx.emltmp.com` | 176 | 176 |
| `mx.spymail.one` | 171 | 171 |
| `fwd.regery.net` | 163 | 163 |
| `email.chatgpt.org.uk` | 159 | 159 |
| `mx.dropmail.me` | 155 | 155 |
| `mx37.m1bp.com` | 155 | 155 |
| `mx37.mb5p.com` | 155 | 155 |
| `mx.emlpro.com` | 151 | 151 |
| `mx.freeml.net` | 135 | 135 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `78.47.124.133` | 888 | 888 |
| `94.130.108.80` | 888 | 888 |
| `91.196.52.205` | 559 | 755 |
| `142.132.166.12` | 459 | 494 |
| `188.166.111.252` | 459 | 494 |
| `116.202.9.167` | 455 | 489 |
| `46.101.111.206` | 455 | 489 |
| `158.101.127.66` | 388 | 388 |
| `162.159.205.23` | 371 | 378 |
| `162.159.205.24` | 371 | 378 |
| `162.159.205.25` | 371 | 378 |
| `13.223.25.84` | 360 | 360 |
| `162.159.205.11` | 360 | 367 |
| `162.159.205.12` | 360 | 367 |
| `162.159.205.13` | 360 | 367 |
| `54.243.117.197` | 360 | 360 |
| `162.159.205.17` | 354 | 361 |
| `162.159.205.18` | 354 | 361 |
| `162.159.205.19` | 354 | 361 |
| `144.91.107.45` | 338 | 338 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 206 |
| High-confidence disposable IPs | 392 |
| Promoted to `domains_inferred.txt` | 0 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**1582 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

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
| `1000rub.com` | `route1.mx.cloudflare.net` |
| `10bir.com` | `route1.mx.cloudflare.net` |
| `10dkmail.net` | `smtp.google.com` |
| `10mi.org` | `alt1.aspmx.l.google.com` |
| `10minemail.com` | `route1.mx.cloudflare.net` |
| `10minutemail.co.za` | `route1.mx.cloudflare.net` |
| `11cows.com` | `mxa.mailgun.org` |
| `123gmail.com` | `park-mx.above.com` |
| `12499aaa.com` | `eforward1.registrar-servers.com` |
| `13dk.net` | `route1.mx.cloudflare.net` |
| `14n.co.uk` | `14n-co-uk.mail.protection.outlook.com` |
| `14p.in` | `eforward1.registrar-servers.com` |
| `15qm-mail.red` | `eforward1.registrar-servers.com` |
| `189.email` | `route1.mx.cloudflare.net` |
| `1987.com` | `park-mx.above.com` |
| `1aolmail.com` | `route1.mx.cloudflare.net` |
| `1ayj8yi7lpiksxawav.gq` | `route1.mx.cloudflare.net` |


*… and 1,552 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
