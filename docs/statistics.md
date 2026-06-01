# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-06-01 03:25 UTC**.*  
*Last DNS snapshot: **2026-06-01T03:13:17+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 72,263 |
| `domains_strict.txt` | 72,294 |
| `domains_inferred.txt` (opt-in) | 0 |

## Reachability

Of **72,747** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 10,643 | 14.6% |
| A_ONLY | 1,523 | 2.1% |
| NXDOMAIN | 19,616 | 27.0% |
| NO_RECORDS | 203 | 0.3% |
| TIMEOUT | 40,762 | 56.0% |

**12,166 domains are mail-reachable today** (16.7%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `mail.wabblywabble.com` | 690 | 707 |  |
| `mail.wallywatts.com` | 690 | 707 |  |
| `mx4.beavis99.com` | 427 | 427 |  |
| `mx4.beavis99.net` | 426 | 426 |  |
| `generator.email` | 395 | 553 |  |
| `route1.mx.cloudflare.net` | 362 | 367 | yes |
| `route2.mx.cloudflare.net` | 362 | 367 | yes |
| `route3.mx.cloudflare.net` | 362 | 367 | yes |
| `park-mx.above.com` | 277 | 278 | yes |
| `mx.emlhub.com` | 259 | 259 |  |
| `emailfake.com` | 215 | 268 |  |
| `aspmx.l.google.com` | 210 | 210 | yes |
| `aero4.unstablemail.com` | 206 | 206 |  |
| `srv4.unstablemail.com` | 205 | 205 |  |
| `alt1.aspmx.l.google.com` | 202 | 202 | yes |
| `alt2.aspmx.l.google.com` | 202 | 202 | yes |
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
| `generator.email` | 395 | 553 |
| `mx.emlhub.com` | 259 | 259 |
| `emailfake.com` | 215 | 268 |
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
| `91.196.52.205` | 440 | 648 |
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
| `195.201.18.63` | 269 | 269 |
| `162.159.205.17` | 268 | 272 |
| `162.159.205.18` | 268 | 272 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 191 |
| High-confidence disposable IPs | 330 |
| Promoted to `domains_inferred.txt` | 0 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**1461 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

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


*… and 1,431 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
