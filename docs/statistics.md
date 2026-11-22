# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-11-22 02:42 UTC**.*  
*Last DNS snapshot: **2026-11-22T02:36:33+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 108,875 |
| `domains_strict.txt` | 109,938 |
| `domains_inferred.txt` (opt-in) | 4 |

## Reachability

Of **114,601** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 39,427 | 34.4% |
| A_ONLY | 4,899 | 4.3% |
| NXDOMAIN | 35,734 | 31.2% |
| NO_RECORDS | 917 | 0.8% |
| TIMEOUT | 33,624 | 29.3% |

**44,326 domains are mail-reachable today** (38.7%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `generator.email` | 8211 | 8475 |  |
| `route2.mx.cloudflare.net` | 1523 | 1751 | yes |
| `route3.mx.cloudflare.net` | 1523 | 1751 | yes |
| `route1.mx.cloudflare.net` | 1522 | 1750 | yes |
| `mail.wabblywabble.com` | 1424 | 1425 |  |
| `mail.wallywatts.com` | 1424 | 1425 |  |
| `mx4.beavis99.com` | 1003 | 1003 |  |
| `mx4.beavis99.net` | 1002 | 1002 |  |
| `park-mx.above.com` | 884 | 1031 | yes |
| `email.chatgpt.org.uk` | 783 | 796 |  |
| `aero4.unstablemail.com` | 643 | 643 |  |
| `srv4.unstablemail.com` | 641 | 641 |  |
| `aspmx.l.google.com` | 574 | 662 | yes |
| `smtp.yopmail.com` | 569 | 578 |  |
| `alt1.aspmx.l.google.com` | 565 | 651 | yes |
| `alt2.aspmx.l.google.com` | 559 | 643 | yes |
| `emailfake.com` | 537 | 553 |  |
| `eforward1.registrar-servers.com` | 472 | 522 | yes |
| `eforward2.registrar-servers.com` | 472 | 522 | yes |
| `eforward3.registrar-servers.com` | 472 | 522 | yes |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `generator.email` | 8211 | 8475 |
| `mail.wabblywabble.com` | 1424 | 1425 |
| `mail.wallywatts.com` | 1424 | 1425 |
| `mx4.beavis99.com` | 1003 | 1003 |
| `mx4.beavis99.net` | 1002 | 1002 |
| `email.chatgpt.org.uk` | 783 | 796 |
| `aero4.unstablemail.com` | 643 | 643 |
| `srv4.unstablemail.com` | 641 | 641 |
| `smtp.yopmail.com` | 569 | 578 |
| `emailfake.com` | 537 | 553 |
| `tinyhost.shop` | 373 | 373 |
| `mx.emlhub.com` | 371 | 371 |
| `mx.spymail.one` | 315 | 315 |
| `email.gravityengine.cc` | 311 | 311 |
| `mx.emltmp.com` | 297 | 297 |
| `mx.emlpro.com` | 277 | 277 |
| `smtp.215.im` | 269 | 273 |
| `mx156.hostedmxserver.com` | 262 | 445 |
| `mx.freeml.net` | 258 | 258 |
| `mx.dropmail.me` | 257 | 257 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `91.196.52.205` | 7845 | 8117 |
| `78.47.124.133` | 2258 | 2258 |
| `94.130.108.80` | 2258 | 2258 |
| `116.202.9.167` | 1302 | 1302 |
| `46.101.111.206` | 1302 | 1302 |
| `162.159.205.17` | 1289 | 1511 |
| `162.159.205.18` | 1289 | 1511 |
| `162.159.205.19` | 1289 | 1511 |
| `162.159.205.23` | 1288 | 1510 |
| `162.159.205.24` | 1288 | 1510 |
| `162.159.205.25` | 1288 | 1510 |
| `142.132.166.12` | 1283 | 1283 |
| `188.166.111.252` | 1283 | 1283 |
| `162.159.205.11` | 1281 | 1502 |
| `162.159.205.12` | 1281 | 1502 |
| `162.159.205.13` | 1281 | 1502 |
| `158.101.127.66` | 1023 | 1023 |
| `188.245.74.208` | 943 | 943 |
| `195.201.18.63` | 929 | 929 |
| `13.223.25.84` | 896 | 902 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 388 |
| High-confidence disposable IPs | 940 |
| Promoted to `domains_inferred.txt` | 4 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**5009 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

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
| `007jlkw.com` | `route1.mx.cloudflare.net` |
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


*… and 4,979 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
