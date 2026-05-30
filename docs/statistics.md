# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-05-30 03:23 UTC**.*  
*Last DNS snapshot: **2026-05-30T03:12:10+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 72,292 |
| `domains_strict.txt` | 72,323 |
| `domains_inferred.txt` (opt-in) | 1 |

## Reachability

Of **72,735** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 10,663 | 14.7% |
| A_ONLY | 1,598 | 2.2% |
| NXDOMAIN | 19,410 | 26.7% |
| NO_RECORDS | 242 | 0.3% |
| TIMEOUT | 40,822 | 56.1% |

**12,261 domains are mail-reachable today** (16.9%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `mail.wabblywabble.com` | 686 | 699 |  |
| `mail.wallywatts.com` | 686 | 699 |  |
| `mx4.beavis99.com` | 475 | 475 |  |
| `mx4.beavis99.net` | 475 | 475 |  |
| `generator.email` | 420 | 564 |  |
| `route1.mx.cloudflare.net` | 360 | 364 | yes |
| `route2.mx.cloudflare.net` | 360 | 364 | yes |
| `route3.mx.cloudflare.net` | 360 | 364 | yes |
| `park-mx.above.com` | 274 | 275 | yes |
| `emailfake.com` | 240 | 284 |  |
| `mx.emlhub.com` | 228 | 228 |  |
| `aspmx.l.google.com` | 226 | 226 | yes |
| `alt1.aspmx.l.google.com` | 219 | 219 | yes |
| `alt2.aspmx.l.google.com` | 217 | 217 | yes |
| `aero4.unstablemail.com` | 199 | 199 |  |
| `srv4.unstablemail.com` | 198 | 198 |  |
| `eforward1.registrar-servers.com` | 177 | 178 | yes |
| `eforward2.registrar-servers.com` | 177 | 178 | yes |
| `eforward3.registrar-servers.com` | 177 | 178 | yes |
| `eforward4.registrar-servers.com` | 177 | 178 | yes |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 686 | 699 |
| `mail.wallywatts.com` | 686 | 699 |
| `mx4.beavis99.com` | 475 | 475 |
| `mx4.beavis99.net` | 475 | 475 |
| `generator.email` | 420 | 564 |
| `emailfake.com` | 240 | 284 |
| `mx.emlhub.com` | 228 | 228 |
| `aero4.unstablemail.com` | 199 | 199 |
| `srv4.unstablemail.com` | 198 | 198 |
| `mx.emlpro.com` | 168 | 168 |
| `mx.spymail.one` | 168 | 168 |
| `mx.emltmp.com` | 158 | 158 |
| `mx37.m1bp.com` | 142 | 142 |
| `mx37.mb5p.com` | 142 | 142 |
| `mx.dropmail.me` | 140 | 140 |
| `mx.freeml.net` | 134 | 134 |
| `mail.casadorock.com` | 122 | 122 |
| `mx.yomail.info` | 122 | 122 |
| `localhost` | 103 | 103 |
| `mail.h-email.net` | 103 | 103 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `78.47.124.133` | 777 | 777 |
| `94.130.108.80` | 777 | 777 |
| `91.196.52.205` | 509 | 698 |
| `142.132.166.12` | 480 | 493 |
| `188.166.111.252` | 480 | 493 |
| `116.202.9.167` | 465 | 477 |
| `46.101.111.206` | 465 | 477 |
| `13.223.25.84` | 310 | 310 |
| `54.243.117.197` | 310 | 310 |
| `188.245.74.208` | 309 | 309 |
| `195.201.18.63` | 296 | 296 |
| `147.182.130.78` | 272 | 273 |
| `147.182.160.18` | 272 | 273 |
| `147.182.180.139` | 272 | 273 |
| `147.182.189.184` | 272 | 273 |
| `164.90.197.105` | 272 | 273 |
| `164.90.197.143` | 272 | 273 |
| `164.90.197.162` | 272 | 273 |
| `164.90.197.79` | 272 | 273 |
| `162.159.205.23` | 249 | 252 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 206 |
| High-confidence disposable IPs | 356 |
| Promoted to `domains_inferred.txt` | 1 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**1512 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

| Listed disposable | MX (shared infra) |
|---|---|
| `0-30-24.com` | `alt1.aspmx.l.google.com` |
| `0-mail.com` | `park-mx.above.com` |
| `0058.ru` | `alt1.aspmx.l.google.com` |
| `01g.cloud` | `alt1.aspmx.l.google.com` |
| `0ak.org` | `mx00.ionos.com` |
| `0celot.com` | `alt1.aspmx.l.google.com` |
| `0hcow.com` | `mxa.mailgun.org` |
| `0hio.net` | `aspmx1.migadu.com` |
| `0ioi.net` | `route1.mx.cloudflare.net` |
| `0live.org` | `route1.mx.cloudflare.net` |
| `0nce.net` | `route1.mx.cloudflare.net` |
| `0ne0ut.com` | `route1.mx.cloudflare.net` |
| `0rg.fr` | `mx1.mail.ovh.net` |
| `0xmiikee.com` | `eforward1.registrar-servers.com` |
| `1-8.biz` | `mail.protonmail.ch` |
| `1-box.ru` | `mx.yandex.ru` |
| `10bir.com` | `route1.mx.cloudflare.net` |
| `10dkmail.net` | `smtp.google.com` |
| `10inbox.online` | `route1.mx.cloudflare.net` |
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


*… and 1,482 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
