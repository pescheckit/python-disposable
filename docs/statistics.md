# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-07-04 03:22 UTC**.*  
*Last DNS snapshot: **2026-07-04T03:06:23+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 74,443 |
| `domains_strict.txt` | 74,474 |
| `domains_inferred.txt` (opt-in) | 1 |

## Reachability

Of **75,041** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 14,149 | 18.9% |
| A_ONLY | 2,425 | 3.2% |
| NXDOMAIN | 23,958 | 31.9% |
| NO_RECORDS | 343 | 0.5% |
| TIMEOUT | 34,166 | 45.5% |

**16,574 domains are mail-reachable today** (22.1%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `mail.wabblywabble.com` | 773 | 811 |  |
| `mail.wallywatts.com` | 773 | 811 |  |
| `email.gravityengine.cc` | 579 | 579 |  |
| `mx4.beavis99.com` | 540 | 541 |  |
| `mx4.beavis99.net` | 540 | 541 |  |
| `route1.mx.cloudflare.net` | 536 | 543 | yes |
| `route2.mx.cloudflare.net` | 536 | 543 | yes |
| `route3.mx.cloudflare.net` | 534 | 541 | yes |
| `generator.email` | 521 | 655 |  |
| `tinyhost.shop` | 359 | 359 |  |
| `park-mx.above.com` | 341 | 343 | yes |
| `mx.emlhub.com` | 300 | 300 |  |
| `emailfake.com` | 267 | 302 |  |
| `aspmx.l.google.com` | 263 | 264 | yes |
| `alt1.aspmx.l.google.com` | 260 | 261 | yes |
| `alt2.aspmx.l.google.com` | 258 | 259 | yes |
| `aero4.unstablemail.com` | 228 | 228 |  |
| `srv4.unstablemail.com` | 228 | 228 |  |
| `mx.spymail.one` | 212 | 212 |  |
| `mx.emltmp.com` | 211 | 211 |  |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 773 | 811 |
| `mail.wallywatts.com` | 773 | 811 |
| `email.gravityengine.cc` | 579 | 579 |
| `mx4.beavis99.com` | 540 | 541 |
| `mx4.beavis99.net` | 540 | 541 |
| `generator.email` | 521 | 655 |
| `tinyhost.shop` | 359 | 359 |
| `mx.emlhub.com` | 300 | 300 |
| `emailfake.com` | 267 | 302 |
| `aero4.unstablemail.com` | 228 | 228 |
| `srv4.unstablemail.com` | 228 | 228 |
| `mx.spymail.one` | 212 | 212 |
| `mx.emltmp.com` | 211 | 211 |
| `email.chatgpt.org.uk` | 203 | 203 |
| `mx.emlpro.com` | 189 | 189 |
| `mx.dropmail.me` | 186 | 186 |
| `mx37.m1bp.com` | 167 | 167 |
| `mx37.mb5p.com` | 167 | 167 |
| `fwd.regery.net` | 164 | 164 |
| `mx.freeml.net` | 158 | 158 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `78.47.124.133` | 1142 | 1142 |
| `94.130.108.80` | 1142 | 1142 |
| `158.101.127.66` | 743 | 743 |
| `91.196.52.205` | 706 | 879 |
| `142.132.166.12` | 607 | 642 |
| `188.166.111.252` | 607 | 642 |
| `116.202.9.167` | 605 | 639 |
| `46.101.111.206` | 605 | 639 |
| `13.223.25.84` | 498 | 498 |
| `54.243.117.197` | 498 | 498 |
| `162.159.205.23` | 448 | 454 |
| `162.159.205.24` | 448 | 454 |
| `162.159.205.25` | 448 | 454 |
| `162.159.205.11` | 437 | 443 |
| `162.159.205.12` | 437 | 443 |
| `162.159.205.13` | 437 | 443 |
| `162.159.205.17` | 430 | 436 |
| `162.159.205.18` | 430 | 436 |
| `162.159.205.19` | 430 | 436 |
| `188.245.74.208` | 422 | 423 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 227 |
| High-confidence disposable IPs | 489 |
| Promoted to `domains_inferred.txt` | 1 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**1887 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

| Listed disposable | MX (shared infra) |
|---|---|
| `0-30-24.com` | `alt1.aspmx.l.google.com` |
| `0-mail.com` | `park-mx.above.com` |
| `0058.ru` | `alt1.aspmx.l.google.com` |
| `01g.cloud` | `alt1.aspmx.l.google.com` |
| `0ak.org` | `mx00.ionos.com` |
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


*… and 1,857 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
