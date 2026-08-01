# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-08-01 03:23 UTC**.*  
*Last DNS snapshot: **2026-08-01T03:05:29+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 74,680 |
| `domains_strict.txt` | 74,711 |
| `domains_inferred.txt` (opt-in) | 0 |

## Reachability

Of **75,413** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 11,827 | 15.7% |
| A_ONLY | 1,959 | 2.6% |
| NXDOMAIN | 20,526 | 27.2% |
| NO_RECORDS | 301 | 0.4% |
| TIMEOUT | 40,800 | 54.1% |

**13,786 domains are mail-reachable today** (18.3%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `mail.wabblywabble.com` | 660 | 708 |  |
| `mail.wallywatts.com` | 660 | 708 |  |
| `route2.mx.cloudflare.net` | 513 | 523 | yes |
| `route1.mx.cloudflare.net` | 512 | 522 | yes |
| `route3.mx.cloudflare.net` | 512 | 522 | yes |
| `mx4.beavis99.com` | 482 | 483 |  |
| `mx4.beavis99.net` | 482 | 483 |  |
| `generator.email` | 424 | 558 |  |
| `tinyhost.shop` | 345 | 345 |  |
| `emailfake.com` | 264 | 302 |  |
| `mx.emlhub.com` | 262 | 262 |  |
| `park-mx.above.com` | 251 | 254 | yes |
| `aspmx.l.google.com` | 223 | 225 | yes |
| `alt1.aspmx.l.google.com` | 222 | 224 | yes |
| `alt2.aspmx.l.google.com` | 218 | 220 | yes |
| `email.chatgpt.org.uk` | 210 | 210 |  |
| `aero4.unstablemail.com` | 205 | 205 |  |
| `srv4.unstablemail.com` | 204 | 204 |  |
| `eforward1.registrar-servers.com` | 184 | 187 | yes |
| `eforward2.registrar-servers.com` | 184 | 187 | yes |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 660 | 708 |
| `mail.wallywatts.com` | 660 | 708 |
| `mx4.beavis99.com` | 482 | 483 |
| `mx4.beavis99.net` | 482 | 483 |
| `generator.email` | 424 | 558 |
| `tinyhost.shop` | 345 | 345 |
| `emailfake.com` | 264 | 302 |
| `mx.emlhub.com` | 262 | 262 |
| `email.chatgpt.org.uk` | 210 | 210 |
| `aero4.unstablemail.com` | 205 | 205 |
| `srv4.unstablemail.com` | 204 | 204 |
| `email.gravityengine.cc` | 178 | 178 |
| `mx.emltmp.com` | 167 | 167 |
| `mx.spymail.one` | 157 | 157 |
| `mx.emlpro.com` | 153 | 153 |
| `mx.dropmail.me` | 146 | 146 |
| `mx37.m1bp.com` | 137 | 137 |
| `mx37.mb5p.com` | 137 | 137 |
| `mail.casadorock.com` | 133 | 133 |
| `mx.freeml.net` | 123 | 123 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `78.47.124.133` | 871 | 871 |
| `94.130.108.80` | 871 | 871 |
| `91.196.52.205` | 581 | 758 |
| `142.132.166.12` | 496 | 538 |
| `188.166.111.252` | 496 | 538 |
| `116.202.9.167` | 481 | 522 |
| `46.101.111.206` | 481 | 522 |
| `162.159.205.23` | 407 | 415 |
| `162.159.205.24` | 407 | 415 |
| `162.159.205.25` | 407 | 415 |
| `162.159.205.17` | 406 | 415 |
| `162.159.205.18` | 406 | 415 |
| `162.159.205.19` | 406 | 415 |
| `162.159.205.11` | 397 | 405 |
| `162.159.205.12` | 397 | 405 |
| `162.159.205.13` | 397 | 405 |
| `13.223.25.84` | 394 | 394 |
| `54.243.117.197` | 394 | 394 |
| `188.245.74.208` | 358 | 359 |
| `195.201.18.63` | 343 | 344 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 203 |
| High-confidence disposable IPs | 429 |
| Promoted to `domains_inferred.txt` | 0 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**1658 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

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


*… and 1,628 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
