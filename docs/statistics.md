# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-10-06 02:26 UTC**.*  
*Last DNS snapshot: **2026-10-06T02:22:23+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 97,791 |
| `domains_strict.txt` | 99,022 |
| `domains_inferred.txt` (opt-in) | 2 |

## Reachability

Of **99,046** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 42,911 | 43.3% |
| A_ONLY | 5,481 | 5.5% |
| NXDOMAIN | 41,164 | 41.6% |
| NO_RECORDS | 983 | 1.0% |
| TIMEOUT | 8,507 | 8.6% |

**48,392 domains are mail-reachable today** (48.9%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `route2.mx.cloudflare.net` | 2638 | 2674 | yes |
| `route1.mx.cloudflare.net` | 2637 | 2673 | yes |
| `route3.mx.cloudflare.net` | 2636 | 2672 | yes |
| `mail.wabblywabble.com` | 1904 | 1908 |  |
| `mail.wallywatts.com` | 1904 | 1908 |  |
| `generator.email` | 1485 | 1524 |  |
| `aero4.unstablemail.com` | 1278 | 1278 |  |
| `srv4.unstablemail.com` | 1277 | 1277 |  |
| `mx4.beavis99.com` | 1206 | 1206 |  |
| `mx4.beavis99.net` | 1205 | 1205 |  |
| `aspmx.l.google.com` | 1066 | 1074 | yes |
| `alt1.aspmx.l.google.com` | 1046 | 1054 | yes |
| `alt2.aspmx.l.google.com` | 1039 | 1047 | yes |
| `park-mx.above.com` | 934 | 946 | yes |
| `eforward1.registrar-servers.com` | 908 | 915 | yes |
| `eforward2.registrar-servers.com` | 908 | 915 | yes |
| `eforward3.registrar-servers.com` | 908 | 915 | yes |
| `eforward4.registrar-servers.com` | 908 | 915 | yes |
| `eforward5.registrar-servers.com` | 908 | 915 | yes |
| `smtp.google.com` | 776 | 779 | yes |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 1904 | 1908 |
| `mail.wallywatts.com` | 1904 | 1908 |
| `generator.email` | 1485 | 1524 |
| `aero4.unstablemail.com` | 1278 | 1278 |
| `srv4.unstablemail.com` | 1277 | 1277 |
| `mx4.beavis99.com` | 1206 | 1206 |
| `mx4.beavis99.net` | 1205 | 1205 |
| `emailfake.com` | 712 | 724 |
| `email.chatgpt.org.uk` | 619 | 619 |
| `publicms1.mail2world.com` | 590 | 592 |
| `publicms2.mail2world.com` | 590 | 592 |
| `mx.emlhub.com` | 441 | 441 |
| `smtp.yopmail.com` | 441 | 446 |
| `tinyhost.shop` | 386 | 386 |
| `email.gravityengine.cc` | 381 | 382 |
| `mail.cleantempmail.com` | 377 | 378 |
| `mail.h-email.net` | 377 | 411 |
| `mx2.timeweb.ru` | 369 | 370 |
| `mx1.timeweb.ru` | 368 | 369 |
| `mx.spymail.one` | 361 | 361 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `78.47.124.133` | 2689 | 2689 |
| `94.130.108.80` | 2689 | 2689 |
| `162.159.205.23` | 2627 | 2663 |
| `162.159.205.24` | 2627 | 2663 |
| `162.159.205.25` | 2627 | 2663 |
| `162.159.205.17` | 2613 | 2649 |
| `162.159.205.18` | 2613 | 2649 |
| `162.159.205.19` | 2613 | 2649 |
| `162.159.205.11` | 2611 | 2645 |
| `162.159.205.12` | 2611 | 2645 |
| `162.159.205.13` | 2611 | 2645 |
| `91.196.52.205` | 2366 | 2419 |
| `116.202.9.167` | 1870 | 1874 |
| `142.132.166.12` | 1870 | 1874 |
| `188.166.111.252` | 1870 | 1874 |
| `46.101.111.206` | 1870 | 1874 |
| `138.226.240.26` | 1317 | 1319 |
| `146.190.212.90` | 1243 | 1243 |
| `195.123.189.142` | 1240 | 1240 |
| `146.190.223.124` | 1227 | 1227 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 454 |
| High-confidence disposable IPs | 1,139 |
| Promoted to `domains_inferred.txt` | 2 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**8401 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

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
| `0nce.net` | `route1.mx.cloudflare.net` |
| `0rg.fr` | `mx1.mail.ovh.net` |
| `0sp.me` | `eforward1.registrar-servers.com` |
| `0ut.online` | `smtp.google.com` |
| `0x7121.com` | `park-mx.above.com` |
| `0xmiikee.com` | `eforward1.registrar-servers.com` |
| `1-2.co.uk` | `12-co-uk0c.mail.protection.outlook.com` |
| `1-8.biz` | `mail.protonmail.ch` |


*… and 8,371 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
