# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-08-28 05:00 UTC**.*  
*Last DNS snapshot: **2026-08-28T04:43:57+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 74,896 |
| `domains_strict.txt` | 74,927 |
| `domains_inferred.txt` (opt-in) | 0 |

## Reachability

Of **75,795** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 13,293 | 17.5% |
| A_ONLY | 2,440 | 3.2% |
| NXDOMAIN | 23,002 | 30.3% |
| NO_RECORDS | 339 | 0.4% |
| TIMEOUT | 36,721 | 48.4% |

**15,733 domains are mail-reachable today** (20.8%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `mail.wabblywabble.com` | 739 | 798 |  |
| `mail.wallywatts.com` | 739 | 798 |  |
| `mx4.beavis99.com` | 612 | 613 |  |
| `mx4.beavis99.net` | 612 | 613 |  |
| `route2.mx.cloudflare.net` | 501 | 511 | yes |
| `route1.mx.cloudflare.net` | 500 | 510 | yes |
| `route3.mx.cloudflare.net` | 500 | 510 | yes |
| `generator.email` | 397 | 533 |  |
| `email.gravityengine.cc` | 362 | 362 |  |
| `email.chatgpt.org.uk` | 306 | 306 |  |
| `park-mx.above.com` | 284 | 288 | yes |
| `mx.emlhub.com` | 258 | 258 |  |
| `aero4.unstablemail.com` | 255 | 255 |  |
| `srv4.unstablemail.com` | 255 | 255 |  |
| `aspmx.l.google.com` | 242 | 244 | yes |
| `alt1.aspmx.l.google.com` | 239 | 241 | yes |
| `alt2.aspmx.l.google.com` | 237 | 239 | yes |
| `emailfake.com` | 236 | 273 |  |
| `mx.spymail.one` | 220 | 220 |  |
| `tinyhost.shop` | 217 | 217 |  |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 739 | 798 |
| `mail.wallywatts.com` | 739 | 798 |
| `mx4.beavis99.com` | 612 | 613 |
| `mx4.beavis99.net` | 612 | 613 |
| `generator.email` | 397 | 533 |
| `email.gravityengine.cc` | 362 | 362 |
| `email.chatgpt.org.uk` | 306 | 306 |
| `mx.emlhub.com` | 258 | 258 |
| `aero4.unstablemail.com` | 255 | 255 |
| `srv4.unstablemail.com` | 255 | 255 |
| `emailfake.com` | 236 | 273 |
| `mx.spymail.one` | 220 | 220 |
| `tinyhost.shop` | 217 | 217 |
| `mx.emltmp.com` | 192 | 192 |
| `mx.emlpro.com` | 187 | 187 |
| `mx.freeml.net` | 163 | 163 |
| `mx.dropmail.me` | 159 | 159 |
| `mx37.m1bp.com` | 144 | 144 |
| `mx37.mb5p.com` | 144 | 144 |
| `mail.casadorock.com` | 137 | 137 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `78.47.124.133` | 1111 | 1111 |
| `94.130.108.80` | 1111 | 1111 |
| `138.226.240.26` | 645 | 645 |
| `142.132.166.12` | 620 | 671 |
| `188.166.111.252` | 620 | 671 |
| `116.202.9.167` | 618 | 668 |
| `46.101.111.206` | 618 | 668 |
| `91.196.52.205` | 533 | 706 |
| `188.245.74.208` | 486 | 487 |
| `13.223.25.84` | 485 | 485 |
| `54.243.117.197` | 485 | 485 |
| `195.201.18.63` | 471 | 472 |
| `162.159.205.17` | 435 | 444 |
| `162.159.205.18` | 435 | 444 |
| `162.159.205.19` | 435 | 444 |
| `162.159.205.23` | 429 | 437 |
| `162.159.205.24` | 429 | 437 |
| `162.159.205.25` | 429 | 437 |
| `162.159.205.11` | 424 | 432 |
| `162.159.205.12` | 424 | 432 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 235 |
| High-confidence disposable IPs | 494 |
| Promoted to `domains_inferred.txt` | 0 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**1751 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

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


*… and 1,721 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
