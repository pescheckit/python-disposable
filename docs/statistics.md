# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-09-11 02:24 UTC**.*  
*Last DNS snapshot: **2026-09-11T02:18:06+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 75,277 |
| `domains_strict.txt` | 75,308 |
| `domains_inferred.txt` (opt-in) | 2 |

## Reachability

Of **76,263** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 22,623 | 29.7% |
| A_ONLY | 5,100 | 6.7% |
| NXDOMAIN | 39,483 | 51.8% |
| NO_RECORDS | 752 | 1.0% |
| TIMEOUT | 8,305 | 10.9% |

**27,723 domains are mail-reachable today** (36.4%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `mail.wabblywabble.com` | 1262 | 1331 |  |
| `mail.wallywatts.com` | 1262 | 1331 |  |
| `mx4.beavis99.com` | 1085 | 1086 |  |
| `mx4.beavis99.net` | 1085 | 1086 |  |
| `route2.mx.cloudflare.net` | 956 | 967 | yes |
| `route1.mx.cloudflare.net` | 955 | 966 | yes |
| `route3.mx.cloudflare.net` | 954 | 965 | yes |
| `generator.email` | 723 | 860 |  |
| `park-mx.above.com` | 489 | 494 | yes |
| `aero4.unstablemail.com` | 449 | 449 |  |
| `srv4.unstablemail.com` | 449 | 449 |  |
| `mx.emlhub.com` | 441 | 441 |  |
| `emailfake.com` | 433 | 470 |  |
| `aspmx.l.google.com` | 428 | 430 | yes |
| `alt1.aspmx.l.google.com` | 419 | 421 | yes |
| `alt2.aspmx.l.google.com` | 415 | 417 | yes |
| `email.chatgpt.org.uk` | 402 | 402 |  |
| `email.gravityengine.cc` | 368 | 368 |  |
| `mx.spymail.one` | 361 | 361 |  |
| `mx.emltmp.com` | 352 | 352 |  |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 1262 | 1331 |
| `mail.wallywatts.com` | 1262 | 1331 |
| `mx4.beavis99.com` | 1085 | 1086 |
| `mx4.beavis99.net` | 1085 | 1086 |
| `generator.email` | 723 | 860 |
| `aero4.unstablemail.com` | 449 | 449 |
| `srv4.unstablemail.com` | 449 | 449 |
| `mx.emlhub.com` | 441 | 441 |
| `emailfake.com` | 433 | 470 |
| `email.chatgpt.org.uk` | 402 | 402 |
| `email.gravityengine.cc` | 368 | 368 |
| `mx.spymail.one` | 361 | 361 |
| `mx.emltmp.com` | 352 | 352 |
| `tinyhost.shop` | 337 | 337 |
| `mx.emlpro.com` | 324 | 324 |
| `mx.dropmail.me` | 309 | 309 |
| `mx.freeml.net` | 298 | 298 |
| `vietxf.com` | 250 | 250 |
| `mail.casadorock.com` | 235 | 235 |
| `mx.yomail.info` | 229 | 229 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `78.47.124.133` | 2455 | 2455 |
| `94.130.108.80` | 2455 | 2455 |
| `116.202.9.167` | 1232 | 1292 |
| `46.101.111.206` | 1232 | 1292 |
| `142.132.166.12` | 1231 | 1292 |
| `188.166.111.252` | 1231 | 1292 |
| `91.196.52.205` | 1216 | 1390 |
| `188.245.74.208` | 1068 | 1069 |
| `195.201.18.63` | 1055 | 1056 |
| `13.223.25.84` | 1040 | 1040 |
| `54.243.117.197` | 1040 | 1040 |
| `162.159.205.17` | 964 | 974 |
| `162.159.205.18` | 964 | 974 |
| `162.159.205.19` | 964 | 974 |
| `162.159.205.23` | 961 | 970 |
| `162.159.205.24` | 961 | 970 |
| `162.159.205.25` | 961 | 970 |
| `162.159.205.11` | 959 | 968 |
| `162.159.205.12` | 959 | 968 |
| `162.159.205.13` | 959 | 968 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 295 |
| High-confidence disposable IPs | 809 |
| Promoted to `domains_inferred.txt` | 2 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**3197 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

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


*… and 3,167 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
