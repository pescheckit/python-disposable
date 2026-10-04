# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-10-04 03:05 UTC**.*  
*Last DNS snapshot: **2026-10-04T02:55:43+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 97,735 |
| `domains_strict.txt` | 98,966 |
| `domains_inferred.txt` (opt-in) | 2 |

## Reachability

Of **98,882** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 42,841 | 43.3% |
| A_ONLY | 5,466 | 5.5% |
| NXDOMAIN | 41,226 | 41.7% |
| NO_RECORDS | 961 | 1.0% |
| TIMEOUT | 8,388 | 8.5% |

**48,307 domains are mail-reachable today** (48.9%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `route2.mx.cloudflare.net` | 2650 | 2672 | yes |
| `route1.mx.cloudflare.net` | 2649 | 2671 | yes |
| `route3.mx.cloudflare.net` | 2648 | 2670 | yes |
| `mail.wabblywabble.com` | 1906 | 1907 |  |
| `mail.wallywatts.com` | 1906 | 1907 |  |
| `generator.email` | 1494 | 1526 |  |
| `aero4.unstablemail.com` | 1278 | 1281 |  |
| `srv4.unstablemail.com` | 1278 | 1281 |  |
| `mx4.beavis99.com` | 1203 | 1205 |  |
| `mx4.beavis99.net` | 1202 | 1204 |  |
| `aspmx.l.google.com` | 1060 | 1064 | yes |
| `alt1.aspmx.l.google.com` | 1040 | 1044 | yes |
| `alt2.aspmx.l.google.com` | 1034 | 1038 | yes |
| `park-mx.above.com` | 944 | 951 | yes |
| `eforward1.registrar-servers.com` | 910 | 913 | yes |
| `eforward2.registrar-servers.com` | 910 | 913 | yes |
| `eforward3.registrar-servers.com` | 910 | 913 | yes |
| `eforward4.registrar-servers.com` | 910 | 913 | yes |
| `eforward5.registrar-servers.com` | 910 | 913 | yes |
| `smtp.google.com` | 774 | 777 | yes |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 1906 | 1907 |
| `mail.wallywatts.com` | 1906 | 1907 |
| `generator.email` | 1494 | 1526 |
| `aero4.unstablemail.com` | 1278 | 1281 |
| `srv4.unstablemail.com` | 1278 | 1281 |
| `mx4.beavis99.com` | 1203 | 1205 |
| `mx4.beavis99.net` | 1202 | 1204 |
| `emailfake.com` | 719 | 734 |
| `publicms1.mail2world.com` | 591 | 592 |
| `publicms2.mail2world.com` | 591 | 592 |
| `email.chatgpt.org.uk` | 585 | 585 |
| `smtp.yopmail.com` | 451 | 453 |
| `mx.emlhub.com` | 445 | 445 |
| `email.gravityengine.cc` | 381 | 382 |
| `mail.h-email.net` | 379 | 408 |
| `mail.cleantempmail.com` | 378 | 378 |
| `mx2.timeweb.ru` | 369 | 371 |
| `mx1.timeweb.ru` | 368 | 370 |
| `mx.spymail.one` | 366 | 366 |
| `tinyhost.shop` | 361 | 361 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `78.47.124.133` | 2708 | 2708 |
| `94.130.108.80` | 2708 | 2708 |
| `162.159.205.23` | 2645 | 2667 |
| `162.159.205.24` | 2645 | 2667 |
| `162.159.205.25` | 2645 | 2667 |
| `162.159.205.17` | 2625 | 2647 |
| `162.159.205.18` | 2625 | 2647 |
| `162.159.205.19` | 2625 | 2647 |
| `162.159.205.11` | 2624 | 2646 |
| `162.159.205.12` | 2624 | 2646 |
| `162.159.205.13` | 2624 | 2646 |
| `91.196.52.205` | 2356 | 2405 |
| `116.202.9.167` | 1875 | 1876 |
| `142.132.166.12` | 1875 | 1876 |
| `188.166.111.252` | 1875 | 1876 |
| `46.101.111.206` | 1875 | 1876 |
| `138.226.240.26` | 1285 | 1286 |
| `146.190.212.90` | 1250 | 1253 |
| `146.190.223.124` | 1231 | 1234 |
| `195.123.189.142` | 1229 | 1229 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 452 |
| High-confidence disposable IPs | 1,117 |
| Promoted to `domains_inferred.txt` | 2 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**8423 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

| Listed disposable | MX (shared infra) |
|---|---|
| `0-30-24.com` | `alt1.aspmx.l.google.com` |
| `0-mail.com` | `park-mx.above.com` |
| `000476.com` | `park-mx.above.com` |
| `000728.xyz` | `route1.mx.cloudflare.net` |
| `001218.xyz` | `route1.mx.cloudflare.net` |
| `001250.xyz` | `eforward1.registrar-servers.com` |
| `001310.xyz` | `route1.mx.cloudflare.net` |
| `005005.xyz` | `route1.mx.cloudflare.net` |
| `0055betplataforma.com` | `route1.mx.cloudflare.net` |
| `0058.ru` | `alt1.aspmx.l.google.com` |
| `00gmail.com` | `park-mx.above.com` |
| `010608.xyz` | `route1.mx.cloudflare.net` |
| `010hb.com` | `route1.mx.cloudflare.net` |
| `012356.xyz` | `route1.mx.cloudflare.net` |
| `01g.cloud` | `alt1.aspmx.l.google.com` |
| `01p.co.jp` | `01p-co-jp.mail.protection.outlook.com` |
| `020307.xyz` | `route1.mx.cloudflare.net` |
| `041998.xyz` | `mx1.alias.proton.me` |
| `099833.xyz` | `park-mx.above.com` |
| `0ak.org` | `mx00.ionos.com` |
| `0hcow.com` | `mxa.mailgun.org` |
| `0hio.net` | `aspmx1.migadu.com` |
| `0live.org` | `route1.mx.cloudflare.net` |
| `0nce.net` | `route1.mx.cloudflare.net` |
| `0rg.fr` | `mx1.mail.ovh.net` |
| `0sp.me` | `eforward1.registrar-servers.com` |
| `0ut.online` | `smtp.google.com` |
| `0x7121.com` | `park-mx.above.com` |
| `0xmiikee.com` | `eforward1.registrar-servers.com` |
| `1-2.co.uk` | `12-co-uk0c.mail.protection.outlook.com` |


*… and 8,393 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
