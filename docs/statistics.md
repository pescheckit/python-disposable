# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-05-18 03:25 UTC**.*  
*Last DNS snapshot: **2026-05-18T03:12:08+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 72,296 |
| `domains_strict.txt` | 72,327 |
| `domains_inferred.txt` (opt-in) | 1 |

## Reachability

Of **72,586** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 10,981 | 15.1% |
| A_ONLY | 1,465 | 2.0% |
| NXDOMAIN | 19,571 | 27.0% |
| NO_RECORDS | 233 | 0.3% |
| TIMEOUT | 40,336 | 55.6% |

**12,446 domains are mail-reachable today** (17.1%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `mail.wabblywabble.com` | 715 | 726 |  |
| `mail.wallywatts.com` | 715 | 726 |  |
| `generator.email` | 483 | 578 |  |
| `mx4.beavis99.com` | 464 | 464 |  |
| `mx4.beavis99.net` | 464 | 464 |  |
| `route1.mx.cloudflare.net` | 380 | 383 | yes |
| `route2.mx.cloudflare.net` | 380 | 383 | yes |
| `route3.mx.cloudflare.net` | 379 | 382 | yes |
| `park-mx.above.com` | 276 | 276 | yes |
| `emailfake.com` | 237 | 269 |  |
| `aspmx.l.google.com` | 209 | 209 | yes |
| `mx.spymail.one` | 207 | 207 |  |
| `alt1.aspmx.l.google.com` | 205 | 205 | yes |
| `alt2.aspmx.l.google.com` | 204 | 204 | yes |
| `mx.emlhub.com` | 202 | 202 |  |
| `mx.emlpro.com` | 201 | 201 |  |
| `aero4.unstablemail.com` | 199 | 199 |  |
| `srv4.unstablemail.com` | 199 | 199 |  |
| `mx.emltmp.com` | 196 | 196 |  |
| `eforward1.registrar-servers.com` | 184 | 185 | yes |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 715 | 726 |
| `mail.wallywatts.com` | 715 | 726 |
| `generator.email` | 483 | 578 |
| `mx4.beavis99.com` | 464 | 464 |
| `mx4.beavis99.net` | 464 | 464 |
| `emailfake.com` | 237 | 269 |
| `mx.spymail.one` | 207 | 207 |
| `mx.emlhub.com` | 202 | 202 |
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
| `78.47.124.133` | 918 | 918 |
| `94.130.108.80` | 918 | 918 |
| `91.196.52.205` | 558 | 689 |
| `116.202.9.167` | 440 | 450 |
| `46.101.111.206` | 440 | 450 |
| `142.132.166.12` | 439 | 450 |
| `188.166.111.252` | 439 | 450 |
| `188.245.74.208` | 300 | 300 |
| `147.182.130.78` | 286 | 287 |
| `147.182.160.18` | 286 | 287 |
| `147.182.180.139` | 286 | 287 |
| `147.182.189.184` | 286 | 287 |
| `164.90.197.105` | 286 | 287 |
| `164.90.197.143` | 286 | 287 |
| `164.90.197.162` | 286 | 287 |
| `164.90.197.79` | 286 | 287 |
| `195.201.18.63` | 274 | 274 |
| `162.159.205.23` | 270 | 272 |
| `162.159.205.24` | 270 | 272 |
| `162.159.205.25` | 270 | 272 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 190 |
| High-confidence disposable IPs | 397 |
| Promoted to `domains_inferred.txt` | 1 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**1535 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

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
| `10x10-bet.com` | `eforward1.registrar-servers.com` |
| `111gmail.com` | `park-mx.above.com` |
| `11cows.com` | `mxa.mailgun.org` |
| `123gmail.com` | `park-mx.above.com` |
| `12499aaa.com` | `eforward1.registrar-servers.com` |
| `13dk.net` | `route1.mx.cloudflare.net` |
| `143gmail.com` | `park-mx.above.com` |


*… and 1,505 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
