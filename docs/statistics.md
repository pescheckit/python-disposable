# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-09-20 02:29 UTC**.*  
*Last DNS snapshot: **2026-09-20T02:24:05+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 75,297 |
| `domains_strict.txt` | 75,328 |
| `domains_inferred.txt` (opt-in) | 2 |

## Reachability

Of **76,339** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 23,352 | 30.6% |
| A_ONLY | 5,416 | 7.1% |
| NXDOMAIN | 41,562 | 54.4% |
| NO_RECORDS | 789 | 1.0% |
| TIMEOUT | 5,220 | 6.8% |

**28,768 domains are mail-reachable today** (37.7%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `mail.wabblywabble.com` | 1277 | 1353 |  |
| `mail.wallywatts.com` | 1277 | 1353 |  |
| `mx4.beavis99.com` | 1148 | 1149 |  |
| `mx4.beavis99.net` | 1148 | 1149 |  |
| `route2.mx.cloudflare.net` | 982 | 995 | yes |
| `route1.mx.cloudflare.net` | 981 | 994 | yes |
| `route3.mx.cloudflare.net` | 980 | 993 | yes |
| `generator.email` | 680 | 817 |  |
| `park-mx.above.com` | 506 | 511 | yes |
| `aero4.unstablemail.com` | 478 | 478 |  |
| `srv4.unstablemail.com` | 478 | 478 |  |
| `aspmx.l.google.com` | 448 | 450 | yes |
| `alt1.aspmx.l.google.com` | 439 | 441 | yes |
| `alt2.aspmx.l.google.com` | 436 | 438 | yes |
| `mx.emlhub.com` | 435 | 435 |  |
| `emailfake.com` | 419 | 456 |  |
| `email.chatgpt.org.uk` | 401 | 401 |  |
| `mx.spymail.one` | 378 | 378 |  |
| `email.gravityengine.cc` | 374 | 374 |  |
| `mx.emltmp.com` | 367 | 367 |  |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 1277 | 1353 |
| `mail.wallywatts.com` | 1277 | 1353 |
| `mx4.beavis99.com` | 1148 | 1149 |
| `mx4.beavis99.net` | 1148 | 1149 |
| `generator.email` | 680 | 817 |
| `aero4.unstablemail.com` | 478 | 478 |
| `srv4.unstablemail.com` | 478 | 478 |
| `mx.emlhub.com` | 435 | 435 |
| `emailfake.com` | 419 | 456 |
| `email.chatgpt.org.uk` | 401 | 401 |
| `mx.spymail.one` | 378 | 378 |
| `email.gravityengine.cc` | 374 | 374 |
| `mx.emltmp.com` | 367 | 367 |
| `mx.emlpro.com` | 350 | 350 |
| `mx.dropmail.me` | 330 | 330 |
| `tinyhost.shop` | 328 | 328 |
| `mx.freeml.net` | 314 | 314 |
| `vietxf.com` | 272 | 272 |
| `mx.yomail.info` | 242 | 242 |
| `mail.casadorock.com` | 241 | 241 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `78.47.124.133` | 2560 | 2560 |
| `94.130.108.80` | 2560 | 2560 |
| `116.202.9.167` | 1254 | 1321 |
| `46.101.111.206` | 1254 | 1321 |
| `142.132.166.12` | 1252 | 1320 |
| `188.166.111.252` | 1252 | 1320 |
| `91.196.52.205` | 1153 | 1327 |
| `188.245.74.208` | 1135 | 1136 |
| `195.201.18.63` | 1121 | 1122 |
| `13.223.25.84` | 1108 | 1109 |
| `54.243.117.197` | 1108 | 1109 |
| `162.159.205.17` | 985 | 997 |
| `162.159.205.18` | 985 | 997 |
| `162.159.205.19` | 985 | 997 |
| `162.159.205.23` | 985 | 996 |
| `162.159.205.24` | 985 | 996 |
| `162.159.205.25` | 985 | 996 |
| `162.159.205.11` | 975 | 986 |
| `162.159.205.12` | 975 | 986 |
| `162.159.205.13` | 975 | 986 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 309 |
| High-confidence disposable IPs | 788 |
| Promoted to `domains_inferred.txt` | 2 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**3338 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

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


*… and 3,308 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
