# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-06-29 03:19 UTC**.*  
*Last DNS snapshot: **2026-06-29T03:13:01+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 74,296 |
| `domains_strict.txt` | 74,327 |
| `domains_inferred.txt` (opt-in) | 2 |

## Reachability

Of **74,853** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 23,682 | 31.6% |
| A_ONLY | 5,270 | 7.0% |
| NXDOMAIN | 41,624 | 55.6% |
| NO_RECORDS | 718 | 1.0% |
| TIMEOUT | 3,559 | 4.8% |

**28,952 domains are mail-reachable today** (38.7%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `mail.wabblywabble.com` | 1367 | 1405 |  |
| `mail.wallywatts.com` | 1367 | 1405 |  |
| `mx4.beavis99.com` | 1029 | 1030 |  |
| `mx4.beavis99.net` | 1028 | 1029 |  |
| `route1.mx.cloudflare.net` | 845 | 851 | yes |
| `route2.mx.cloudflare.net` | 845 | 851 | yes |
| `route3.mx.cloudflare.net` | 843 | 849 | yes |
| `generator.email` | 791 | 932 |  |
| `park-mx.above.com` | 647 | 649 | yes |
| `email.gravityengine.cc` | 633 | 633 |  |
| `mx.emlhub.com` | 470 | 470 |  |
| `aspmx.l.google.com` | 464 | 465 | yes |
| `alt1.aspmx.l.google.com` | 455 | 456 | yes |
| `alt2.aspmx.l.google.com` | 451 | 452 | yes |
| `aero4.unstablemail.com` | 450 | 450 |  |
| `srv4.unstablemail.com` | 450 | 450 |  |
| `emailfake.com` | 449 | 490 |  |
| `mx.spymail.one` | 379 | 379 |  |
| `mx.emltmp.com` | 368 | 368 |  |
| `mx.emlpro.com` | 358 | 358 |  |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 1367 | 1405 |
| `mail.wallywatts.com` | 1367 | 1405 |
| `mx4.beavis99.com` | 1029 | 1030 |
| `mx4.beavis99.net` | 1028 | 1029 |
| `generator.email` | 791 | 932 |
| `email.gravityengine.cc` | 633 | 633 |
| `mx.emlhub.com` | 470 | 470 |
| `aero4.unstablemail.com` | 450 | 450 |
| `srv4.unstablemail.com` | 450 | 450 |
| `emailfake.com` | 449 | 490 |
| `mx.spymail.one` | 379 | 379 |
| `mx.emltmp.com` | 368 | 368 |
| `mx.emlpro.com` | 358 | 358 |
| `mx.dropmail.me` | 333 | 333 |
| `tinyhost.shop` | 318 | 318 |
| `mx.freeml.net` | 308 | 308 |
| `mx37.m1bp.com` | 258 | 258 |
| `mx37.mb5p.com` | 258 | 258 |
| `mail.casadorock.com` | 252 | 252 |
| `mx.yomail.info` | 252 | 252 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `78.47.124.133` | 2619 | 2619 |
| `94.130.108.80` | 2619 | 2619 |
| `116.202.9.167` | 1332 | 1366 |
| `46.101.111.206` | 1332 | 1366 |
| `91.196.52.205` | 1315 | 1503 |
| `142.132.166.12` | 1311 | 1346 |
| `188.166.111.252` | 1311 | 1346 |
| `13.223.25.84` | 1089 | 1089 |
| `54.243.117.197` | 1089 | 1089 |
| `188.245.74.208` | 1002 | 1003 |
| `195.201.18.63` | 993 | 994 |
| `162.159.205.17` | 861 | 866 |
| `162.159.205.18` | 861 | 866 |
| `162.159.205.19` | 861 | 866 |
| `162.159.205.23` | 860 | 865 |
| `162.159.205.24` | 860 | 865 |
| `162.159.205.25` | 860 | 865 |
| `162.159.205.11` | 850 | 855 |
| `162.159.205.12` | 850 | 855 |
| `162.159.205.13` | 850 | 855 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 296 |
| High-confidence disposable IPs | 776 |
| Promoted to `domains_inferred.txt` | 2 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**3331 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

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


*… and 3,301 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
