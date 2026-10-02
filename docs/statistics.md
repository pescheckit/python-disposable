# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-10-02 02:29 UTC**.*  
*Last DNS snapshot: **2026-10-02T02:29:17+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 97,716 |
| `domains_strict.txt` | 98,947 |
| `domains_inferred.txt` (opt-in) | 2 |

## Reachability

Of **98,663** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 41,524 | 42.1% |
| A_ONLY | 5,098 | 5.2% |
| NXDOMAIN | 38,845 | 39.4% |
| NO_RECORDS | 887 | 0.9% |
| TIMEOUT | 12,309 | 12.5% |

**46,622 domains are mail-reachable today** (47.3%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `route1.mx.cloudflare.net` | 2604 | 2609 | yes |
| `route2.mx.cloudflare.net` | 2604 | 2609 | yes |
| `route3.mx.cloudflare.net` | 2601 | 2606 | yes |
| `mail.wabblywabble.com` | 1828 | 1830 |  |
| `mail.wallywatts.com` | 1828 | 1830 |  |
| `generator.email` | 1461 | 1475 |  |
| `aero4.unstablemail.com` | 1253 | 1255 |  |
| `srv4.unstablemail.com` | 1253 | 1255 |  |
| `mx4.beavis99.com` | 1160 | 1161 |  |
| `mx4.beavis99.net` | 1159 | 1160 |  |
| `aspmx.l.google.com` | 1008 | 1010 | yes |
| `alt1.aspmx.l.google.com` | 987 | 989 | yes |
| `alt2.aspmx.l.google.com` | 981 | 983 | yes |
| `park-mx.above.com` | 913 | 917 | yes |
| `eforward1.registrar-servers.com` | 881 | 883 | yes |
| `eforward2.registrar-servers.com` | 881 | 883 | yes |
| `eforward3.registrar-servers.com` | 881 | 883 | yes |
| `eforward4.registrar-servers.com` | 881 | 883 | yes |
| `eforward5.registrar-servers.com` | 881 | 883 | yes |
| `smtp.google.com` | 762 | 764 | yes |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 1828 | 1830 |
| `mail.wallywatts.com` | 1828 | 1830 |
| `generator.email` | 1461 | 1475 |
| `aero4.unstablemail.com` | 1253 | 1255 |
| `srv4.unstablemail.com` | 1253 | 1255 |
| `mx4.beavis99.com` | 1160 | 1161 |
| `mx4.beavis99.net` | 1159 | 1160 |
| `emailfake.com` | 699 | 711 |
| `publicms1.mail2world.com` | 591 | 592 |
| `publicms2.mail2world.com` | 591 | 592 |
| `email.chatgpt.org.uk` | 564 | 564 |
| `smtp.yopmail.com` | 442 | 444 |
| `mx.emlhub.com` | 440 | 440 |
| `mail.cleantempmail.com` | 379 | 379 |
| `email.gravityengine.cc` | 371 | 371 |
| `mail.h-email.net` | 361 | 389 |
| `mx2.timeweb.ru` | 361 | 361 |
| `mx1.timeweb.ru` | 360 | 360 |
| `mx.spymail.one` | 354 | 354 |
| `tinyhost.shop` | 351 | 351 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `78.47.124.133` | 2608 | 2608 |
| `94.130.108.80` | 2608 | 2608 |
| `162.159.205.23` | 2593 | 2598 |
| `162.159.205.24` | 2593 | 2598 |
| `162.159.205.25` | 2593 | 2598 |
| `162.159.205.17` | 2569 | 2574 |
| `162.159.205.18` | 2569 | 2574 |
| `162.159.205.19` | 2569 | 2574 |
| `162.159.205.11` | 2559 | 2564 |
| `162.159.205.12` | 2559 | 2564 |
| `162.159.205.13` | 2559 | 2564 |
| `91.196.52.205` | 2274 | 2302 |
| `116.202.9.167` | 1786 | 1788 |
| `46.101.111.206` | 1786 | 1788 |
| `142.132.166.12` | 1780 | 1782 |
| `188.166.111.252` | 1780 | 1782 |
| `138.226.240.26` | 1244 | 1244 |
| `195.123.189.142` | 1229 | 1229 |
| `146.190.212.90` | 1222 | 1224 |
| `146.190.223.124` | 1202 | 1204 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 443 |
| High-confidence disposable IPs | 1,099 |
| Promoted to `domains_inferred.txt` | 2 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**8223 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

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


*… and 8,193 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
