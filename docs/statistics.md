# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-10-23 02:21 UTC**.*  
*Last DNS snapshot: **2026-10-23T02:16:31+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 98,465 |
| `domains_strict.txt` | 99,697 |
| `domains_inferred.txt` (opt-in) | 4 |

## Reachability

Of **102,232** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 46,341 | 45.3% |
| A_ONLY | 6,042 | 5.9% |
| NXDOMAIN | 42,835 | 41.9% |
| NO_RECORDS | 1,088 | 1.1% |
| TIMEOUT | 5,926 | 5.8% |

**52,383 domains are mail-reachable today** (51.2%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `route2.mx.cloudflare.net` | 2700 | 2840 | yes |
| `route1.mx.cloudflare.net` | 2699 | 2839 | yes |
| `route3.mx.cloudflare.net` | 2699 | 2839 | yes |
| `mail.wabblywabble.com` | 2009 | 2010 |  |
| `mail.wallywatts.com` | 2009 | 2010 |  |
| `generator.email` | 1356 | 1569 |  |
| `aero4.unstablemail.com` | 1307 | 1308 |  |
| `srv4.unstablemail.com` | 1305 | 1306 |  |
| `mx4.beavis99.com` | 1251 | 1251 |  |
| `mx4.beavis99.net` | 1250 | 1250 |  |
| `smtp.yopmail.com` | 1095 | 1103 |  |
| `park-mx.above.com` | 1005 | 1080 | yes |
| `aspmx.l.google.com` | 963 | 1047 | yes |
| `alt1.aspmx.l.google.com` | 947 | 1029 | yes |
| `alt2.aspmx.l.google.com` | 942 | 1022 | yes |
| `eforward1.registrar-servers.com` | 914 | 942 | yes |
| `eforward2.registrar-servers.com` | 914 | 942 | yes |
| `eforward3.registrar-servers.com` | 914 | 942 | yes |
| `eforward4.registrar-servers.com` | 914 | 942 | yes |
| `eforward5.registrar-servers.com` | 914 | 942 | yes |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 2009 | 2010 |
| `mail.wallywatts.com` | 2009 | 2010 |
| `generator.email` | 1356 | 1569 |
| `aero4.unstablemail.com` | 1307 | 1308 |
| `srv4.unstablemail.com` | 1305 | 1306 |
| `mx4.beavis99.com` | 1251 | 1251 |
| `mx4.beavis99.net` | 1250 | 1250 |
| `smtp.yopmail.com` | 1095 | 1103 |
| `email.chatgpt.org.uk` | 729 | 729 |
| `emailfake.com` | 712 | 726 |
| `mx.emlhub.com` | 484 | 484 |
| `tinyhost.shop` | 454 | 454 |
| `mail.cleantempmail.com` | 416 | 417 |
| `mx.spymail.one` | 389 | 389 |
| `mail.h-email.net` | 379 | 437 |
| `mx.emltmp.com` | 370 | 370 |
| `email.gravityengine.cc` | 365 | 378 |
| `mx156.hostedmxserver.com` | 365 | 460 |
| `mx.emlpro.com` | 356 | 356 |
| `mx2.timeweb.ru` | 348 | 378 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `78.47.124.133` | 2927 | 2927 |
| `94.130.108.80` | 2927 | 2927 |
| `162.159.205.23` | 2690 | 2827 |
| `162.159.205.24` | 2690 | 2827 |
| `162.159.205.25` | 2690 | 2827 |
| `162.159.205.17` | 2686 | 2822 |
| `162.159.205.18` | 2686 | 2822 |
| `162.159.205.19` | 2686 | 2822 |
| `162.159.205.11` | 2667 | 2804 |
| `162.159.205.12` | 2667 | 2804 |
| `162.159.205.13` | 2667 | 2804 |
| `91.196.52.205` | 2307 | 2530 |
| `116.202.9.167` | 1977 | 1978 |
| `46.101.111.206` | 1977 | 1978 |
| `142.132.166.12` | 1958 | 1959 |
| `188.166.111.252` | 1958 | 1959 |
| `138.226.240.26` | 1477 | 1491 |
| `146.190.212.90` | 1276 | 1277 |
| `146.190.223.124` | 1250 | 1251 |
| `195.123.189.142` | 1234 | 1257 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 459 |
| High-confidence disposable IPs | 1,158 |
| Promoted to `domains_inferred.txt` | 4 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**8457 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

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


*… and 8,427 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
