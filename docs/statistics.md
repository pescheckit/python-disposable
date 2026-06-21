# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-06-21 03:27 UTC**.*  
*Last DNS snapshot: **2026-06-21T03:13:48+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 73,781 |
| `domains_strict.txt` | 73,812 |
| `domains_inferred.txt` (opt-in) | 2 |

## Reachability

Of **74,288** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 21,905 | 29.5% |
| A_ONLY | 5,159 | 6.9% |
| NXDOMAIN | 39,634 | 53.4% |
| NO_RECORDS | 694 | 0.9% |
| TIMEOUT | 6,896 | 9.3% |

**27,064 domains are mail-reachable today** (36.4%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `mail.wabblywabble.com` | 1346 | 1369 |  |
| `mail.wallywatts.com` | 1346 | 1369 |  |
| `mx4.beavis99.com` | 985 | 986 |  |
| `mx4.beavis99.net` | 984 | 985 |  |
| `generator.email` | 798 | 945 |  |
| `route1.mx.cloudflare.net` | 787 | 793 | yes |
| `route2.mx.cloudflare.net` | 787 | 793 | yes |
| `route3.mx.cloudflare.net` | 785 | 791 | yes |
| `park-mx.above.com` | 621 | 622 | yes |
| `mx.emlhub.com` | 461 | 461 |  |
| `aspmx.l.google.com` | 439 | 440 | yes |
| `alt1.aspmx.l.google.com` | 430 | 431 | yes |
| `alt2.aspmx.l.google.com` | 426 | 427 | yes |
| `aero4.unstablemail.com` | 423 | 423 |  |
| `srv4.unstablemail.com` | 422 | 422 |  |
| `emailfake.com` | 421 | 472 |  |
| `mx.emltmp.com` | 354 | 354 |  |
| `mx.spymail.one` | 349 | 349 |  |
| `mx.emlpro.com` | 336 | 336 |  |
| `eforward1.registrar-servers.com` | 331 | 332 | yes |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 1346 | 1369 |
| `mail.wallywatts.com` | 1346 | 1369 |
| `mx4.beavis99.com` | 985 | 986 |
| `mx4.beavis99.net` | 984 | 985 |
| `generator.email` | 798 | 945 |
| `mx.emlhub.com` | 461 | 461 |
| `aero4.unstablemail.com` | 423 | 423 |
| `srv4.unstablemail.com` | 422 | 422 |
| `emailfake.com` | 421 | 472 |
| `mx.emltmp.com` | 354 | 354 |
| `mx.spymail.one` | 349 | 349 |
| `mx.emlpro.com` | 336 | 336 |
| `tinyhost.shop` | 325 | 325 |
| `mx.dropmail.me` | 314 | 314 |
| `mx.freeml.net` | 298 | 298 |
| `mx37.m1bp.com` | 256 | 256 |
| `mx37.mb5p.com` | 256 | 256 |
| `mx.yomail.info` | 242 | 242 |
| `mx156.hostedmxserver.com` | 220 | 220 |
| `mx195.m1bp.com` | 217 | 218 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `78.47.124.133` | 2471 | 2471 |
| `94.130.108.80` | 2471 | 2471 |
| `116.202.9.167` | 1333 | 1352 |
| `46.101.111.206` | 1333 | 1352 |
| `142.132.166.12` | 1319 | 1339 |
| `188.166.111.252` | 1319 | 1339 |
| `91.196.52.205` | 1288 | 1491 |
| `13.223.25.84` | 1067 | 1067 |
| `54.243.117.197` | 1067 | 1067 |
| `188.245.74.208` | 965 | 966 |
| `195.201.18.63` | 950 | 951 |
| `162.159.205.17` | 801 | 806 |
| `162.159.205.18` | 801 | 806 |
| `162.159.205.19` | 801 | 806 |
| `162.159.205.23` | 799 | 804 |
| `162.159.205.24` | 799 | 804 |
| `162.159.205.25` | 799 | 804 |
| `162.159.205.11` | 797 | 802 |
| `162.159.205.12` | 797 | 802 |
| `162.159.205.13` | 797 | 802 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 290 |
| High-confidence disposable IPs | 754 |
| Promoted to `domains_inferred.txt` | 2 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**3171 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

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


*… and 3,141 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
