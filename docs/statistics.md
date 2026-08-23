# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-08-23 02:53 UTC**.*  
*Last DNS snapshot: **2026-08-23T02:34:19+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 74,858 |
| `domains_strict.txt` | 74,889 |
| `domains_inferred.txt` (opt-in) | 1 |

## Reachability

Of **75,739** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 13,642 | 18.0% |
| A_ONLY | 2,504 | 3.3% |
| NXDOMAIN | 23,932 | 31.6% |
| NO_RECORDS | 411 | 0.5% |
| TIMEOUT | 35,250 | 46.5% |

**16,146 domains are mail-reachable today** (21.3%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `mail.wabblywabble.com` | 756 | 815 |  |
| `mail.wallywatts.com` | 756 | 815 |  |
| `mx4.beavis99.com` | 607 | 608 |  |
| `mx4.beavis99.net` | 607 | 608 |  |
| `route2.mx.cloudflare.net` | 560 | 570 | yes |
| `route1.mx.cloudflare.net` | 559 | 569 | yes |
| `route3.mx.cloudflare.net` | 559 | 569 | yes |
| `generator.email` | 461 | 596 |  |
| `email.gravityengine.cc` | 394 | 394 |  |
| `email.chatgpt.org.uk` | 363 | 363 |  |
| `tinyhost.shop` | 322 | 322 |  |
| `mx.emlhub.com` | 289 | 289 |  |
| `emailfake.com` | 287 | 324 |  |
| `park-mx.above.com` | 281 | 285 | yes |
| `aspmx.l.google.com` | 262 | 264 | yes |
| `alt1.aspmx.l.google.com` | 257 | 259 | yes |
| `alt2.aspmx.l.google.com` | 253 | 255 | yes |
| `aero4.unstablemail.com` | 248 | 248 |  |
| `srv4.unstablemail.com` | 248 | 248 |  |
| `mx.spymail.one` | 212 | 212 |  |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 756 | 815 |
| `mail.wallywatts.com` | 756 | 815 |
| `mx4.beavis99.com` | 607 | 608 |
| `mx4.beavis99.net` | 607 | 608 |
| `generator.email` | 461 | 596 |
| `email.gravityengine.cc` | 394 | 394 |
| `email.chatgpt.org.uk` | 363 | 363 |
| `tinyhost.shop` | 322 | 322 |
| `mx.emlhub.com` | 289 | 289 |
| `emailfake.com` | 287 | 324 |
| `aero4.unstablemail.com` | 248 | 248 |
| `srv4.unstablemail.com` | 248 | 248 |
| `mx.spymail.one` | 212 | 212 |
| `mx.emlpro.com` | 183 | 183 |
| `mx.emltmp.com` | 183 | 183 |
| `mx.dropmail.me` | 178 | 178 |
| `mx.freeml.net` | 163 | 163 |
| `mail.casadorock.com` | 147 | 147 |
| `mx156.hostedmxserver.com` | 136 | 136 |
| `mail.mailerhost.net` | 133 | 133 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `78.47.124.133` | 1172 | 1172 |
| `94.130.108.80` | 1172 | 1172 |
| `138.226.240.26` | 724 | 724 |
| `91.196.52.205` | 659 | 831 |
| `116.202.9.167` | 622 | 672 |
| `46.101.111.206` | 622 | 672 |
| `142.132.166.12` | 608 | 659 |
| `188.166.111.252` | 608 | 659 |
| `13.223.25.84` | 526 | 526 |
| `54.243.117.197` | 526 | 526 |
| `162.159.205.23` | 484 | 492 |
| `162.159.205.24` | 484 | 492 |
| `162.159.205.25` | 484 | 492 |
| `162.159.205.17` | 481 | 490 |
| `162.159.205.18` | 481 | 490 |
| `162.159.205.19` | 481 | 490 |
| `162.159.205.11` | 468 | 476 |
| `162.159.205.12` | 468 | 476 |
| `162.159.205.13` | 468 | 476 |
| `188.245.74.208` | 438 | 439 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 224 |
| High-confidence disposable IPs | 504 |
| Promoted to `domains_inferred.txt` | 1 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**1858 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

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
| `129.in` | `park-mx.above.com` |
| `12storage.com` | `park-mx.above.com` |
| `13dk.net` | `route1.mx.cloudflare.net` |
| `14n.co.uk` | `14n-co-uk.mail.protection.outlook.com` |
| `14p.in` | `eforward1.registrar-servers.com` |
| `15qm-mail.red` | `eforward1.registrar-servers.com` |
| `189.email` | `route1.mx.cloudflare.net` |


*… and 1,828 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
