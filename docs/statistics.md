# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-08-31 02:35 UTC**.*  
*Last DNS snapshot: **2026-08-31T02:19:34+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 74,914 |
| `domains_strict.txt` | 74,945 |
| `domains_inferred.txt` (opt-in) | 0 |

## Reachability

Of **75,834** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 13,678 | 18.0% |
| A_ONLY | 2,498 | 3.3% |
| NXDOMAIN | 23,582 | 31.1% |
| NO_RECORDS | 355 | 0.5% |
| TIMEOUT | 35,721 | 47.1% |

**16,176 domains are mail-reachable today** (21.3%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `mail.wabblywabble.com` | 758 | 822 |  |
| `mail.wallywatts.com` | 758 | 822 |  |
| `mx4.beavis99.com` | 618 | 619 |  |
| `mx4.beavis99.net` | 618 | 619 |  |
| `route2.mx.cloudflare.net` | 529 | 539 | yes |
| `route1.mx.cloudflare.net` | 528 | 538 | yes |
| `route3.mx.cloudflare.net` | 528 | 538 | yes |
| `generator.email` | 437 | 574 |  |
| `email.gravityengine.cc` | 368 | 368 |  |
| `email.chatgpt.org.uk` | 326 | 326 |  |
| `park-mx.above.com` | 283 | 288 | yes |
| `mx.emlhub.com` | 280 | 280 |  |
| `emailfake.com` | 262 | 299 |  |
| `aero4.unstablemail.com` | 257 | 257 |  |
| `srv4.unstablemail.com` | 257 | 257 |  |
| `aspmx.l.google.com` | 246 | 248 | yes |
| `alt1.aspmx.l.google.com` | 243 | 245 | yes |
| `alt2.aspmx.l.google.com` | 241 | 243 | yes |
| `mx.spymail.one` | 223 | 223 |  |
| `tinyhost.shop` | 221 | 222 |  |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 758 | 822 |
| `mail.wallywatts.com` | 758 | 822 |
| `mx4.beavis99.com` | 618 | 619 |
| `mx4.beavis99.net` | 618 | 619 |
| `generator.email` | 437 | 574 |
| `email.gravityengine.cc` | 368 | 368 |
| `email.chatgpt.org.uk` | 326 | 326 |
| `mx.emlhub.com` | 280 | 280 |
| `emailfake.com` | 262 | 299 |
| `aero4.unstablemail.com` | 257 | 257 |
| `srv4.unstablemail.com` | 257 | 257 |
| `mx.spymail.one` | 223 | 223 |
| `tinyhost.shop` | 221 | 222 |
| `mx.emltmp.com` | 192 | 192 |
| `mx.emlpro.com` | 187 | 187 |
| `mx.freeml.net` | 162 | 162 |
| `mx37.m1bp.com` | 162 | 162 |
| `mx37.mb5p.com` | 162 | 162 |
| `mx.dropmail.me` | 159 | 159 |
| `mail.casadorock.com` | 141 | 141 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `78.47.124.133` | 1144 | 1144 |
| `94.130.108.80` | 1144 | 1144 |
| `138.226.240.26` | 671 | 671 |
| `142.132.166.12` | 642 | 698 |
| `188.166.111.252` | 642 | 698 |
| `116.202.9.167` | 640 | 695 |
| `46.101.111.206` | 640 | 695 |
| `91.196.52.205` | 610 | 784 |
| `188.245.74.208` | 493 | 494 |
| `13.223.25.84` | 490 | 490 |
| `54.243.117.197` | 490 | 490 |
| `195.201.18.63` | 478 | 479 |
| `162.159.205.17` | 459 | 468 |
| `162.159.205.18` | 459 | 468 |
| `162.159.205.19` | 459 | 468 |
| `162.159.205.23` | 454 | 462 |
| `162.159.205.24` | 454 | 462 |
| `162.159.205.25` | 454 | 462 |
| `162.159.205.11` | 449 | 457 |
| `162.159.205.12` | 449 | 457 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 235 |
| High-confidence disposable IPs | 503 |
| Promoted to `domains_inferred.txt` | 0 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**1787 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

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
| `129.in` | `park-mx.above.com` |
| `12storage.com` | `park-mx.above.com` |
| `13dk.net` | `route1.mx.cloudflare.net` |
| `14n.co.uk` | `14n-co-uk.mail.protection.outlook.com` |
| `14p.in` | `eforward1.registrar-servers.com` |
| `15qm-mail.red` | `eforward1.registrar-servers.com` |
| `189.email` | `route1.mx.cloudflare.net` |
| `1987.com` | `park-mx.above.com` |


*… and 1,757 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
