# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-07-26 04:21 UTC**.*  
*Last DNS snapshot: **2026-07-26T04:08:56+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 74,620 |
| `domains_strict.txt` | 74,651 |
| `domains_inferred.txt` (opt-in) | 0 |

## Reachability

Of **75,330** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 11,590 | 15.4% |
| A_ONLY | 1,902 | 2.5% |
| NXDOMAIN | 20,165 | 26.8% |
| NO_RECORDS | 287 | 0.4% |
| TIMEOUT | 41,386 | 54.9% |

**13,492 domains are mail-reachable today** (17.9%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `mail.wabblywabble.com` | 651 | 698 |  |
| `mail.wallywatts.com` | 651 | 698 |  |
| `route2.mx.cloudflare.net` | 497 | 506 | yes |
| `route1.mx.cloudflare.net` | 496 | 505 | yes |
| `route3.mx.cloudflare.net` | 496 | 505 | yes |
| `mx4.beavis99.com` | 489 | 490 |  |
| `mx4.beavis99.net` | 489 | 490 |  |
| `generator.email` | 380 | 515 |  |
| `tinyhost.shop` | 332 | 332 |  |
| `park-mx.above.com` | 253 | 255 | yes |
| `emailfake.com` | 250 | 291 |  |
| `mx.emlhub.com` | 242 | 242 |  |
| `aspmx.l.google.com` | 224 | 226 | yes |
| `alt1.aspmx.l.google.com` | 223 | 225 | yes |
| `alt2.aspmx.l.google.com` | 219 | 221 | yes |
| `aero4.unstablemail.com` | 216 | 216 |  |
| `srv4.unstablemail.com` | 215 | 215 |  |
| `eforward1.registrar-servers.com` | 181 | 184 | yes |
| `eforward2.registrar-servers.com` | 181 | 184 | yes |
| `eforward3.registrar-servers.com` | 181 | 184 | yes |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 651 | 698 |
| `mail.wallywatts.com` | 651 | 698 |
| `mx4.beavis99.com` | 489 | 490 |
| `mx4.beavis99.net` | 489 | 490 |
| `generator.email` | 380 | 515 |
| `tinyhost.shop` | 332 | 332 |
| `emailfake.com` | 250 | 291 |
| `mx.emlhub.com` | 242 | 242 |
| `aero4.unstablemail.com` | 216 | 216 |
| `srv4.unstablemail.com` | 215 | 215 |
| `email.gravityengine.cc` | 178 | 178 |
| `mx.emltmp.com` | 172 | 172 |
| `mx.spymail.one` | 162 | 162 |
| `email.chatgpt.org.uk` | 152 | 152 |
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
| `91.196.52.205` | 512 | 693 |
| `142.132.166.12` | 487 | 528 |
| `188.166.111.252` | 487 | 528 |
| `116.202.9.167` | 471 | 511 |
| `46.101.111.206` | 471 | 511 |
| `13.223.25.84` | 395 | 395 |
| `54.243.117.197` | 395 | 395 |
| `162.159.205.23` | 387 | 395 |
| `162.159.205.24` | 387 | 395 |
| `162.159.205.25` | 387 | 395 |
| `162.159.205.17` | 385 | 393 |
| `162.159.205.18` | 385 | 393 |
| `162.159.205.19` | 385 | 393 |
| `162.159.205.11` | 375 | 383 |
| `162.159.205.12` | 375 | 383 |
| `162.159.205.13` | 375 | 383 |
| `188.245.74.208` | 365 | 366 |
| `195.201.18.63` | 349 | 350 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 205 |
| High-confidence disposable IPs | 445 |
| Promoted to `domains_inferred.txt` | 0 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**1651 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

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


*… and 1,621 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
