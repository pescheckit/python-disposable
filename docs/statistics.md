# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-09-23 02:25 UTC**.*  
*Last DNS snapshot: **2026-09-23T02:19:29+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 75,337 |
| `domains_strict.txt` | 75,368 |
| `domains_inferred.txt` (opt-in) | 2 |

## Reachability

Of **76,402** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 23,139 | 30.3% |
| A_ONLY | 5,353 | 7.0% |
| NXDOMAIN | 41,061 | 53.7% |
| NO_RECORDS | 784 | 1.0% |
| TIMEOUT | 6,065 | 7.9% |

**28,492 domains are mail-reachable today** (37.3%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `mail.wabblywabble.com` | 1273 | 1349 |  |
| `mail.wallywatts.com` | 1273 | 1349 |  |
| `mx4.beavis99.com` | 1128 | 1129 |  |
| `mx4.beavis99.net` | 1128 | 1129 |  |
| `route2.mx.cloudflare.net` | 978 | 991 | yes |
| `route1.mx.cloudflare.net` | 977 | 990 | yes |
| `route3.mx.cloudflare.net` | 976 | 989 | yes |
| `generator.email` | 698 | 835 |  |
| `park-mx.above.com` | 501 | 506 | yes |
| `aero4.unstablemail.com` | 454 | 454 |  |
| `srv4.unstablemail.com` | 454 | 454 |  |
| `aspmx.l.google.com` | 452 | 455 | yes |
| `mx.emlhub.com` | 451 | 451 |  |
| `alt1.aspmx.l.google.com` | 443 | 446 | yes |
| `alt2.aspmx.l.google.com` | 440 | 443 | yes |
| `emailfake.com` | 432 | 469 |  |
| `email.chatgpt.org.uk` | 402 | 402 |  |
| `email.gravityengine.cc` | 373 | 373 |  |
| `mx.spymail.one` | 368 | 368 |  |
| `mx.emltmp.com` | 363 | 363 |  |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 1273 | 1349 |
| `mail.wallywatts.com` | 1273 | 1349 |
| `mx4.beavis99.com` | 1128 | 1129 |
| `mx4.beavis99.net` | 1128 | 1129 |
| `generator.email` | 698 | 835 |
| `aero4.unstablemail.com` | 454 | 454 |
| `srv4.unstablemail.com` | 454 | 454 |
| `mx.emlhub.com` | 451 | 451 |
| `emailfake.com` | 432 | 469 |
| `email.chatgpt.org.uk` | 402 | 402 |
| `email.gravityengine.cc` | 373 | 373 |
| `mx.spymail.one` | 368 | 368 |
| `mx.emltmp.com` | 363 | 363 |
| `mx.emlpro.com` | 344 | 344 |
| `tinyhost.shop` | 329 | 329 |
| `mx.dropmail.me` | 323 | 323 |
| `mx.freeml.net` | 305 | 305 |
| `vietxf.com` | 269 | 269 |
| `mx.yomail.info` | 235 | 235 |
| `mx37.m1bp.com` | 229 | 229 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `78.47.124.133` | 2500 | 2500 |
| `94.130.108.80` | 2500 | 2500 |
| `142.132.166.12` | 1252 | 1320 |
| `188.166.111.252` | 1252 | 1320 |
| `116.202.9.167` | 1251 | 1318 |
| `46.101.111.206` | 1251 | 1318 |
| `91.196.52.205` | 1184 | 1358 |
| `188.245.74.208` | 1114 | 1115 |
| `195.201.18.63` | 1099 | 1100 |
| `13.223.25.84` | 1086 | 1088 |
| `54.243.117.197` | 1086 | 1088 |
| `162.159.205.23` | 979 | 990 |
| `162.159.205.24` | 979 | 990 |
| `162.159.205.25` | 979 | 990 |
| `162.159.205.17` | 974 | 986 |
| `162.159.205.18` | 974 | 986 |
| `162.159.205.19` | 974 | 986 |
| `162.159.205.11` | 966 | 977 |
| `162.159.205.12` | 966 | 977 |
| `162.159.205.13` | 966 | 977 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 311 |
| High-confidence disposable IPs | 796 |
| Promoted to `domains_inferred.txt` | 2 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**3298 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

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
| `0live.org` | `route1.mx.cloudflare.net` |
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
| `11cows.com` | `mxa.mailgun.org` |
| `123gmail.com` | `park-mx.above.com` |
| `12499aaa.com` | `eforward1.registrar-servers.com` |
| `12storage.com` | `route1.mx.cloudflare.net` |
| `13dk.net` | `route1.mx.cloudflare.net` |
| `14n.co.uk` | `14n-co-uk.mail.protection.outlook.com` |
| `14p.in` | `eforward1.registrar-servers.com` |
| `15qm-mail.red` | `eforward1.registrar-servers.com` |
| `189.email` | `route1.mx.cloudflare.net` |


*… and 3,268 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
