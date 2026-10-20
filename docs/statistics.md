# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-10-20 02:43 UTC**.*  
*Last DNS snapshot: **2026-10-20T02:23:58+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 97,672 |
| `domains_strict.txt` | 98,904 |
| `domains_inferred.txt` (opt-in) | 4 |

## Reachability

Of **101,272** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 45,061 | 44.5% |
| A_ONLY | 5,898 | 5.8% |
| NXDOMAIN | 42,776 | 42.2% |
| NO_RECORDS | 1,022 | 1.0% |
| TIMEOUT | 6,515 | 6.4% |

**50,959 domains are mail-reachable today** (50.3%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `route2.mx.cloudflare.net` | 2693 | 2814 | yes |
| `route1.mx.cloudflare.net` | 2692 | 2813 | yes |
| `route3.mx.cloudflare.net` | 2692 | 2813 | yes |
| `mail.wabblywabble.com` | 2005 | 2005 |  |
| `mail.wallywatts.com` | 2005 | 2005 |  |
| `generator.email` | 1354 | 1561 |  |
| `aero4.unstablemail.com` | 1300 | 1302 |  |
| `srv4.unstablemail.com` | 1299 | 1301 |  |
| `mx4.beavis99.com` | 1253 | 1253 |  |
| `mx4.beavis99.net` | 1252 | 1252 |  |
| `park-mx.above.com` | 984 | 1054 | yes |
| `aspmx.l.google.com` | 963 | 1046 | yes |
| `alt1.aspmx.l.google.com` | 947 | 1028 | yes |
| `alt2.aspmx.l.google.com` | 942 | 1021 | yes |
| `eforward1.registrar-servers.com` | 909 | 937 | yes |
| `eforward2.registrar-servers.com` | 909 | 937 | yes |
| `eforward3.registrar-servers.com` | 909 | 937 | yes |
| `eforward4.registrar-servers.com` | 909 | 937 | yes |
| `eforward5.registrar-servers.com` | 909 | 937 | yes |
| `smtp.google.com` | 798 | 820 | yes |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 2005 | 2005 |
| `mail.wallywatts.com` | 2005 | 2005 |
| `generator.email` | 1354 | 1561 |
| `aero4.unstablemail.com` | 1300 | 1302 |
| `srv4.unstablemail.com` | 1299 | 1301 |
| `mx4.beavis99.com` | 1253 | 1253 |
| `mx4.beavis99.net` | 1252 | 1252 |
| `email.chatgpt.org.uk` | 765 | 765 |
| `emailfake.com` | 695 | 707 |
| `mx.emlhub.com` | 482 | 482 |
| `smtp.yopmail.com` | 422 | 432 |
| `mail.cleantempmail.com` | 413 | 413 |
| `mx.spymail.one` | 386 | 386 |
| `tinyhost.shop` | 382 | 382 |
| `email.gravityengine.cc` | 365 | 378 |
| `mail.h-email.net` | 364 | 435 |
| `mx.emltmp.com` | 363 | 363 |
| `mx156.hostedmxserver.com` | 363 | 443 |
| `mx.emlpro.com` | 355 | 355 |
| `mx2-hosting.jellyfish.systems` | 348 | 354 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `78.47.124.133` | 2762 | 2762 |
| `94.130.108.80` | 2762 | 2762 |
| `162.159.205.23` | 2674 | 2793 |
| `162.159.205.24` | 2674 | 2793 |
| `162.159.205.25` | 2674 | 2793 |
| `162.159.205.17` | 2668 | 2787 |
| `162.159.205.18` | 2668 | 2787 |
| `162.159.205.19` | 2668 | 2787 |
| `162.159.205.11` | 2657 | 2775 |
| `162.159.205.12` | 2657 | 2775 |
| `162.159.205.13` | 2657 | 2775 |
| `91.196.52.205` | 2258 | 2473 |
| `116.202.9.167` | 1972 | 1972 |
| `46.101.111.206` | 1972 | 1972 |
| `142.132.166.12` | 1953 | 1953 |
| `188.166.111.252` | 1953 | 1953 |
| `138.226.240.26` | 1472 | 1485 |
| `146.190.212.90` | 1266 | 1268 |
| `195.123.189.142` | 1251 | 1257 |
| `146.190.223.124` | 1240 | 1242 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 455 |
| High-confidence disposable IPs | 1,162 |
| Promoted to `domains_inferred.txt` | 4 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**8431 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

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


*… and 8,401 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
