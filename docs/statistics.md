# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-11-06 02:52 UTC**.*  
*Last DNS snapshot: **2026-11-06T02:31:39+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 98,896 |
| `domains_strict.txt` | 100,128 |
| `domains_inferred.txt` (opt-in) | 4 |

## Reachability

Of **103,759** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 33,345 | 32.1% |
| A_ONLY | 2,250 | 2.2% |
| NXDOMAIN | 18,945 | 18.3% |
| NO_RECORDS | 524 | 0.5% |
| TIMEOUT | 48,695 | 46.9% |

**35,595 domains are mail-reachable today** (34.3%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `route2.mx.cloudflare.net` | 2138 | 2331 | yes |
| `route1.mx.cloudflare.net` | 2137 | 2330 | yes |
| `route3.mx.cloudflare.net` | 2137 | 2330 | yes |
| `mail.wabblywabble.com` | 1240 | 1242 |  |
| `mail.wallywatts.com` | 1240 | 1242 |  |
| `generator.email` | 1227 | 1464 |  |
| `aero4.unstablemail.com` | 1038 | 1038 |  |
| `srv4.unstablemail.com` | 1038 | 1038 |  |
| `park-mx.above.com` | 819 | 921 | yes |
| `smtp.google.com` | 749 | 777 | yes |
| `aspmx.l.google.com` | 733 | 819 | yes |
| `alt1.aspmx.l.google.com` | 724 | 808 | yes |
| `alt2.aspmx.l.google.com` | 722 | 804 | yes |
| `eforward1.registrar-servers.com` | 689 | 728 | yes |
| `eforward2.registrar-servers.com` | 689 | 728 | yes |
| `eforward3.registrar-servers.com` | 689 | 728 | yes |
| `eforward4.registrar-servers.com` | 689 | 728 | yes |
| `eforward5.registrar-servers.com` | 689 | 728 | yes |
| `mx4.beavis99.com` | 570 | 570 |  |
| `mx4.beavis99.net` | 569 | 569 |  |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 1240 | 1242 |
| `mail.wallywatts.com` | 1240 | 1242 |
| `generator.email` | 1227 | 1464 |
| `aero4.unstablemail.com` | 1038 | 1038 |
| `srv4.unstablemail.com` | 1038 | 1038 |
| `mx4.beavis99.com` | 570 | 570 |
| `mx4.beavis99.net` | 569 | 569 |
| `email.chatgpt.org.uk` | 537 | 549 |
| `emailfake.com` | 509 | 523 |
| `smtp.yopmail.com` | 465 | 473 |
| `mx1.timeweb.ru` | 325 | 356 |
| `mx2.timeweb.ru` | 325 | 356 |
| `mx2-hosting.jellyfish.systems` | 305 | 316 |
| `mx3-hosting.jellyfish.systems` | 305 | 316 |
| `mx1-hosting.jellyfish.systems` | 304 | 315 |
| `void.blackhole.mx` | 286 | 289 |
| `mx1.titan.email` | 269 | 271 |
| `mx2.titan.email` | 266 | 268 |
| `smtp.215.im` | 257 | 261 |
| `tinyhost.shop` | 254 | 254 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `162.159.205.23` | 2026 | 2215 |
| `162.159.205.24` | 2026 | 2215 |
| `162.159.205.25` | 2026 | 2215 |
| `162.159.205.17` | 2025 | 2214 |
| `162.159.205.18` | 2025 | 2214 |
| `162.159.205.19` | 2025 | 2214 |
| `162.159.205.11` | 2007 | 2196 |
| `162.159.205.12` | 2007 | 2196 |
| `162.159.205.13` | 2007 | 2196 |
| `91.196.52.205` | 1828 | 2072 |
| `78.47.124.133` | 1193 | 1193 |
| `94.130.108.80` | 1193 | 1193 |
| `195.123.189.142` | 1150 | 1219 |
| `116.202.9.167` | 1110 | 1112 |
| `46.101.111.206` | 1110 | 1112 |
| `142.132.166.12` | 1098 | 1100 |
| `188.166.111.252` | 1098 | 1100 |
| `146.190.212.90` | 984 | 984 |
| `146.190.223.124` | 975 | 975 |
| `103.224.212.34` | 739 | 839 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 377 |
| High-confidence disposable IPs | 933 |
| Promoted to `domains_inferred.txt` | 4 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**6648 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

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
| `0ak.org` | `mx00.ionos.com` |
| `0hcow.com` | `mxa.mailgun.org` |
| `0hio.net` | `aspmx1.migadu.com` |
| `0nce.net` | `route1.mx.cloudflare.net` |


*… and 6,618 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
