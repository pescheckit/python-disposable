# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-07-15 03:18 UTC**.*  
*Last DNS snapshot: **2026-07-15T03:05:25+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 74,499 |
| `domains_strict.txt` | 74,530 |
| `domains_inferred.txt` (opt-in) | 2 |

## Reachability

Of **75,157** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 20,896 | 27.8% |
| A_ONLY | 4,745 | 6.3% |
| NXDOMAIN | 37,011 | 49.2% |
| NO_RECORDS | 654 | 0.9% |
| TIMEOUT | 11,851 | 15.8% |

**25,641 domains are mail-reachable today** (34.1%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `mail.wabblywabble.com` | 1184 | 1227 |  |
| `mail.wallywatts.com` | 1184 | 1227 |  |
| `mx4.beavis99.com` | 970 | 971 |  |
| `mx4.beavis99.net` | 970 | 971 |  |
| `route1.mx.cloudflare.net` | 869 | 878 | yes |
| `route2.mx.cloudflare.net` | 869 | 878 | yes |
| `route3.mx.cloudflare.net` | 867 | 876 | yes |
| `generator.email` | 712 | 849 |  |
| `park-mx.above.com` | 553 | 555 | yes |
| `mx.emlhub.com` | 419 | 419 |  |
| `aspmx.l.google.com` | 406 | 408 | yes |
| `aero4.unstablemail.com` | 400 | 400 |  |
| `srv4.unstablemail.com` | 400 | 400 |  |
| `alt1.aspmx.l.google.com` | 398 | 400 | yes |
| `alt2.aspmx.l.google.com` | 394 | 396 | yes |
| `emailfake.com` | 394 | 437 |  |
| `tinyhost.shop` | 392 | 392 |  |
| `mx.spymail.one` | 334 | 334 |  |
| `mx.emltmp.com` | 330 | 330 |  |
| `email.gravityengine.cc` | 310 | 310 |  |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 1184 | 1227 |
| `mail.wallywatts.com` | 1184 | 1227 |
| `mx4.beavis99.com` | 970 | 971 |
| `mx4.beavis99.net` | 970 | 971 |
| `generator.email` | 712 | 849 |
| `mx.emlhub.com` | 419 | 419 |
| `aero4.unstablemail.com` | 400 | 400 |
| `srv4.unstablemail.com` | 400 | 400 |
| `emailfake.com` | 394 | 437 |
| `tinyhost.shop` | 392 | 392 |
| `mx.spymail.one` | 334 | 334 |
| `mx.emltmp.com` | 330 | 330 |
| `email.gravityengine.cc` | 310 | 310 |
| `mx.emlpro.com` | 305 | 305 |
| `mx.dropmail.me` | 286 | 286 |
| `mx.freeml.net` | 284 | 284 |
| `mx37.m1bp.com` | 232 | 232 |
| `mx37.mb5p.com` | 232 | 232 |
| `mx.yomail.info` | 230 | 230 |
| `mail.casadorock.com` | 197 | 197 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `78.47.124.133` | 2260 | 2260 |
| `94.130.108.80` | 2260 | 2260 |
| `91.196.52.205` | 1162 | 1348 |
| `116.202.9.167` | 1149 | 1187 |
| `46.101.111.206` | 1149 | 1187 |
| `142.132.166.12` | 1144 | 1183 |
| `188.166.111.252` | 1144 | 1183 |
| `188.245.74.208` | 942 | 943 |
| `13.223.25.84` | 938 | 938 |
| `54.243.117.197` | 938 | 938 |
| `195.201.18.63` | 931 | 932 |
| `162.159.205.17` | 872 | 880 |
| `162.159.205.18` | 872 | 880 |
| `162.159.205.19` | 872 | 880 |
| `162.159.205.23` | 867 | 875 |
| `162.159.205.24` | 867 | 875 |
| `162.159.205.25` | 867 | 875 |
| `162.159.205.11` | 865 | 873 |
| `162.159.205.12` | 865 | 873 |
| `162.159.205.13` | 865 | 873 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 295 |
| High-confidence disposable IPs | 741 |
| Promoted to `domains_inferred.txt` | 2 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**3058 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

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
| `11cows.com` | `mxa.mailgun.org` |
| `123gmail.com` | `park-mx.above.com` |
| `12499aaa.com` | `eforward1.registrar-servers.com` |
| `13dk.net` | `route1.mx.cloudflare.net` |
| `14n.co.uk` | `14n-co-uk.mail.protection.outlook.com` |
| `14p.in` | `eforward1.registrar-servers.com` |
| `15qm-mail.red` | `eforward1.registrar-servers.com` |
| `189.email` | `route1.mx.cloudflare.net` |
| `1987.com` | `park-mx.above.com` |
| `1aolmail.com` | `route1.mx.cloudflare.net` |
| `1ayj8yi7lpiksxawav.gq` | `route1.mx.cloudflare.net` |


*… and 3,028 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
