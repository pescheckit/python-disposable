# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-06-22 04:16 UTC**.*  
*Last DNS snapshot: **2026-06-22T03:14:09+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 73,803 |
| `domains_strict.txt` | 73,834 |
| `domains_inferred.txt` (opt-in) | 2 |

## Reachability

Of **74,309** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 21,966 | 29.6% |
| A_ONLY | 5,170 | 7.0% |
| NXDOMAIN | 39,757 | 53.5% |
| NO_RECORDS | 696 | 0.9% |
| TIMEOUT | 6,720 | 9.0% |

**27,136 domains are mail-reachable today** (36.5%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `mail.wabblywabble.com` | 1347 | 1370 |  |
| `mail.wallywatts.com` | 1347 | 1370 |  |
| `mx4.beavis99.com` | 994 | 995 |  |
| `mx4.beavis99.net` | 993 | 994 |  |
| `generator.email` | 796 | 946 |  |
| `route1.mx.cloudflare.net` | 792 | 798 | yes |
| `route2.mx.cloudflare.net` | 792 | 798 | yes |
| `route3.mx.cloudflare.net` | 790 | 796 | yes |
| `park-mx.above.com` | 621 | 622 | yes |
| `mx.emlhub.com` | 461 | 461 |  |
| `aspmx.l.google.com` | 440 | 441 | yes |
| `emailfake.com` | 432 | 478 |  |
| `alt1.aspmx.l.google.com` | 431 | 432 | yes |
| `alt2.aspmx.l.google.com` | 427 | 428 | yes |
| `aero4.unstablemail.com` | 423 | 423 |  |
| `srv4.unstablemail.com` | 422 | 422 |  |
| `mx.emltmp.com` | 354 | 354 |  |
| `mx.spymail.one` | 349 | 349 |  |
| `mx.emlpro.com` | 336 | 336 |  |
| `tinyhost.shop` | 334 | 334 |  |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 1347 | 1370 |
| `mail.wallywatts.com` | 1347 | 1370 |
| `mx4.beavis99.com` | 994 | 995 |
| `mx4.beavis99.net` | 993 | 994 |
| `generator.email` | 796 | 946 |
| `mx.emlhub.com` | 461 | 461 |
| `emailfake.com` | 432 | 478 |
| `aero4.unstablemail.com` | 423 | 423 |
| `srv4.unstablemail.com` | 422 | 422 |
| `mx.emltmp.com` | 354 | 354 |
| `mx.spymail.one` | 349 | 349 |
| `mx.emlpro.com` | 336 | 336 |
| `tinyhost.shop` | 334 | 334 |
| `mx.dropmail.me` | 314 | 314 |
| `mx.freeml.net` | 298 | 298 |
| `mx37.m1bp.com` | 257 | 257 |
| `mx37.mb5p.com` | 257 | 257 |
| `mx.yomail.info` | 242 | 242 |
| `mx156.hostedmxserver.com` | 220 | 220 |
| `mx195.m1bp.com` | 217 | 218 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `78.47.124.133` | 2471 | 2471 |
| `94.130.108.80` | 2471 | 2471 |
| `116.202.9.167` | 1334 | 1353 |
| `46.101.111.206` | 1334 | 1353 |
| `142.132.166.12` | 1320 | 1340 |
| `188.166.111.252` | 1320 | 1340 |
| `91.196.52.205` | 1300 | 1501 |
| `13.223.25.84` | 1068 | 1068 |
| `54.243.117.197` | 1068 | 1068 |
| `188.245.74.208` | 977 | 978 |
| `195.201.18.63` | 962 | 963 |
| `162.159.205.17` | 807 | 812 |
| `162.159.205.18` | 807 | 812 |
| `162.159.205.19` | 807 | 812 |
| `162.159.205.23` | 805 | 810 |
| `162.159.205.24` | 805 | 810 |
| `162.159.205.25` | 805 | 810 |
| `162.159.205.11` | 803 | 808 |
| `162.159.205.12` | 803 | 808 |
| `162.159.205.13` | 803 | 808 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 290 |
| High-confidence disposable IPs | 754 |
| Promoted to `domains_inferred.txt` | 2 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**3178 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

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


*… and 3,148 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
