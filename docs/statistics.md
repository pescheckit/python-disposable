# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-06-23 03:23 UTC**.*  
*Last DNS snapshot: **2026-06-23T03:11:43+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 73,804 |
| `domains_strict.txt` | 73,835 |
| `domains_inferred.txt` (opt-in) | 2 |

## Reachability

Of **74,315** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 23,661 | 31.8% |
| A_ONLY | 5,450 | 7.3% |
| NXDOMAIN | 41,727 | 56.1% |
| NO_RECORDS | 743 | 1.0% |
| TIMEOUT | 2,734 | 3.7% |

**29,111 domains are mail-reachable today** (39.2%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `mail.wabblywabble.com` | 1436 | 1459 |  |
| `mail.wallywatts.com` | 1436 | 1459 |  |
| `mx4.beavis99.com` | 1035 | 1036 |  |
| `mx4.beavis99.net` | 1034 | 1035 |  |
| `route1.mx.cloudflare.net` | 834 | 840 | yes |
| `route2.mx.cloudflare.net` | 834 | 840 | yes |
| `route3.mx.cloudflare.net` | 832 | 838 | yes |
| `generator.email` | 831 | 981 |  |
| `park-mx.above.com` | 644 | 645 | yes |
| `email.gravityengine.cc` | 633 | 633 |  |
| `mx.emlhub.com` | 478 | 478 |  |
| `aero4.unstablemail.com` | 462 | 462 |  |
| `srv4.unstablemail.com` | 461 | 461 |  |
| `aspmx.l.google.com` | 457 | 458 | yes |
| `alt1.aspmx.l.google.com` | 448 | 449 | yes |
| `emailfake.com` | 446 | 495 |  |
| `alt2.aspmx.l.google.com` | 444 | 445 | yes |
| `mx.spymail.one` | 387 | 387 |  |
| `mx.emltmp.com` | 371 | 371 |  |
| `mx.emlpro.com` | 362 | 362 |  |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 1436 | 1459 |
| `mail.wallywatts.com` | 1436 | 1459 |
| `mx4.beavis99.com` | 1035 | 1036 |
| `mx4.beavis99.net` | 1034 | 1035 |
| `generator.email` | 831 | 981 |
| `email.gravityengine.cc` | 633 | 633 |
| `mx.emlhub.com` | 478 | 478 |
| `aero4.unstablemail.com` | 462 | 462 |
| `srv4.unstablemail.com` | 461 | 461 |
| `emailfake.com` | 446 | 495 |
| `mx.spymail.one` | 387 | 387 |
| `mx.emltmp.com` | 371 | 371 |
| `mx.emlpro.com` | 362 | 362 |
| `mx.dropmail.me` | 341 | 341 |
| `tinyhost.shop` | 337 | 337 |
| `mx.freeml.net` | 318 | 318 |
| `mx37.m1bp.com` | 266 | 266 |
| `mx37.mb5p.com` | 266 | 266 |
| `mail.casadorock.com` | 253 | 253 |
| `mx.yomail.info` | 253 | 253 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `78.47.124.133` | 2695 | 2695 |
| `94.130.108.80` | 2695 | 2695 |
| `116.202.9.167` | 1428 | 1447 |
| `46.101.111.206` | 1428 | 1447 |
| `142.132.166.12` | 1411 | 1431 |
| `188.166.111.252` | 1411 | 1431 |
| `91.196.52.205` | 1355 | 1560 |
| `13.223.25.84` | 1119 | 1119 |
| `54.243.117.197` | 1119 | 1119 |
| `188.245.74.208` | 1019 | 1020 |
| `195.201.18.63` | 1007 | 1008 |
| `162.159.205.17` | 854 | 859 |
| `162.159.205.18` | 854 | 859 |
| `162.159.205.19` | 854 | 859 |
| `162.159.205.23` | 853 | 858 |
| `162.159.205.24` | 853 | 858 |
| `162.159.205.25` | 853 | 858 |
| `162.159.205.11` | 850 | 855 |
| `162.159.205.12` | 850 | 855 |
| `162.159.205.13` | 850 | 855 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 293 |
| High-confidence disposable IPs | 775 |
| Promoted to `domains_inferred.txt` | 2 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**3336 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

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


*… and 3,306 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
