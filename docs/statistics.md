# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-11-03 02:17 UTC**.*  
*Last DNS snapshot: **2026-11-03T02:10:04+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 98,465 |
| `domains_strict.txt` | 99,697 |
| `domains_inferred.txt` (opt-in) | 4 |

## Reachability

Of **103,318** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 40,364 | 39.1% |
| A_ONLY | 4,244 | 4.1% |
| NXDOMAIN | 31,483 | 30.5% |
| NO_RECORDS | 825 | 0.8% |
| TIMEOUT | 26,402 | 25.6% |

**44,608 domains are mail-reachable today** (43.2%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `route1.mx.cloudflare.net` | 2473 | 2650 | yes |
| `route2.mx.cloudflare.net` | 2473 | 2650 | yes |
| `route3.mx.cloudflare.net` | 2472 | 2649 | yes |
| `mail.wabblywabble.com` | 1622 | 1623 |  |
| `mail.wallywatts.com` | 1622 | 1623 |  |
| `generator.email` | 1383 | 1610 |  |
| `aero4.unstablemail.com` | 1191 | 1193 |  |
| `srv4.unstablemail.com` | 1190 | 1192 |  |
| `park-mx.above.com` | 1010 | 1104 | yes |
| `mx4.beavis99.com` | 975 | 975 |  |
| `mx4.beavis99.net` | 974 | 974 |  |
| `aspmx.l.google.com` | 855 | 939 | yes |
| `alt1.aspmx.l.google.com` | 841 | 923 | yes |
| `alt2.aspmx.l.google.com` | 836 | 916 | yes |
| `eforward1.registrar-servers.com` | 810 | 848 | yes |
| `eforward2.registrar-servers.com` | 810 | 848 | yes |
| `eforward3.registrar-servers.com` | 810 | 848 | yes |
| `eforward4.registrar-servers.com` | 810 | 848 | yes |
| `eforward5.registrar-servers.com` | 810 | 848 | yes |
| `smtp.google.com` | 787 | 816 | yes |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 1622 | 1623 |
| `mail.wallywatts.com` | 1622 | 1623 |
| `generator.email` | 1383 | 1610 |
| `aero4.unstablemail.com` | 1191 | 1193 |
| `srv4.unstablemail.com` | 1190 | 1192 |
| `mx4.beavis99.com` | 975 | 975 |
| `mx4.beavis99.net` | 974 | 974 |
| `emailfake.com` | 621 | 634 |
| `email.chatgpt.org.uk` | 608 | 612 |
| `smtp.yopmail.com` | 527 | 535 |
| `tinyhost.shop` | 396 | 396 |
| `mx.emlhub.com` | 367 | 367 |
| `mx2.timeweb.ru` | 329 | 360 |
| `mx1.timeweb.ru` | 328 | 359 |
| `mx2-hosting.jellyfish.systems` | 325 | 336 |
| `mx3-hosting.jellyfish.systems` | 325 | 336 |
| `mx1-hosting.jellyfish.systems` | 324 | 335 |
| `mail.h-email.net` | 298 | 369 |
| `void.blackhole.mx` | 294 | 294 |
| `mx156.hostedmxserver.com` | 287 | 440 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `162.159.205.23` | 2432 | 2606 |
| `162.159.205.24` | 2432 | 2606 |
| `162.159.205.25` | 2432 | 2606 |
| `162.159.205.17` | 2423 | 2596 |
| `162.159.205.18` | 2423 | 2596 |
| `162.159.205.19` | 2423 | 2596 |
| `162.159.205.11` | 2402 | 2575 |
| `162.159.205.12` | 2402 | 2575 |
| `162.159.205.13` | 2402 | 2575 |
| `91.196.52.205` | 2192 | 2426 |
| `78.47.124.133` | 2090 | 2090 |
| `94.130.108.80` | 2090 | 2090 |
| `116.202.9.167` | 1519 | 1520 |
| `46.101.111.206` | 1519 | 1520 |
| `142.132.166.12` | 1516 | 1517 |
| `188.166.111.252` | 1516 | 1517 |
| `146.190.212.90` | 1142 | 1144 |
| `146.190.223.124` | 1136 | 1138 |
| `195.123.189.142` | 1122 | 1229 |
| `103.224.212.34` | 950 | 1042 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 430 |
| High-confidence disposable IPs | 1,073 |
| Promoted to `domains_inferred.txt` | 4 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**7745 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

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
| `041998.xyz` | `mx1.alias.proton.me` |
| `0500betvip.com` | `route1.mx.cloudflare.net` |
| `057gmail.com` | `route1.mx.cloudflare.net` |
| `099833.xyz` | `park-mx.above.com` |
| `0ak.org` | `mx00.ionos.com` |
| `0hcow.com` | `mxa.mailgun.org` |
| `0hio.net` | `aspmx1.migadu.com` |


*… and 7,715 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
