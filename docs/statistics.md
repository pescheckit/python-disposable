# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-08-02 03:32 UTC**.*  
*Last DNS snapshot: **2026-08-02T03:32:22+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 74,695 |
| `domains_strict.txt` | 74,726 |
| `domains_inferred.txt` (opt-in) | 0 |

## Reachability

Of **75,433** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 11,885 | 15.8% |
| A_ONLY | 1,949 | 2.6% |
| NXDOMAIN | 20,828 | 27.6% |
| NO_RECORDS | 281 | 0.4% |
| TIMEOUT | 40,490 | 53.7% |

**13,834 domains are mail-reachable today** (18.3%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `mail.wabblywabble.com` | 657 | 707 |  |
| `mail.wallywatts.com` | 657 | 707 |  |
| `route2.mx.cloudflare.net` | 507 | 518 | yes |
| `route1.mx.cloudflare.net` | 506 | 517 | yes |
| `route3.mx.cloudflare.net` | 505 | 516 | yes |
| `mx4.beavis99.com` | 479 | 480 |  |
| `mx4.beavis99.net` | 479 | 480 |  |
| `generator.email` | 450 | 583 |  |
| `tinyhost.shop` | 345 | 345 |  |
| `mx.emlhub.com` | 272 | 272 |  |
| `emailfake.com` | 260 | 296 |  |
| `park-mx.above.com` | 253 | 256 | yes |
| `alt1.aspmx.l.google.com` | 217 | 219 | yes |
| `aspmx.l.google.com` | 217 | 219 | yes |
| `aero4.unstablemail.com` | 214 | 214 |  |
| `srv4.unstablemail.com` | 213 | 213 |  |
| `alt2.aspmx.l.google.com` | 211 | 213 | yes |
| `email.chatgpt.org.uk` | 209 | 209 |  |
| `mx.spymail.one` | 189 | 189 |  |
| `eforward1.registrar-servers.com` | 181 | 184 | yes |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 657 | 707 |
| `mail.wallywatts.com` | 657 | 707 |
| `mx4.beavis99.com` | 479 | 480 |
| `mx4.beavis99.net` | 479 | 480 |
| `generator.email` | 450 | 583 |
| `tinyhost.shop` | 345 | 345 |
| `mx.emlhub.com` | 272 | 272 |
| `emailfake.com` | 260 | 296 |
| `aero4.unstablemail.com` | 214 | 214 |
| `srv4.unstablemail.com` | 213 | 213 |
| `email.chatgpt.org.uk` | 209 | 209 |
| `mx.spymail.one` | 189 | 189 |
| `email.gravityengine.cc` | 170 | 170 |
| `mx.emltmp.com` | 169 | 169 |
| `mx.dropmail.me` | 162 | 162 |
| `mx.emlpro.com` | 162 | 162 |
| `mx37.m1bp.com` | 143 | 143 |
| `mx37.mb5p.com` | 143 | 143 |
| `mail.casadorock.com` | 132 | 132 |
| `mx.freeml.net` | 130 | 130 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `78.47.124.133` | 982 | 982 |
| `94.130.108.80` | 982 | 982 |
| `91.196.52.205` | 592 | 763 |
| `142.132.166.12` | 498 | 542 |
| `188.166.111.252` | 498 | 542 |
| `116.202.9.167` | 485 | 528 |
| `46.101.111.206` | 485 | 528 |
| `162.159.205.23` | 403 | 412 |
| `162.159.205.24` | 403 | 412 |
| `162.159.205.25` | 403 | 412 |
| `162.159.205.17` | 400 | 410 |
| `162.159.205.18` | 400 | 410 |
| `162.159.205.19` | 400 | 410 |
| `162.159.205.11` | 394 | 403 |
| `162.159.205.12` | 394 | 403 |
| `162.159.205.13` | 394 | 403 |
| `13.223.25.84` | 385 | 385 |
| `54.243.117.197` | 385 | 385 |
| `188.245.74.208` | 349 | 350 |
| `195.201.18.63` | 336 | 337 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 202 |
| High-confidence disposable IPs | 417 |
| Promoted to `domains_inferred.txt` | 0 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**1649 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

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


*… and 1,619 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
