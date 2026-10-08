# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-10-08 02:41 UTC**.*  
*Last DNS snapshot: **2026-10-08T02:26:15+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 97,740 |
| `domains_strict.txt` | 98,971 |
| `domains_inferred.txt` (opt-in) | 2 |

## Reachability

Of **99,182** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 43,436 | 43.8% |
| A_ONLY | 5,613 | 5.7% |
| NXDOMAIN | 42,083 | 42.4% |
| NO_RECORDS | 946 | 1.0% |
| TIMEOUT | 7,104 | 7.2% |

**49,049 domains are mail-reachable today** (49.5%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `route2.mx.cloudflare.net` | 2647 | 2704 | yes |
| `route1.mx.cloudflare.net` | 2646 | 2703 | yes |
| `route3.mx.cloudflare.net` | 2645 | 2702 | yes |
| `mail.wabblywabble.com` | 1937 | 1948 |  |
| `mail.wallywatts.com` | 1937 | 1948 |  |
| `generator.email` | 1471 | 1522 |  |
| `aero4.unstablemail.com` | 1284 | 1287 |  |
| `srv4.unstablemail.com` | 1283 | 1286 |  |
| `mx4.beavis99.com` | 1235 | 1235 |  |
| `mx4.beavis99.net` | 1234 | 1234 |  |
| `aspmx.l.google.com` | 1076 | 1083 | yes |
| `alt1.aspmx.l.google.com` | 1057 | 1064 | yes |
| `alt2.aspmx.l.google.com` | 1050 | 1057 | yes |
| `park-mx.above.com` | 947 | 961 | yes |
| `eforward1.registrar-servers.com` | 913 | 923 | yes |
| `eforward2.registrar-servers.com` | 913 | 923 | yes |
| `eforward3.registrar-servers.com` | 913 | 923 | yes |
| `eforward4.registrar-servers.com` | 913 | 923 | yes |
| `eforward5.registrar-servers.com` | 913 | 923 | yes |
| `alt3.aspmx.l.google.com` | 780 | 783 | yes |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 1937 | 1948 |
| `mail.wallywatts.com` | 1937 | 1948 |
| `generator.email` | 1471 | 1522 |
| `aero4.unstablemail.com` | 1284 | 1287 |
| `srv4.unstablemail.com` | 1283 | 1286 |
| `mx4.beavis99.com` | 1235 | 1235 |
| `mx4.beavis99.net` | 1234 | 1234 |
| `email.chatgpt.org.uk` | 747 | 747 |
| `emailfake.com` | 684 | 694 |
| `publicms1.mail2world.com` | 591 | 592 |
| `publicms2.mail2world.com` | 591 | 592 |
| `mx.emlhub.com` | 461 | 461 |
| `smtp.yopmail.com` | 438 | 443 |
| `email.gravityengine.cc` | 385 | 386 |
| `tinyhost.shop` | 379 | 379 |
| `mail.cleantempmail.com` | 374 | 374 |
| `mail.h-email.net` | 374 | 416 |
| `mx.spymail.one` | 373 | 373 |
| `mx2.timeweb.ru` | 370 | 370 |
| `mx1.timeweb.ru` | 369 | 369 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `78.47.124.133` | 2676 | 2676 |
| `94.130.108.80` | 2676 | 2676 |
| `162.159.205.23` | 2638 | 2695 |
| `162.159.205.24` | 2638 | 2695 |
| `162.159.205.25` | 2638 | 2695 |
| `162.159.205.17` | 2623 | 2680 |
| `162.159.205.18` | 2623 | 2680 |
| `162.159.205.19` | 2623 | 2680 |
| `162.159.205.11` | 2621 | 2676 |
| `162.159.205.12` | 2621 | 2676 |
| `162.159.205.13` | 2621 | 2676 |
| `91.196.52.205` | 2347 | 2410 |
| `116.202.9.167` | 1907 | 1918 |
| `142.132.166.12` | 1907 | 1918 |
| `188.166.111.252` | 1907 | 1918 |
| `46.101.111.206` | 1907 | 1918 |
| `138.226.240.26` | 1428 | 1429 |
| `146.190.212.90` | 1252 | 1255 |
| `195.123.189.142` | 1239 | 1242 |
| `146.190.223.124` | 1236 | 1239 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 459 |
| High-confidence disposable IPs | 1,147 |
| Promoted to `domains_inferred.txt` | 2 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**8470 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

| Listed disposable | MX (shared infra) |
|---|---|
| `0-30-24.com` | `alt1.aspmx.l.google.com` |
| `0-mail.com` | `park-mx.above.com` |
| `000476.com` | `park-mx.above.com` |
| `000728.xyz` | `route1.mx.cloudflare.net` |
| `001218.xyz` | `route1.mx.cloudflare.net` |
| `001250.xyz` | `eforward1.registrar-servers.com` |
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


*… and 8,440 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
