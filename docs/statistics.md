# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-11-04 02:34 UTC**.*  
*Last DNS snapshot: **2026-11-04T02:27:22+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 98,829 |
| `domains_strict.txt` | 100,061 |
| `domains_inferred.txt` (opt-in) | 4 |

## Reachability

Of **103,479** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 37,530 | 36.3% |
| A_ONLY | 3,459 | 3.3% |
| NXDOMAIN | 26,714 | 25.8% |
| NO_RECORDS | 704 | 0.7% |
| TIMEOUT | 35,072 | 33.9% |

**40,989 domains are mail-reachable today** (39.6%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `route1.mx.cloudflare.net` | 2341 | 2517 | yes |
| `route2.mx.cloudflare.net` | 2341 | 2517 | yes |
| `route3.mx.cloudflare.net` | 2340 | 2516 | yes |
| `mail.wabblywabble.com` | 1433 | 1435 |  |
| `mail.wallywatts.com` | 1433 | 1435 |  |
| `generator.email` | 1334 | 1563 |  |
| `aero4.unstablemail.com` | 1123 | 1124 |  |
| `srv4.unstablemail.com` | 1123 | 1124 |  |
| `park-mx.above.com` | 940 | 1034 | yes |
| `mx4.beavis99.com` | 860 | 860 |  |
| `mx4.beavis99.net` | 859 | 859 |  |
| `aspmx.l.google.com` | 787 | 872 | yes |
| `alt1.aspmx.l.google.com` | 773 | 856 | yes |
| `alt2.aspmx.l.google.com` | 769 | 850 | yes |
| `smtp.google.com` | 765 | 794 | yes |
| `eforward1.registrar-servers.com` | 753 | 791 | yes |
| `eforward2.registrar-servers.com` | 753 | 791 | yes |
| `eforward3.registrar-servers.com` | 753 | 791 | yes |
| `eforward4.registrar-servers.com` | 753 | 791 | yes |
| `eforward5.registrar-servers.com` | 753 | 791 | yes |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 1433 | 1435 |
| `mail.wallywatts.com` | 1433 | 1435 |
| `generator.email` | 1334 | 1563 |
| `aero4.unstablemail.com` | 1123 | 1124 |
| `srv4.unstablemail.com` | 1123 | 1124 |
| `mx4.beavis99.com` | 860 | 860 |
| `mx4.beavis99.net` | 859 | 859 |
| `emailfake.com` | 583 | 597 |
| `email.chatgpt.org.uk` | 562 | 566 |
| `smtp.yopmail.com` | 512 | 520 |
| `tinyhost.shop` | 335 | 335 |
| `mx2.timeweb.ru` | 324 | 354 |
| `mx1.timeweb.ru` | 323 | 353 |
| `mx.emlhub.com` | 322 | 322 |
| `mx2-hosting.jellyfish.systems` | 315 | 326 |
| `mx3-hosting.jellyfish.systems` | 315 | 326 |
| `mx1-hosting.jellyfish.systems` | 314 | 325 |
| `void.blackhole.mx` | 289 | 290 |
| `mail.h-email.net` | 275 | 341 |
| `mx1.titan.email` | 275 | 277 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `162.159.205.23` | 2278 | 2451 |
| `162.159.205.24` | 2278 | 2451 |
| `162.159.205.25` | 2278 | 2451 |
| `162.159.205.17` | 2273 | 2445 |
| `162.159.205.18` | 2273 | 2445 |
| `162.159.205.19` | 2273 | 2445 |
| `162.159.205.11` | 2250 | 2422 |
| `162.159.205.12` | 2250 | 2422 |
| `162.159.205.13` | 2250 | 2422 |
| `91.196.52.205` | 2057 | 2294 |
| `78.47.124.133` | 1827 | 1827 |
| `94.130.108.80` | 1827 | 1827 |
| `116.202.9.167` | 1310 | 1312 |
| `46.101.111.206` | 1310 | 1312 |
| `142.132.166.12` | 1308 | 1310 |
| `188.166.111.252` | 1308 | 1310 |
| `195.123.189.142` | 1161 | 1223 |
| `146.190.212.90` | 1072 | 1073 |
| `146.190.223.124` | 1066 | 1067 |
| `103.224.212.34` | 865 | 957 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 417 |
| High-confidence disposable IPs | 1,015 |
| Promoted to `domains_inferred.txt` | 4 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**7299 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

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


*… and 7,269 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
