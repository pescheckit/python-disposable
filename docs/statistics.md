# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-07-18 04:23 UTC**.*  
*Last DNS snapshot: **2026-07-18T04:08:28+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 74,528 |
| `domains_strict.txt` | 74,559 |
| `domains_inferred.txt` (opt-in) | 0 |

## Reachability

Of **75,195** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 11,998 | 16.0% |
| A_ONLY | 1,946 | 2.6% |
| NXDOMAIN | 19,908 | 26.5% |
| NO_RECORDS | 268 | 0.4% |
| TIMEOUT | 41,075 | 54.6% |

**13,944 domains are mail-reachable today** (18.5%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `mail.wabblywabble.com` | 631 | 674 |  |
| `mail.wallywatts.com` | 631 | 674 |  |
| `mx4.beavis99.com` | 561 | 562 |  |
| `mx4.beavis99.net` | 561 | 562 |  |
| `route1.mx.cloudflare.net` | 522 | 531 | yes |
| `route2.mx.cloudflare.net` | 522 | 531 | yes |
| `route3.mx.cloudflare.net` | 520 | 529 | yes |
| `generator.email` | 407 | 546 |  |
| `tinyhost.shop` | 343 | 343 |  |
| `park-mx.above.com` | 296 | 298 | yes |
| `email.gravityengine.cc` | 271 | 271 |  |
| `mx.emlhub.com` | 253 | 253 |  |
| `aspmx.l.google.com` | 222 | 224 | yes |
| `alt1.aspmx.l.google.com` | 215 | 217 | yes |
| `alt2.aspmx.l.google.com` | 213 | 215 | yes |
| `aero4.unstablemail.com` | 204 | 204 |  |
| `srv4.unstablemail.com` | 204 | 204 |  |
| `emailfake.com` | 200 | 241 |  |
| `eforward1.registrar-servers.com` | 175 | 178 | yes |
| `eforward2.registrar-servers.com` | 175 | 178 | yes |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 631 | 674 |
| `mail.wallywatts.com` | 631 | 674 |
| `mx4.beavis99.com` | 561 | 562 |
| `mx4.beavis99.net` | 561 | 562 |
| `generator.email` | 407 | 546 |
| `tinyhost.shop` | 343 | 343 |
| `email.gravityengine.cc` | 271 | 271 |
| `mx.emlhub.com` | 253 | 253 |
| `aero4.unstablemail.com` | 204 | 204 |
| `srv4.unstablemail.com` | 204 | 204 |
| `emailfake.com` | 200 | 241 |
| `mx.emltmp.com` | 166 | 166 |
| `mx.spymail.one` | 163 | 163 |
| `email.chatgpt.org.uk` | 161 | 161 |
| `mx37.m1bp.com` | 157 | 157 |
| `mx37.mb5p.com` | 157 | 157 |
| `mx.emlpro.com` | 154 | 154 |
| `mx.dropmail.me` | 147 | 147 |
| `mail.casadorock.com` | 136 | 136 |
| `mx.freeml.net` | 134 | 134 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `78.47.124.133` | 904 | 904 |
| `94.130.108.80` | 904 | 904 |
| `91.196.52.205` | 492 | 677 |
| `116.202.9.167` | 488 | 526 |
| `46.101.111.206` | 488 | 526 |
| `142.132.166.12` | 472 | 511 |
| `188.166.111.252` | 472 | 511 |
| `188.245.74.208` | 434 | 435 |
| `162.159.205.11` | 417 | 425 |
| `162.159.205.12` | 417 | 425 |
| `162.159.205.13` | 417 | 425 |
| `195.201.18.63` | 414 | 415 |
| `162.159.205.23` | 413 | 421 |
| `162.159.205.24` | 413 | 421 |
| `162.159.205.25` | 413 | 421 |
| `162.159.205.17` | 407 | 415 |
| `162.159.205.18` | 407 | 415 |
| `162.159.205.19` | 407 | 415 |
| `158.101.127.66` | 347 | 347 |
| `13.223.25.84` | 345 | 345 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 204 |
| High-confidence disposable IPs | 414 |
| Promoted to `domains_inferred.txt` | 0 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**1709 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

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
| `13dk.net` | `route1.mx.cloudflare.net` |
| `14n.co.uk` | `14n-co-uk.mail.protection.outlook.com` |
| `14p.in` | `eforward1.registrar-servers.com` |
| `15qm-mail.red` | `eforward1.registrar-servers.com` |
| `189.email` | `route1.mx.cloudflare.net` |
| `1987.com` | `park-mx.above.com` |
| `1aolmail.com` | `route1.mx.cloudflare.net` |
| `1ayj8yi7lpiksxawav.gq` | `route1.mx.cloudflare.net` |


*… and 1,679 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
