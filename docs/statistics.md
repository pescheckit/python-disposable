# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-07-31 03:23 UTC**.*  
*Last DNS snapshot: **2026-07-31T03:09:27+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 74,660 |
| `domains_strict.txt` | 74,691 |
| `domains_inferred.txt` (opt-in) | 0 |

## Reachability

Of **75,398** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 11,514 | 15.3% |
| A_ONLY | 1,871 | 2.5% |
| NXDOMAIN | 20,037 | 26.6% |
| NO_RECORDS | 293 | 0.4% |
| TIMEOUT | 41,683 | 55.3% |

**13,385 domains are mail-reachable today** (17.8%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `mail.wabblywabble.com` | 632 | 680 |  |
| `mail.wallywatts.com` | 632 | 680 |  |
| `route2.mx.cloudflare.net` | 501 | 511 | yes |
| `route1.mx.cloudflare.net` | 500 | 510 | yes |
| `route3.mx.cloudflare.net` | 500 | 510 | yes |
| `mx4.beavis99.com` | 475 | 476 |  |
| `mx4.beavis99.net` | 475 | 476 |  |
| `generator.email` | 403 | 539 |  |
| `tinyhost.shop` | 336 | 336 |  |
| `mx.emlhub.com` | 261 | 261 |  |
| `emailfake.com` | 258 | 299 |  |
| `park-mx.above.com` | 248 | 251 | yes |
| `aspmx.l.google.com` | 221 | 223 | yes |
| `alt1.aspmx.l.google.com` | 220 | 222 | yes |
| `alt2.aspmx.l.google.com` | 216 | 218 | yes |
| `aero4.unstablemail.com` | 196 | 196 |  |
| `srv4.unstablemail.com` | 195 | 195 |  |
| `email.chatgpt.org.uk` | 185 | 185 |  |
| `eforward1.registrar-servers.com` | 177 | 180 | yes |
| `eforward2.registrar-servers.com` | 177 | 180 | yes |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 632 | 680 |
| `mail.wallywatts.com` | 632 | 680 |
| `mx4.beavis99.com` | 475 | 476 |
| `mx4.beavis99.net` | 475 | 476 |
| `generator.email` | 403 | 539 |
| `tinyhost.shop` | 336 | 336 |
| `mx.emlhub.com` | 261 | 261 |
| `emailfake.com` | 258 | 299 |
| `aero4.unstablemail.com` | 196 | 196 |
| `srv4.unstablemail.com` | 195 | 195 |
| `email.chatgpt.org.uk` | 185 | 185 |
| `email.gravityengine.cc` | 175 | 175 |
| `mx.emltmp.com` | 168 | 168 |
| `mx.spymail.one` | 154 | 154 |
| `mx.emlpro.com` | 147 | 147 |
| `mx.dropmail.me` | 145 | 145 |
| `mx37.m1bp.com` | 136 | 136 |
| `mx37.mb5p.com` | 136 | 136 |
| `mx.freeml.net` | 121 | 121 |
| `mx.yomail.info` | 108 | 108 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `78.47.124.133` | 855 | 855 |
| `94.130.108.80` | 855 | 855 |
| `91.196.52.205` | 547 | 728 |
| `142.132.166.12` | 466 | 508 |
| `188.166.111.252` | 466 | 508 |
| `116.202.9.167` | 449 | 490 |
| `46.101.111.206` | 449 | 490 |
| `162.159.205.23` | 393 | 401 |
| `162.159.205.24` | 393 | 401 |
| `162.159.205.25` | 393 | 401 |
| `162.159.205.17` | 391 | 400 |
| `162.159.205.18` | 391 | 400 |
| `162.159.205.19` | 391 | 400 |
| `162.159.205.11` | 382 | 390 |
| `162.159.205.12` | 382 | 390 |
| `162.159.205.13` | 382 | 390 |
| `13.223.25.84` | 378 | 378 |
| `54.243.117.197` | 378 | 378 |
| `188.245.74.208` | 355 | 356 |
| `195.201.18.63` | 340 | 341 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 201 |
| High-confidence disposable IPs | 418 |
| Promoted to `domains_inferred.txt` | 0 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**1623 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

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


*… and 1,593 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
