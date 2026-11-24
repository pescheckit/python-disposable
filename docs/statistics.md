# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-11-24 02:19 UTC**.*  
*Last DNS snapshot: **2026-11-24T02:19:25+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 109,208 |
| `domains_strict.txt` | 110,271 |
| `domains_inferred.txt` (opt-in) | 4 |

## Reachability

Of **114,962** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 40,770 | 35.5% |
| A_ONLY | 4,920 | 4.3% |
| NXDOMAIN | 35,830 | 31.2% |
| NO_RECORDS | 992 | 0.9% |
| TIMEOUT | 32,450 | 28.2% |

**45,690 domains are mail-reachable today** (39.7%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `generator.email` | 8420 | 8688 |  |
| `route2.mx.cloudflare.net` | 1554 | 1789 | yes |
| `route1.mx.cloudflare.net` | 1553 | 1788 | yes |
| `route3.mx.cloudflare.net` | 1553 | 1788 | yes |
| `mail.wabblywabble.com` | 1428 | 1428 |  |
| `mail.wallywatts.com` | 1428 | 1428 |  |
| `mx4.beavis99.com` | 1003 | 1003 |  |
| `mx4.beavis99.net` | 1002 | 1002 |  |
| `park-mx.above.com` | 936 | 1083 | yes |
| `email.chatgpt.org.uk` | 806 | 819 |  |
| `smtp.yopmail.com` | 754 | 763 |  |
| `emailfake.com` | 752 | 767 |  |
| `aero4.unstablemail.com` | 656 | 656 |  |
| `srv4.unstablemail.com` | 654 | 654 |  |
| `aspmx.l.google.com` | 579 | 665 | yes |
| `alt1.aspmx.l.google.com` | 569 | 653 | yes |
| `alt2.aspmx.l.google.com` | 563 | 645 | yes |
| `eforward1.registrar-servers.com` | 472 | 524 | yes |
| `eforward2.registrar-servers.com` | 472 | 524 | yes |
| `eforward3.registrar-servers.com` | 472 | 524 | yes |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `generator.email` | 8420 | 8688 |
| `mail.wabblywabble.com` | 1428 | 1428 |
| `mail.wallywatts.com` | 1428 | 1428 |
| `mx4.beavis99.com` | 1003 | 1003 |
| `mx4.beavis99.net` | 1002 | 1002 |
| `email.chatgpt.org.uk` | 806 | 819 |
| `smtp.yopmail.com` | 754 | 763 |
| `emailfake.com` | 752 | 767 |
| `aero4.unstablemail.com` | 656 | 656 |
| `srv4.unstablemail.com` | 654 | 654 |
| `tinyhost.shop` | 456 | 456 |
| `mx.emlhub.com` | 372 | 372 |
| `smtp.215.im` | 328 | 333 |
| `mx.spymail.one` | 315 | 315 |
| `email.gravityengine.cc` | 314 | 314 |
| `mx.10mail.org` | 298 | 298 |
| `mx.emltmp.com` | 297 | 297 |
| `mx.emlpro.com` | 277 | 277 |
| `mx156.hostedmxserver.com` | 269 | 450 |
| `mx.freeml.net` | 258 | 258 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `91.196.52.205` | 8350 | 8623 |
| `78.47.124.133` | 2466 | 2466 |
| `94.130.108.80` | 2466 | 2466 |
| `162.159.205.17` | 1326 | 1553 |
| `162.159.205.18` | 1326 | 1553 |
| `162.159.205.19` | 1326 | 1553 |
| `162.159.205.23` | 1326 | 1553 |
| `162.159.205.24` | 1326 | 1553 |
| `162.159.205.25` | 1326 | 1553 |
| `162.159.205.11` | 1320 | 1546 |
| `162.159.205.12` | 1320 | 1546 |
| `162.159.205.13` | 1320 | 1546 |
| `116.202.9.167` | 1306 | 1306 |
| `46.101.111.206` | 1306 | 1306 |
| `142.132.166.12` | 1287 | 1287 |
| `188.166.111.252` | 1287 | 1287 |
| `158.101.127.66` | 1071 | 1071 |
| `188.245.74.208` | 943 | 943 |
| `195.201.18.63` | 929 | 929 |
| `13.223.25.84` | 897 | 903 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 392 |
| High-confidence disposable IPs | 949 |
| Promoted to `domains_inferred.txt` | 4 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**5112 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

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
| `01g.cloud` | `alt1.aspmx.l.google.com` |
| `01p.co.jp` | `01p-co-jp.mail.protection.outlook.com` |
| `020307.xyz` | `route1.mx.cloudflare.net` |
| `02bet.info` | `park-mx.above.com` |
| `041998.xyz` | `mx1.alias.proton.me` |
| `0500betvip.com` | `route1.mx.cloudflare.net` |
| `057gmail.com` | `route1.mx.cloudflare.net` |
| `0ak.org` | `mx00.ionos.com` |


*… and 5,082 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
