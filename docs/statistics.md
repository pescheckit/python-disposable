# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-10-31 02:19 UTC**.*  
*Last DNS snapshot: **2026-10-31T02:19:35+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 98,543 |
| `domains_strict.txt` | 99,775 |
| `domains_inferred.txt` (opt-in) | 4 |

## Reachability

Of **102,707** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 39,723 | 38.7% |
| A_ONLY | 4,225 | 4.1% |
| NXDOMAIN | 31,379 | 30.6% |
| NO_RECORDS | 812 | 0.8% |
| TIMEOUT | 26,568 | 25.9% |

**43,948 domains are mail-reachable today** (42.8%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `route1.mx.cloudflare.net` | 2436 | 2598 | yes |
| `route2.mx.cloudflare.net` | 2436 | 2598 | yes |
| `route3.mx.cloudflare.net` | 2435 | 2597 | yes |
| `mail.wabblywabble.com` | 1603 | 1604 |  |
| `mail.wallywatts.com` | 1603 | 1604 |  |
| `generator.email` | 1237 | 1457 |  |
| `aero4.unstablemail.com` | 1182 | 1183 |  |
| `srv4.unstablemail.com` | 1181 | 1182 |  |
| `mx4.beavis99.com` | 972 | 972 |  |
| `mx4.beavis99.net` | 971 | 971 |  |
| `park-mx.above.com` | 936 | 1027 | yes |
| `aspmx.l.google.com` | 835 | 920 | yes |
| `alt1.aspmx.l.google.com` | 820 | 903 | yes |
| `alt2.aspmx.l.google.com` | 815 | 896 | yes |
| `eforward1.registrar-servers.com` | 810 | 840 | yes |
| `eforward2.registrar-servers.com` | 810 | 840 | yes |
| `eforward3.registrar-servers.com` | 810 | 840 | yes |
| `eforward4.registrar-servers.com` | 810 | 840 | yes |
| `eforward5.registrar-servers.com` | 810 | 840 | yes |
| `smtp.google.com` | 763 | 790 | yes |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 1603 | 1604 |
| `mail.wallywatts.com` | 1603 | 1604 |
| `generator.email` | 1237 | 1457 |
| `aero4.unstablemail.com` | 1182 | 1183 |
| `srv4.unstablemail.com` | 1181 | 1182 |
| `mx4.beavis99.com` | 972 | 972 |
| `mx4.beavis99.net` | 971 | 971 |
| `emailfake.com` | 616 | 628 |
| `smtp.yopmail.com` | 549 | 557 |
| `email.chatgpt.org.uk` | 465 | 469 |
| `mx.emlhub.com` | 367 | 367 |
| `tinyhost.shop` | 362 | 362 |
| `mx2-hosting.jellyfish.systems` | 330 | 340 |
| `mx3-hosting.jellyfish.systems` | 330 | 340 |
| `mx1-hosting.jellyfish.systems` | 329 | 339 |
| `mx2.timeweb.ru` | 327 | 358 |
| `mx1.timeweb.ru` | 326 | 357 |
| `mx156.hostedmxserver.com` | 311 | 431 |
| `mail.h-email.net` | 302 | 374 |
| `mx1.beget.com` | 296 | 303 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `162.159.205.23` | 2386 | 2545 |
| `162.159.205.24` | 2386 | 2545 |
| `162.159.205.25` | 2386 | 2545 |
| `162.159.205.17` | 2379 | 2537 |
| `162.159.205.18` | 2379 | 2537 |
| `162.159.205.19` | 2379 | 2537 |
| `162.159.205.11` | 2356 | 2514 |
| `162.159.205.12` | 2356 | 2514 |
| `162.159.205.13` | 2356 | 2514 |
| `78.47.124.133` | 2046 | 2046 |
| `94.130.108.80` | 2046 | 2046 |
| `91.196.52.205` | 2006 | 2233 |
| `116.202.9.167` | 1497 | 1498 |
| `46.101.111.206` | 1497 | 1498 |
| `142.132.166.12` | 1493 | 1493 |
| `188.166.111.252` | 1493 | 1493 |
| `195.123.189.142` | 1149 | 1209 |
| `146.190.212.90` | 1135 | 1136 |
| `146.190.223.124` | 1124 | 1125 |
| `188.245.74.208` | 896 | 896 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 429 |
| High-confidence disposable IPs | 1,052 |
| Promoted to `domains_inferred.txt` | 4 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**7588 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

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


*… and 7,558 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
