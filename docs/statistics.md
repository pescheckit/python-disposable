# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-11-02 02:21 UTC**.*  
*Last DNS snapshot: **2026-11-02T02:21:41+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 98,628 |
| `domains_strict.txt` | 99,860 |
| `domains_inferred.txt` (opt-in) | 4 |

## Reachability

Of **103,241** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 40,305 | 39.0% |
| A_ONLY | 4,243 | 4.1% |
| NXDOMAIN | 31,473 | 30.5% |
| NO_RECORDS | 824 | 0.8% |
| TIMEOUT | 26,396 | 25.6% |

**44,548 domains are mail-reachable today** (43.1%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `route1.mx.cloudflare.net` | 2472 | 2648 | yes |
| `route2.mx.cloudflare.net` | 2472 | 2648 | yes |
| `route3.mx.cloudflare.net` | 2471 | 2647 | yes |
| `mail.wabblywabble.com` | 1617 | 1617 |  |
| `mail.wallywatts.com` | 1617 | 1617 |  |
| `generator.email` | 1382 | 1609 |  |
| `aero4.unstablemail.com` | 1193 | 1193 |  |
| `srv4.unstablemail.com` | 1192 | 1192 |  |
| `park-mx.above.com` | 1009 | 1103 | yes |
| `mx4.beavis99.com` | 974 | 974 |  |
| `mx4.beavis99.net` | 973 | 973 |  |
| `aspmx.l.google.com` | 851 | 938 | yes |
| `alt1.aspmx.l.google.com` | 837 | 922 | yes |
| `alt2.aspmx.l.google.com` | 832 | 915 | yes |
| `eforward1.registrar-servers.com` | 810 | 848 | yes |
| `eforward2.registrar-servers.com` | 810 | 848 | yes |
| `eforward3.registrar-servers.com` | 810 | 848 | yes |
| `eforward4.registrar-servers.com` | 810 | 848 | yes |
| `eforward5.registrar-servers.com` | 810 | 848 | yes |
| `smtp.google.com` | 787 | 815 | yes |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 1617 | 1617 |
| `mail.wallywatts.com` | 1617 | 1617 |
| `generator.email` | 1382 | 1609 |
| `aero4.unstablemail.com` | 1193 | 1193 |
| `srv4.unstablemail.com` | 1192 | 1192 |
| `mx4.beavis99.com` | 974 | 974 |
| `mx4.beavis99.net` | 973 | 973 |
| `emailfake.com` | 621 | 634 |
| `email.chatgpt.org.uk` | 593 | 597 |
| `smtp.yopmail.com` | 527 | 535 |
| `tinyhost.shop` | 395 | 395 |
| `mx.emlhub.com` | 367 | 367 |
| `mx2.timeweb.ru` | 329 | 361 |
| `mx1.timeweb.ru` | 328 | 360 |
| `mx2-hosting.jellyfish.systems` | 325 | 336 |
| `mx3-hosting.jellyfish.systems` | 325 | 336 |
| `mx1-hosting.jellyfish.systems` | 324 | 335 |
| `mail.h-email.net` | 300 | 373 |
| `void.blackhole.mx` | 290 | 293 |
| `mx156.hostedmxserver.com` | 288 | 441 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `162.159.205.23` | 2432 | 2605 |
| `162.159.205.24` | 2432 | 2605 |
| `162.159.205.25` | 2432 | 2605 |
| `162.159.205.17` | 2418 | 2590 |
| `162.159.205.18` | 2418 | 2590 |
| `162.159.205.19` | 2418 | 2590 |
| `162.159.205.11` | 2396 | 2568 |
| `162.159.205.12` | 2396 | 2568 |
| `162.159.205.13` | 2396 | 2568 |
| `91.196.52.205` | 2187 | 2421 |
| `78.47.124.133` | 2090 | 2090 |
| `94.130.108.80` | 2090 | 2090 |
| `116.202.9.167` | 1514 | 1514 |
| `46.101.111.206` | 1514 | 1514 |
| `142.132.166.12` | 1510 | 1510 |
| `188.166.111.252` | 1510 | 1510 |
| `195.123.189.142` | 1169 | 1229 |
| `146.190.212.90` | 1144 | 1144 |
| `146.190.223.124` | 1138 | 1138 |
| `103.224.212.34` | 948 | 1040 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 430 |
| High-confidence disposable IPs | 1,086 |
| Promoted to `domains_inferred.txt` | 4 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**7742 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

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


*… and 7,712 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
