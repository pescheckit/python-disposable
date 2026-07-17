# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-07-17 04:21 UTC**.*  
*Last DNS snapshot: **2026-07-17T04:21:16+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 74,519 |
| `domains_strict.txt` | 74,550 |
| `domains_inferred.txt` (opt-in) | 2 |

## Reachability

Of **75,181** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 20,873 | 27.8% |
| A_ONLY | 4,732 | 6.3% |
| NXDOMAIN | 37,059 | 49.3% |
| NO_RECORDS | 652 | 0.9% |
| TIMEOUT | 11,865 | 15.8% |

**25,605 domains are mail-reachable today** (34.1%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `mail.wabblywabble.com` | 1192 | 1235 |  |
| `mail.wallywatts.com` | 1192 | 1235 |  |
| `mx4.beavis99.com` | 968 | 969 |  |
| `mx4.beavis99.net` | 968 | 969 |  |
| `route1.mx.cloudflare.net` | 882 | 891 | yes |
| `route2.mx.cloudflare.net` | 882 | 891 | yes |
| `route3.mx.cloudflare.net` | 880 | 889 | yes |
| `generator.email` | 709 | 846 |  |
| `park-mx.above.com` | 561 | 563 | yes |
| `mx.emlhub.com` | 418 | 418 |  |
| `aspmx.l.google.com` | 409 | 411 | yes |
| `alt1.aspmx.l.google.com` | 401 | 403 | yes |
| `alt2.aspmx.l.google.com` | 397 | 399 | yes |
| `emailfake.com` | 392 | 434 |  |
| `tinyhost.shop` | 392 | 392 |  |
| `aero4.unstablemail.com` | 390 | 390 |  |
| `srv4.unstablemail.com` | 390 | 390 |  |
| `mx.spymail.one` | 335 | 335 |  |
| `mx.emltmp.com` | 333 | 333 |  |
| `eforward1.registrar-servers.com` | 304 | 307 | yes |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 1192 | 1235 |
| `mail.wallywatts.com` | 1192 | 1235 |
| `mx4.beavis99.com` | 968 | 969 |
| `mx4.beavis99.net` | 968 | 969 |
| `generator.email` | 709 | 846 |
| `mx.emlhub.com` | 418 | 418 |
| `emailfake.com` | 392 | 434 |
| `tinyhost.shop` | 392 | 392 |
| `aero4.unstablemail.com` | 390 | 390 |
| `srv4.unstablemail.com` | 390 | 390 |
| `mx.spymail.one` | 335 | 335 |
| `mx.emltmp.com` | 333 | 333 |
| `mx.emlpro.com` | 304 | 304 |
| `mx.dropmail.me` | 285 | 285 |
| `mx.freeml.net` | 283 | 283 |
| `email.gravityengine.cc` | 273 | 273 |
| `mx.yomail.info` | 229 | 229 |
| `mx37.m1bp.com` | 229 | 229 |
| `mx37.mb5p.com` | 229 | 229 |
| `mail.casadorock.com` | 199 | 199 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `78.47.124.133` | 2262 | 2262 |
| `94.130.108.80` | 2262 | 2262 |
| `116.202.9.167` | 1155 | 1193 |
| `46.101.111.206` | 1155 | 1193 |
| `91.196.52.205` | 1154 | 1339 |
| `142.132.166.12` | 1152 | 1191 |
| `188.166.111.252` | 1152 | 1191 |
| `188.245.74.208` | 945 | 946 |
| `13.223.25.84` | 934 | 934 |
| `54.243.117.197` | 934 | 934 |
| `195.201.18.63` | 931 | 932 |
| `162.159.205.17` | 880 | 888 |
| `162.159.205.18` | 880 | 888 |
| `162.159.205.19` | 880 | 888 |
| `162.159.205.11` | 878 | 886 |
| `162.159.205.12` | 878 | 886 |
| `162.159.205.13` | 878 | 886 |
| `162.159.205.23` | 878 | 886 |
| `162.159.205.24` | 878 | 886 |
| `162.159.205.25` | 878 | 886 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 295 |
| High-confidence disposable IPs | 746 |
| Promoted to `domains_inferred.txt` | 2 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**3087 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

| Listed disposable | MX (shared infra) |
|---|---|
| `0-30-24.com` | `alt1.aspmx.l.google.com` |
| `0-mail.com` | `park-mx.above.com` |
| `0058.ru` | `alt1.aspmx.l.google.com` |
| `01g.cloud` | `alt1.aspmx.l.google.com` |
| `020307.xyz` | `route1.mx.cloudflare.net` |
| `0ak.org` | `mx00.ionos.com` |
| `0hcow.com` | `mxa.mailgun.org` |
| `0hio.net` | `aspmx1.migadu.com` |
| `0nce.net` | `route1.mx.cloudflare.net` |
| `0rg.fr` | `mx1.mail.ovh.net` |
| `0xmiikee.com` | `eforward1.registrar-servers.com` |
| `1-8.biz` | `mail.protonmail.ch` |
| `1-box.ru` | `mx.yandex.ru` |
| `10bir.com` | `route1.mx.cloudflare.net` |
| `10dkmail.net` | `smtp.google.com` |
| `10m.email` | `eforward1.registrar-servers.com` |
| `10mi.org` | `alt1.aspmx.l.google.com` |
| `10minemail.com` | `route1.mx.cloudflare.net` |
| `10minutemail.co.za` | `route1.mx.cloudflare.net` |
| `11cows.com` | `mxa.mailgun.org` |
| `123gmail.com` | `park-mx.above.com` |
| `12499aaa.com` | `eforward1.registrar-servers.com` |
| `13dk.net` | `route1.mx.cloudflare.net` |
| `14n.co.uk` | `14n-co-uk.mail.protection.outlook.com` |
| `14p.in` | `eforward1.registrar-servers.com` |
| `15qm-mail.red` | `eforward1.registrar-servers.com` |
| `189.email` | `route1.mx.cloudflare.net` |
| `1987.com` | `park-mx.above.com` |
| `1aolmail.com` | `route1.mx.cloudflare.net` |
| `1ayj8yi7lpiksxawav.gq` | `route1.mx.cloudflare.net` |


*… and 3,057 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
