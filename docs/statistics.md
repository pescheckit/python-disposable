# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-10-09 02:45 UTC**.*  
*Last DNS snapshot: **2026-10-09T02:45:45+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 96,306 |
| `domains_strict.txt` | 97,537 |
| `domains_inferred.txt` (opt-in) | 2 |

## Reachability

Of **99,255** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 43,508 | 43.8% |
| A_ONLY | 5,630 | 5.7% |
| NXDOMAIN | 42,101 | 42.4% |
| NO_RECORDS | 958 | 1.0% |
| TIMEOUT | 7,058 | 7.1% |

**49,138 domains are mail-reachable today** (49.5%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `route2.mx.cloudflare.net` | 2610 | 2685 | yes |
| `route1.mx.cloudflare.net` | 2609 | 2684 | yes |
| `route3.mx.cloudflare.net` | 2608 | 2683 | yes |
| `mail.wabblywabble.com` | 1939 | 1952 |  |
| `mail.wallywatts.com` | 1939 | 1952 |  |
| `generator.email` | 1431 | 1512 |  |
| `aero4.unstablemail.com` | 1293 | 1293 |  |
| `srv4.unstablemail.com` | 1292 | 1292 |  |
| `mx4.beavis99.com` | 1236 | 1236 |  |
| `mx4.beavis99.net` | 1235 | 1235 |  |
| `aspmx.l.google.com` | 994 | 1075 | yes |
| `alt1.aspmx.l.google.com` | 976 | 1055 | yes |
| `alt2.aspmx.l.google.com` | 972 | 1049 | yes |
| `park-mx.above.com` | 930 | 965 | yes |
| `eforward1.registrar-servers.com` | 909 | 925 | yes |
| `eforward2.registrar-servers.com` | 909 | 925 | yes |
| `eforward3.registrar-servers.com` | 909 | 925 | yes |
| `eforward4.registrar-servers.com` | 909 | 925 | yes |
| `eforward5.registrar-servers.com` | 909 | 925 | yes |
| `smtp.google.com` | 762 | 781 | yes |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 1939 | 1952 |
| `mail.wallywatts.com` | 1939 | 1952 |
| `generator.email` | 1431 | 1512 |
| `aero4.unstablemail.com` | 1293 | 1293 |
| `srv4.unstablemail.com` | 1292 | 1292 |
| `mx4.beavis99.com` | 1236 | 1236 |
| `mx4.beavis99.net` | 1235 | 1235 |
| `email.chatgpt.org.uk` | 754 | 754 |
| `emailfake.com` | 690 | 701 |
| `mx.emlhub.com` | 461 | 461 |
| `smtp.yopmail.com` | 436 | 443 |
| `mail.cleantempmail.com` | 388 | 388 |
| `email.gravityengine.cc` | 385 | 386 |
| `tinyhost.shop` | 381 | 381 |
| `mx.spymail.one` | 373 | 373 |
| `mx2.timeweb.ru` | 367 | 367 |
| `mx1.timeweb.ru` | 366 | 366 |
| `mx.emltmp.com` | 358 | 358 |
| `mail.h-email.net` | 355 | 411 |
| `mx.emlpro.com` | 342 | 342 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `78.47.124.133` | 2676 | 2676 |
| `94.130.108.80` | 2676 | 2676 |
| `162.159.205.23` | 2615 | 2690 |
| `162.159.205.24` | 2615 | 2690 |
| `162.159.205.25` | 2615 | 2690 |
| `162.159.205.17` | 2604 | 2679 |
| `162.159.205.18` | 2604 | 2679 |
| `162.159.205.19` | 2604 | 2679 |
| `162.159.205.11` | 2583 | 2657 |
| `162.159.205.12` | 2583 | 2657 |
| `162.159.205.13` | 2583 | 2657 |
| `91.196.52.205` | 2311 | 2404 |
| `116.202.9.167` | 1915 | 1928 |
| `46.101.111.206` | 1915 | 1928 |
| `142.132.166.12` | 1901 | 1913 |
| `188.166.111.252` | 1901 | 1913 |
| `138.226.240.26` | 1463 | 1464 |
| `146.190.212.90` | 1270 | 1270 |
| `146.190.223.124` | 1266 | 1266 |
| `195.123.189.142` | 1219 | 1222 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 443 |
| High-confidence disposable IPs | 1,112 |
| Promoted to `domains_inferred.txt` | 2 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**8242 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

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
| `00gmail.com` | `park-mx.above.com` |
| `010608.xyz` | `route1.mx.cloudflare.net` |
| `010hb.com` | `route1.mx.cloudflare.net` |
| `012356.xyz` | `route1.mx.cloudflare.net` |
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
| `1-2.co.uk` | `12-co-uk0c.mail.protection.outlook.com` |
| `1-8.biz` | `mail.protonmail.ch` |
| `1-box.ru` | `mx.yandex.ru` |


*… and 8,212 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
