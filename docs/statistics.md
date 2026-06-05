# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-06-05 03:29 UTC**.*  
*Last DNS snapshot: **2026-06-05T03:12:24+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 72,512 |
| `domains_strict.txt` | 72,543 |
| `domains_inferred.txt` (opt-in) | 0 |

## Reachability

Of **73,007** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 10,812 | 14.8% |
| A_ONLY | 1,624 | 2.2% |
| NXDOMAIN | 19,620 | 26.9% |
| NO_RECORDS | 204 | 0.3% |
| TIMEOUT | 40,747 | 55.8% |

**12,436 domains are mail-reachable today** (17.0%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `mail.wabblywabble.com` | 690 | 707 |  |
| `mail.wallywatts.com` | 690 | 707 |  |
| `mx4.beavis99.com` | 427 | 427 |  |
| `mx4.beavis99.net` | 426 | 426 |  |
| `generator.email` | 406 | 568 |  |
| `route1.mx.cloudflare.net` | 365 | 371 | yes |
| `route2.mx.cloudflare.net` | 365 | 371 | yes |
| `route3.mx.cloudflare.net` | 365 | 371 | yes |
| `park-mx.above.com` | 277 | 278 | yes |
| `mx.emlhub.com` | 259 | 259 |  |
| `emailfake.com` | 219 | 274 |  |
| `aspmx.l.google.com` | 215 | 215 | yes |
| `alt1.aspmx.l.google.com` | 207 | 207 | yes |
| `alt2.aspmx.l.google.com` | 207 | 207 | yes |
| `aero4.unstablemail.com` | 206 | 206 |  |
| `srv4.unstablemail.com` | 205 | 205 |  |
| `mx.spymail.one` | 197 | 197 |  |
| `mx.emltmp.com` | 186 | 186 |  |
| `mx.emlpro.com` | 176 | 176 |  |
| `mx.dropmail.me` | 174 | 174 |  |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 690 | 707 |
| `mail.wallywatts.com` | 690 | 707 |
| `mx4.beavis99.com` | 427 | 427 |
| `mx4.beavis99.net` | 426 | 426 |
| `generator.email` | 406 | 568 |
| `mx.emlhub.com` | 259 | 259 |
| `emailfake.com` | 219 | 274 |
| `aero4.unstablemail.com` | 206 | 206 |
| `srv4.unstablemail.com` | 205 | 205 |
| `mx.spymail.one` | 197 | 197 |
| `mx.emltmp.com` | 186 | 186 |
| `mx.emlpro.com` | 176 | 176 |
| `mx.dropmail.me` | 174 | 174 |
| `mx.freeml.net` | 158 | 158 |
| `mx37.m1bp.com` | 144 | 144 |
| `mx37.mb5p.com` | 144 | 144 |
| `mx.yomail.info` | 136 | 136 |
| `mail.casadorock.com` | 117 | 117 |
| `mail.h-email.net` | 108 | 108 |
| `mail.mailerhost.net` | 107 | 107 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `78.47.124.133` | 991 | 991 |
| `94.130.108.80` | 991 | 991 |
| `116.202.9.167` | 468 | 482 |
| `46.101.111.206` | 468 | 482 |
| `91.196.52.205` | 456 | 675 |
| `142.132.166.12` | 413 | 428 |
| `188.166.111.252` | 413 | 428 |
| `13.223.25.84` | 311 | 311 |
| `54.243.117.197` | 311 | 311 |
| `147.182.130.78` | 275 | 276 |
| `147.182.160.18` | 275 | 276 |
| `147.182.180.139` | 275 | 276 |
| `147.182.189.184` | 275 | 276 |
| `164.90.197.105` | 275 | 276 |
| `164.90.197.143` | 275 | 276 |
| `164.90.197.162` | 275 | 276 |
| `164.90.197.79` | 275 | 276 |
| `162.159.205.17` | 271 | 276 |
| `162.159.205.18` | 271 | 276 |
| `162.159.205.19` | 271 | 276 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 191 |
| High-confidence disposable IPs | 339 |
| Promoted to `domains_inferred.txt` | 0 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**1468 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

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


*… and 1,438 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
