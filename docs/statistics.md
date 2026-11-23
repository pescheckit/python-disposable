# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-11-23 02:30 UTC**.*  
*Last DNS snapshot: **2026-11-23T02:10:32+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 109,114 |
| `domains_strict.txt` | 110,177 |
| `domains_inferred.txt` (opt-in) | 4 |

## Reachability

Of **114,898** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 39,712 | 34.6% |
| A_ONLY | 4,901 | 4.3% |
| NXDOMAIN | 35,745 | 31.1% |
| NO_RECORDS | 919 | 0.8% |
| TIMEOUT | 33,621 | 29.3% |

**44,613 domains are mail-reachable today** (38.8%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `generator.email` | 8210 | 8475 |  |
| `route2.mx.cloudflare.net` | 1537 | 1768 | yes |
| `route1.mx.cloudflare.net` | 1536 | 1767 | yes |
| `route3.mx.cloudflare.net` | 1536 | 1767 | yes |
| `mail.wabblywabble.com` | 1425 | 1425 |  |
| `mail.wallywatts.com` | 1425 | 1425 |  |
| `mx4.beavis99.com` | 1003 | 1003 |  |
| `mx4.beavis99.net` | 1002 | 1002 |  |
| `park-mx.above.com` | 902 | 1048 | yes |
| `email.chatgpt.org.uk` | 783 | 796 |  |
| `emailfake.com` | 717 | 732 |  |
| `aero4.unstablemail.com` | 643 | 643 |  |
| `srv4.unstablemail.com` | 641 | 641 |  |
| `aspmx.l.google.com` | 574 | 661 | yes |
| `smtp.yopmail.com` | 569 | 578 |  |
| `alt1.aspmx.l.google.com` | 565 | 650 | yes |
| `alt2.aspmx.l.google.com` | 559 | 642 | yes |
| `eforward1.registrar-servers.com` | 470 | 522 | yes |
| `eforward2.registrar-servers.com` | 470 | 522 | yes |
| `eforward3.registrar-servers.com` | 470 | 522 | yes |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `generator.email` | 8210 | 8475 |
| `mail.wabblywabble.com` | 1425 | 1425 |
| `mail.wallywatts.com` | 1425 | 1425 |
| `mx4.beavis99.com` | 1003 | 1003 |
| `mx4.beavis99.net` | 1002 | 1002 |
| `email.chatgpt.org.uk` | 783 | 796 |
| `emailfake.com` | 717 | 732 |
| `aero4.unstablemail.com` | 643 | 643 |
| `srv4.unstablemail.com` | 641 | 641 |
| `smtp.yopmail.com` | 569 | 578 |
| `tinyhost.shop` | 375 | 375 |
| `mx.emlhub.com` | 371 | 371 |
| `mx.spymail.one` | 315 | 315 |
| `email.gravityengine.cc` | 311 | 311 |
| `mx.emltmp.com` | 297 | 297 |
| `mx.emlpro.com` | 277 | 277 |
| `smtp.215.im` | 269 | 273 |
| `mx156.hostedmxserver.com` | 266 | 447 |
| `mx.freeml.net` | 258 | 258 |
| `mx.dropmail.me` | 257 | 257 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `91.196.52.205` | 8035 | 8308 |
| `78.47.124.133` | 2258 | 2258 |
| `94.130.108.80` | 2258 | 2258 |
| `162.159.205.17` | 1305 | 1528 |
| `162.159.205.18` | 1305 | 1528 |
| `162.159.205.19` | 1305 | 1528 |
| `162.159.205.23` | 1303 | 1526 |
| `162.159.205.24` | 1303 | 1526 |
| `162.159.205.25` | 1303 | 1526 |
| `116.202.9.167` | 1302 | 1302 |
| `46.101.111.206` | 1302 | 1302 |
| `162.159.205.11` | 1296 | 1519 |
| `162.159.205.12` | 1296 | 1519 |
| `162.159.205.13` | 1296 | 1519 |
| `142.132.166.12` | 1283 | 1283 |
| `188.166.111.252` | 1283 | 1283 |
| `158.101.127.66` | 1023 | 1023 |
| `188.245.74.208` | 943 | 943 |
| `195.201.18.63` | 929 | 929 |
| `13.223.25.84` | 896 | 902 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 388 |
| High-confidence disposable IPs | 946 |
| Promoted to `domains_inferred.txt` | 4 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**5041 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

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


*… and 5,011 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
