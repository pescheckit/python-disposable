# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-06-07 03:36 UTC**.*  
*Last DNS snapshot: **2026-06-07T03:16:44+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 73,332 |
| `domains_strict.txt` | 73,363 |
| `domains_inferred.txt` (opt-in) | 0 |

## Reachability

Of **73,811** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 11,300 | 15.3% |
| A_ONLY | 1,561 | 2.1% |
| NXDOMAIN | 18,908 | 25.6% |
| NO_RECORDS | 198 | 0.3% |
| TIMEOUT | 41,844 | 56.7% |

**12,861 domains are mail-reachable today** (17.4%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `mail.wabblywabble.com` | 683 | 700 |  |
| `mail.wallywatts.com` | 683 | 700 |  |
| `email.gravityengine.cc` | 643 | 643 |  |
| `generator.email` | 421 | 570 |  |
| `mx4.beavis99.com` | 416 | 416 |  |
| `mx4.beavis99.net` | 415 | 415 |  |
| `route1.mx.cloudflare.net` | 365 | 371 | yes |
| `route2.mx.cloudflare.net` | 365 | 371 | yes |
| `route3.mx.cloudflare.net` | 365 | 371 | yes |
| `park-mx.above.com` | 273 | 274 | yes |
| `mx.emlhub.com` | 237 | 237 |  |
| `emailfake.com` | 221 | 274 |  |
| `aspmx.l.google.com` | 213 | 213 | yes |
| `alt1.aspmx.l.google.com` | 205 | 205 | yes |
| `alt2.aspmx.l.google.com` | 205 | 205 | yes |
| `aero4.unstablemail.com` | 193 | 193 |  |
| `srv4.unstablemail.com` | 192 | 192 |  |
| `mx.spymail.one` | 190 | 190 |  |
| `mx.emltmp.com` | 183 | 183 |  |
| `mx.emlpro.com` | 172 | 172 |  |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 683 | 700 |
| `mail.wallywatts.com` | 683 | 700 |
| `email.gravityengine.cc` | 643 | 643 |
| `generator.email` | 421 | 570 |
| `mx4.beavis99.com` | 416 | 416 |
| `mx4.beavis99.net` | 415 | 415 |
| `mx.emlhub.com` | 237 | 237 |
| `emailfake.com` | 221 | 274 |
| `aero4.unstablemail.com` | 193 | 193 |
| `srv4.unstablemail.com` | 192 | 192 |
| `mx.spymail.one` | 190 | 190 |
| `mx.emltmp.com` | 183 | 183 |
| `mx.emlpro.com` | 172 | 172 |
| `mx.dropmail.me` | 167 | 167 |
| `mx.freeml.net` | 155 | 155 |
| `mx.yomail.info` | 134 | 134 |
| `mx37.m1bp.com` | 134 | 134 |
| `mx37.mb5p.com` | 134 | 134 |
| `email.chatgpt.org.uk` | 111 | 111 |
| `mail.mailerhost.net` | 106 | 106 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `78.47.124.133` | 900 | 900 |
| `94.130.108.80` | 900 | 900 |
| `158.101.127.66` | 731 | 731 |
| `91.196.52.205` | 473 | 677 |
| `116.202.9.167` | 459 | 473 |
| `46.101.111.206` | 459 | 473 |
| `142.132.166.12` | 404 | 419 |
| `188.166.111.252` | 404 | 419 |
| `13.223.25.84` | 298 | 298 |
| `54.243.117.197` | 298 | 298 |
| `162.159.205.17` | 269 | 274 |
| `162.159.205.18` | 269 | 274 |
| `162.159.205.19` | 269 | 274 |
| `162.159.205.23` | 265 | 270 |
| `162.159.205.24` | 265 | 270 |
| `162.159.205.25` | 265 | 270 |
| `195.201.18.63` | 256 | 256 |
| `147.182.130.78` | 255 | 256 |
| `147.182.160.18` | 255 | 256 |
| `147.182.180.139` | 255 | 256 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 190 |
| High-confidence disposable IPs | 345 |
| Promoted to `domains_inferred.txt` | 0 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**1451 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

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


*… and 1,421 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
