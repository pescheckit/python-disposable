# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-11-09 02:21 UTC**.*  
*Last DNS snapshot: **2026-11-09T02:10:06+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 98,957 |
| `domains_strict.txt` | 100,189 |
| `domains_inferred.txt` (opt-in) | 4 |

## Reachability

Of **104,100** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 35,667 | 34.3% |
| A_ONLY | 2,418 | 2.3% |
| NXDOMAIN | 19,892 | 19.1% |
| NO_RECORDS | 677 | 0.7% |
| TIMEOUT | 45,446 | 43.7% |

**38,085 domains are mail-reachable today** (36.6%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `route2.mx.cloudflare.net` | 2174 | 2381 | yes |
| `route1.mx.cloudflare.net` | 2173 | 2380 | yes |
| `route3.mx.cloudflare.net` | 2173 | 2380 | yes |
| `mail.wabblywabble.com` | 1296 | 1297 |  |
| `mail.wallywatts.com` | 1296 | 1297 |  |
| `generator.email` | 1271 | 1514 |  |
| `aero4.unstablemail.com` | 1084 | 1085 |  |
| `srv4.unstablemail.com` | 1083 | 1084 |  |
| `smtp.yopmail.com` | 1033 | 1042 |  |
| `park-mx.above.com` | 898 | 1012 | yes |
| `smtp.google.com` | 763 | 791 | yes |
| `aspmx.l.google.com` | 745 | 830 | yes |
| `alt1.aspmx.l.google.com` | 736 | 819 | yes |
| `alt2.aspmx.l.google.com` | 734 | 815 | yes |
| `eforward1.registrar-servers.com` | 707 | 748 | yes |
| `eforward2.registrar-servers.com` | 707 | 748 | yes |
| `eforward3.registrar-servers.com` | 707 | 748 | yes |
| `eforward4.registrar-servers.com` | 707 | 748 | yes |
| `eforward5.registrar-servers.com` | 707 | 748 | yes |
| `email.chatgpt.org.uk` | 688 | 700 |  |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 1296 | 1297 |
| `mail.wallywatts.com` | 1296 | 1297 |
| `generator.email` | 1271 | 1514 |
| `aero4.unstablemail.com` | 1084 | 1085 |
| `srv4.unstablemail.com` | 1083 | 1084 |
| `smtp.yopmail.com` | 1033 | 1042 |
| `email.chatgpt.org.uk` | 688 | 700 |
| `mx4.beavis99.com` | 592 | 592 |
| `mx4.beavis99.net` | 591 | 591 |
| `emailfake.com` | 570 | 583 |
| `smtp.215.im` | 393 | 397 |
| `mx.10mail.org` | 344 | 344 |
| `mx1.timeweb.ru` | 334 | 364 |
| `mx2.timeweb.ru` | 334 | 364 |
| `tinyhost.shop` | 323 | 323 |
| `mx2-hosting.jellyfish.systems` | 315 | 326 |
| `mx3-hosting.jellyfish.systems` | 315 | 326 |
| `mx1-hosting.jellyfish.systems` | 314 | 325 |
| `void.blackhole.mx` | 294 | 297 |
| `mx1.titan.email` | 269 | 271 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `162.159.205.23` | 2068 | 2271 |
| `162.159.205.24` | 2068 | 2271 |
| `162.159.205.25` | 2068 | 2271 |
| `162.159.205.17` | 2066 | 2269 |
| `162.159.205.18` | 2066 | 2269 |
| `162.159.205.19` | 2066 | 2269 |
| `162.159.205.11` | 2048 | 2251 |
| `162.159.205.12` | 2048 | 2251 |
| `162.159.205.13` | 2048 | 2251 |
| `91.196.52.205` | 1992 | 2241 |
| `78.47.124.133` | 1510 | 1510 |
| `94.130.108.80` | 1510 | 1510 |
| `116.202.9.167` | 1168 | 1169 |
| `46.101.111.206` | 1168 | 1169 |
| `142.132.166.12` | 1156 | 1157 |
| `188.166.111.252` | 1156 | 1157 |
| `195.123.189.142` | 1145 | 1219 |
| `87.98.164.155` | 1079 | 1088 |
| `146.190.212.90` | 1037 | 1038 |
| `146.190.223.124` | 1030 | 1031 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 376 |
| High-confidence disposable IPs | 955 |
| Promoted to `domains_inferred.txt` | 4 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**6817 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

| Listed disposable | MX (shared infra) |
|---|---|
| `0-30-24.com` | `alt1.aspmx.l.google.com` |
| `0-mail.com` | `park-mx.above.com` |
| `000476.com` | `park-mx.above.com` |
| `000728.xyz` | `route1.mx.cloudflare.net` |
| `001041.xyz` | `route1.mx.cloudflare.net` |
| `001218.xyz` | `route1.mx.cloudflare.net` |
| `001310.xyz` | `route1.mx.cloudflare.net` |
| `005005.xyz` | `route1.mx.cloudflare.net` |
| `0055betplataforma.com` | `route1.mx.cloudflare.net` |
| `0058.ru` | `alt1.aspmx.l.google.com` |
| `0066bet32.info` | `park-mx.above.com` |
| `0066betapp.info` | `park-mx.above.com` |
| `007bet.info` | `park-mx.above.com` |
| `007gamecasino.net` | `park-mx.above.com` |
| `007jlbu.com` | `route1.mx.cloudflare.net` |
| `007jlphp.com` | `route1.mx.cloudflare.net` |
| `008686.xyz` | `route1.mx.cloudflare.net` |
| `00gmail.com` | `park-mx.above.com` |
| `010608.xyz` | `route1.mx.cloudflare.net` |
| `010hb.com` | `route1.mx.cloudflare.net` |
| `012356.xyz` | `route1.mx.cloudflare.net` |
| `012pg.bet` | `route1.mx.cloudflare.net` |
| `01g.cloud` | `alt1.aspmx.l.google.com` |
| `01p.co.jp` | `01p-co-jp.mail.protection.outlook.com` |
| `020307.xyz` | `route1.mx.cloudflare.net` |
| `02bet.info` | `park-mx.above.com` |
| `041998.xyz` | `mx1.alias.proton.me` |
| `0500betvip.com` | `route1.mx.cloudflare.net` |
| `057gmail.com` | `route1.mx.cloudflare.net` |
| `0ak.org` | `mx00.ionos.com` |


*… and 6,787 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
