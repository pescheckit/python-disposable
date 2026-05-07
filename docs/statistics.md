# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-05-07 04:50 UTC**.*  
*Last DNS snapshot: **2026-05-07T04:50:06+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 72,189 |
| `domains_strict.txt` | 72,220 |
| `domains_inferred.txt` (opt-in) | 0 |

## Reachability

Of **72,400** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 10,818 | 14.9% |
| A_ONLY | 1,476 | 2.0% |
| NXDOMAIN | 19,397 | 26.8% |
| NO_RECORDS | 224 | 0.3% |
| TIMEOUT | 40,485 | 55.9% |

**12,294 domains are mail-reachable today** (17.0%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `mail.wabblywabble.com` | 697 | 705 |  |
| `mail.wallywatts.com` | 697 | 705 |  |
| `mx4.beavis99.com` | 458 | 458 |  |
| `mx4.beavis99.net` | 458 | 458 |  |
| `generator.email` | 400 | 483 |  |
| `route1.mx.cloudflare.net` | 354 | 354 | yes |
| `route2.mx.cloudflare.net` | 354 | 354 | yes |
| `route3.mx.cloudflare.net` | 354 | 354 | yes |
| `park-mx.above.com` | 288 | 288 | yes |
| `aero4.unstablemail.com` | 224 | 224 |  |
| `srv4.unstablemail.com` | 224 | 224 |  |
| `mx.emlhub.com` | 214 | 214 |  |
| `mx.spymail.one` | 207 | 207 |  |
| `aspmx.l.google.com` | 204 | 204 | yes |
| `emailfake.com` | 203 | 254 |  |
| `alt1.aspmx.l.google.com` | 197 | 197 | yes |
| `alt2.aspmx.l.google.com` | 195 | 195 | yes |
| `eforward1.registrar-servers.com` | 178 | 178 | yes |
| `eforward2.registrar-servers.com` | 178 | 178 | yes |
| `eforward3.registrar-servers.com` | 178 | 178 | yes |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 697 | 705 |
| `mail.wallywatts.com` | 697 | 705 |
| `mx4.beavis99.com` | 458 | 458 |
| `mx4.beavis99.net` | 458 | 458 |
| `generator.email` | 400 | 483 |
| `aero4.unstablemail.com` | 224 | 224 |
| `srv4.unstablemail.com` | 224 | 224 |
| `mx.emlhub.com` | 214 | 214 |
| `mx.spymail.one` | 207 | 207 |
| `emailfake.com` | 203 | 254 |
| `mx.emltmp.com` | 175 | 175 |
| `mx.emlpro.com` | 172 | 172 |
| `mx.dropmail.me` | 169 | 169 |
| `mx.freeml.net` | 151 | 151 |
| `mail.casadorock.com` | 136 | 136 |
| `mx37.m1bp.com` | 125 | 125 |
| `mx37.mb5p.com` | 125 | 125 |
| `mx.yomail.info` | 124 | 124 |
| `mail.mailerhost.net` | 119 | 119 |
| `mx195.m1bp.com` | 114 | 114 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `78.47.124.133` | 858 | 858 |
| `94.130.108.80` | 858 | 858 |
| `116.202.9.167` | 430 | 438 |
| `46.101.111.206` | 430 | 438 |
| `142.132.166.12` | 425 | 433 |
| `188.166.111.252` | 425 | 433 |
| `91.196.52.205` | 407 | 551 |
| `188.245.74.208` | 288 | 288 |
| `195.201.18.63` | 265 | 265 |
| `147.182.130.78` | 261 | 261 |
| `147.182.160.18` | 261 | 261 |
| `147.182.180.139` | 261 | 261 |
| `147.182.189.184` | 261 | 261 |
| `164.90.197.105` | 261 | 261 |
| `164.90.197.143` | 261 | 261 |
| `164.90.197.162` | 261 | 261 |
| `164.90.197.79` | 261 | 261 |
| `162.159.205.23` | 253 | 253 |
| `162.159.205.24` | 253 | 253 |
| `162.159.205.25` | 253 | 253 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 196 |
| High-confidence disposable IPs | 374 |
| Promoted to `domains_inferred.txt` | 0 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**1516 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

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


*… and 1,486 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
