# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-09-03 02:35 UTC**.*  
*Last DNS snapshot: **2026-09-03T02:30:30+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 75,257 |
| `domains_strict.txt` | 75,288 |
| `domains_inferred.txt` (opt-in) | 1 |

## Reachability

Of **76,189** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 13,249 | 17.4% |
| A_ONLY | 2,340 | 3.1% |
| NXDOMAIN | 23,180 | 30.4% |
| NO_RECORDS | 328 | 0.4% |
| TIMEOUT | 37,092 | 48.7% |

**15,589 domains are mail-reachable today** (20.5%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `mail.wabblywabble.com` | 713 | 777 |  |
| `mail.wallywatts.com` | 713 | 777 |  |
| `mx4.beavis99.com` | 575 | 576 |  |
| `mx4.beavis99.net` | 575 | 576 |  |
| `route2.mx.cloudflare.net` | 499 | 510 | yes |
| `route1.mx.cloudflare.net` | 498 | 509 | yes |
| `route3.mx.cloudflare.net` | 497 | 508 | yes |
| `tinyhost.shop` | 465 | 465 |  |
| `generator.email` | 441 | 578 |  |
| `email.chatgpt.org.uk` | 290 | 290 |  |
| `park-mx.above.com` | 271 | 276 | yes |
| `mx.emlhub.com` | 267 | 267 |  |
| `emailfake.com` | 258 | 295 |  |
| `aero4.unstablemail.com` | 237 | 237 |  |
| `srv4.unstablemail.com` | 237 | 237 |  |
| `aspmx.l.google.com` | 231 | 233 | yes |
| `alt1.aspmx.l.google.com` | 229 | 231 | yes |
| `alt2.aspmx.l.google.com` | 225 | 227 | yes |
| `mx.spymail.one` | 209 | 209 |  |
| `eforward1.registrar-servers.com` | 185 | 188 | yes |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 713 | 777 |
| `mail.wallywatts.com` | 713 | 777 |
| `mx4.beavis99.com` | 575 | 576 |
| `mx4.beavis99.net` | 575 | 576 |
| `tinyhost.shop` | 465 | 465 |
| `generator.email` | 441 | 578 |
| `email.chatgpt.org.uk` | 290 | 290 |
| `mx.emlhub.com` | 267 | 267 |
| `emailfake.com` | 258 | 295 |
| `aero4.unstablemail.com` | 237 | 237 |
| `srv4.unstablemail.com` | 237 | 237 |
| `mx.spymail.one` | 209 | 209 |
| `mx.emlpro.com` | 185 | 185 |
| `mx.emltmp.com` | 177 | 177 |
| `mx.dropmail.me` | 158 | 158 |
| `mx37.m1bp.com` | 158 | 158 |
| `mx37.mb5p.com` | 158 | 158 |
| `email.gravityengine.cc` | 151 | 151 |
| `mx.freeml.net` | 147 | 147 |
| `mail.casadorock.com` | 142 | 142 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `78.47.124.133` | 1070 | 1070 |
| `94.130.108.80` | 1070 | 1070 |
| `91.196.52.205` | 622 | 796 |
| `116.202.9.167` | 592 | 647 |
| `46.101.111.206` | 592 | 647 |
| `142.132.166.12` | 591 | 647 |
| `188.166.111.252` | 591 | 647 |
| `13.223.25.84` | 466 | 466 |
| `54.243.117.197` | 466 | 466 |
| `188.245.74.208` | 447 | 448 |
| `195.201.18.63` | 432 | 433 |
| `162.159.205.17` | 424 | 434 |
| `162.159.205.18` | 424 | 434 |
| `162.159.205.19` | 424 | 434 |
| `162.159.205.23` | 422 | 431 |
| `162.159.205.24` | 422 | 431 |
| `162.159.205.25` | 422 | 431 |
| `144.91.107.45` | 417 | 417 |
| `162.159.205.11` | 415 | 424 |
| `162.159.205.12` | 415 | 424 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 224 |
| High-confidence disposable IPs | 503 |
| Promoted to `domains_inferred.txt` | 1 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**1720 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

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
| `129.in` | `park-mx.above.com` |
| `12storage.com` | `park-mx.above.com` |
| `13dk.net` | `route1.mx.cloudflare.net` |
| `14n.co.uk` | `14n-co-uk.mail.protection.outlook.com` |
| `14p.in` | `eforward1.registrar-servers.com` |
| `15qm-mail.red` | `eforward1.registrar-servers.com` |
| `189.email` | `route1.mx.cloudflare.net` |
| `1987.com` | `park-mx.above.com` |


*… and 1,690 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
