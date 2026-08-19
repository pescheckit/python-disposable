# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-08-19 03:49 UTC**.*  
*Last DNS snapshot: **2026-08-19T03:29:38+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 74,754 |
| `domains_strict.txt` | 74,785 |
| `domains_inferred.txt` (opt-in) | 2 |

## Reachability

Of **75,614** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 14,522 | 19.2% |
| A_ONLY | 2,674 | 3.5% |
| NXDOMAIN | 25,460 | 33.7% |
| NO_RECORDS | 405 | 0.5% |
| TIMEOUT | 32,553 | 43.1% |

**17,196 domains are mail-reachable today** (22.7%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `mail.wabblywabble.com` | 811 | 867 |  |
| `mail.wallywatts.com` | 811 | 867 |  |
| `mx4.beavis99.com` | 641 | 642 |  |
| `mx4.beavis99.net` | 641 | 642 |  |
| `route2.mx.cloudflare.net` | 602 | 611 | yes |
| `route1.mx.cloudflare.net` | 601 | 610 | yes |
| `route3.mx.cloudflare.net` | 601 | 610 | yes |
| `generator.email` | 508 | 644 |  |
| `email.gravityengine.cc` | 411 | 411 |  |
| `email.chatgpt.org.uk` | 364 | 364 |  |
| `tinyhost.shop` | 332 | 332 |  |
| `mx.emlhub.com` | 321 | 321 |  |
| `emailfake.com` | 310 | 347 |  |
| `park-mx.above.com` | 290 | 294 | yes |
| `aspmx.l.google.com` | 276 | 278 | yes |
| `aero4.unstablemail.com` | 272 | 272 |  |
| `srv4.unstablemail.com` | 272 | 272 |  |
| `alt1.aspmx.l.google.com` | 271 | 273 | yes |
| `alt2.aspmx.l.google.com` | 267 | 269 | yes |
| `mx.spymail.one` | 226 | 226 |  |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 811 | 867 |
| `mail.wallywatts.com` | 811 | 867 |
| `mx4.beavis99.com` | 641 | 642 |
| `mx4.beavis99.net` | 641 | 642 |
| `generator.email` | 508 | 644 |
| `email.gravityengine.cc` | 411 | 411 |
| `email.chatgpt.org.uk` | 364 | 364 |
| `tinyhost.shop` | 332 | 332 |
| `mx.emlhub.com` | 321 | 321 |
| `emailfake.com` | 310 | 347 |
| `aero4.unstablemail.com` | 272 | 272 |
| `srv4.unstablemail.com` | 272 | 272 |
| `mx.spymail.one` | 226 | 226 |
| `mx.emlpro.com` | 189 | 189 |
| `mx.emltmp.com` | 189 | 189 |
| `mx.dropmail.me` | 188 | 188 |
| `mail.casadorock.com` | 183 | 183 |
| `mx.freeml.net` | 171 | 171 |
| `mx37.m1bp.com` | 155 | 155 |
| `mx37.mb5p.com` | 155 | 155 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `78.47.124.133` | 1297 | 1297 |
| `94.130.108.80` | 1297 | 1297 |
| `91.196.52.205` | 742 | 915 |
| `116.202.9.167` | 677 | 726 |
| `46.101.111.206` | 677 | 726 |
| `142.132.166.12` | 663 | 713 |
| `188.166.111.252` | 663 | 713 |
| `13.223.25.84` | 554 | 554 |
| `54.243.117.197` | 554 | 554 |
| `138.226.240.26` | 553 | 553 |
| `162.159.205.23` | 531 | 538 |
| `162.159.205.24` | 531 | 538 |
| `162.159.205.25` | 531 | 538 |
| `162.159.205.17` | 527 | 535 |
| `162.159.205.18` | 527 | 535 |
| `162.159.205.19` | 527 | 535 |
| `162.159.205.11` | 515 | 522 |
| `162.159.205.12` | 515 | 522 |
| `162.159.205.13` | 515 | 522 |
| `188.245.74.208` | 474 | 475 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 231 |
| High-confidence disposable IPs | 535 |
| Promoted to `domains_inferred.txt` | 2 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**1967 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

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


*… and 1,937 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
