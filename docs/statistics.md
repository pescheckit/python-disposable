# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-08-22 02:46 UTC**.*  
*Last DNS snapshot: **2026-08-22T02:29:56+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 74,854 |
| `domains_strict.txt` | 74,885 |
| `domains_inferred.txt` (opt-in) | 2 |

## Reachability

Of **75,722** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 14,222 | 18.8% |
| A_ONLY | 2,617 | 3.5% |
| NXDOMAIN | 24,921 | 32.9% |
| NO_RECORDS | 429 | 0.6% |
| TIMEOUT | 33,533 | 44.3% |

**16,839 domains are mail-reachable today** (22.2%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `mail.wabblywabble.com` | 797 | 853 |  |
| `mail.wallywatts.com` | 797 | 853 |  |
| `mx4.beavis99.com` | 634 | 635 |  |
| `mx4.beavis99.net` | 634 | 635 |  |
| `route2.mx.cloudflare.net` | 580 | 590 | yes |
| `route1.mx.cloudflare.net` | 579 | 589 | yes |
| `route3.mx.cloudflare.net` | 579 | 589 | yes |
| `generator.email` | 479 | 614 |  |
| `email.gravityengine.cc` | 407 | 407 |  |
| `email.chatgpt.org.uk` | 369 | 369 |  |
| `tinyhost.shop` | 326 | 326 |  |
| `mx.emlhub.com` | 297 | 297 |  |
| `emailfake.com` | 296 | 333 |  |
| `park-mx.above.com` | 289 | 293 | yes |
| `aspmx.l.google.com` | 272 | 274 | yes |
| `aero4.unstablemail.com` | 271 | 271 |  |
| `srv4.unstablemail.com` | 271 | 271 |  |
| `alt1.aspmx.l.google.com` | 267 | 269 | yes |
| `alt2.aspmx.l.google.com` | 263 | 265 | yes |
| `mx.spymail.one` | 225 | 225 |  |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 797 | 853 |
| `mail.wallywatts.com` | 797 | 853 |
| `mx4.beavis99.com` | 634 | 635 |
| `mx4.beavis99.net` | 634 | 635 |
| `generator.email` | 479 | 614 |
| `email.gravityengine.cc` | 407 | 407 |
| `email.chatgpt.org.uk` | 369 | 369 |
| `tinyhost.shop` | 326 | 326 |
| `mx.emlhub.com` | 297 | 297 |
| `emailfake.com` | 296 | 333 |
| `aero4.unstablemail.com` | 271 | 271 |
| `srv4.unstablemail.com` | 271 | 271 |
| `mx.spymail.one` | 225 | 225 |
| `mx.emlpro.com` | 189 | 189 |
| `mx.emltmp.com` | 189 | 189 |
| `mx.dropmail.me` | 187 | 187 |
| `mail.casadorock.com` | 182 | 182 |
| `mx.freeml.net` | 171 | 171 |
| `mx156.hostedmxserver.com` | 140 | 140 |
| `mx.yomail.info` | 138 | 138 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `78.47.124.133` | 1262 | 1262 |
| `94.130.108.80` | 1262 | 1262 |
| `138.226.240.26` | 707 | 707 |
| `91.196.52.205` | 693 | 865 |
| `116.202.9.167` | 663 | 712 |
| `46.101.111.206` | 663 | 712 |
| `142.132.166.12` | 649 | 699 |
| `188.166.111.252` | 649 | 699 |
| `13.223.25.84` | 549 | 549 |
| `54.243.117.197` | 549 | 549 |
| `162.159.205.23` | 508 | 516 |
| `162.159.205.24` | 508 | 516 |
| `162.159.205.25` | 508 | 516 |
| `162.159.205.17` | 504 | 513 |
| `162.159.205.18` | 504 | 513 |
| `162.159.205.19` | 504 | 513 |
| `162.159.205.11` | 492 | 500 |
| `162.159.205.12` | 492 | 500 |
| `162.159.205.13` | 492 | 500 |
| `188.245.74.208` | 466 | 467 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 227 |
| High-confidence disposable IPs | 523 |
| Promoted to `domains_inferred.txt` | 2 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**1933 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

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


*… and 1,903 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
