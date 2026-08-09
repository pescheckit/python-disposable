# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-08-09 02:59 UTC**.*  
*Last DNS snapshot: **2026-08-09T02:46:08+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 74,688 |
| `domains_strict.txt` | 74,719 |
| `domains_inferred.txt` (opt-in) | 1 |

## Reachability

Of **75,490** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 12,073 | 16.0% |
| A_ONLY | 1,965 | 2.6% |
| NXDOMAIN | 21,406 | 28.4% |
| NO_RECORDS | 302 | 0.4% |
| TIMEOUT | 39,744 | 52.6% |

**14,038 domains are mail-reachable today** (18.6%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `mail.wabblywabble.com` | 643 | 698 |  |
| `mail.wallywatts.com` | 643 | 698 |  |
| `route2.mx.cloudflare.net` | 501 | 510 | yes |
| `route1.mx.cloudflare.net` | 499 | 508 | yes |
| `route3.mx.cloudflare.net` | 499 | 508 | yes |
| `mx4.beavis99.com` | 487 | 488 |  |
| `mx4.beavis99.net` | 487 | 488 |  |
| `generator.email` | 403 | 540 |  |
| `tinyhost.shop` | 318 | 318 |  |
| `mx.emlhub.com` | 280 | 280 |  |
| `emailfake.com` | 257 | 293 |  |
| `park-mx.above.com` | 240 | 244 | yes |
| `aspmx.l.google.com` | 230 | 232 | yes |
| `alt1.aspmx.l.google.com` | 225 | 227 | yes |
| `mx.spymail.one` | 222 | 222 |  |
| `alt2.aspmx.l.google.com` | 220 | 222 | yes |
| `aero4.unstablemail.com` | 213 | 213 |  |
| `srv4.unstablemail.com` | 213 | 213 |  |
| `email.chatgpt.org.uk` | 180 | 180 |  |
| `email.gravityengine.cc` | 179 | 179 |  |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 643 | 698 |
| `mail.wallywatts.com` | 643 | 698 |
| `mx4.beavis99.com` | 487 | 488 |
| `mx4.beavis99.net` | 487 | 488 |
| `generator.email` | 403 | 540 |
| `tinyhost.shop` | 318 | 318 |
| `mx.emlhub.com` | 280 | 280 |
| `emailfake.com` | 257 | 293 |
| `mx.spymail.one` | 222 | 222 |
| `aero4.unstablemail.com` | 213 | 213 |
| `srv4.unstablemail.com` | 213 | 213 |
| `email.chatgpt.org.uk` | 180 | 180 |
| `email.gravityengine.cc` | 179 | 179 |
| `mx.emlpro.com` | 177 | 177 |
| `mx.emltmp.com` | 173 | 173 |
| `mx.dropmail.me` | 170 | 170 |
| `mx.freeml.net` | 163 | 163 |
| `mail.casadorock.com` | 157 | 157 |
| `mx37.m1bp.com` | 147 | 147 |
| `mx37.mb5p.com` | 147 | 147 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `78.47.124.133` | 1116 | 1116 |
| `94.130.108.80` | 1116 | 1116 |
| `91.196.52.205` | 560 | 737 |
| `142.132.166.12` | 506 | 555 |
| `188.166.111.252` | 506 | 555 |
| `116.202.9.167` | 490 | 538 |
| `46.101.111.206` | 490 | 538 |
| `162.159.205.23` | 407 | 414 |
| `162.159.205.24` | 407 | 414 |
| `162.159.205.25` | 407 | 414 |
| `162.159.205.17` | 403 | 411 |
| `162.159.205.18` | 403 | 411 |
| `162.159.205.19` | 403 | 411 |
| `13.223.25.84` | 399 | 399 |
| `54.243.117.197` | 399 | 399 |
| `162.159.205.11` | 384 | 391 |
| `162.159.205.12` | 384 | 391 |
| `162.159.205.13` | 384 | 391 |
| `188.245.74.208` | 351 | 352 |
| `195.201.18.63` | 348 | 349 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 204 |
| High-confidence disposable IPs | 438 |
| Promoted to `domains_inferred.txt` | 1 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**1646 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

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


*… and 1,616 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
