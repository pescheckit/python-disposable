# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-11-07 02:18 UTC**.*  
*Last DNS snapshot: **2026-11-07T02:09:37+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 98,914 |
| `domains_strict.txt` | 100,146 |
| `domains_inferred.txt` (opt-in) | 4 |

## Reachability

Of **103,888** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 34,103 | 32.8% |
| A_ONLY | 2,375 | 2.3% |
| NXDOMAIN | 19,800 | 19.1% |
| NO_RECORDS | 563 | 0.5% |
| TIMEOUT | 47,047 | 45.3% |

**36,478 domains are mail-reachable today** (35.1%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `route2.mx.cloudflare.net` | 2154 | 2357 | yes |
| `route1.mx.cloudflare.net` | 2153 | 2356 | yes |
| `route3.mx.cloudflare.net` | 2153 | 2356 | yes |
| `mail.wabblywabble.com` | 1273 | 1274 |  |
| `mail.wallywatts.com` | 1273 | 1274 |  |
| `generator.email` | 1243 | 1483 |  |
| `aero4.unstablemail.com` | 1059 | 1059 |  |
| `srv4.unstablemail.com` | 1059 | 1059 |  |
| `park-mx.above.com` | 858 | 969 | yes |
| `smtp.google.com` | 749 | 779 | yes |
| `aspmx.l.google.com` | 746 | 831 | yes |
| `alt1.aspmx.l.google.com` | 737 | 820 | yes |
| `alt2.aspmx.l.google.com` | 735 | 816 | yes |
| `eforward1.registrar-servers.com` | 702 | 742 | yes |
| `eforward2.registrar-servers.com` | 702 | 742 | yes |
| `eforward3.registrar-servers.com` | 702 | 742 | yes |
| `eforward4.registrar-servers.com` | 702 | 742 | yes |
| `eforward5.registrar-servers.com` | 702 | 742 | yes |
| `mx4.beavis99.com` | 591 | 591 |  |
| `mx4.beavis99.net` | 590 | 590 |  |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 1273 | 1274 |
| `mail.wallywatts.com` | 1273 | 1274 |
| `generator.email` | 1243 | 1483 |
| `aero4.unstablemail.com` | 1059 | 1059 |
| `srv4.unstablemail.com` | 1059 | 1059 |
| `mx4.beavis99.com` | 591 | 591 |
| `mx4.beavis99.net` | 590 | 590 |
| `email.chatgpt.org.uk` | 539 | 551 |
| `emailfake.com` | 516 | 530 |
| `smtp.yopmail.com` | 472 | 480 |
| `mx1.timeweb.ru` | 326 | 357 |
| `mx2.timeweb.ru` | 326 | 357 |
| `mx2-hosting.jellyfish.systems` | 310 | 322 |
| `mx3-hosting.jellyfish.systems` | 310 | 322 |
| `mx1-hosting.jellyfish.systems` | 309 | 321 |
| `void.blackhole.mx` | 293 | 294 |
| `mx1.titan.email` | 269 | 271 |
| `smtp.215.im` | 268 | 272 |
| `mx2.titan.email` | 266 | 268 |
| `mx.emlhub.com` | 265 | 265 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `162.159.205.23` | 2045 | 2244 |
| `162.159.205.24` | 2045 | 2244 |
| `162.159.205.25` | 2045 | 2244 |
| `162.159.205.17` | 2044 | 2243 |
| `162.159.205.18` | 2044 | 2243 |
| `162.159.205.19` | 2044 | 2243 |
| `162.159.205.11` | 2026 | 2225 |
| `162.159.205.12` | 2026 | 2225 |
| `162.159.205.13` | 2026 | 2225 |
| `91.196.52.205` | 1876 | 2123 |
| `78.47.124.133` | 1301 | 1301 |
| `94.130.108.80` | 1301 | 1301 |
| `195.123.189.142` | 1153 | 1219 |
| `116.202.9.167` | 1145 | 1146 |
| `46.101.111.206` | 1145 | 1146 |
| `142.132.166.12` | 1132 | 1133 |
| `188.166.111.252` | 1132 | 1133 |
| `146.190.212.90` | 1006 | 1006 |
| `146.190.223.124` | 998 | 998 |
| `103.224.212.34` | 780 | 889 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 379 |
| High-confidence disposable IPs | 937 |
| Promoted to `domains_inferred.txt` | 4 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**6747 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

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


*… and 6,717 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
