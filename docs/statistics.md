# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-08-10 03:20 UTC**.*  
*Last DNS snapshot: **2026-08-10T03:20:40+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 74,690 |
| `domains_strict.txt` | 74,721 |
| `domains_inferred.txt` (opt-in) | 0 |

## Reachability

Of **75,495** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 12,036 | 15.9% |
| A_ONLY | 1,984 | 2.6% |
| NXDOMAIN | 21,376 | 28.3% |
| NO_RECORDS | 300 | 0.4% |
| TIMEOUT | 39,799 | 52.7% |

**14,020 domains are mail-reachable today** (18.6%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `mail.wabblywabble.com` | 639 | 694 |  |
| `mail.wallywatts.com` | 639 | 694 |  |
| `route2.mx.cloudflare.net` | 504 | 513 | yes |
| `route1.mx.cloudflare.net` | 502 | 511 | yes |
| `route3.mx.cloudflare.net` | 502 | 511 | yes |
| `mx4.beavis99.com` | 487 | 488 |  |
| `mx4.beavis99.net` | 487 | 488 |  |
| `generator.email` | 400 | 535 |  |
| `tinyhost.shop` | 318 | 318 |  |
| `mx.emlhub.com` | 281 | 281 |  |
| `emailfake.com` | 254 | 290 |  |
| `park-mx.above.com` | 232 | 236 | yes |
| `aspmx.l.google.com` | 223 | 225 | yes |
| `mx.spymail.one` | 221 | 221 |  |
| `alt1.aspmx.l.google.com` | 218 | 220 | yes |
| `aero4.unstablemail.com` | 214 | 214 |  |
| `srv4.unstablemail.com` | 214 | 214 |  |
| `alt2.aspmx.l.google.com` | 213 | 215 | yes |
| `mx.emlpro.com` | 184 | 184 |  |
| `email.chatgpt.org.uk` | 182 | 182 |  |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 639 | 694 |
| `mail.wallywatts.com` | 639 | 694 |
| `mx4.beavis99.com` | 487 | 488 |
| `mx4.beavis99.net` | 487 | 488 |
| `generator.email` | 400 | 535 |
| `tinyhost.shop` | 318 | 318 |
| `mx.emlhub.com` | 281 | 281 |
| `emailfake.com` | 254 | 290 |
| `mx.spymail.one` | 221 | 221 |
| `aero4.unstablemail.com` | 214 | 214 |
| `srv4.unstablemail.com` | 214 | 214 |
| `mx.emlpro.com` | 184 | 184 |
| `email.chatgpt.org.uk` | 182 | 182 |
| `mx.emltmp.com` | 177 | 177 |
| `mx.dropmail.me` | 167 | 167 |
| `mx.freeml.net` | 163 | 163 |
| `mail.casadorock.com` | 159 | 159 |
| `email.gravityengine.cc` | 153 | 153 |
| `mx37.m1bp.com` | 146 | 146 |
| `mx37.mb5p.com` | 146 | 146 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `78.47.124.133` | 1116 | 1116 |
| `94.130.108.80` | 1116 | 1116 |
| `91.196.52.205` | 563 | 737 |
| `142.132.166.12` | 503 | 552 |
| `188.166.111.252` | 503 | 552 |
| `116.202.9.167` | 491 | 539 |
| `46.101.111.206` | 491 | 539 |
| `162.159.205.23` | 410 | 417 |
| `162.159.205.24` | 410 | 417 |
| `162.159.205.25` | 410 | 417 |
| `162.159.205.17` | 406 | 414 |
| `162.159.205.18` | 406 | 414 |
| `162.159.205.19` | 406 | 414 |
| `13.223.25.84` | 400 | 400 |
| `54.243.117.197` | 400 | 400 |
| `162.159.205.11` | 385 | 392 |
| `162.159.205.12` | 385 | 392 |
| `162.159.205.13` | 385 | 392 |
| `188.245.74.208` | 353 | 354 |
| `195.201.18.63` | 346 | 347 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 205 |
| High-confidence disposable IPs | 449 |
| Promoted to `domains_inferred.txt` | 0 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**1632 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

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


*… and 1,602 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
