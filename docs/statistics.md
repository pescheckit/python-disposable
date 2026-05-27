# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-05-27 03:35 UTC**.*  
*Last DNS snapshot: **2026-05-27T03:12:08+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 72,247 |
| `domains_strict.txt` | 72,278 |
| `domains_inferred.txt` (opt-in) | 1 |

## Reachability

Of **72,684** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 10,763 | 14.8% |
| A_ONLY | 1,645 | 2.3% |
| NXDOMAIN | 19,792 | 27.2% |
| NO_RECORDS | 243 | 0.3% |
| TIMEOUT | 40,241 | 55.4% |

**12,408 domains are mail-reachable today** (17.1%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `mail.wabblywabble.com` | 691 | 704 |  |
| `mail.wallywatts.com` | 691 | 704 |  |
| `mx4.beavis99.com` | 490 | 490 |  |
| `mx4.beavis99.net` | 490 | 490 |  |
| `generator.email` | 412 | 551 |  |
| `route1.mx.cloudflare.net` | 368 | 372 | yes |
| `route2.mx.cloudflare.net` | 368 | 372 | yes |
| `route3.mx.cloudflare.net` | 368 | 372 | yes |
| `park-mx.above.com` | 278 | 279 | yes |
| `mx.emlhub.com` | 264 | 264 |  |
| `emailfake.com` | 230 | 281 |  |
| `aspmx.l.google.com` | 227 | 227 | yes |
| `alt1.aspmx.l.google.com` | 220 | 220 | yes |
| `alt2.aspmx.l.google.com` | 218 | 218 | yes |
| `aero4.unstablemail.com` | 198 | 198 |  |
| `srv4.unstablemail.com` | 198 | 198 |  |
| `eforward1.registrar-servers.com` | 179 | 180 | yes |
| `eforward2.registrar-servers.com` | 179 | 180 | yes |
| `eforward3.registrar-servers.com` | 179 | 180 | yes |
| `eforward4.registrar-servers.com` | 179 | 180 | yes |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 691 | 704 |
| `mail.wallywatts.com` | 691 | 704 |
| `mx4.beavis99.com` | 490 | 490 |
| `mx4.beavis99.net` | 490 | 490 |
| `generator.email` | 412 | 551 |
| `mx.emlhub.com` | 264 | 264 |
| `emailfake.com` | 230 | 281 |
| `aero4.unstablemail.com` | 198 | 198 |
| `srv4.unstablemail.com` | 198 | 198 |
| `mx.emlpro.com` | 169 | 169 |
| `mx.spymail.one` | 169 | 169 |
| `mx37.m1bp.com` | 161 | 161 |
| `mx37.mb5p.com` | 161 | 161 |
| `mx.emltmp.com` | 158 | 158 |
| `mx.dropmail.me` | 139 | 139 |
| `mx.freeml.net` | 134 | 134 |
| `mail.casadorock.com` | 126 | 126 |
| `mx.yomail.info` | 122 | 122 |
| `mail.h-email.net` | 105 | 105 |
| `localhost` | 103 | 103 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `78.47.124.133` | 820 | 820 |
| `94.130.108.80` | 820 | 820 |
| `91.196.52.205` | 494 | 681 |
| `142.132.166.12` | 486 | 499 |
| `188.166.111.252` | 486 | 499 |
| `116.202.9.167` | 471 | 483 |
| `46.101.111.206` | 471 | 483 |
| `188.245.74.208` | 322 | 322 |
| `13.223.25.84` | 313 | 313 |
| `54.243.117.197` | 313 | 313 |
| `195.201.18.63` | 309 | 309 |
| `147.182.130.78` | 282 | 283 |
| `147.182.160.18` | 282 | 283 |
| `147.182.180.139` | 282 | 283 |
| `147.182.189.184` | 282 | 283 |
| `164.90.197.105` | 282 | 283 |
| `164.90.197.143` | 282 | 283 |
| `164.90.197.162` | 282 | 283 |
| `164.90.197.79` | 282 | 283 |
| `162.159.205.23` | 258 | 261 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 205 |
| High-confidence disposable IPs | 362 |
| Promoted to `domains_inferred.txt` | 1 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**1527 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

| Listed disposable | MX (shared infra) |
|---|---|
| `0-30-24.com` | `alt1.aspmx.l.google.com` |
| `0-mail.com` | `park-mx.above.com` |
| `0058.ru` | `alt1.aspmx.l.google.com` |
| `01g.cloud` | `alt1.aspmx.l.google.com` |
| `0ak.org` | `mx00.ionos.com` |
| `0hcow.com` | `mxa.mailgun.org` |
| `0hio.net` | `aspmx1.migadu.com` |
| `0ioi.net` | `route1.mx.cloudflare.net` |
| `0live.org` | `route1.mx.cloudflare.net` |
| `0nce.net` | `route1.mx.cloudflare.net` |
| `0ne0ut.com` | `route1.mx.cloudflare.net` |
| `0rg.fr` | `mx1.mail.ovh.net` |
| `0xmiikee.com` | `eforward1.registrar-servers.com` |
| `1-8.biz` | `mail.protonmail.ch` |
| `1-box.ru` | `mx.yandex.ru` |
| `10bir.com` | `route1.mx.cloudflare.net` |
| `10dkmail.net` | `smtp.google.com` |
| `10inbox.online` | `route1.mx.cloudflare.net` |
| `10m.email` | `eforward1.registrar-servers.com` |
| `10mi.org` | `alt1.aspmx.l.google.com` |
| `10minemail.com` | `route1.mx.cloudflare.net` |
| `10minutemail.co.za` | `route1.mx.cloudflare.net` |
| `10x10-bet.com` | `eforward1.registrar-servers.com` |
| `111gmail.com` | `park-mx.above.com` |
| `11cows.com` | `mxa.mailgun.org` |
| `123gmail.com` | `park-mx.above.com` |
| `12499aaa.com` | `eforward1.registrar-servers.com` |
| `13dk.net` | `route1.mx.cloudflare.net` |
| `143gmail.com` | `park-mx.above.com` |
| `14n.co.uk` | `14n-co-uk.mail.protection.outlook.com` |


*… and 1,497 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
