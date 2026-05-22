# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-05-22 04:14 UTC**.*  
*Last DNS snapshot: **2026-05-22T03:12:58+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 72,280 |
| `domains_strict.txt` | 72,311 |
| `domains_inferred.txt` (opt-in) | 1 |

## Reachability

Of **72,639** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 10,993 | 15.1% |
| A_ONLY | 1,472 | 2.0% |
| NXDOMAIN | 19,583 | 27.0% |
| NO_RECORDS | 232 | 0.3% |
| TIMEOUT | 40,359 | 55.6% |

**12,465 domains are mail-reachable today** (17.2%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `mail.wabblywabble.com` | 713 | 725 |  |
| `mail.wallywatts.com` | 713 | 725 |  |
| `generator.email` | 480 | 599 |  |
| `mx4.beavis99.com` | 464 | 464 |  |
| `mx4.beavis99.net` | 464 | 464 |  |
| `route1.mx.cloudflare.net` | 380 | 384 | yes |
| `route2.mx.cloudflare.net` | 380 | 384 | yes |
| `route3.mx.cloudflare.net` | 379 | 383 | yes |
| `park-mx.above.com` | 276 | 276 | yes |
| `emailfake.com` | 236 | 274 |  |
| `aspmx.l.google.com` | 209 | 209 | yes |
| `mx.spymail.one` | 208 | 208 |  |
| `alt1.aspmx.l.google.com` | 205 | 205 | yes |
| `alt2.aspmx.l.google.com` | 204 | 204 | yes |
| `mx.emlhub.com` | 204 | 204 |  |
| `mx.emlpro.com` | 201 | 201 |  |
| `aero4.unstablemail.com` | 199 | 199 |  |
| `srv4.unstablemail.com` | 199 | 199 |  |
| `mx.emltmp.com` | 196 | 196 |  |
| `eforward1.registrar-servers.com` | 185 | 186 | yes |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 713 | 725 |
| `mail.wallywatts.com` | 713 | 725 |
| `generator.email` | 480 | 599 |
| `mx4.beavis99.com` | 464 | 464 |
| `mx4.beavis99.net` | 464 | 464 |
| `emailfake.com` | 236 | 274 |
| `mx.spymail.one` | 208 | 208 |
| `mx.emlhub.com` | 204 | 204 |
| `mx.emlpro.com` | 201 | 201 |
| `aero4.unstablemail.com` | 199 | 199 |
| `srv4.unstablemail.com` | 199 | 199 |
| `mx.emltmp.com` | 196 | 196 |
| `mx.dropmail.me` | 158 | 158 |
| `mx.freeml.net` | 157 | 157 |
| `mx37.m1bp.com` | 144 | 144 |
| `mx37.mb5p.com` | 144 | 144 |
| `mail.casadorock.com` | 127 | 127 |
| `mail.mailerhost.net` | 124 | 124 |
| `mail.h-email.net` | 122 | 122 |
| `mail.mailinator.com` | 115 | 115 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `78.47.124.133` | 921 | 921 |
| `94.130.108.80` | 921 | 921 |
| `91.196.52.205` | 556 | 717 |
| `116.202.9.167` | 439 | 450 |
| `46.101.111.206` | 439 | 450 |
| `142.132.166.12` | 438 | 450 |
| `188.166.111.252` | 438 | 450 |
| `188.245.74.208` | 298 | 298 |
| `147.182.130.78` | 281 | 282 |
| `147.182.160.18` | 281 | 282 |
| `147.182.180.139` | 281 | 282 |
| `147.182.189.184` | 281 | 282 |
| `164.90.197.105` | 281 | 282 |
| `164.90.197.143` | 281 | 282 |
| `164.90.197.162` | 281 | 282 |
| `164.90.197.79` | 281 | 282 |
| `195.201.18.63` | 272 | 272 |
| `162.159.205.23` | 270 | 273 |
| `162.159.205.24` | 270 | 273 |
| `162.159.205.25` | 270 | 273 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 192 |
| High-confidence disposable IPs | 401 |
| Promoted to `domains_inferred.txt` | 1 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**1536 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

| Listed disposable | MX (shared infra) |
|---|---|
| `0-30-24.com` | `alt1.aspmx.l.google.com` |
| `0-mail.com` | `park-mx.above.com` |
| `0058.ru` | `alt1.aspmx.l.google.com` |
| `01g.cloud` | `alt1.aspmx.l.google.com` |
| `0ak.org` | `mx00.ionos.com` |
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
| `10x10-bet.com` | `eforward1.registrar-servers.com` |
| `111gmail.com` | `park-mx.above.com` |
| `11cows.com` | `mxa.mailgun.org` |
| `123gmail.com` | `park-mx.above.com` |
| `12499aaa.com` | `eforward1.registrar-servers.com` |
| `13dk.net` | `route1.mx.cloudflare.net` |
| `143gmail.com` | `park-mx.above.com` |
| `14n.co.uk` | `14n-co-uk.mail.protection.outlook.com` |


*… and 1,506 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
