# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-08-17 02:36 UTC**.*  
*Last DNS snapshot: **2026-08-17T02:28:47+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 74,695 |
| `domains_strict.txt` | 74,726 |
| `domains_inferred.txt` (opt-in) | 0 |

## Reachability

Of **75,542** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 12,388 | 16.4% |
| A_ONLY | 2,067 | 2.7% |
| NXDOMAIN | 21,905 | 29.0% |
| NO_RECORDS | 298 | 0.4% |
| TIMEOUT | 38,884 | 51.5% |

**14,455 domains are mail-reachable today** (19.1%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `mail.wabblywabble.com` | 684 | 740 |  |
| `mail.wallywatts.com` | 684 | 740 |  |
| `route2.mx.cloudflare.net` | 536 | 545 | yes |
| `route1.mx.cloudflare.net` | 535 | 544 | yes |
| `route3.mx.cloudflare.net` | 535 | 544 | yes |
| `mx4.beavis99.com` | 523 | 524 |  |
| `mx4.beavis99.net` | 523 | 524 |  |
| `generator.email` | 456 | 592 |  |
| `tinyhost.shop` | 318 | 318 |  |
| `mx.emlhub.com` | 293 | 293 |  |
| `emailfake.com` | 272 | 309 |  |
| `park-mx.above.com` | 247 | 251 | yes |
| `aspmx.l.google.com` | 232 | 234 | yes |
| `alt1.aspmx.l.google.com` | 228 | 230 | yes |
| `aero4.unstablemail.com` | 223 | 223 |  |
| `alt2.aspmx.l.google.com` | 223 | 225 | yes |
| `srv4.unstablemail.com` | 223 | 223 |  |
| `mx.spymail.one` | 216 | 216 |  |
| `email.chatgpt.org.uk` | 199 | 199 |  |
| `mx.emlpro.com` | 196 | 196 |  |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 684 | 740 |
| `mail.wallywatts.com` | 684 | 740 |
| `mx4.beavis99.com` | 523 | 524 |
| `mx4.beavis99.net` | 523 | 524 |
| `generator.email` | 456 | 592 |
| `tinyhost.shop` | 318 | 318 |
| `mx.emlhub.com` | 293 | 293 |
| `emailfake.com` | 272 | 309 |
| `aero4.unstablemail.com` | 223 | 223 |
| `srv4.unstablemail.com` | 223 | 223 |
| `mx.spymail.one` | 216 | 216 |
| `email.chatgpt.org.uk` | 199 | 199 |
| `mx.emlpro.com` | 196 | 196 |
| `mx.emltmp.com` | 182 | 182 |
| `mx.dropmail.me` | 178 | 178 |
| `mail.casadorock.com` | 167 | 167 |
| `mx.freeml.net` | 158 | 158 |
| `email.gravityengine.cc` | 154 | 154 |
| `mx37.m1bp.com` | 151 | 151 |
| `mx37.mb5p.com` | 151 | 151 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `78.47.124.133` | 1123 | 1123 |
| `94.130.108.80` | 1123 | 1123 |
| `91.196.52.205` | 635 | 808 |
| `116.202.9.167` | 530 | 579 |
| `46.101.111.206` | 530 | 579 |
| `142.132.166.12` | 524 | 574 |
| `188.166.111.252` | 524 | 574 |
| `162.159.205.23` | 450 | 457 |
| `162.159.205.24` | 450 | 457 |
| `162.159.205.25` | 450 | 457 |
| `162.159.205.17` | 435 | 443 |
| `162.159.205.18` | 435 | 443 |
| `162.159.205.19` | 435 | 443 |
| `162.159.205.11` | 428 | 435 |
| `162.159.205.12` | 428 | 435 |
| `162.159.205.13` | 428 | 435 |
| `13.223.25.84` | 391 | 391 |
| `54.243.117.197` | 391 | 391 |
| `188.245.74.208` | 378 | 379 |
| `195.201.18.63` | 345 | 346 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 216 |
| High-confidence disposable IPs | 439 |
| Promoted to `domains_inferred.txt` | 0 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**1702 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

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


*… and 1,672 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
