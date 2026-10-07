# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-10-07 02:30 UTC**.*  
*Last DNS snapshot: **2026-10-07T02:24:17+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 97,751 |
| `domains_strict.txt` | 98,982 |
| `domains_inferred.txt` (opt-in) | 2 |

## Reachability

Of **99,118** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 43,465 | 43.9% |
| A_ONLY | 5,593 | 5.6% |
| NXDOMAIN | 41,900 | 42.3% |
| NO_RECORDS | 993 | 1.0% |
| TIMEOUT | 7,167 | 7.2% |

**49,058 domains are mail-reachable today** (49.5%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `route2.mx.cloudflare.net` | 2648 | 2692 | yes |
| `route1.mx.cloudflare.net` | 2647 | 2691 | yes |
| `route3.mx.cloudflare.net` | 2646 | 2690 | yes |
| `mail.wabblywabble.com` | 1932 | 1934 |  |
| `mail.wallywatts.com` | 1932 | 1934 |  |
| `generator.email` | 1497 | 1538 |  |
| `aero4.unstablemail.com` | 1295 | 1295 |  |
| `srv4.unstablemail.com` | 1294 | 1294 |  |
| `mx4.beavis99.com` | 1224 | 1224 |  |
| `mx4.beavis99.net` | 1223 | 1223 |  |
| `aspmx.l.google.com` | 1071 | 1082 | yes |
| `alt1.aspmx.l.google.com` | 1051 | 1062 | yes |
| `alt2.aspmx.l.google.com` | 1044 | 1055 | yes |
| `park-mx.above.com` | 941 | 953 | yes |
| `eforward1.registrar-servers.com` | 912 | 920 | yes |
| `eforward2.registrar-servers.com` | 912 | 920 | yes |
| `eforward3.registrar-servers.com` | 912 | 920 | yes |
| `eforward4.registrar-servers.com` | 912 | 920 | yes |
| `eforward5.registrar-servers.com` | 912 | 920 | yes |
| `alt3.aspmx.l.google.com` | 776 | 782 | yes |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 1932 | 1934 |
| `mail.wallywatts.com` | 1932 | 1934 |
| `generator.email` | 1497 | 1538 |
| `aero4.unstablemail.com` | 1295 | 1295 |
| `srv4.unstablemail.com` | 1294 | 1294 |
| `mx4.beavis99.com` | 1224 | 1224 |
| `mx4.beavis99.net` | 1223 | 1223 |
| `emailfake.com` | 720 | 730 |
| `email.chatgpt.org.uk` | 626 | 626 |
| `publicms1.mail2world.com` | 590 | 592 |
| `publicms2.mail2world.com` | 590 | 592 |
| `mx.emlhub.com` | 460 | 460 |
| `smtp.yopmail.com` | 442 | 448 |
| `email.gravityengine.cc` | 390 | 391 |
| `tinyhost.shop` | 390 | 390 |
| `mail.cleantempmail.com` | 377 | 378 |
| `mail.h-email.net` | 371 | 416 |
| `mx2.timeweb.ru` | 371 | 371 |
| `mx1.timeweb.ru` | 370 | 370 |
| `mx.spymail.one` | 369 | 369 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `78.47.124.133` | 2787 | 2787 |
| `94.130.108.80` | 2787 | 2787 |
| `162.159.205.23` | 2640 | 2684 |
| `162.159.205.24` | 2640 | 2684 |
| `162.159.205.25` | 2640 | 2684 |
| `162.159.205.17` | 2625 | 2669 |
| `162.159.205.18` | 2625 | 2669 |
| `162.159.205.19` | 2625 | 2669 |
| `162.159.205.11` | 2623 | 2665 |
| `162.159.205.12` | 2623 | 2665 |
| `162.159.205.13` | 2623 | 2665 |
| `91.196.52.205` | 2398 | 2451 |
| `116.202.9.167` | 1900 | 1902 |
| `142.132.166.12` | 1900 | 1902 |
| `188.166.111.252` | 1900 | 1902 |
| `46.101.111.206` | 1900 | 1902 |
| `138.226.240.26` | 1334 | 1336 |
| `146.190.212.90` | 1262 | 1262 |
| `146.190.223.124` | 1247 | 1247 |
| `195.123.189.142` | 1241 | 1242 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 458 |
| High-confidence disposable IPs | 1,146 |
| Promoted to `domains_inferred.txt` | 2 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**8448 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

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


*… and 8,418 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
