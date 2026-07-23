# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-07-23 03:23 UTC**.*  
*Last DNS snapshot: **2026-07-23T03:06:15+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 74,569 |
| `domains_strict.txt` | 74,600 |
| `domains_inferred.txt` (opt-in) | 0 |

## Reachability

Of **75,264** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 11,729 | 15.6% |
| A_ONLY | 1,891 | 2.5% |
| NXDOMAIN | 19,381 | 25.8% |
| NO_RECORDS | 256 | 0.3% |
| TIMEOUT | 42,007 | 55.8% |

**13,620 domains are mail-reachable today** (18.1%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `mail.wabblywabble.com` | 616 | 662 |  |
| `mail.wallywatts.com` | 616 | 662 |  |
| `mx4.beavis99.com` | 558 | 559 |  |
| `mx4.beavis99.net` | 558 | 559 |  |
| `route1.mx.cloudflare.net` | 512 | 521 | yes |
| `route2.mx.cloudflare.net` | 512 | 521 | yes |
| `route3.mx.cloudflare.net` | 510 | 519 | yes |
| `generator.email` | 381 | 517 |  |
| `tinyhost.shop` | 337 | 337 |  |
| `park-mx.above.com` | 293 | 295 | yes |
| `email.gravityengine.cc` | 264 | 264 |  |
| `mx.emlhub.com` | 228 | 228 |  |
| `aspmx.l.google.com` | 220 | 222 | yes |
| `alt1.aspmx.l.google.com` | 213 | 215 | yes |
| `alt2.aspmx.l.google.com` | 211 | 213 | yes |
| `aero4.unstablemail.com` | 206 | 206 |  |
| `srv4.unstablemail.com` | 205 | 205 |  |
| `emailfake.com` | 191 | 232 |  |
| `eforward1.registrar-servers.com` | 173 | 176 | yes |
| `eforward2.registrar-servers.com` | 173 | 176 | yes |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 616 | 662 |
| `mail.wallywatts.com` | 616 | 662 |
| `mx4.beavis99.com` | 558 | 559 |
| `mx4.beavis99.net` | 558 | 559 |
| `generator.email` | 381 | 517 |
| `tinyhost.shop` | 337 | 337 |
| `email.gravityengine.cc` | 264 | 264 |
| `mx.emlhub.com` | 228 | 228 |
| `aero4.unstablemail.com` | 206 | 206 |
| `srv4.unstablemail.com` | 205 | 205 |
| `emailfake.com` | 191 | 232 |
| `mx.emltmp.com` | 166 | 166 |
| `mx.spymail.one` | 162 | 162 |
| `email.chatgpt.org.uk` | 156 | 156 |
| `mx.emlpro.com` | 154 | 154 |
| `mx.dropmail.me` | 147 | 147 |
| `mx37.m1bp.com` | 137 | 137 |
| `mx37.mb5p.com` | 137 | 137 |
| `mail.casadorock.com` | 135 | 135 |
| `mx.freeml.net` | 134 | 134 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `78.47.124.133` | 871 | 871 |
| `94.130.108.80` | 871 | 871 |
| `116.202.9.167` | 473 | 513 |
| `46.101.111.206` | 473 | 513 |
| `142.132.166.12` | 457 | 497 |
| `188.166.111.252` | 457 | 497 |
| `91.196.52.205` | 452 | 634 |
| `188.245.74.208` | 428 | 429 |
| `162.159.205.11` | 408 | 416 |
| `162.159.205.12` | 408 | 416 |
| `162.159.205.13` | 408 | 416 |
| `195.201.18.63` | 408 | 409 |
| `162.159.205.23` | 404 | 412 |
| `162.159.205.24` | 404 | 412 |
| `162.159.205.25` | 404 | 412 |
| `162.159.205.17` | 398 | 406 |
| `162.159.205.18` | 398 | 406 |
| `162.159.205.19` | 398 | 406 |
| `13.223.25.84` | 340 | 340 |
| `54.243.117.197` | 340 | 340 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 199 |
| High-confidence disposable IPs | 399 |
| Promoted to `domains_inferred.txt` | 0 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**1691 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

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


*… and 1,661 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
