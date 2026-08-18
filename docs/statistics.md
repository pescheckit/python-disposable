# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-08-18 02:45 UTC**.*  
*Last DNS snapshot: **2026-08-18T02:45:49+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 74,691 |
| `domains_strict.txt` | 74,722 |
| `domains_inferred.txt` (opt-in) | 2 |

## Reachability

Of **75,547** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 14,524 | 19.2% |
| A_ONLY | 2,666 | 3.5% |
| NXDOMAIN | 25,453 | 33.7% |
| NO_RECORDS | 397 | 0.5% |
| TIMEOUT | 32,507 | 43.0% |

**17,190 domains are mail-reachable today** (22.8%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `mail.wabblywabble.com` | 818 | 874 |  |
| `mail.wallywatts.com` | 818 | 874 |  |
| `route2.mx.cloudflare.net` | 624 | 633 | yes |
| `route1.mx.cloudflare.net` | 623 | 632 | yes |
| `route3.mx.cloudflare.net` | 623 | 632 | yes |
| `mx4.beavis99.com` | 599 | 600 |  |
| `mx4.beavis99.net` | 599 | 600 |  |
| `generator.email` | 518 | 654 |  |
| `email.gravityengine.cc` | 409 | 409 |  |
| `email.chatgpt.org.uk` | 338 | 338 |  |
| `tinyhost.shop` | 321 | 321 |  |
| `emailfake.com` | 319 | 356 |  |
| `mx.emlhub.com` | 313 | 313 |  |
| `aspmx.l.google.com` | 292 | 294 | yes |
| `alt1.aspmx.l.google.com` | 288 | 290 | yes |
| `park-mx.above.com` | 287 | 291 | yes |
| `alt2.aspmx.l.google.com` | 283 | 285 | yes |
| `aero4.unstablemail.com` | 272 | 272 |  |
| `srv4.unstablemail.com` | 272 | 272 |  |
| `mx.spymail.one` | 237 | 237 |  |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 818 | 874 |
| `mail.wallywatts.com` | 818 | 874 |
| `mx4.beavis99.com` | 599 | 600 |
| `mx4.beavis99.net` | 599 | 600 |
| `generator.email` | 518 | 654 |
| `email.gravityengine.cc` | 409 | 409 |
| `email.chatgpt.org.uk` | 338 | 338 |
| `tinyhost.shop` | 321 | 321 |
| `emailfake.com` | 319 | 356 |
| `mx.emlhub.com` | 313 | 313 |
| `aero4.unstablemail.com` | 272 | 272 |
| `srv4.unstablemail.com` | 272 | 272 |
| `mx.spymail.one` | 237 | 237 |
| `mx.emlpro.com` | 211 | 211 |
| `mx.dropmail.me` | 203 | 203 |
| `mx.emltmp.com` | 200 | 200 |
| `mail.casadorock.com` | 183 | 183 |
| `mx.freeml.net` | 175 | 175 |
| `mx37.m1bp.com` | 158 | 158 |
| `mx37.mb5p.com` | 158 | 158 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `78.47.124.133` | 1286 | 1286 |
| `94.130.108.80` | 1286 | 1286 |
| `91.196.52.205` | 750 | 923 |
| `116.202.9.167` | 669 | 718 |
| `46.101.111.206` | 669 | 718 |
| `142.132.166.12` | 662 | 712 |
| `188.166.111.252` | 662 | 712 |
| `162.159.205.23` | 555 | 562 |
| `162.159.205.24` | 555 | 562 |
| `162.159.205.25` | 555 | 562 |
| `162.159.205.17` | 539 | 547 |
| `162.159.205.18` | 539 | 547 |
| `162.159.205.19` | 539 | 547 |
| `162.159.205.11` | 532 | 539 |
| `162.159.205.12` | 532 | 539 |
| `162.159.205.13` | 532 | 539 |
| `13.223.25.84` | 527 | 527 |
| `54.243.117.197` | 527 | 527 |
| `138.226.240.26` | 520 | 520 |
| `188.245.74.208` | 464 | 465 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 233 |
| High-confidence disposable IPs | 544 |
| Promoted to `domains_inferred.txt` | 2 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**1999 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

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


*… and 1,969 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
