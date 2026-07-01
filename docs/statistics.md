# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-07-01 03:26 UTC**.*  
*Last DNS snapshot: **2026-07-01T03:14:47+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 74,297 |
| `domains_strict.txt` | 74,328 |
| `domains_inferred.txt` (opt-in) | 2 |

## Reachability

Of **74,877** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 23,129 | 30.9% |
| A_ONLY | 5,167 | 6.9% |
| NXDOMAIN | 40,895 | 54.6% |
| NO_RECORDS | 707 | 0.9% |
| TIMEOUT | 4,979 | 6.6% |

**28,296 domains are mail-reachable today** (37.8%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `mail.wabblywabble.com` | 1338 | 1376 |  |
| `mail.wallywatts.com` | 1338 | 1376 |  |
| `mx4.beavis99.com` | 1016 | 1017 |  |
| `mx4.beavis99.net` | 1015 | 1016 |  |
| `route1.mx.cloudflare.net` | 843 | 850 | yes |
| `route2.mx.cloudflare.net` | 843 | 850 | yes |
| `route3.mx.cloudflare.net` | 841 | 848 | yes |
| `generator.email` | 774 | 922 |  |
| `park-mx.above.com` | 636 | 638 | yes |
| `email.gravityengine.cc` | 582 | 582 |  |
| `aspmx.l.google.com` | 458 | 459 | yes |
| `alt1.aspmx.l.google.com` | 449 | 450 | yes |
| `mx.emlhub.com` | 448 | 448 |  |
| `alt2.aspmx.l.google.com` | 445 | 446 | yes |
| `aero4.unstablemail.com` | 433 | 433 |  |
| `srv4.unstablemail.com` | 433 | 433 |  |
| `emailfake.com` | 432 | 477 |  |
| `mx.spymail.one` | 370 | 370 |  |
| `mx.emltmp.com` | 363 | 363 |  |
| `mx.emlpro.com` | 352 | 352 |  |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 1338 | 1376 |
| `mail.wallywatts.com` | 1338 | 1376 |
| `mx4.beavis99.com` | 1016 | 1017 |
| `mx4.beavis99.net` | 1015 | 1016 |
| `generator.email` | 774 | 922 |
| `email.gravityengine.cc` | 582 | 582 |
| `mx.emlhub.com` | 448 | 448 |
| `aero4.unstablemail.com` | 433 | 433 |
| `srv4.unstablemail.com` | 433 | 433 |
| `emailfake.com` | 432 | 477 |
| `mx.spymail.one` | 370 | 370 |
| `mx.emltmp.com` | 363 | 363 |
| `mx.emlpro.com` | 352 | 352 |
| `mx.dropmail.me` | 319 | 319 |
| `tinyhost.shop` | 308 | 308 |
| `mx.freeml.net` | 301 | 301 |
| `mx.yomail.info` | 249 | 249 |
| `mx37.m1bp.com` | 246 | 246 |
| `mx37.mb5p.com` | 246 | 246 |
| `mx156.hostedmxserver.com` | 222 | 222 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `78.47.124.133` | 2506 | 2506 |
| `94.130.108.80` | 2506 | 2506 |
| `116.202.9.167` | 1305 | 1339 |
| `46.101.111.206` | 1305 | 1339 |
| `142.132.166.12` | 1289 | 1324 |
| `188.166.111.252` | 1289 | 1324 |
| `91.196.52.205` | 1274 | 1473 |
| `13.223.25.84` | 1070 | 1070 |
| `54.243.117.197` | 1070 | 1070 |
| `188.245.74.208` | 993 | 994 |
| `195.201.18.63` | 979 | 980 |
| `162.159.205.17` | 858 | 864 |
| `162.159.205.18` | 858 | 864 |
| `162.159.205.19` | 858 | 864 |
| `162.159.205.23` | 856 | 862 |
| `162.159.205.24` | 856 | 862 |
| `162.159.205.25` | 856 | 862 |
| `162.159.205.11` | 845 | 851 |
| `162.159.205.12` | 845 | 851 |
| `162.159.205.13` | 845 | 851 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 298 |
| High-confidence disposable IPs | 777 |
| Promoted to `domains_inferred.txt` | 2 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**3281 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

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


*… and 3,251 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
