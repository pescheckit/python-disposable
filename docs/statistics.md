# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-11-01 02:15 UTC**.*  
*Last DNS snapshot: **2026-11-01T02:10:13+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 98,626 |
| `domains_strict.txt` | 99,858 |
| `domains_inferred.txt` (opt-in) | 4 |

## Reachability

Of **103,132** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 40,362 | 39.1% |
| A_ONLY | 4,232 | 4.1% |
| NXDOMAIN | 31,407 | 30.5% |
| NO_RECORDS | 827 | 0.8% |
| TIMEOUT | 26,304 | 25.5% |

**44,594 domains are mail-reachable today** (43.2%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `route1.mx.cloudflare.net` | 2452 | 2625 | yes |
| `route2.mx.cloudflare.net` | 2452 | 2625 | yes |
| `route3.mx.cloudflare.net` | 2451 | 2624 | yes |
| `mail.wabblywabble.com` | 1602 | 1604 |  |
| `mail.wallywatts.com` | 1602 | 1604 |  |
| `generator.email` | 1371 | 1600 |  |
| `aero4.unstablemail.com` | 1181 | 1182 |  |
| `srv4.unstablemail.com` | 1180 | 1181 |  |
| `park-mx.above.com` | 993 | 1086 | yes |
| `mx4.beavis99.com` | 972 | 972 |  |
| `mx4.beavis99.net` | 971 | 971 |  |
| `aspmx.l.google.com` | 846 | 930 | yes |
| `alt1.aspmx.l.google.com` | 831 | 913 | yes |
| `alt2.aspmx.l.google.com` | 826 | 906 | yes |
| `eforward1.registrar-servers.com` | 806 | 844 | yes |
| `eforward2.registrar-servers.com` | 806 | 844 | yes |
| `eforward3.registrar-servers.com` | 806 | 844 | yes |
| `eforward4.registrar-servers.com` | 806 | 844 | yes |
| `eforward5.registrar-servers.com` | 806 | 844 | yes |
| `smtp.google.com` | 770 | 798 | yes |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 1602 | 1604 |
| `mail.wallywatts.com` | 1602 | 1604 |
| `generator.email` | 1371 | 1600 |
| `aero4.unstablemail.com` | 1181 | 1182 |
| `srv4.unstablemail.com` | 1180 | 1181 |
| `mx4.beavis99.com` | 972 | 972 |
| `mx4.beavis99.net` | 971 | 971 |
| `emailfake.com` | 621 | 634 |
| `email.chatgpt.org.uk` | 594 | 598 |
| `smtp.yopmail.com` | 551 | 559 |
| `tinyhost.shop` | 390 | 390 |
| `mx.emlhub.com` | 367 | 367 |
| `mx2.timeweb.ru` | 333 | 363 |
| `mx1.timeweb.ru` | 332 | 362 |
| `mx2-hosting.jellyfish.systems` | 328 | 340 |
| `mx3-hosting.jellyfish.systems` | 328 | 340 |
| `mx1-hosting.jellyfish.systems` | 327 | 339 |
| `mail.h-email.net` | 308 | 373 |
| `mx1.beget.com` | 297 | 304 |
| `mx2.beget.com` | 297 | 304 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `162.159.205.23` | 2403 | 2573 |
| `162.159.205.24` | 2403 | 2573 |
| `162.159.205.25` | 2403 | 2573 |
| `162.159.205.17` | 2396 | 2565 |
| `162.159.205.18` | 2396 | 2565 |
| `162.159.205.19` | 2396 | 2565 |
| `162.159.205.11` | 2373 | 2542 |
| `162.159.205.12` | 2373 | 2542 |
| `162.159.205.13` | 2373 | 2542 |
| `91.196.52.205` | 2167 | 2403 |
| `78.47.124.133` | 2090 | 2090 |
| `94.130.108.80` | 2090 | 2090 |
| `116.202.9.167` | 1496 | 1498 |
| `46.101.111.206` | 1496 | 1498 |
| `142.132.166.12` | 1490 | 1492 |
| `188.166.111.252` | 1490 | 1492 |
| `195.123.189.142` | 1147 | 1209 |
| `146.190.212.90` | 1129 | 1130 |
| `146.190.223.124` | 1118 | 1119 |
| `103.224.212.34` | 932 | 1023 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 431 |
| High-confidence disposable IPs | 1,052 |
| Promoted to `domains_inferred.txt` | 4 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**7680 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

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


*… and 7,650 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
