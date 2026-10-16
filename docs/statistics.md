# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-10-16 02:26 UTC**.*  
*Last DNS snapshot: **2026-10-16T02:17:59+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 97,503 |
| `domains_strict.txt` | 98,735 |
| `domains_inferred.txt` (opt-in) | 2 |

## Reachability

Of **100,900** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 44,790 | 44.4% |
| A_ONLY | 5,709 | 5.7% |
| NXDOMAIN | 42,358 | 42.0% |
| NO_RECORDS | 976 | 1.0% |
| TIMEOUT | 7,067 | 7.0% |

**50,499 domains are mail-reachable today** (50.0%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `route2.mx.cloudflare.net` | 2680 | 2778 | yes |
| `route1.mx.cloudflare.net` | 2679 | 2777 | yes |
| `route3.mx.cloudflare.net` | 2678 | 2776 | yes |
| `mail.wabblywabble.com` | 1971 | 1974 |  |
| `mail.wallywatts.com` | 1971 | 1974 |  |
| `generator.email` | 1365 | 1567 |  |
| `aero4.unstablemail.com` | 1302 | 1303 |  |
| `srv4.unstablemail.com` | 1301 | 1302 |  |
| `mx4.beavis99.com` | 1234 | 1234 |  |
| `mx4.beavis99.net` | 1233 | 1233 |  |
| `aspmx.l.google.com` | 1006 | 1089 | yes |
| `alt1.aspmx.l.google.com` | 988 | 1069 | yes |
| `alt2.aspmx.l.google.com` | 984 | 1063 | yes |
| `park-mx.above.com` | 943 | 1001 | yes |
| `eforward1.registrar-servers.com` | 903 | 928 | yes |
| `eforward2.registrar-servers.com` | 903 | 928 | yes |
| `eforward3.registrar-servers.com` | 903 | 928 | yes |
| `eforward4.registrar-servers.com` | 903 | 928 | yes |
| `eforward5.registrar-servers.com` | 903 | 928 | yes |
| `smtp.google.com` | 797 | 819 | yes |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 1971 | 1974 |
| `mail.wallywatts.com` | 1971 | 1974 |
| `generator.email` | 1365 | 1567 |
| `aero4.unstablemail.com` | 1302 | 1303 |
| `srv4.unstablemail.com` | 1301 | 1302 |
| `mx4.beavis99.com` | 1234 | 1234 |
| `mx4.beavis99.net` | 1233 | 1233 |
| `email.chatgpt.org.uk` | 745 | 745 |
| `emailfake.com` | 691 | 703 |
| `mx.emlhub.com` | 482 | 482 |
| `smtp.yopmail.com` | 439 | 448 |
| `mail.cleantempmail.com` | 415 | 415 |
| `email.gravityengine.cc` | 390 | 402 |
| `mx.spymail.one` | 378 | 378 |
| `mail.h-email.net` | 360 | 424 |
| `mx.emltmp.com` | 355 | 355 |
| `mx.emlpro.com` | 353 | 353 |
| `mx156.hostedmxserver.com` | 349 | 412 |
| `mx2-hosting.jellyfish.systems` | 344 | 350 |
| `mx3-hosting.jellyfish.systems` | 344 | 350 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `78.47.124.133` | 2712 | 2712 |
| `94.130.108.80` | 2712 | 2712 |
| `162.159.205.23` | 2678 | 2776 |
| `162.159.205.24` | 2678 | 2776 |
| `162.159.205.25` | 2678 | 2776 |
| `162.159.205.17` | 2671 | 2767 |
| `162.159.205.18` | 2671 | 2767 |
| `162.159.205.19` | 2671 | 2767 |
| `162.159.205.11` | 2659 | 2755 |
| `162.159.205.12` | 2659 | 2755 |
| `162.159.205.13` | 2659 | 2755 |
| `91.196.52.205` | 2251 | 2461 |
| `116.202.9.167` | 1941 | 1944 |
| `46.101.111.206` | 1941 | 1944 |
| `142.132.166.12` | 1912 | 1915 |
| `188.166.111.252` | 1912 | 1915 |
| `138.226.240.26` | 1469 | 1481 |
| `146.190.212.90` | 1275 | 1276 |
| `146.190.223.124` | 1268 | 1269 |
| `195.123.189.142` | 1217 | 1227 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 455 |
| High-confidence disposable IPs | 1,160 |
| Promoted to `domains_inferred.txt` | 2 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**8405 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

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
| `007jlbu.com` | `route1.mx.cloudflare.net` |
| `007jlphp.com` | `route1.mx.cloudflare.net` |
| `00gmail.com` | `park-mx.above.com` |
| `010608.xyz` | `route1.mx.cloudflare.net` |
| `010hb.com` | `route1.mx.cloudflare.net` |
| `012356.xyz` | `route1.mx.cloudflare.net` |
| `012pg.bet` | `route1.mx.cloudflare.net` |
| `01g.cloud` | `alt1.aspmx.l.google.com` |
| `01p.co.jp` | `01p-co-jp.mail.protection.outlook.com` |
| `020307.xyz` | `route1.mx.cloudflare.net` |
| `041998.xyz` | `mx1.alias.proton.me` |
| `099833.xyz` | `park-mx.above.com` |
| `0ak.org` | `mx00.ionos.com` |
| `0hcow.com` | `mxa.mailgun.org` |
| `0hio.net` | `aspmx1.migadu.com` |
| `0nce.net` | `route1.mx.cloudflare.net` |
| `0rg.fr` | `mx1.mail.ovh.net` |
| `0sp.me` | `eforward1.registrar-servers.com` |
| `0ut.online` | `smtp.google.com` |
| `0x7121.com` | `park-mx.above.com` |
| `0xmiikee.com` | `eforward1.registrar-servers.com` |


*… and 8,375 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
