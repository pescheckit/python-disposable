# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-11-11 02:16 UTC**.*  
*Last DNS snapshot: **2026-11-11T02:09:04+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 102,763 |
| `domains_strict.txt` | 103,995 |
| `domains_inferred.txt` (opt-in) | 4 |

## Reachability

Of **107,984** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 39,943 | 37.0% |
| A_ONLY | 2,455 | 2.3% |
| NXDOMAIN | 19,974 | 18.5% |
| NO_RECORDS | 688 | 0.6% |
| TIMEOUT | 44,924 | 41.6% |

**42,398 domains are mail-reachable today** (39.3%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `generator.email` | 4922 | 5170 |  |
| `route2.mx.cloudflare.net` | 2202 | 2414 | yes |
| `route1.mx.cloudflare.net` | 2201 | 2413 | yes |
| `route3.mx.cloudflare.net` | 2201 | 2413 | yes |
| `mail.wabblywabble.com` | 1307 | 1308 |  |
| `mail.wallywatts.com` | 1307 | 1308 |  |
| `aero4.unstablemail.com` | 1088 | 1088 |  |
| `srv4.unstablemail.com` | 1087 | 1087 |  |
| `smtp.yopmail.com` | 999 | 1008 |  |
| `park-mx.above.com` | 896 | 1019 | yes |
| `smtp.google.com` | 801 | 829 | yes |
| `aspmx.l.google.com` | 745 | 831 | yes |
| `alt1.aspmx.l.google.com` | 736 | 820 | yes |
| `alt2.aspmx.l.google.com` | 734 | 816 | yes |
| `eforward1.registrar-servers.com` | 716 | 756 | yes |
| `eforward2.registrar-servers.com` | 716 | 756 | yes |
| `eforward3.registrar-servers.com` | 716 | 756 | yes |
| `eforward4.registrar-servers.com` | 716 | 756 | yes |
| `eforward5.registrar-servers.com` | 716 | 756 | yes |
| `email.chatgpt.org.uk` | 700 | 713 |  |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `generator.email` | 4922 | 5170 |
| `mail.wabblywabble.com` | 1307 | 1308 |
| `mail.wallywatts.com` | 1307 | 1308 |
| `aero4.unstablemail.com` | 1088 | 1088 |
| `srv4.unstablemail.com` | 1087 | 1087 |
| `smtp.yopmail.com` | 999 | 1008 |
| `email.chatgpt.org.uk` | 700 | 713 |
| `emailfake.com` | 629 | 646 |
| `mx4.beavis99.com` | 596 | 596 |
| `mx4.beavis99.net` | 595 | 595 |
| `smtp.215.im` | 402 | 406 |
| `mx.10mail.org` | 344 | 344 |
| `mx1.timeweb.ru` | 340 | 372 |
| `mx2.timeweb.ru` | 340 | 372 |
| `tinyhost.shop` | 325 | 325 |
| `mx2-hosting.jellyfish.systems` | 315 | 328 |
| `mx3-hosting.jellyfish.systems` | 315 | 328 |
| `mx1-hosting.jellyfish.systems` | 314 | 327 |
| `void.blackhole.mx` | 303 | 306 |
| `mx1.titan.email` | 276 | 278 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `91.196.52.205` | 5671 | 5929 |
| `162.159.205.17` | 2107 | 2315 |
| `162.159.205.18` | 2107 | 2315 |
| `162.159.205.19` | 2107 | 2315 |
| `162.159.205.23` | 2103 | 2311 |
| `162.159.205.24` | 2103 | 2311 |
| `162.159.205.25` | 2103 | 2311 |
| `162.159.205.11` | 2089 | 2297 |
| `162.159.205.12` | 2089 | 2297 |
| `162.159.205.13` | 2089 | 2297 |
| `201.3.122.6` | 1660 | 1667 |
| `78.47.124.133` | 1520 | 1520 |
| `94.130.108.80` | 1520 | 1520 |
| `116.202.9.167` | 1183 | 1184 |
| `46.101.111.206` | 1183 | 1184 |
| `142.132.166.12` | 1166 | 1167 |
| `188.166.111.252` | 1166 | 1167 |
| `87.98.164.155` | 1045 | 1054 |
| `146.190.212.90` | 1043 | 1043 |
| `146.190.223.124` | 1036 | 1036 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 378 |
| High-confidence disposable IPs | 918 |
| Promoted to `domains_inferred.txt` | 4 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**6908 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

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


*… and 6,878 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
