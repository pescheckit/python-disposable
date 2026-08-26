# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-08-26 02:51 UTC**.*  
*Last DNS snapshot: **2026-08-26T02:34:00+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 74,878 |
| `domains_strict.txt` | 74,909 |
| `domains_inferred.txt` (opt-in) | 0 |

## Reachability

Of **75,767** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 13,364 | 17.6% |
| A_ONLY | 2,400 | 3.2% |
| NXDOMAIN | 23,100 | 30.5% |
| NO_RECORDS | 398 | 0.5% |
| TIMEOUT | 36,505 | 48.2% |

**15,764 domains are mail-reachable today** (20.8%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `mail.wabblywabble.com` | 740 | 799 |  |
| `mail.wallywatts.com` | 740 | 799 |  |
| `mx4.beavis99.com` | 622 | 623 |  |
| `mx4.beavis99.net` | 622 | 623 |  |
| `route2.mx.cloudflare.net` | 536 | 546 | yes |
| `route3.mx.cloudflare.net` | 536 | 546 | yes |
| `route1.mx.cloudflare.net` | 535 | 545 | yes |
| `generator.email` | 426 | 561 |  |
| `email.gravityengine.cc` | 368 | 368 |  |
| `email.chatgpt.org.uk` | 324 | 324 |  |
| `tinyhost.shop` | 316 | 316 |  |
| `mx.emlhub.com` | 292 | 292 |  |
| `park-mx.above.com` | 270 | 274 | yes |
| `emailfake.com` | 265 | 302 |  |
| `aspmx.l.google.com` | 255 | 257 | yes |
| `aero4.unstablemail.com` | 251 | 251 |  |
| `srv4.unstablemail.com` | 251 | 251 |  |
| `alt1.aspmx.l.google.com` | 249 | 251 | yes |
| `alt2.aspmx.l.google.com` | 247 | 249 | yes |
| `mx.spymail.one` | 216 | 216 |  |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 740 | 799 |
| `mail.wallywatts.com` | 740 | 799 |
| `mx4.beavis99.com` | 622 | 623 |
| `mx4.beavis99.net` | 622 | 623 |
| `generator.email` | 426 | 561 |
| `email.gravityengine.cc` | 368 | 368 |
| `email.chatgpt.org.uk` | 324 | 324 |
| `tinyhost.shop` | 316 | 316 |
| `mx.emlhub.com` | 292 | 292 |
| `emailfake.com` | 265 | 302 |
| `aero4.unstablemail.com` | 251 | 251 |
| `srv4.unstablemail.com` | 251 | 251 |
| `mx.spymail.one` | 216 | 216 |
| `mx.emltmp.com` | 187 | 187 |
| `mx.emlpro.com` | 177 | 177 |
| `mx.freeml.net` | 172 | 172 |
| `mx.dropmail.me` | 168 | 168 |
| `mail.casadorock.com` | 143 | 143 |
| `mx37.m1bp.com` | 136 | 136 |
| `mx37.mb5p.com` | 136 | 136 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `78.47.124.133` | 1172 | 1172 |
| `94.130.108.80` | 1172 | 1172 |
| `138.226.240.26` | 668 | 668 |
| `116.202.9.167` | 609 | 659 |
| `46.101.111.206` | 609 | 659 |
| `142.132.166.12` | 596 | 647 |
| `188.166.111.252` | 596 | 647 |
| `91.196.52.205` | 592 | 764 |
| `13.223.25.84` | 486 | 486 |
| `54.243.117.197` | 486 | 486 |
| `162.159.205.23` | 459 | 467 |
| `162.159.205.24` | 459 | 467 |
| `162.159.205.25` | 459 | 467 |
| `162.159.205.17` | 455 | 464 |
| `162.159.205.18` | 455 | 464 |
| `162.159.205.19` | 455 | 464 |
| `188.245.74.208` | 445 | 446 |
| `162.159.205.11` | 442 | 450 |
| `162.159.205.12` | 442 | 450 |
| `162.159.205.13` | 442 | 450 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 215 |
| High-confidence disposable IPs | 475 |
| Promoted to `domains_inferred.txt` | 0 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**1799 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

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


*… and 1,769 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
