# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-08-24 02:52 UTC**.*  
*Last DNS snapshot: **2026-08-24T02:32:57+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 74,861 |
| `domains_strict.txt` | 74,892 |
| `domains_inferred.txt` (opt-in) | 1 |

## Reachability

Of **75,743** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 13,319 | 17.6% |
| A_ONLY | 2,409 | 3.2% |
| NXDOMAIN | 23,476 | 31.0% |
| NO_RECORDS | 401 | 0.5% |
| TIMEOUT | 36,138 | 47.7% |

**15,728 domains are mail-reachable today** (20.8%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `mail.wabblywabble.com` | 729 | 788 |  |
| `mail.wallywatts.com` | 729 | 788 |  |
| `mx4.beavis99.com` | 593 | 594 |  |
| `mx4.beavis99.net` | 593 | 594 |  |
| `route2.mx.cloudflare.net` | 550 | 560 | yes |
| `route1.mx.cloudflare.net` | 549 | 559 | yes |
| `route3.mx.cloudflare.net` | 549 | 559 | yes |
| `generator.email` | 435 | 570 |  |
| `email.gravityengine.cc` | 388 | 388 |  |
| `email.chatgpt.org.uk` | 342 | 342 |  |
| `tinyhost.shop` | 311 | 311 |  |
| `mx.emlhub.com` | 287 | 287 |  |
| `emailfake.com` | 279 | 316 |  |
| `park-mx.above.com` | 271 | 275 | yes |
| `aspmx.l.google.com` | 255 | 257 | yes |
| `alt1.aspmx.l.google.com` | 249 | 251 | yes |
| `aero4.unstablemail.com` | 246 | 246 |  |
| `srv4.unstablemail.com` | 246 | 246 |  |
| `alt2.aspmx.l.google.com` | 245 | 247 | yes |
| `mx.spymail.one` | 211 | 211 |  |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 729 | 788 |
| `mail.wallywatts.com` | 729 | 788 |
| `mx4.beavis99.com` | 593 | 594 |
| `mx4.beavis99.net` | 593 | 594 |
| `generator.email` | 435 | 570 |
| `email.gravityengine.cc` | 388 | 388 |
| `email.chatgpt.org.uk` | 342 | 342 |
| `tinyhost.shop` | 311 | 311 |
| `mx.emlhub.com` | 287 | 287 |
| `emailfake.com` | 279 | 316 |
| `aero4.unstablemail.com` | 246 | 246 |
| `srv4.unstablemail.com` | 246 | 246 |
| `mx.spymail.one` | 211 | 211 |
| `mx.emlpro.com` | 182 | 182 |
| `mx.emltmp.com` | 182 | 182 |
| `mx.dropmail.me` | 174 | 174 |
| `mx.freeml.net` | 163 | 163 |
| `mail.casadorock.com` | 145 | 145 |
| `mx156.hostedmxserver.com` | 132 | 132 |
| `mx37.m1bp.com` | 131 | 131 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `78.47.124.133` | 1155 | 1155 |
| `94.130.108.80` | 1155 | 1155 |
| `138.226.240.26` | 696 | 696 |
| `91.196.52.205` | 617 | 789 |
| `116.202.9.167` | 593 | 643 |
| `46.101.111.206` | 593 | 643 |
| `142.132.166.12` | 579 | 630 |
| `188.166.111.252` | 579 | 630 |
| `13.223.25.84` | 502 | 502 |
| `54.243.117.197` | 502 | 502 |
| `162.159.205.23` | 474 | 482 |
| `162.159.205.24` | 474 | 482 |
| `162.159.205.25` | 474 | 482 |
| `162.159.205.17` | 472 | 481 |
| `162.159.205.18` | 472 | 481 |
| `162.159.205.19` | 472 | 481 |
| `162.159.205.11` | 458 | 466 |
| `162.159.205.12` | 458 | 466 |
| `162.159.205.13` | 458 | 466 |
| `188.245.74.208` | 423 | 424 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 222 |
| High-confidence disposable IPs | 485 |
| Promoted to `domains_inferred.txt` | 1 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**1809 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

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
| `0nes.net` | `park-mx.above.com` |
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
| `129.in` | `park-mx.above.com` |
| `12storage.com` | `park-mx.above.com` |
| `13dk.net` | `route1.mx.cloudflare.net` |
| `14n.co.uk` | `14n-co-uk.mail.protection.outlook.com` |
| `14p.in` | `eforward1.registrar-servers.com` |
| `15qm-mail.red` | `eforward1.registrar-servers.com` |
| `189.email` | `route1.mx.cloudflare.net` |


*… and 1,779 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
