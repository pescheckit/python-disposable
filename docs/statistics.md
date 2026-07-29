# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-07-29 03:21 UTC**.*  
*Last DNS snapshot: **2026-07-29T03:05:09+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 74,655 |
| `domains_strict.txt` | 74,686 |
| `domains_inferred.txt` (opt-in) | 0 |

## Reachability

Of **75,381** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 11,625 | 15.4% |
| A_ONLY | 1,910 | 2.5% |
| NXDOMAIN | 20,171 | 26.8% |
| NO_RECORDS | 288 | 0.4% |
| TIMEOUT | 41,387 | 54.9% |

**13,535 domains are mail-reachable today** (18.0%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `mail.wabblywabble.com` | 650 | 698 |  |
| `mail.wallywatts.com` | 650 | 698 |  |
| `route2.mx.cloudflare.net` | 503 | 512 | yes |
| `route1.mx.cloudflare.net` | 502 | 511 | yes |
| `route3.mx.cloudflare.net` | 502 | 511 | yes |
| `mx4.beavis99.com` | 489 | 490 |  |
| `mx4.beavis99.net` | 489 | 490 |  |
| `generator.email` | 383 | 519 |  |
| `tinyhost.shop` | 331 | 331 |  |
| `park-mx.above.com` | 252 | 255 | yes |
| `emailfake.com` | 251 | 291 |  |
| `mx.emlhub.com` | 242 | 242 |  |
| `aspmx.l.google.com` | 223 | 225 | yes |
| `alt1.aspmx.l.google.com` | 222 | 224 | yes |
| `alt2.aspmx.l.google.com` | 218 | 220 | yes |
| `aero4.unstablemail.com` | 216 | 216 |  |
| `srv4.unstablemail.com` | 215 | 215 |  |
| `eforward1.registrar-servers.com` | 181 | 184 | yes |
| `eforward2.registrar-servers.com` | 181 | 184 | yes |
| `eforward3.registrar-servers.com` | 181 | 184 | yes |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 650 | 698 |
| `mail.wallywatts.com` | 650 | 698 |
| `mx4.beavis99.com` | 489 | 490 |
| `mx4.beavis99.net` | 489 | 490 |
| `generator.email` | 383 | 519 |
| `tinyhost.shop` | 331 | 331 |
| `emailfake.com` | 251 | 291 |
| `mx.emlhub.com` | 242 | 242 |
| `aero4.unstablemail.com` | 216 | 216 |
| `srv4.unstablemail.com` | 215 | 215 |
| `email.gravityengine.cc` | 179 | 179 |
| `email.chatgpt.org.uk` | 175 | 175 |
| `mx.emltmp.com` | 172 | 172 |
| `mx.spymail.one` | 162 | 162 |
| `mx.emlpro.com` | 151 | 151 |
| `mx.dropmail.me` | 150 | 150 |
| `mail.casadorock.com` | 142 | 142 |
| `mx.freeml.net` | 126 | 126 |
| `mx37.m1bp.com` | 119 | 119 |
| `mx37.mb5p.com` | 119 | 119 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `78.47.124.133` | 897 | 897 |
| `94.130.108.80` | 897 | 897 |
| `91.196.52.205` | 518 | 698 |
| `142.132.166.12` | 486 | 528 |
| `188.166.111.252` | 486 | 528 |
| `116.202.9.167` | 470 | 511 |
| `46.101.111.206` | 470 | 511 |
| `13.223.25.84` | 395 | 395 |
| `54.243.117.197` | 395 | 395 |
| `162.159.205.23` | 393 | 401 |
| `162.159.205.24` | 393 | 401 |
| `162.159.205.25` | 393 | 401 |
| `162.159.205.17` | 391 | 399 |
| `162.159.205.18` | 391 | 399 |
| `162.159.205.19` | 391 | 399 |
| `162.159.205.11` | 381 | 389 |
| `162.159.205.12` | 381 | 389 |
| `162.159.205.13` | 381 | 389 |
| `188.245.74.208` | 365 | 366 |
| `195.201.18.63` | 349 | 350 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 205 |
| High-confidence disposable IPs | 436 |
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
| `13dk.net` | `route1.mx.cloudflare.net` |
| `14n.co.uk` | `14n-co-uk.mail.protection.outlook.com` |
| `14p.in` | `eforward1.registrar-servers.com` |
| `15qm-mail.red` | `eforward1.registrar-servers.com` |
| `189.email` | `route1.mx.cloudflare.net` |
| `1987.com` | `park-mx.above.com` |
| `1ayj8yi7lpiksxawav.gq` | `route1.mx.cloudflare.net` |


*… and 1,625 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
