# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-06-30 03:20 UTC**.*  
*Last DNS snapshot: **2026-06-30T03:13:32+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 74,296 |
| `domains_strict.txt` | 74,327 |
| `domains_inferred.txt` (opt-in) | 2 |

## Reachability

Of **74,867** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 23,178 | 31.0% |
| A_ONLY | 5,170 | 6.9% |
| NXDOMAIN | 40,915 | 54.7% |
| NO_RECORDS | 705 | 0.9% |
| TIMEOUT | 4,899 | 6.5% |

**28,348 domains are mail-reachable today** (37.9%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `mail.wabblywabble.com` | 1343 | 1381 |  |
| `mail.wallywatts.com` | 1343 | 1381 |  |
| `mx4.beavis99.com` | 1010 | 1011 |  |
| `mx4.beavis99.net` | 1009 | 1010 |  |
| `route1.mx.cloudflare.net` | 834 | 841 | yes |
| `route2.mx.cloudflare.net` | 834 | 841 | yes |
| `route3.mx.cloudflare.net` | 832 | 839 | yes |
| `generator.email` | 771 | 919 |  |
| `park-mx.above.com` | 638 | 640 | yes |
| `email.gravityengine.cc` | 619 | 619 |  |
| `aspmx.l.google.com` | 458 | 459 | yes |
| `mx.emlhub.com` | 450 | 450 |  |
| `alt1.aspmx.l.google.com` | 449 | 450 | yes |
| `alt2.aspmx.l.google.com` | 445 | 446 | yes |
| `emailfake.com` | 436 | 478 |  |
| `aero4.unstablemail.com` | 429 | 429 |  |
| `srv4.unstablemail.com` | 429 | 429 |  |
| `mx.spymail.one` | 371 | 371 |  |
| `mx.emltmp.com` | 362 | 362 |  |
| `mx.emlpro.com` | 353 | 353 |  |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 1343 | 1381 |
| `mail.wallywatts.com` | 1343 | 1381 |
| `mx4.beavis99.com` | 1010 | 1011 |
| `mx4.beavis99.net` | 1009 | 1010 |
| `generator.email` | 771 | 919 |
| `email.gravityengine.cc` | 619 | 619 |
| `mx.emlhub.com` | 450 | 450 |
| `emailfake.com` | 436 | 478 |
| `aero4.unstablemail.com` | 429 | 429 |
| `srv4.unstablemail.com` | 429 | 429 |
| `mx.spymail.one` | 371 | 371 |
| `mx.emltmp.com` | 362 | 362 |
| `mx.emlpro.com` | 353 | 353 |
| `mx.dropmail.me` | 325 | 325 |
| `tinyhost.shop` | 309 | 309 |
| `mx.freeml.net` | 303 | 303 |
| `mx.yomail.info` | 249 | 249 |
| `mx37.m1bp.com` | 249 | 249 |
| `mx37.mb5p.com` | 249 | 249 |
| `mx156.hostedmxserver.com` | 223 | 223 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `78.47.124.133` | 2524 | 2524 |
| `94.130.108.80` | 2524 | 2524 |
| `116.202.9.167` | 1304 | 1338 |
| `46.101.111.206` | 1304 | 1338 |
| `142.132.166.12` | 1283 | 1318 |
| `188.166.111.252` | 1283 | 1318 |
| `91.196.52.205` | 1273 | 1469 |
| `13.223.25.84` | 1071 | 1071 |
| `54.243.117.197` | 1071 | 1071 |
| `188.245.74.208` | 984 | 985 |
| `195.201.18.63` | 973 | 974 |
| `162.159.205.17` | 848 | 854 |
| `162.159.205.18` | 848 | 854 |
| `162.159.205.19` | 848 | 854 |
| `162.159.205.23` | 846 | 852 |
| `162.159.205.24` | 846 | 852 |
| `162.159.205.25` | 846 | 852 |
| `162.159.205.11` | 838 | 844 |
| `162.159.205.12` | 838 | 844 |
| `162.159.205.13` | 838 | 844 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 296 |
| High-confidence disposable IPs | 765 |
| Promoted to `domains_inferred.txt` | 2 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**3275 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

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


*… and 3,245 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
