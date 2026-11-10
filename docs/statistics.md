# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-11-10 03:15 UTC**.*  
*Last DNS snapshot: **2026-11-10T03:15:13+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 98,976 |
| `domains_strict.txt` | 100,208 |
| `domains_inferred.txt` (opt-in) | 4 |

## Reachability

Of **104,186** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 36,206 | 34.8% |
| A_ONLY | 2,454 | 2.4% |
| NXDOMAIN | 19,964 | 19.2% |
| NO_RECORDS | 687 | 0.7% |
| TIMEOUT | 44,875 | 43.1% |

**38,660 domains are mail-reachable today** (37.1%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `route2.mx.cloudflare.net` | 2192 | 2403 | yes |
| `route1.mx.cloudflare.net` | 2191 | 2402 | yes |
| `route3.mx.cloudflare.net` | 2191 | 2402 | yes |
| `mail.wabblywabble.com` | 1308 | 1308 |  |
| `mail.wallywatts.com` | 1308 | 1308 |  |
| `generator.email` | 1306 | 1555 |  |
| `aero4.unstablemail.com` | 1086 | 1088 |  |
| `srv4.unstablemail.com` | 1085 | 1087 |  |
| `smtp.yopmail.com` | 1000 | 1009 |  |
| `park-mx.above.com` | 899 | 1018 | yes |
| `smtp.google.com` | 797 | 825 | yes |
| `aspmx.l.google.com` | 746 | 831 | yes |
| `alt1.aspmx.l.google.com` | 737 | 820 | yes |
| `alt2.aspmx.l.google.com` | 735 | 816 | yes |
| `eforward1.registrar-servers.com` | 714 | 754 | yes |
| `eforward2.registrar-servers.com` | 714 | 754 | yes |
| `eforward3.registrar-servers.com` | 714 | 754 | yes |
| `eforward4.registrar-servers.com` | 714 | 754 | yes |
| `eforward5.registrar-servers.com` | 714 | 754 | yes |
| `email.chatgpt.org.uk` | 702 | 714 |  |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 1308 | 1308 |
| `mail.wallywatts.com` | 1308 | 1308 |
| `generator.email` | 1306 | 1555 |
| `aero4.unstablemail.com` | 1086 | 1088 |
| `srv4.unstablemail.com` | 1085 | 1087 |
| `smtp.yopmail.com` | 1000 | 1009 |
| `email.chatgpt.org.uk` | 702 | 714 |
| `mx4.beavis99.com` | 596 | 596 |
| `mx4.beavis99.net` | 595 | 595 |
| `emailfake.com` | 574 | 590 |
| `smtp.215.im` | 402 | 406 |
| `mx.10mail.org` | 344 | 344 |
| `mx1.timeweb.ru` | 339 | 371 |
| `mx2.timeweb.ru` | 339 | 371 |
| `tinyhost.shop` | 324 | 324 |
| `mx2-hosting.jellyfish.systems` | 315 | 327 |
| `mx3-hosting.jellyfish.systems` | 315 | 327 |
| `mx1-hosting.jellyfish.systems` | 314 | 326 |
| `void.blackhole.mx` | 304 | 306 |
| `mx1.titan.email` | 275 | 277 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `162.159.205.17` | 2096 | 2303 |
| `162.159.205.18` | 2096 | 2303 |
| `162.159.205.19` | 2096 | 2303 |
| `162.159.205.23` | 2091 | 2298 |
| `162.159.205.24` | 2091 | 2298 |
| `162.159.205.25` | 2091 | 2298 |
| `162.159.205.11` | 2079 | 2286 |
| `162.159.205.12` | 2079 | 2286 |
| `162.159.205.13` | 2079 | 2286 |
| `91.196.52.205` | 2041 | 2299 |
| `201.3.122.6` | 1625 | 1625 |
| `78.47.124.133` | 1520 | 1520 |
| `94.130.108.80` | 1520 | 1520 |
| `116.202.9.167` | 1184 | 1184 |
| `46.101.111.206` | 1184 | 1184 |
| `142.132.166.12` | 1168 | 1168 |
| `188.166.111.252` | 1168 | 1168 |
| `87.98.164.155` | 1046 | 1055 |
| `146.190.212.90` | 1041 | 1043 |
| `146.190.223.124` | 1034 | 1036 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 377 |
| High-confidence disposable IPs | 926 |
| Promoted to `domains_inferred.txt` | 4 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**6895 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

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
| `0ak.org` | `mx00.ionos.com` |


*… and 6,865 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
