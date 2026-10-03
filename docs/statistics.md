# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-10-03 03:18 UTC**.*  
*Last DNS snapshot: **2026-10-03T02:16:02+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 97,735 |
| `domains_strict.txt` | 98,966 |
| `domains_inferred.txt` (opt-in) | 2 |

## Reachability

Of **98,786** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 41,815 | 42.3% |
| A_ONLY | 5,168 | 5.2% |
| NXDOMAIN | 39,391 | 39.9% |
| NO_RECORDS | 907 | 0.9% |
| TIMEOUT | 11,505 | 11.6% |

**46,983 domains are mail-reachable today** (47.6%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `route1.mx.cloudflare.net` | 2617 | 2627 | yes |
| `route2.mx.cloudflare.net` | 2617 | 2627 | yes |
| `route3.mx.cloudflare.net` | 2614 | 2624 | yes |
| `mail.wabblywabble.com` | 1842 | 1844 |  |
| `mail.wallywatts.com` | 1842 | 1844 |  |
| `generator.email` | 1468 | 1485 |  |
| `aero4.unstablemail.com` | 1248 | 1259 |  |
| `srv4.unstablemail.com` | 1248 | 1259 |  |
| `mx4.beavis99.com` | 1169 | 1169 |  |
| `mx4.beavis99.net` | 1168 | 1168 |  |
| `aspmx.l.google.com` | 1017 | 1019 | yes |
| `alt1.aspmx.l.google.com` | 996 | 998 | yes |
| `alt2.aspmx.l.google.com` | 990 | 992 | yes |
| `park-mx.above.com` | 914 | 919 | yes |
| `eforward1.registrar-servers.com` | 886 | 889 | yes |
| `eforward2.registrar-servers.com` | 886 | 889 | yes |
| `eforward3.registrar-servers.com` | 886 | 889 | yes |
| `eforward4.registrar-servers.com` | 886 | 889 | yes |
| `eforward5.registrar-servers.com` | 886 | 889 | yes |
| `smtp.google.com` | 766 | 767 | yes |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 1842 | 1844 |
| `mail.wallywatts.com` | 1842 | 1844 |
| `generator.email` | 1468 | 1485 |
| `aero4.unstablemail.com` | 1248 | 1259 |
| `srv4.unstablemail.com` | 1248 | 1259 |
| `mx4.beavis99.com` | 1169 | 1169 |
| `mx4.beavis99.net` | 1168 | 1168 |
| `emailfake.com` | 701 | 712 |
| `publicms1.mail2world.com` | 591 | 592 |
| `publicms2.mail2world.com` | 591 | 592 |
| `email.chatgpt.org.uk` | 565 | 565 |
| `mx.emlhub.com` | 442 | 442 |
| `smtp.yopmail.com` | 442 | 444 |
| `mail.cleantempmail.com` | 379 | 379 |
| `email.gravityengine.cc` | 372 | 373 |
| `mail.h-email.net` | 369 | 399 |
| `mx2.timeweb.ru` | 366 | 366 |
| `mx1.timeweb.ru` | 365 | 365 |
| `mx.spymail.one` | 359 | 359 |
| `tinyhost.shop` | 353 | 353 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `78.47.124.133` | 2632 | 2632 |
| `94.130.108.80` | 2632 | 2632 |
| `162.159.205.23` | 2609 | 2619 |
| `162.159.205.24` | 2609 | 2619 |
| `162.159.205.25` | 2609 | 2619 |
| `162.159.205.17` | 2585 | 2595 |
| `162.159.205.18` | 2585 | 2595 |
| `162.159.205.19` | 2585 | 2595 |
| `162.159.205.11` | 2575 | 2585 |
| `162.159.205.12` | 2575 | 2585 |
| `162.159.205.13` | 2575 | 2585 |
| `91.196.52.205` | 2296 | 2326 |
| `116.202.9.167` | 1800 | 1802 |
| `46.101.111.206` | 1800 | 1802 |
| `142.132.166.12` | 1796 | 1798 |
| `188.166.111.252` | 1796 | 1798 |
| `138.226.240.26` | 1245 | 1246 |
| `195.123.189.142` | 1227 | 1229 |
| `146.190.212.90` | 1217 | 1227 |
| `146.190.223.124` | 1198 | 1209 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 449 |
| High-confidence disposable IPs | 1,105 |
| Promoted to `domains_inferred.txt` | 2 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**8259 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

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
| `0live.org` | `route1.mx.cloudflare.net` |
| `0nce.net` | `route1.mx.cloudflare.net` |
| `0rg.fr` | `mx1.mail.ovh.net` |
| `0sp.me` | `eforward1.registrar-servers.com` |
| `0ut.online` | `smtp.google.com` |
| `0x7121.com` | `park-mx.above.com` |
| `0xmiikee.com` | `eforward1.registrar-servers.com` |
| `1-2.co.uk` | `12-co-uk0c.mail.protection.outlook.com` |


*… and 8,229 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
