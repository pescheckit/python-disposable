# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-09-09 02:22 UTC**.*  
*Last DNS snapshot: **2026-09-09T02:15:22+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 75,264 |
| `domains_strict.txt` | 75,295 |
| `domains_inferred.txt` (opt-in) | 2 |

## Reachability

Of **76,233** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 21,970 | 28.8% |
| A_ONLY | 4,934 | 6.5% |
| NXDOMAIN | 39,295 | 51.5% |
| NO_RECORDS | 729 | 1.0% |
| TIMEOUT | 9,305 | 12.2% |

**26,904 domains are mail-reachable today** (35.3%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `mail.wabblywabble.com` | 1209 | 1278 |  |
| `mail.wallywatts.com` | 1209 | 1278 |  |
| `mx4.beavis99.com` | 1050 | 1051 |  |
| `mx4.beavis99.net` | 1050 | 1051 |  |
| `route2.mx.cloudflare.net` | 908 | 919 | yes |
| `route1.mx.cloudflare.net` | 907 | 918 | yes |
| `route3.mx.cloudflare.net` | 906 | 917 | yes |
| `generator.email` | 722 | 859 |  |
| `park-mx.above.com` | 478 | 483 | yes |
| `aero4.unstablemail.com` | 432 | 432 |  |
| `mx.emlhub.com` | 432 | 432 |  |
| `srv4.unstablemail.com` | 432 | 432 |  |
| `emailfake.com` | 431 | 468 |  |
| `aspmx.l.google.com` | 411 | 413 | yes |
| `alt1.aspmx.l.google.com` | 402 | 404 | yes |
| `alt2.aspmx.l.google.com` | 398 | 400 | yes |
| `mx.spymail.one` | 353 | 353 |  |
| `tinyhost.shop` | 338 | 338 |  |
| `mx.emltmp.com` | 337 | 337 |  |
| `mx.emlpro.com` | 330 | 330 |  |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 1209 | 1278 |
| `mail.wallywatts.com` | 1209 | 1278 |
| `mx4.beavis99.com` | 1050 | 1051 |
| `mx4.beavis99.net` | 1050 | 1051 |
| `generator.email` | 722 | 859 |
| `aero4.unstablemail.com` | 432 | 432 |
| `mx.emlhub.com` | 432 | 432 |
| `srv4.unstablemail.com` | 432 | 432 |
| `emailfake.com` | 431 | 468 |
| `mx.spymail.one` | 353 | 353 |
| `tinyhost.shop` | 338 | 338 |
| `mx.emltmp.com` | 337 | 337 |
| `mx.emlpro.com` | 330 | 330 |
| `email.chatgpt.org.uk` | 323 | 323 |
| `mx.dropmail.me` | 315 | 315 |
| `mx.freeml.net` | 288 | 288 |
| `vietxf.com` | 250 | 250 |
| `mail.casadorock.com` | 243 | 243 |
| `mx.yomail.info` | 226 | 226 |
| `mx37.m1bp.com` | 217 | 217 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `78.47.124.133` | 2411 | 2411 |
| `94.130.108.80` | 2411 | 2411 |
| `91.196.52.205` | 1207 | 1381 |
| `116.202.9.167` | 1179 | 1239 |
| `46.101.111.206` | 1179 | 1239 |
| `142.132.166.12` | 1175 | 1236 |
| `188.166.111.252` | 1175 | 1236 |
| `188.245.74.208` | 1025 | 1026 |
| `195.201.18.63` | 1015 | 1016 |
| `13.223.25.84` | 1006 | 1006 |
| `54.243.117.197` | 1006 | 1006 |
| `162.159.205.23` | 913 | 922 |
| `162.159.205.24` | 913 | 922 |
| `162.159.205.25` | 913 | 922 |
| `162.159.205.17` | 910 | 920 |
| `162.159.205.18` | 910 | 920 |
| `162.159.205.19` | 910 | 920 |
| `162.159.205.11` | 908 | 917 |
| `162.159.205.12` | 908 | 917 |
| `162.159.205.13` | 908 | 917 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 284 |
| High-confidence disposable IPs | 782 |
| Promoted to `domains_inferred.txt` | 2 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**3098 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

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
| `117.yyolf.net` | `route1.mx.cloudflare.net` |
| `11cows.com` | `mxa.mailgun.org` |
| `123gmail.com` | `park-mx.above.com` |
| `12499aaa.com` | `eforward1.registrar-servers.com` |
| `12storage.com` | `route1.mx.cloudflare.net` |
| `13dk.net` | `route1.mx.cloudflare.net` |
| `14n.co.uk` | `14n-co-uk.mail.protection.outlook.com` |
| `14p.in` | `eforward1.registrar-servers.com` |
| `15qm-mail.red` | `eforward1.registrar-servers.com` |
| `189.email` | `route1.mx.cloudflare.net` |
| `1987.com` | `park-mx.above.com` |


*… and 3,068 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
