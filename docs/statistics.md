# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-06-15 03:38 UTC**.*  
*Last DNS snapshot: **2026-06-15T03:22:08+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 73,442 |
| `domains_strict.txt` | 73,473 |
| `domains_inferred.txt` (opt-in) | 2 |

## Reachability

Of **73,956** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 21,284 | 28.8% |
| A_ONLY | 4,917 | 6.6% |
| NXDOMAIN | 39,182 | 53.0% |
| NO_RECORDS | 660 | 0.9% |
| TIMEOUT | 7,913 | 10.7% |

**26,201 domains are mail-reachable today** (35.4%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `mail.wabblywabble.com` | 1355 | 1378 |  |
| `mail.wallywatts.com` | 1355 | 1378 |  |
| `mx4.beavis99.com` | 964 | 965 |  |
| `mx4.beavis99.net` | 963 | 964 |  |
| `generator.email` | 783 | 936 |  |
| `route1.mx.cloudflare.net` | 770 | 777 | yes |
| `route2.mx.cloudflare.net` | 770 | 777 | yes |
| `route3.mx.cloudflare.net` | 769 | 776 | yes |
| `park-mx.above.com` | 602 | 603 | yes |
| `mx.emlhub.com` | 460 | 460 |  |
| `aspmx.l.google.com` | 441 | 441 | yes |
| `alt1.aspmx.l.google.com` | 432 | 432 | yes |
| `alt2.aspmx.l.google.com` | 429 | 429 | yes |
| `emailfake.com` | 429 | 483 |  |
| `aero4.unstablemail.com` | 409 | 409 |  |
| `srv4.unstablemail.com` | 408 | 408 |  |
| `mx.emltmp.com` | 352 | 352 |  |
| `eforward1.registrar-servers.com` | 332 | 333 | yes |
| `eforward2.registrar-servers.com` | 332 | 333 | yes |
| `eforward3.registrar-servers.com` | 332 | 333 | yes |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 1355 | 1378 |
| `mail.wallywatts.com` | 1355 | 1378 |
| `mx4.beavis99.com` | 964 | 965 |
| `mx4.beavis99.net` | 963 | 964 |
| `generator.email` | 783 | 936 |
| `mx.emlhub.com` | 460 | 460 |
| `emailfake.com` | 429 | 483 |
| `aero4.unstablemail.com` | 409 | 409 |
| `srv4.unstablemail.com` | 408 | 408 |
| `mx.emltmp.com` | 352 | 352 |
| `mx.spymail.one` | 332 | 332 |
| `mx.emlpro.com` | 327 | 327 |
| `mx.dropmail.me` | 304 | 304 |
| `mx.freeml.net` | 289 | 289 |
| `mx37.m1bp.com` | 259 | 259 |
| `mx37.mb5p.com` | 259 | 259 |
| `mx.yomail.info` | 231 | 231 |
| `mx156.hostedmxserver.com` | 221 | 221 |
| `mail.h-email.net` | 210 | 210 |
| `mx195.m1bp.com` | 210 | 211 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `78.47.124.133` | 2386 | 2386 |
| `94.130.108.80` | 2386 | 2386 |
| `116.202.9.167` | 1304 | 1323 |
| `46.101.111.206` | 1304 | 1323 |
| `142.132.166.12` | 1282 | 1302 |
| `188.166.111.252` | 1282 | 1302 |
| `91.196.52.205` | 1264 | 1475 |
| `13.223.25.84` | 1036 | 1036 |
| `54.243.117.197` | 1036 | 1036 |
| `188.245.74.208` | 936 | 937 |
| `195.201.18.63` | 919 | 920 |
| `162.159.205.17` | 777 | 783 |
| `162.159.205.18` | 777 | 783 |
| `162.159.205.19` | 777 | 783 |
| `162.159.205.23` | 773 | 779 |
| `162.159.205.24` | 773 | 779 |
| `162.159.205.25` | 773 | 779 |
| `162.159.205.11` | 764 | 770 |
| `162.159.205.12` | 764 | 770 |
| `162.159.205.13` | 764 | 770 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 286 |
| High-confidence disposable IPs | 753 |
| Promoted to `domains_inferred.txt` | 2 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**3119 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

| Listed disposable | MX (shared infra) |
|---|---|
| `0-30-24.com` | `alt1.aspmx.l.google.com` |
| `0-mail.com` | `park-mx.above.com` |
| `0058.ru` | `alt1.aspmx.l.google.com` |
| `01g.cloud` | `alt1.aspmx.l.google.com` |
| `0ak.org` | `mx00.ionos.com` |
| `0hcow.com` | `mxa.mailgun.org` |
| `0hio.net` | `aspmx1.migadu.com` |
| `0ioi.net` | `route1.mx.cloudflare.net` |
| `0live.org` | `route1.mx.cloudflare.net` |
| `0nce.net` | `route1.mx.cloudflare.net` |
| `0ne0ut.com` | `route1.mx.cloudflare.net` |
| `0rg.fr` | `mx1.mail.ovh.net` |
| `0xmiikee.com` | `eforward1.registrar-servers.com` |
| `1-8.biz` | `mail.protonmail.ch` |
| `1-box.ru` | `mx.yandex.ru` |
| `10bir.com` | `route1.mx.cloudflare.net` |
| `10dkmail.net` | `smtp.google.com` |
| `10inbox.online` | `route1.mx.cloudflare.net` |
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


*… and 3,089 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
