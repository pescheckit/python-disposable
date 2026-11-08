# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-11-08 02:16 UTC**.*  
*Last DNS snapshot: **2026-11-08T02:16:47+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 98,919 |
| `domains_strict.txt` | 100,151 |
| `domains_inferred.txt` (opt-in) | 4 |

## Reachability

Of **104,009** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 35,552 | 34.2% |
| A_ONLY | 2,413 | 2.3% |
| NXDOMAIN | 19,873 | 19.1% |
| NO_RECORDS | 662 | 0.6% |
| TIMEOUT | 45,509 | 43.8% |

**37,965 domains are mail-reachable today** (36.5%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `route2.mx.cloudflare.net` | 2170 | 2374 | yes |
| `route1.mx.cloudflare.net` | 2169 | 2373 | yes |
| `route3.mx.cloudflare.net` | 2169 | 2373 | yes |
| `mail.wabblywabble.com` | 1289 | 1289 |  |
| `mail.wallywatts.com` | 1289 | 1289 |  |
| `generator.email` | 1264 | 1508 |  |
| `aero4.unstablemail.com` | 1082 | 1082 |  |
| `srv4.unstablemail.com` | 1081 | 1081 |  |
| `smtp.yopmail.com` | 1034 | 1042 |  |
| `park-mx.above.com` | 871 | 983 | yes |
| `smtp.google.com` | 761 | 789 | yes |
| `aspmx.l.google.com` | 748 | 835 | yes |
| `alt1.aspmx.l.google.com` | 739 | 824 | yes |
| `alt2.aspmx.l.google.com` | 737 | 820 | yes |
| `eforward1.registrar-servers.com` | 706 | 747 | yes |
| `eforward2.registrar-servers.com` | 706 | 747 | yes |
| `eforward3.registrar-servers.com` | 706 | 747 | yes |
| `eforward4.registrar-servers.com` | 706 | 747 | yes |
| `eforward5.registrar-servers.com` | 706 | 747 | yes |
| `email.chatgpt.org.uk` | 684 | 696 |  |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 1289 | 1289 |
| `mail.wallywatts.com` | 1289 | 1289 |
| `generator.email` | 1264 | 1508 |
| `aero4.unstablemail.com` | 1082 | 1082 |
| `srv4.unstablemail.com` | 1081 | 1081 |
| `smtp.yopmail.com` | 1034 | 1042 |
| `email.chatgpt.org.uk` | 684 | 696 |
| `mx4.beavis99.com` | 592 | 592 |
| `mx4.beavis99.net` | 591 | 591 |
| `emailfake.com` | 571 | 586 |
| `smtp.215.im` | 392 | 396 |
| `mx.10mail.org` | 339 | 339 |
| `mx1.timeweb.ru` | 333 | 363 |
| `mx2.timeweb.ru` | 333 | 363 |
| `tinyhost.shop` | 316 | 316 |
| `mx2-hosting.jellyfish.systems` | 314 | 325 |
| `mx3-hosting.jellyfish.systems` | 314 | 325 |
| `mx1-hosting.jellyfish.systems` | 313 | 324 |
| `void.blackhole.mx` | 290 | 296 |
| `mx1.titan.email` | 269 | 271 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `162.159.205.23` | 2064 | 2264 |
| `162.159.205.24` | 2064 | 2264 |
| `162.159.205.25` | 2064 | 2264 |
| `162.159.205.17` | 2062 | 2262 |
| `162.159.205.18` | 2062 | 2262 |
| `162.159.205.19` | 2062 | 2262 |
| `162.159.205.11` | 2044 | 2244 |
| `162.159.205.12` | 2044 | 2244 |
| `162.159.205.13` | 2044 | 2244 |
| `91.196.52.205` | 1981 | 2232 |
| `78.47.124.133` | 1502 | 1502 |
| `94.130.108.80` | 1502 | 1502 |
| `116.202.9.167` | 1161 | 1161 |
| `46.101.111.206` | 1161 | 1161 |
| `195.123.189.142` | 1153 | 1219 |
| `142.132.166.12` | 1148 | 1148 |
| `188.166.111.252` | 1148 | 1148 |
| `87.98.164.155` | 1080 | 1088 |
| `146.190.212.90` | 1030 | 1030 |
| `146.190.223.124` | 1023 | 1023 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 377 |
| High-confidence disposable IPs | 947 |
| Promoted to `domains_inferred.txt` | 4 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**6789 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

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


*… and 6,759 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
