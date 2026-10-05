# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-10-05 02:48 UTC**.*  
*Last DNS snapshot: **2026-10-05T02:28:25+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 97,774 |
| `domains_strict.txt` | 99,005 |
| `domains_inferred.txt` (opt-in) | 2 |

## Reachability

Of **98,985** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 42,889 | 43.3% |
| A_ONLY | 5,456 | 5.5% |
| NXDOMAIN | 41,198 | 41.6% |
| NO_RECORDS | 974 | 1.0% |
| TIMEOUT | 8,468 | 8.6% |

**48,345 domains are mail-reachable today** (48.8%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `route2.mx.cloudflare.net` | 2644 | 2677 | yes |
| `route1.mx.cloudflare.net` | 2643 | 2676 | yes |
| `route3.mx.cloudflare.net` | 2642 | 2675 | yes |
| `mail.wabblywabble.com` | 1911 | 1913 |  |
| `mail.wallywatts.com` | 1911 | 1913 |  |
| `generator.email` | 1486 | 1522 |  |
| `aero4.unstablemail.com` | 1281 | 1282 |  |
| `srv4.unstablemail.com` | 1280 | 1281 |  |
| `mx4.beavis99.com` | 1208 | 1208 |  |
| `mx4.beavis99.net` | 1207 | 1207 |  |
| `aspmx.l.google.com` | 1061 | 1069 | yes |
| `alt1.aspmx.l.google.com` | 1041 | 1049 | yes |
| `alt2.aspmx.l.google.com` | 1034 | 1042 | yes |
| `park-mx.above.com` | 939 | 948 | yes |
| `eforward1.registrar-servers.com` | 911 | 917 | yes |
| `eforward2.registrar-servers.com` | 911 | 917 | yes |
| `eforward3.registrar-servers.com` | 911 | 917 | yes |
| `eforward4.registrar-servers.com` | 911 | 917 | yes |
| `eforward5.registrar-servers.com` | 911 | 917 | yes |
| `smtp.google.com` | 775 | 777 | yes |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 1911 | 1913 |
| `mail.wallywatts.com` | 1911 | 1913 |
| `generator.email` | 1486 | 1522 |
| `aero4.unstablemail.com` | 1281 | 1282 |
| `srv4.unstablemail.com` | 1280 | 1281 |
| `mx4.beavis99.com` | 1208 | 1208 |
| `mx4.beavis99.net` | 1207 | 1207 |
| `emailfake.com` | 720 | 730 |
| `publicms1.mail2world.com` | 590 | 592 |
| `publicms2.mail2world.com` | 590 | 592 |
| `email.chatgpt.org.uk` | 587 | 587 |
| `smtp.yopmail.com` | 451 | 453 |
| `mx.emlhub.com` | 441 | 441 |
| `email.gravityengine.cc` | 381 | 382 |
| `mail.cleantempmail.com` | 378 | 378 |
| `tinyhost.shop` | 372 | 372 |
| `mx2.timeweb.ru` | 369 | 370 |
| `mail.h-email.net` | 368 | 408 |
| `mx1.timeweb.ru` | 368 | 369 |
| `mx.spymail.one` | 365 | 365 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `78.47.124.133` | 2693 | 2693 |
| `94.130.108.80` | 2693 | 2693 |
| `162.159.205.23` | 2638 | 2671 |
| `162.159.205.24` | 2638 | 2671 |
| `162.159.205.25` | 2638 | 2671 |
| `162.159.205.17` | 2620 | 2652 |
| `162.159.205.18` | 2620 | 2652 |
| `162.159.205.19` | 2620 | 2652 |
| `162.159.205.11` | 2618 | 2650 |
| `162.159.205.12` | 2618 | 2650 |
| `162.159.205.13` | 2618 | 2650 |
| `91.196.52.205` | 2368 | 2416 |
| `142.132.166.12` | 1881 | 1883 |
| `188.166.111.252` | 1881 | 1883 |
| `116.202.9.167` | 1879 | 1881 |
| `46.101.111.206` | 1879 | 1881 |
| `138.226.240.26` | 1286 | 1287 |
| `146.190.212.90` | 1251 | 1252 |
| `195.123.189.142` | 1237 | 1238 |
| `146.190.223.124` | 1233 | 1234 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 454 |
| High-confidence disposable IPs | 1,112 |
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


*… and 8,386 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
