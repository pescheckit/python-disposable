# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-06-08 03:43 UTC**.*  
*Last DNS snapshot: **2026-06-08T03:43:38+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 73,342 |
| `domains_strict.txt` | 73,373 |
| `domains_inferred.txt` (opt-in) | 2 |

## Reachability

Of **73,815** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 22,295 | 30.2% |
| A_ONLY | 5,045 | 6.8% |
| NXDOMAIN | 39,968 | 54.1% |
| NO_RECORDS | 683 | 0.9% |
| TIMEOUT | 5,824 | 7.9% |

**27,340 domains are mail-reachable today** (37.0%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `mail.wabblywabble.com` | 1429 | 1446 |  |
| `mail.wallywatts.com` | 1429 | 1446 |  |
| `mx4.beavis99.com` | 983 | 983 |  |
| `mx4.beavis99.net` | 982 | 982 |  |
| `generator.email` | 800 | 946 |  |
| `route1.mx.cloudflare.net` | 789 | 796 | yes |
| `route2.mx.cloudflare.net` | 789 | 796 | yes |
| `route3.mx.cloudflare.net` | 788 | 795 | yes |
| `email.gravityengine.cc` | 647 | 647 |  |
| `park-mx.above.com` | 615 | 616 | yes |
| `aspmx.l.google.com` | 454 | 454 | yes |
| `alt1.aspmx.l.google.com` | 445 | 445 | yes |
| `alt2.aspmx.l.google.com` | 442 | 442 | yes |
| `emailfake.com` | 440 | 489 |  |
| `aero4.unstablemail.com` | 435 | 435 |  |
| `srv4.unstablemail.com` | 434 | 434 |  |
| `mx.emlhub.com` | 409 | 409 |  |
| `mx.emltmp.com` | 366 | 366 |  |
| `mx.spymail.one` | 362 | 362 |  |
| `mx.emlpro.com` | 347 | 347 |  |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 1429 | 1446 |
| `mail.wallywatts.com` | 1429 | 1446 |
| `mx4.beavis99.com` | 983 | 983 |
| `mx4.beavis99.net` | 982 | 982 |
| `generator.email` | 800 | 946 |
| `email.gravityengine.cc` | 647 | 647 |
| `emailfake.com` | 440 | 489 |
| `aero4.unstablemail.com` | 435 | 435 |
| `srv4.unstablemail.com` | 434 | 434 |
| `mx.emlhub.com` | 409 | 409 |
| `mx.emltmp.com` | 366 | 366 |
| `mx.spymail.one` | 362 | 362 |
| `mx.emlpro.com` | 347 | 347 |
| `mx.dropmail.me` | 323 | 323 |
| `mx.freeml.net` | 306 | 306 |
| `mx.yomail.info` | 240 | 240 |
| `mx37.m1bp.com` | 230 | 230 |
| `mx37.mb5p.com` | 230 | 230 |
| `mx156.hostedmxserver.com` | 228 | 228 |
| `mail.casadorock.com` | 225 | 225 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `78.47.124.133` | 2452 | 2452 |
| `94.130.108.80` | 2452 | 2452 |
| `116.202.9.167` | 1378 | 1392 |
| `46.101.111.206` | 1378 | 1392 |
| `142.132.166.12` | 1359 | 1374 |
| `188.166.111.252` | 1359 | 1374 |
| `91.196.52.205` | 1291 | 1487 |
| `13.223.25.84` | 1076 | 1076 |
| `54.243.117.197` | 1076 | 1076 |
| `188.245.74.208` | 960 | 960 |
| `195.201.18.63` | 945 | 945 |
| `162.159.205.17` | 800 | 806 |
| `162.159.205.18` | 800 | 806 |
| `162.159.205.19` | 800 | 806 |
| `162.159.205.23` | 797 | 803 |
| `162.159.205.24` | 797 | 803 |
| `162.159.205.25` | 797 | 803 |
| `162.159.205.11` | 787 | 793 |
| `162.159.205.12` | 787 | 793 |
| `162.159.205.13` | 787 | 793 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 285 |
| High-confidence disposable IPs | 765 |
| Promoted to `domains_inferred.txt` | 2 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**3225 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

| Listed disposable | MX (shared infra) |
|---|---|
| `0-30-24.com` | `alt1.aspmx.l.google.com` |
| `0-mail.com` | `park-mx.above.com` |
| `0058.ru` | `alt1.aspmx.l.google.com` |
| `01g.cloud` | `alt1.aspmx.l.google.com` |
| `0ak.org` | `mx00.ionos.com` |
| `0celot.com` | `alt1.aspmx.l.google.com` |
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
| `10inbox.online` | `route1.mx.cloudflare.net` |
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


*… and 3,195 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
