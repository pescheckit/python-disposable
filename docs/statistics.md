# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-07-25 03:35 UTC**.*  
*Last DNS snapshot: **2026-07-25T03:35:30+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 74,615 |
| `domains_strict.txt` | 74,646 |
| `domains_inferred.txt` (opt-in) | 0 |

## Reachability

Of **75,319** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 11,770 | 15.6% |
| A_ONLY | 1,870 | 2.5% |
| NXDOMAIN | 19,456 | 25.8% |
| NO_RECORDS | 259 | 0.3% |
| TIMEOUT | 41,964 | 55.7% |

**13,640 domains are mail-reachable today** (18.1%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `mail.wabblywabble.com` | 626 | 672 |  |
| `mail.wallywatts.com` | 626 | 672 |  |
| `mx4.beavis99.com` | 568 | 569 |  |
| `mx4.beavis99.net` | 568 | 569 |  |
| `route1.mx.cloudflare.net` | 483 | 492 | yes |
| `route2.mx.cloudflare.net` | 483 | 492 | yes |
| `route3.mx.cloudflare.net` | 482 | 491 | yes |
| `generator.email` | 370 | 505 |  |
| `tinyhost.shop` | 326 | 326 |  |
| `park-mx.above.com` | 304 | 306 | yes |
| `mx.emlhub.com` | 234 | 234 |  |
| `aspmx.l.google.com` | 218 | 220 | yes |
| `alt1.aspmx.l.google.com` | 212 | 214 | yes |
| `alt2.aspmx.l.google.com` | 211 | 213 | yes |
| `aero4.unstablemail.com` | 209 | 209 |  |
| `srv4.unstablemail.com` | 208 | 208 |  |
| `emailfake.com` | 202 | 243 |  |
| `email.gravityengine.cc` | 181 | 181 |  |
| `mx.emltmp.com` | 178 | 178 |  |
| `eforward1.registrar-servers.com` | 177 | 180 | yes |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 626 | 672 |
| `mail.wallywatts.com` | 626 | 672 |
| `mx4.beavis99.com` | 568 | 569 |
| `mx4.beavis99.net` | 568 | 569 |
| `generator.email` | 370 | 505 |
| `tinyhost.shop` | 326 | 326 |
| `mx.emlhub.com` | 234 | 234 |
| `aero4.unstablemail.com` | 209 | 209 |
| `srv4.unstablemail.com` | 208 | 208 |
| `emailfake.com` | 202 | 243 |
| `email.gravityengine.cc` | 181 | 181 |
| `mx.emltmp.com` | 178 | 178 |
| `mx.emlpro.com` | 163 | 163 |
| `mx.spymail.one` | 154 | 154 |
| `email.chatgpt.org.uk` | 148 | 148 |
| `mx.dropmail.me` | 147 | 147 |
| `mail.casadorock.com` | 143 | 143 |
| `mx37.m1bp.com` | 139 | 139 |
| `mx37.mb5p.com` | 139 | 139 |
| `mx.freeml.net` | 138 | 138 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `78.47.124.133` | 909 | 909 |
| `94.130.108.80` | 909 | 909 |
| `116.202.9.167` | 470 | 510 |
| `46.101.111.206` | 470 | 510 |
| `142.132.166.12` | 461 | 501 |
| `188.166.111.252` | 461 | 501 |
| `91.196.52.205` | 445 | 626 |
| `188.245.74.208` | 440 | 441 |
| `195.201.18.63` | 422 | 423 |
| `162.159.205.11` | 366 | 374 |
| `162.159.205.12` | 366 | 374 |
| `162.159.205.13` | 366 | 374 |
| `13.223.25.84` | 365 | 365 |
| `54.243.117.197` | 365 | 365 |
| `162.159.205.23` | 363 | 371 |
| `162.159.205.24` | 363 | 371 |
| `162.159.205.25` | 363 | 371 |
| `162.159.205.17` | 361 | 369 |
| `162.159.205.18` | 361 | 369 |
| `162.159.205.19` | 361 | 369 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 204 |
| High-confidence disposable IPs | 427 |
| Promoted to `domains_inferred.txt` | 0 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**1687 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

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
| `13dk.net` | `route1.mx.cloudflare.net` |
| `14n.co.uk` | `14n-co-uk.mail.protection.outlook.com` |
| `14p.in` | `eforward1.registrar-servers.com` |
| `15qm-mail.red` | `eforward1.registrar-servers.com` |
| `189.email` | `route1.mx.cloudflare.net` |
| `1987.com` | `park-mx.above.com` |
| `1ayj8yi7lpiksxawav.gq` | `route1.mx.cloudflare.net` |


*… and 1,657 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
