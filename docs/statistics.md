# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-10-28 02:53 UTC**.*  
*Last DNS snapshot: **2026-10-28T02:48:42+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 98,543 |
| `domains_strict.txt` | 99,775 |
| `domains_inferred.txt` (opt-in) | 4 |

## Reachability

Of **102,706** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 41,562 | 40.5% |
| A_ONLY | 4,369 | 4.3% |
| NXDOMAIN | 32,131 | 31.3% |
| NO_RECORDS | 908 | 0.9% |
| TIMEOUT | 23,736 | 23.1% |

**45,931 domains are mail-reachable today** (44.7%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `route1.mx.cloudflare.net` | 2465 | 2627 | yes |
| `route2.mx.cloudflare.net` | 2465 | 2627 | yes |
| `route3.mx.cloudflare.net` | 2464 | 2626 | yes |
| `mail.wabblywabble.com` | 1649 | 1650 |  |
| `mail.wallywatts.com` | 1649 | 1650 |  |
| `generator.email` | 1272 | 1492 |  |
| `aero4.unstablemail.com` | 1218 | 1219 |  |
| `srv4.unstablemail.com` | 1216 | 1217 |  |
| `smtp.yopmail.com` | 1083 | 1091 |  |
| `mx4.beavis99.com` | 982 | 982 |  |
| `mx4.beavis99.net` | 981 | 981 |  |
| `park-mx.above.com` | 958 | 1049 | yes |
| `aspmx.l.google.com` | 857 | 942 | yes |
| `alt1.aspmx.l.google.com` | 842 | 925 | yes |
| `alt2.aspmx.l.google.com` | 837 | 918 | yes |
| `eforward1.registrar-servers.com` | 822 | 852 | yes |
| `eforward2.registrar-servers.com` | 822 | 852 | yes |
| `eforward3.registrar-servers.com` | 822 | 852 | yes |
| `eforward4.registrar-servers.com` | 822 | 852 | yes |
| `eforward5.registrar-servers.com` | 822 | 852 | yes |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 1649 | 1650 |
| `mail.wallywatts.com` | 1649 | 1650 |
| `generator.email` | 1272 | 1492 |
| `aero4.unstablemail.com` | 1218 | 1219 |
| `srv4.unstablemail.com` | 1216 | 1217 |
| `smtp.yopmail.com` | 1083 | 1091 |
| `mx4.beavis99.com` | 982 | 982 |
| `mx4.beavis99.net` | 981 | 981 |
| `emailfake.com` | 653 | 665 |
| `email.chatgpt.org.uk` | 625 | 629 |
| `tinyhost.shop` | 423 | 423 |
| `mx.emlhub.com` | 385 | 385 |
| `smtp.215.im` | 345 | 348 |
| `mx2-hosting.jellyfish.systems` | 335 | 345 |
| `mx3-hosting.jellyfish.systems` | 335 | 345 |
| `mx1-hosting.jellyfish.systems` | 334 | 344 |
| `mx2.timeweb.ru` | 332 | 363 |
| `mx1.timeweb.ru` | 331 | 362 |
| `mail.h-email.net` | 312 | 384 |
| `mx.10mail.org` | 302 | 302 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `162.159.205.23` | 2419 | 2578 |
| `162.159.205.24` | 2419 | 2578 |
| `162.159.205.25` | 2419 | 2578 |
| `162.159.205.17` | 2413 | 2571 |
| `162.159.205.18` | 2413 | 2571 |
| `162.159.205.19` | 2413 | 2571 |
| `162.159.205.11` | 2399 | 2557 |
| `162.159.205.12` | 2399 | 2557 |
| `162.159.205.13` | 2399 | 2557 |
| `78.47.124.133` | 2333 | 2333 |
| `94.130.108.80` | 2333 | 2333 |
| `91.196.52.205` | 2124 | 2351 |
| `116.202.9.167` | 1543 | 1544 |
| `142.132.166.12` | 1543 | 1543 |
| `188.166.111.252` | 1543 | 1543 |
| `46.101.111.206` | 1543 | 1544 |
| `146.190.212.90` | 1175 | 1176 |
| `146.190.223.124` | 1165 | 1166 |
| `87.98.164.155` | 1151 | 1159 |
| `195.123.189.142` | 1150 | 1210 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 437 |
| High-confidence disposable IPs | 1,055 |
| Promoted to `domains_inferred.txt` | 4 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**7708 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

| Listed disposable | MX (shared infra) |
|---|---|
| `0-30-24.com` | `alt1.aspmx.l.google.com` |
| `0-mail.com` | `park-mx.above.com` |
| `000476.com` | `park-mx.above.com` |
| `000728.xyz` | `route1.mx.cloudflare.net` |
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
| `0nce.net` | `route1.mx.cloudflare.net` |


*… and 7,678 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
