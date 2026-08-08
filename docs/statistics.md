# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-08-08 02:53 UTC**.*  
*Last DNS snapshot: **2026-08-08T02:40:41+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 74,683 |
| `domains_strict.txt` | 74,714 |
| `domains_inferred.txt` (opt-in) | 1 |

## Reachability

Of **75,478** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 12,389 | 16.4% |
| A_ONLY | 2,066 | 2.7% |
| NXDOMAIN | 21,867 | 29.0% |
| NO_RECORDS | 310 | 0.4% |
| TIMEOUT | 38,846 | 51.5% |

**14,455 domains are mail-reachable today** (19.2%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `mail.wabblywabble.com` | 668 | 722 |  |
| `mail.wallywatts.com` | 668 | 722 |  |
| `route2.mx.cloudflare.net` | 509 | 518 | yes |
| `route1.mx.cloudflare.net` | 507 | 516 | yes |
| `route3.mx.cloudflare.net` | 507 | 516 | yes |
| `mx4.beavis99.com` | 501 | 502 |  |
| `mx4.beavis99.net` | 501 | 502 |  |
| `generator.email` | 430 | 567 |  |
| `tinyhost.shop` | 329 | 329 |  |
| `mx.emlhub.com` | 282 | 282 |  |
| `emailfake.com` | 261 | 297 |  |
| `park-mx.above.com` | 251 | 255 | yes |
| `aspmx.l.google.com` | 236 | 238 | yes |
| `alt1.aspmx.l.google.com` | 232 | 234 | yes |
| `alt2.aspmx.l.google.com` | 227 | 229 | yes |
| `mx.spymail.one` | 223 | 223 |  |
| `aero4.unstablemail.com` | 215 | 215 |  |
| `srv4.unstablemail.com` | 215 | 215 |  |
| `email.chatgpt.org.uk` | 203 | 203 |  |
| `email.gravityengine.cc` | 184 | 184 |  |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 668 | 722 |
| `mail.wallywatts.com` | 668 | 722 |
| `mx4.beavis99.com` | 501 | 502 |
| `mx4.beavis99.net` | 501 | 502 |
| `generator.email` | 430 | 567 |
| `tinyhost.shop` | 329 | 329 |
| `mx.emlhub.com` | 282 | 282 |
| `emailfake.com` | 261 | 297 |
| `mx.spymail.one` | 223 | 223 |
| `aero4.unstablemail.com` | 215 | 215 |
| `srv4.unstablemail.com` | 215 | 215 |
| `email.chatgpt.org.uk` | 203 | 203 |
| `email.gravityengine.cc` | 184 | 184 |
| `mx.emlpro.com` | 179 | 179 |
| `mx.emltmp.com` | 176 | 176 |
| `mx.dropmail.me` | 174 | 174 |
| `mx.freeml.net` | 164 | 164 |
| `mail.casadorock.com` | 159 | 159 |
| `mx37.m1bp.com` | 148 | 148 |
| `mx37.mb5p.com` | 148 | 148 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `78.47.124.133` | 1133 | 1133 |
| `94.130.108.80` | 1133 | 1133 |
| `91.196.52.205` | 599 | 775 |
| `142.132.166.12` | 531 | 579 |
| `188.166.111.252` | 531 | 579 |
| `116.202.9.167` | 516 | 563 |
| `46.101.111.206` | 516 | 563 |
| `13.223.25.84` | 426 | 426 |
| `54.243.117.197` | 426 | 426 |
| `162.159.205.23` | 415 | 422 |
| `162.159.205.24` | 415 | 422 |
| `162.159.205.25` | 415 | 422 |
| `162.159.205.17` | 412 | 420 |
| `162.159.205.18` | 412 | 420 |
| `162.159.205.19` | 412 | 420 |
| `162.159.205.11` | 393 | 400 |
| `162.159.205.12` | 393 | 400 |
| `162.159.205.13` | 393 | 400 |
| `188.245.74.208` | 364 | 365 |
| `195.201.18.63` | 361 | 362 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 206 |
| High-confidence disposable IPs | 442 |
| Promoted to `domains_inferred.txt` | 1 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**1694 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

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


*… and 1,664 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
