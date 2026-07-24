# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-07-24 03:24 UTC**.*  
*Last DNS snapshot: **2026-07-24T03:07:23+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 74,603 |
| `domains_strict.txt` | 74,634 |
| `domains_inferred.txt` (opt-in) | 0 |

## Reachability

Of **75,299** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 11,768 | 15.6% |
| A_ONLY | 1,905 | 2.5% |
| NXDOMAIN | 19,368 | 25.7% |
| NO_RECORDS | 253 | 0.3% |
| TIMEOUT | 42,005 | 55.8% |

**13,673 domains are mail-reachable today** (18.2%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `mail.wabblywabble.com` | 605 | 651 |  |
| `mail.wallywatts.com` | 605 | 651 |  |
| `mx4.beavis99.com` | 555 | 556 |  |
| `mx4.beavis99.net` | 555 | 556 |  |
| `route1.mx.cloudflare.net` | 500 | 509 | yes |
| `route2.mx.cloudflare.net` | 500 | 509 | yes |
| `route3.mx.cloudflare.net` | 498 | 507 | yes |
| `generator.email` | 383 | 517 |  |
| `tinyhost.shop` | 336 | 336 |  |
| `park-mx.above.com` | 298 | 300 | yes |
| `email.gravityengine.cc` | 265 | 265 |  |
| `mx.emlhub.com` | 232 | 232 |  |
| `aspmx.l.google.com` | 219 | 221 | yes |
| `aero4.unstablemail.com` | 216 | 216 |  |
| `srv4.unstablemail.com` | 215 | 215 |  |
| `alt1.aspmx.l.google.com` | 212 | 214 | yes |
| `alt2.aspmx.l.google.com` | 210 | 212 | yes |
| `emailfake.com` | 193 | 234 |  |
| `mx.emltmp.com` | 171 | 171 |  |
| `eforward1.registrar-servers.com` | 170 | 173 | yes |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 605 | 651 |
| `mail.wallywatts.com` | 605 | 651 |
| `mx4.beavis99.com` | 555 | 556 |
| `mx4.beavis99.net` | 555 | 556 |
| `generator.email` | 383 | 517 |
| `tinyhost.shop` | 336 | 336 |
| `email.gravityengine.cc` | 265 | 265 |
| `mx.emlhub.com` | 232 | 232 |
| `aero4.unstablemail.com` | 216 | 216 |
| `srv4.unstablemail.com` | 215 | 215 |
| `emailfake.com` | 193 | 234 |
| `mx.emltmp.com` | 171 | 171 |
| `mx.spymail.one` | 165 | 165 |
| `email.chatgpt.org.uk` | 157 | 157 |
| `mx.emlpro.com` | 155 | 155 |
| `mx.dropmail.me` | 150 | 150 |
| `mail.casadorock.com` | 142 | 142 |
| `mx37.m1bp.com` | 137 | 137 |
| `mx37.mb5p.com` | 137 | 137 |
| `mx.freeml.net` | 135 | 135 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `78.47.124.133` | 920 | 920 |
| `94.130.108.80` | 920 | 920 |
| `116.202.9.167` | 464 | 504 |
| `46.101.111.206` | 464 | 504 |
| `91.196.52.205` | 457 | 637 |
| `142.132.166.12` | 449 | 489 |
| `188.166.111.252` | 449 | 489 |
| `188.245.74.208` | 426 | 427 |
| `195.201.18.63` | 405 | 406 |
| `162.159.205.11` | 389 | 397 |
| `162.159.205.12` | 389 | 397 |
| `162.159.205.13` | 389 | 397 |
| `162.159.205.23` | 385 | 393 |
| `162.159.205.24` | 385 | 393 |
| `162.159.205.25` | 385 | 393 |
| `162.159.205.17` | 379 | 387 |
| `162.159.205.18` | 379 | 387 |
| `162.159.205.19` | 379 | 387 |
| `13.223.25.84` | 347 | 347 |
| `54.243.117.197` | 347 | 347 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 205 |
| High-confidence disposable IPs | 410 |
| Promoted to `domains_inferred.txt` | 0 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**1680 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

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
| `13dk.net` | `route1.mx.cloudflare.net` |
| `14n.co.uk` | `14n-co-uk.mail.protection.outlook.com` |
| `14p.in` | `eforward1.registrar-servers.com` |
| `15qm-mail.red` | `eforward1.registrar-servers.com` |
| `189.email` | `route1.mx.cloudflare.net` |
| `1987.com` | `park-mx.above.com` |
| `1ayj8yi7lpiksxawav.gq` | `route1.mx.cloudflare.net` |


*… and 1,650 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
