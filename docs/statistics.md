# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-09-19 02:22 UTC**.*  
*Last DNS snapshot: **2026-09-19T02:16:42+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 75,297 |
| `domains_strict.txt` | 75,328 |
| `domains_inferred.txt` (opt-in) | 2 |

## Reachability

Of **76,333** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 23,317 | 30.5% |
| A_ONLY | 5,390 | 7.1% |
| NXDOMAIN | 41,484 | 54.3% |
| NO_RECORDS | 801 | 1.0% |
| TIMEOUT | 5,341 | 7.0% |

**28,707 domains are mail-reachable today** (37.6%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `mail.wabblywabble.com` | 1290 | 1364 |  |
| `mail.wallywatts.com` | 1290 | 1364 |  |
| `mx4.beavis99.com` | 1142 | 1143 |  |
| `mx4.beavis99.net` | 1142 | 1143 |  |
| `route2.mx.cloudflare.net` | 992 | 1005 | yes |
| `route1.mx.cloudflare.net` | 991 | 1004 | yes |
| `route3.mx.cloudflare.net` | 990 | 1003 | yes |
| `generator.email` | 697 | 834 |  |
| `park-mx.above.com` | 502 | 507 | yes |
| `aero4.unstablemail.com` | 475 | 475 |  |
| `srv4.unstablemail.com` | 475 | 475 |  |
| `aspmx.l.google.com` | 448 | 450 | yes |
| `alt1.aspmx.l.google.com` | 440 | 442 | yes |
| `alt2.aspmx.l.google.com` | 436 | 438 | yes |
| `mx.emlhub.com` | 431 | 431 |  |
| `emailfake.com` | 424 | 461 |  |
| `email.chatgpt.org.uk` | 407 | 407 |  |
| `email.gravityengine.cc` | 374 | 374 |  |
| `mx.spymail.one` | 371 | 371 |  |
| `mx.emltmp.com` | 365 | 365 |  |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 1290 | 1364 |
| `mail.wallywatts.com` | 1290 | 1364 |
| `mx4.beavis99.com` | 1142 | 1143 |
| `mx4.beavis99.net` | 1142 | 1143 |
| `generator.email` | 697 | 834 |
| `aero4.unstablemail.com` | 475 | 475 |
| `srv4.unstablemail.com` | 475 | 475 |
| `mx.emlhub.com` | 431 | 431 |
| `emailfake.com` | 424 | 461 |
| `email.chatgpt.org.uk` | 407 | 407 |
| `email.gravityengine.cc` | 374 | 374 |
| `mx.spymail.one` | 371 | 371 |
| `mx.emltmp.com` | 365 | 365 |
| `mx.emlpro.com` | 350 | 350 |
| `mx.dropmail.me` | 329 | 329 |
| `tinyhost.shop` | 310 | 310 |
| `mx.freeml.net` | 308 | 308 |
| `vietxf.com` | 272 | 272 |
| `mx.yomail.info` | 238 | 238 |
| `mail.casadorock.com` | 235 | 235 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `78.47.124.133` | 2541 | 2541 |
| `94.130.108.80` | 2541 | 2541 |
| `116.202.9.167` | 1261 | 1326 |
| `46.101.111.206` | 1261 | 1326 |
| `142.132.166.12` | 1254 | 1320 |
| `188.166.111.252` | 1254 | 1320 |
| `91.196.52.205` | 1179 | 1353 |
| `188.245.74.208` | 1128 | 1129 |
| `195.201.18.63` | 1113 | 1114 |
| `13.223.25.84` | 1100 | 1101 |
| `54.243.117.197` | 1100 | 1101 |
| `162.159.205.23` | 996 | 1007 |
| `162.159.205.24` | 996 | 1007 |
| `162.159.205.25` | 996 | 1007 |
| `162.159.205.17` | 994 | 1006 |
| `162.159.205.18` | 994 | 1006 |
| `162.159.205.19` | 994 | 1006 |
| `162.159.205.11` | 985 | 996 |
| `162.159.205.12` | 985 | 996 |
| `162.159.205.13` | 985 | 996 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 307 |
| High-confidence disposable IPs | 794 |
| Promoted to `domains_inferred.txt` | 2 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**3339 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

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


*… and 3,309 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
