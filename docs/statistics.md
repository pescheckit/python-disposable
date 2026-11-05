# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-11-05 03:12 UTC**.*  
*Last DNS snapshot: **2026-11-05T02:51:35+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 98,860 |
| `domains_strict.txt` | 100,092 |
| `domains_inferred.txt` (opt-in) | 4 |

## Reachability

Of **103,645** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 36,747 | 35.5% |
| A_ONLY | 3,240 | 3.1% |
| NXDOMAIN | 25,024 | 24.1% |
| NO_RECORDS | 659 | 0.6% |
| TIMEOUT | 37,975 | 36.6% |

**39,987 domains are mail-reachable today** (38.6%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `route2.mx.cloudflare.net` | 2314 | 2493 | yes |
| `route1.mx.cloudflare.net` | 2313 | 2492 | yes |
| `route3.mx.cloudflare.net` | 2313 | 2492 | yes |
| `mail.wabblywabble.com` | 1369 | 1369 |  |
| `mail.wallywatts.com` | 1369 | 1369 |  |
| `generator.email` | 1338 | 1572 |  |
| `aero4.unstablemail.com` | 1101 | 1103 |  |
| `srv4.unstablemail.com` | 1101 | 1103 |  |
| `park-mx.above.com` | 918 | 1019 | yes |
| `aspmx.l.google.com` | 794 | 880 | yes |
| `alt1.aspmx.l.google.com` | 782 | 866 | yes |
| `alt2.aspmx.l.google.com` | 780 | 862 | yes |
| `mx4.beavis99.com` | 780 | 780 |  |
| `mx4.beavis99.net` | 779 | 779 |  |
| `smtp.google.com` | 761 | 790 | yes |
| `eforward1.registrar-servers.com` | 744 | 782 | yes |
| `eforward2.registrar-servers.com` | 744 | 782 | yes |
| `eforward3.registrar-servers.com` | 744 | 782 | yes |
| `eforward4.registrar-servers.com` | 744 | 782 | yes |
| `eforward5.registrar-servers.com` | 744 | 782 | yes |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 1369 | 1369 |
| `mail.wallywatts.com` | 1369 | 1369 |
| `generator.email` | 1338 | 1572 |
| `aero4.unstablemail.com` | 1101 | 1103 |
| `srv4.unstablemail.com` | 1101 | 1103 |
| `mx4.beavis99.com` | 780 | 780 |
| `mx4.beavis99.net` | 779 | 779 |
| `emailfake.com` | 571 | 584 |
| `email.chatgpt.org.uk` | 559 | 570 |
| `smtp.yopmail.com` | 507 | 515 |
| `tinyhost.shop` | 326 | 326 |
| `mx2.timeweb.ru` | 325 | 355 |
| `mx1.timeweb.ru` | 324 | 354 |
| `mx.emlhub.com` | 308 | 308 |
| `mx2-hosting.jellyfish.systems` | 308 | 319 |
| `mx3-hosting.jellyfish.systems` | 308 | 319 |
| `mx1-hosting.jellyfish.systems` | 307 | 318 |
| `void.blackhole.mx` | 291 | 293 |
| `mx1.titan.email` | 274 | 276 |
| `mx2.titan.email` | 271 | 273 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `162.159.205.23` | 2237 | 2413 |
| `162.159.205.24` | 2237 | 2413 |
| `162.159.205.25` | 2237 | 2413 |
| `162.159.205.17` | 2236 | 2411 |
| `162.159.205.18` | 2236 | 2411 |
| `162.159.205.19` | 2236 | 2411 |
| `162.159.205.11` | 2210 | 2385 |
| `162.159.205.12` | 2210 | 2385 |
| `162.159.205.13` | 2210 | 2385 |
| `91.196.52.205` | 2035 | 2274 |
| `78.47.124.133` | 1737 | 1737 |
| `94.130.108.80` | 1737 | 1737 |
| `116.202.9.167` | 1251 | 1251 |
| `46.101.111.206` | 1251 | 1251 |
| `142.132.166.12` | 1234 | 1234 |
| `188.166.111.252` | 1234 | 1234 |
| `195.123.189.142` | 1163 | 1223 |
| `146.190.212.90` | 1059 | 1061 |
| `146.190.223.124` | 1046 | 1048 |
| `103.224.212.34` | 848 | 947 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 400 |
| High-confidence disposable IPs | 985 |
| Promoted to `domains_inferred.txt` | 4 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**7208 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

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


*… and 7,178 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
