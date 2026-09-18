# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-09-18 02:20 UTC**.*  
*Last DNS snapshot: **2026-09-18T02:20:22+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 75,293 |
| `domains_strict.txt` | 75,324 |
| `domains_inferred.txt` (opt-in) | 2 |

## Reachability

Of **76,323** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 23,323 | 30.6% |
| A_ONLY | 5,403 | 7.1% |
| NXDOMAIN | 41,456 | 54.3% |
| NO_RECORDS | 800 | 1.0% |
| TIMEOUT | 5,341 | 7.0% |

**28,726 domains are mail-reachable today** (37.6%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `mail.wabblywabble.com` | 1292 | 1365 |  |
| `mail.wallywatts.com` | 1292 | 1365 |  |
| `mx4.beavis99.com` | 1140 | 1141 |  |
| `mx4.beavis99.net` | 1140 | 1141 |  |
| `route2.mx.cloudflare.net` | 984 | 996 | yes |
| `route1.mx.cloudflare.net` | 983 | 995 | yes |
| `route3.mx.cloudflare.net` | 982 | 994 | yes |
| `generator.email` | 693 | 830 |  |
| `park-mx.above.com` | 502 | 507 | yes |
| `aero4.unstablemail.com` | 477 | 477 |  |
| `srv4.unstablemail.com` | 477 | 477 |  |
| `aspmx.l.google.com` | 444 | 446 | yes |
| `alt1.aspmx.l.google.com` | 436 | 438 | yes |
| `alt2.aspmx.l.google.com` | 432 | 434 | yes |
| `mx.emlhub.com` | 432 | 432 |  |
| `emailfake.com` | 428 | 465 |  |
| `email.chatgpt.org.uk` | 414 | 414 |  |
| `email.gravityengine.cc` | 373 | 373 |  |
| `mx.spymail.one` | 368 | 368 |  |
| `mx.emltmp.com` | 365 | 365 |  |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 1292 | 1365 |
| `mail.wallywatts.com` | 1292 | 1365 |
| `mx4.beavis99.com` | 1140 | 1141 |
| `mx4.beavis99.net` | 1140 | 1141 |
| `generator.email` | 693 | 830 |
| `aero4.unstablemail.com` | 477 | 477 |
| `srv4.unstablemail.com` | 477 | 477 |
| `mx.emlhub.com` | 432 | 432 |
| `emailfake.com` | 428 | 465 |
| `email.chatgpt.org.uk` | 414 | 414 |
| `email.gravityengine.cc` | 373 | 373 |
| `mx.spymail.one` | 368 | 368 |
| `mx.emltmp.com` | 365 | 365 |
| `mx.emlpro.com` | 348 | 348 |
| `mx.dropmail.me` | 328 | 328 |
| `mx.freeml.net` | 307 | 307 |
| `tinyhost.shop` | 306 | 306 |
| `vietxf.com` | 272 | 272 |
| `mx.yomail.info` | 238 | 238 |
| `mail.casadorock.com` | 236 | 236 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `78.47.124.133` | 2537 | 2537 |
| `94.130.108.80` | 2537 | 2537 |
| `116.202.9.167` | 1259 | 1323 |
| `46.101.111.206` | 1259 | 1323 |
| `142.132.166.12` | 1255 | 1320 |
| `188.166.111.252` | 1255 | 1320 |
| `91.196.52.205` | 1176 | 1350 |
| `188.245.74.208` | 1126 | 1127 |
| `195.201.18.63` | 1112 | 1113 |
| `13.223.25.84` | 1103 | 1104 |
| `54.243.117.197` | 1103 | 1104 |
| `162.159.205.23` | 991 | 1001 |
| `162.159.205.24` | 991 | 1001 |
| `162.159.205.25` | 991 | 1001 |
| `162.159.205.17` | 989 | 1000 |
| `162.159.205.18` | 989 | 1000 |
| `162.159.205.19` | 989 | 1000 |
| `162.159.205.11` | 982 | 992 |
| `162.159.205.12` | 982 | 992 |
| `162.159.205.13` | 982 | 992 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 306 |
| High-confidence disposable IPs | 782 |
| Promoted to `domains_inferred.txt` | 2 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**3335 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

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
| `0regon.org` | `route1.mx.cloudflare.net` |
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


*… and 3,305 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
