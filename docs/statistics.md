# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-08-03 04:22 UTC**.*  
*Last DNS snapshot: **2026-08-03T04:09:02+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 74,685 |
| `domains_strict.txt` | 74,716 |
| `domains_inferred.txt` (opt-in) | 1 |

## Reachability

Of **75,448** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 11,834 | 15.7% |
| A_ONLY | 1,947 | 2.6% |
| NXDOMAIN | 20,840 | 27.6% |
| NO_RECORDS | 285 | 0.4% |
| TIMEOUT | 40,542 | 53.7% |

**13,781 domains are mail-reachable today** (18.3%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `mail.wabblywabble.com` | 634 | 688 |  |
| `mail.wallywatts.com` | 634 | 688 |  |
| `route2.mx.cloudflare.net` | 481 | 492 | yes |
| `route1.mx.cloudflare.net` | 480 | 491 | yes |
| `route3.mx.cloudflare.net` | 479 | 490 | yes |
| `mx4.beavis99.com` | 474 | 475 |  |
| `mx4.beavis99.net` | 474 | 475 |  |
| `generator.email` | 405 | 543 |  |
| `tinyhost.shop` | 324 | 324 |  |
| `mx.emlhub.com` | 276 | 276 |  |
| `park-mx.above.com` | 247 | 250 | yes |
| `emailfake.com` | 245 | 283 |  |
| `aspmx.l.google.com` | 227 | 229 | yes |
| `alt1.aspmx.l.google.com` | 223 | 225 | yes |
| `alt2.aspmx.l.google.com` | 218 | 220 | yes |
| `mx.spymail.one` | 211 | 211 |  |
| `email.chatgpt.org.uk` | 209 | 209 |  |
| `aero4.unstablemail.com` | 195 | 195 |  |
| `srv4.unstablemail.com` | 194 | 194 |  |
| `mx.emlpro.com` | 175 | 175 |  |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 634 | 688 |
| `mail.wallywatts.com` | 634 | 688 |
| `mx4.beavis99.com` | 474 | 475 |
| `mx4.beavis99.net` | 474 | 475 |
| `generator.email` | 405 | 543 |
| `tinyhost.shop` | 324 | 324 |
| `mx.emlhub.com` | 276 | 276 |
| `emailfake.com` | 245 | 283 |
| `mx.spymail.one` | 211 | 211 |
| `email.chatgpt.org.uk` | 209 | 209 |
| `aero4.unstablemail.com` | 195 | 195 |
| `srv4.unstablemail.com` | 194 | 194 |
| `mx.emlpro.com` | 175 | 175 |
| `email.gravityengine.cc` | 171 | 171 |
| `mx.emltmp.com` | 171 | 171 |
| `mx.dropmail.me` | 165 | 165 |
| `mx.freeml.net` | 156 | 156 |
| `mx37.m1bp.com` | 146 | 146 |
| `mx37.mb5p.com` | 146 | 146 |
| `mail.casadorock.com` | 123 | 123 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `78.47.124.133` | 1040 | 1040 |
| `94.130.108.80` | 1040 | 1040 |
| `91.196.52.205` | 553 | 730 |
| `142.132.166.12` | 494 | 542 |
| `188.166.111.252` | 494 | 542 |
| `116.202.9.167` | 478 | 525 |
| `46.101.111.206` | 478 | 525 |
| `13.223.25.84` | 403 | 403 |
| `54.243.117.197` | 403 | 403 |
| `162.159.205.23` | 384 | 393 |
| `162.159.205.24` | 384 | 393 |
| `162.159.205.25` | 384 | 393 |
| `162.159.205.17` | 382 | 392 |
| `162.159.205.18` | 382 | 392 |
| `162.159.205.19` | 382 | 392 |
| `162.159.205.11` | 364 | 373 |
| `162.159.205.12` | 364 | 373 |
| `162.159.205.13` | 364 | 373 |
| `188.245.74.208` | 335 | 336 |
| `195.201.18.63` | 332 | 333 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 210 |
| High-confidence disposable IPs | 426 |
| Promoted to `domains_inferred.txt` | 1 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**1620 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

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
| `12storage.com` | `park-mx.above.com` |
| `13dk.net` | `route1.mx.cloudflare.net` |
| `14n.co.uk` | `14n-co-uk.mail.protection.outlook.com` |
| `14p.in` | `eforward1.registrar-servers.com` |
| `15qm-mail.red` | `eforward1.registrar-servers.com` |
| `189.email` | `route1.mx.cloudflare.net` |
| `1987.com` | `park-mx.above.com` |


*… and 1,590 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
