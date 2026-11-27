# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-11-27 02:19 UTC**.*  
*Last DNS snapshot: **2026-11-27T02:09:57+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 109,018 |
| `domains_strict.txt` | 110,081 |
| `domains_inferred.txt` (opt-in) | 4 |

## Reachability

Of **115,302** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 55,103 | 47.8% |
| A_ONLY | 5,023 | 4.4% |
| NXDOMAIN | 36,616 | 31.8% |
| NO_RECORDS | 1,088 | 0.9% |
| TIMEOUT | 17,472 | 15.2% |

**60,126 domains are mail-reachable today** (52.1%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `generator.email` | 10273 | 10836 |  |
| `route2.mx.cloudflare.net` | 2697 | 2933 | yes |
| `route1.mx.cloudflare.net` | 2696 | 2932 | yes |
| `route3.mx.cloudflare.net` | 2695 | 2931 | yes |
| `mail.wabblywabble.com` | 1913 | 1913 |  |
| `mail.wallywatts.com` | 1913 | 1913 |  |
| `park-mx.above.com` | 1285 | 1442 | yes |
| `aero4.unstablemail.com` | 1271 | 1272 |  |
| `srv4.unstablemail.com` | 1269 | 1270 |  |
| `mx4.beavis99.com` | 1079 | 1079 |  |
| `mx4.beavis99.net` | 1078 | 1078 |  |
| `aspmx.l.google.com` | 933 | 1019 | yes |
| `emailfake.com` | 931 | 948 |  |
| `alt1.aspmx.l.google.com` | 917 | 1001 | yes |
| `alt2.aspmx.l.google.com` | 911 | 993 | yes |
| `smtp.yopmail.com` | 867 | 880 |  |
| `email.chatgpt.org.uk` | 861 | 874 |  |
| `eforward1.registrar-servers.com` | 843 | 896 | yes |
| `eforward2.registrar-servers.com` | 843 | 896 | yes |
| `eforward3.registrar-servers.com` | 843 | 896 | yes |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `generator.email` | 10273 | 10836 |
| `mail.wabblywabble.com` | 1913 | 1913 |
| `mail.wallywatts.com` | 1913 | 1913 |
| `aero4.unstablemail.com` | 1271 | 1272 |
| `srv4.unstablemail.com` | 1269 | 1270 |
| `mx4.beavis99.com` | 1079 | 1079 |
| `mx4.beavis99.net` | 1078 | 1078 |
| `emailfake.com` | 931 | 948 |
| `smtp.yopmail.com` | 867 | 880 |
| `email.chatgpt.org.uk` | 861 | 874 |
| `tinyhost.shop` | 478 | 478 |
| `mx.emlhub.com` | 375 | 375 |
| `smtp.215.im` | 363 | 367 |
| `mx1.timeweb.ru` | 355 | 386 |
| `mx2.timeweb.ru` | 355 | 386 |
| `mx156.hostedmxserver.com` | 346 | 527 |
| `mx2-hosting.jellyfish.systems` | 345 | 361 |
| `mx3-hosting.jellyfish.systems` | 345 | 361 |
| `mx1-hosting.jellyfish.systems` | 344 | 360 |
| `void.blackhole.mx` | 332 | 334 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `91.196.52.205` | 11356 | 11908 |
| `162.159.205.23` | 2679 | 2906 |
| `162.159.205.24` | 2679 | 2906 |
| `162.159.205.25` | 2679 | 2906 |
| `162.159.205.11` | 2676 | 2902 |
| `162.159.205.12` | 2676 | 2902 |
| `162.159.205.13` | 2676 | 2902 |
| `162.159.205.17` | 2675 | 2902 |
| `162.159.205.18` | 2675 | 2902 |
| `162.159.205.19` | 2675 | 2902 |
| `78.47.124.133` | 2458 | 2458 |
| `94.130.108.80` | 2458 | 2458 |
| `116.202.9.167` | 1870 | 1870 |
| `46.101.111.206` | 1870 | 1870 |
| `142.132.166.12` | 1862 | 1862 |
| `188.166.111.252` | 1862 | 1862 |
| `201.3.122.6` | 1683 | 1690 |
| `103.224.212.34` | 1245 | 1397 |
| `146.190.223.124` | 1237 | 1238 |
| `146.190.212.90` | 1233 | 1234 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 456 |
| High-confidence disposable IPs | 1,165 |
| Promoted to `domains_inferred.txt` | 4 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**8523 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

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
| `0hcow.com` | `mxa.mailgun.org` |
| `0hio.net` | `aspmx1.migadu.com` |


*… and 8,493 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
