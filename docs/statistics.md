# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-10-12 02:53 UTC**.*  
*Last DNS snapshot: **2026-10-12T02:41:48+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 97,285 |
| `domains_strict.txt` | 98,517 |
| `domains_inferred.txt` (opt-in) | 2 |

## Reachability

Of **100,406** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 44,534 | 44.4% |
| A_ONLY | 5,696 | 5.7% |
| NXDOMAIN | 42,416 | 42.2% |
| NO_RECORDS | 967 | 1.0% |
| TIMEOUT | 6,793 | 6.8% |

**50,230 domains are mail-reachable today** (50.0%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `route2.mx.cloudflare.net` | 2691 | 2760 | yes |
| `route1.mx.cloudflare.net` | 2690 | 2759 | yes |
| `route3.mx.cloudflare.net` | 2689 | 2758 | yes |
| `mail.wabblywabble.com` | 1961 | 1962 |  |
| `mail.wallywatts.com` | 1961 | 1962 |  |
| `generator.email` | 1371 | 1556 |  |
| `aero4.unstablemail.com` | 1299 | 1300 |  |
| `srv4.unstablemail.com` | 1298 | 1299 |  |
| `mx4.beavis99.com` | 1234 | 1234 |  |
| `mx4.beavis99.net` | 1233 | 1233 |  |
| `aspmx.l.google.com` | 1005 | 1087 | yes |
| `alt1.aspmx.l.google.com` | 987 | 1067 | yes |
| `alt2.aspmx.l.google.com` | 983 | 1061 | yes |
| `park-mx.above.com` | 944 | 981 | yes |
| `eforward1.registrar-servers.com` | 906 | 925 | yes |
| `eforward2.registrar-servers.com` | 906 | 925 | yes |
| `eforward3.registrar-servers.com` | 906 | 925 | yes |
| `eforward4.registrar-servers.com` | 906 | 925 | yes |
| `eforward5.registrar-servers.com` | 906 | 925 | yes |
| `smtp.google.com` | 797 | 816 | yes |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 1961 | 1962 |
| `mail.wallywatts.com` | 1961 | 1962 |
| `generator.email` | 1371 | 1556 |
| `aero4.unstablemail.com` | 1299 | 1300 |
| `srv4.unstablemail.com` | 1298 | 1299 |
| `mx4.beavis99.com` | 1234 | 1234 |
| `mx4.beavis99.net` | 1233 | 1233 |
| `email.chatgpt.org.uk` | 750 | 750 |
| `emailfake.com` | 687 | 697 |
| `mx.emlhub.com` | 481 | 481 |
| `smtp.yopmail.com` | 434 | 443 |
| `mail.cleantempmail.com` | 416 | 416 |
| `email.gravityengine.cc` | 400 | 400 |
| `mx.spymail.one` | 375 | 375 |
| `mail.h-email.net` | 373 | 427 |
| `mx2.timeweb.ru` | 359 | 366 |
| `mx1.timeweb.ru` | 358 | 365 |
| `mx.emltmp.com` | 353 | 353 |
| `mx156.hostedmxserver.com` | 352 | 397 |
| `mx.emlpro.com` | 349 | 349 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `78.47.124.133` | 2728 | 2728 |
| `94.130.108.80` | 2728 | 2728 |
| `162.159.205.23` | 2694 | 2763 |
| `162.159.205.24` | 2694 | 2763 |
| `162.159.205.25` | 2694 | 2763 |
| `162.159.205.17` | 2684 | 2753 |
| `162.159.205.18` | 2684 | 2753 |
| `162.159.205.19` | 2684 | 2753 |
| `162.159.205.11` | 2669 | 2737 |
| `162.159.205.12` | 2669 | 2737 |
| `162.159.205.13` | 2669 | 2737 |
| `91.196.52.205` | 2249 | 2441 |
| `116.202.9.167` | 1935 | 1936 |
| `46.101.111.206` | 1935 | 1936 |
| `142.132.166.12` | 1904 | 1905 |
| `188.166.111.252` | 1904 | 1905 |
| `138.226.240.26` | 1481 | 1481 |
| `146.190.212.90` | 1271 | 1272 |
| `146.190.223.124` | 1267 | 1268 |
| `195.123.189.142` | 1221 | 1226 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 451 |
| High-confidence disposable IPs | 1,156 |
| Promoted to `domains_inferred.txt` | 2 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**8416 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

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


*… and 8,386 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
