# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-11-15 02:16 UTC**.*  
*Last DNS snapshot: **2026-11-15T02:09:58+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 108,451 |
| `domains_strict.txt` | 109,514 |
| `domains_inferred.txt` (opt-in) | 4 |

## Reachability

Of **113,893** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 55,858 | 49.0% |
| A_ONLY | 5,381 | 4.7% |
| NXDOMAIN | 38,223 | 33.6% |
| NO_RECORDS | 1,181 | 1.0% |
| TIMEOUT | 13,250 | 11.6% |

**61,239 domains are mail-reachable today** (53.8%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `generator.email` | 10552 | 10809 |  |
| `route2.mx.cloudflare.net` | 2728 | 2944 | yes |
| `route1.mx.cloudflare.net` | 2727 | 2943 | yes |
| `route3.mx.cloudflare.net` | 2727 | 2943 | yes |
| `mail.wabblywabble.com` | 1861 | 1861 |  |
| `mail.wallywatts.com` | 1861 | 1861 |  |
| `aero4.unstablemail.com` | 1295 | 1297 |  |
| `srv4.unstablemail.com` | 1293 | 1295 |  |
| `park-mx.above.com` | 1216 | 1341 | yes |
| `mx4.beavis99.com` | 1153 | 1153 |  |
| `mx4.beavis99.net` | 1152 | 1152 |  |
| `smtp.yopmail.com` | 1076 | 1085 |  |
| `aspmx.l.google.com` | 932 | 1019 | yes |
| `alt1.aspmx.l.google.com` | 914 | 999 | yes |
| `alt2.aspmx.l.google.com` | 911 | 994 | yes |
| `eforward1.registrar-servers.com` | 881 | 926 | yes |
| `eforward2.registrar-servers.com` | 881 | 926 | yes |
| `eforward3.registrar-servers.com` | 881 | 926 | yes |
| `eforward4.registrar-servers.com` | 881 | 926 | yes |
| `eforward5.registrar-servers.com` | 881 | 926 | yes |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `generator.email` | 10552 | 10809 |
| `mail.wabblywabble.com` | 1861 | 1861 |
| `mail.wallywatts.com` | 1861 | 1861 |
| `aero4.unstablemail.com` | 1295 | 1297 |
| `srv4.unstablemail.com` | 1293 | 1295 |
| `mx4.beavis99.com` | 1153 | 1153 |
| `mx4.beavis99.net` | 1152 | 1152 |
| `smtp.yopmail.com` | 1076 | 1085 |
| `email.chatgpt.org.uk` | 837 | 850 |
| `emailfake.com` | 789 | 805 |
| `tinyhost.shop` | 514 | 514 |
| `mx.emlhub.com` | 444 | 444 |
| `smtp.215.im` | 413 | 417 |
| `mx1.timeweb.ru` | 360 | 393 |
| `mx2.timeweb.ru` | 360 | 393 |
| `mx.spymail.one` | 345 | 345 |
| `mail.h-email.net` | 343 | 412 |
| `mx.10mail.org` | 343 | 343 |
| `mx2-hosting.jellyfish.systems` | 339 | 353 |
| `mx3-hosting.jellyfish.systems` | 339 | 353 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `91.196.52.205` | 11540 | 11806 |
| `78.47.124.133` | 2917 | 2917 |
| `94.130.108.80` | 2917 | 2917 |
| `162.159.205.17` | 2730 | 2942 |
| `162.159.205.18` | 2730 | 2942 |
| `162.159.205.19` | 2730 | 2942 |
| `162.159.205.23` | 2725 | 2937 |
| `162.159.205.24` | 2725 | 2937 |
| `162.159.205.25` | 2725 | 2937 |
| `162.159.205.11` | 2718 | 2930 |
| `162.159.205.12` | 2718 | 2930 |
| `162.159.205.13` | 2718 | 2930 |
| `116.202.9.167` | 1808 | 1808 |
| `46.101.111.206` | 1808 | 1808 |
| `142.132.166.12` | 1800 | 1800 |
| `188.166.111.252` | 1800 | 1800 |
| `201.3.122.6` | 1689 | 1699 |
| `146.190.212.90` | 1271 | 1273 |
| `146.190.223.124` | 1259 | 1261 |
| `103.224.212.34` | 1196 | 1319 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 456 |
| High-confidence disposable IPs | 1,156 |
| Promoted to `domains_inferred.txt` | 4 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**8608 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

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


*… and 8,578 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
