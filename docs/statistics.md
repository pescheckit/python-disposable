# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-11-13 02:21 UTC**.*  
*Last DNS snapshot: **2026-11-13T02:12:36+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 108,358 |
| `domains_strict.txt` | 109,421 |
| `domains_inferred.txt` (opt-in) | 4 |

## Reachability

Of **113,703** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 52,048 | 45.8% |
| A_ONLY | 4,332 | 3.8% |
| NXDOMAIN | 31,733 | 27.9% |
| NO_RECORDS | 1,017 | 0.9% |
| TIMEOUT | 24,573 | 21.6% |

**56,380 domains are mail-reachable today** (49.6%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `generator.email` | 10441 | 10691 |  |
| `route2.mx.cloudflare.net` | 2545 | 2758 | yes |
| `route1.mx.cloudflare.net` | 2544 | 2757 | yes |
| `route3.mx.cloudflare.net` | 2544 | 2757 | yes |
| `mail.wabblywabble.com` | 1721 | 1721 |  |
| `mail.wallywatts.com` | 1721 | 1721 |  |
| `aero4.unstablemail.com` | 1224 | 1225 |  |
| `srv4.unstablemail.com` | 1222 | 1223 |  |
| `park-mx.above.com` | 1072 | 1196 | yes |
| `smtp.yopmail.com` | 1034 | 1043 |  |
| `mx4.beavis99.com` | 932 | 932 |  |
| `mx4.beavis99.net` | 931 | 931 |  |
| `aspmx.l.google.com` | 864 | 950 | yes |
| `alt1.aspmx.l.google.com` | 849 | 933 | yes |
| `alt2.aspmx.l.google.com` | 846 | 928 | yes |
| `smtp.google.com` | 830 | 877 | yes |
| `eforward1.registrar-servers.com` | 826 | 867 | yes |
| `eforward2.registrar-servers.com` | 826 | 867 | yes |
| `eforward3.registrar-servers.com` | 826 | 867 | yes |
| `eforward4.registrar-servers.com` | 826 | 867 | yes |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `generator.email` | 10441 | 10691 |
| `mail.wabblywabble.com` | 1721 | 1721 |
| `mail.wallywatts.com` | 1721 | 1721 |
| `aero4.unstablemail.com` | 1224 | 1225 |
| `srv4.unstablemail.com` | 1222 | 1223 |
| `smtp.yopmail.com` | 1034 | 1043 |
| `mx4.beavis99.com` | 932 | 932 |
| `mx4.beavis99.net` | 931 | 931 |
| `email.chatgpt.org.uk` | 798 | 811 |
| `emailfake.com` | 731 | 747 |
| `tinyhost.shop` | 446 | 446 |
| `smtp.215.im` | 414 | 418 |
| `mx.emlhub.com` | 381 | 381 |
| `mx1.timeweb.ru` | 356 | 388 |
| `mx2.timeweb.ru` | 356 | 388 |
| `mx.10mail.org` | 344 | 344 |
| `mx2-hosting.jellyfish.systems` | 334 | 347 |
| `mx3-hosting.jellyfish.systems` | 334 | 347 |
| `mx1-hosting.jellyfish.systems` | 333 | 346 |
| `mail.h-email.net` | 316 | 379 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `91.196.52.205` | 11330 | 11590 |
| `162.159.205.17` | 2511 | 2720 |
| `162.159.205.18` | 2511 | 2720 |
| `162.159.205.19` | 2511 | 2720 |
| `162.159.205.23` | 2506 | 2715 |
| `162.159.205.24` | 2506 | 2715 |
| `162.159.205.25` | 2506 | 2715 |
| `162.159.205.11` | 2500 | 2709 |
| `162.159.205.12` | 2500 | 2709 |
| `162.159.205.13` | 2500 | 2709 |
| `78.47.124.133` | 2340 | 2340 |
| `94.130.108.80` | 2340 | 2340 |
| `201.3.122.6` | 1674 | 1679 |
| `116.202.9.167` | 1653 | 1653 |
| `46.101.111.206` | 1653 | 1653 |
| `142.132.166.12` | 1650 | 1650 |
| `188.166.111.252` | 1650 | 1650 |
| `146.190.212.90` | 1185 | 1186 |
| `146.190.223.124` | 1180 | 1180 |
| `158.101.127.66` | 1124 | 1124 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 429 |
| High-confidence disposable IPs | 1,091 |
| Promoted to `domains_inferred.txt` | 4 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**7968 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

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


*… and 7,938 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
