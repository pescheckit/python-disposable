# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-08-25 02:48 UTC**.*  
*Last DNS snapshot: **2026-08-25T02:48:49+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 74,876 |
| `domains_strict.txt` | 74,907 |
| `domains_inferred.txt` (opt-in) | 0 |

## Reachability

Of **75,760** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 12,595 | 16.6% |
| A_ONLY | 2,190 | 2.9% |
| NXDOMAIN | 21,833 | 28.8% |
| NO_RECORDS | 372 | 0.5% |
| TIMEOUT | 38,770 | 51.2% |

**14,785 domains are mail-reachable today** (19.5%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `mail.wabblywabble.com` | 676 | 735 |  |
| `mail.wallywatts.com` | 676 | 735 |  |
| `mx4.beavis99.com` | 566 | 567 |  |
| `mx4.beavis99.net` | 566 | 567 |  |
| `route2.mx.cloudflare.net` | 520 | 530 | yes |
| `route1.mx.cloudflare.net` | 519 | 529 | yes |
| `route3.mx.cloudflare.net` | 519 | 529 | yes |
| `generator.email` | 414 | 549 |  |
| `email.gravityengine.cc` | 379 | 379 |  |
| `email.chatgpt.org.uk` | 340 | 340 |  |
| `tinyhost.shop` | 311 | 311 |  |
| `mx.emlhub.com` | 277 | 277 |  |
| `emailfake.com` | 262 | 299 |  |
| `park-mx.above.com` | 255 | 259 | yes |
| `aero4.unstablemail.com` | 234 | 234 |  |
| `srv4.unstablemail.com` | 234 | 234 |  |
| `aspmx.l.google.com` | 232 | 234 | yes |
| `alt1.aspmx.l.google.com` | 226 | 228 | yes |
| `alt2.aspmx.l.google.com` | 223 | 225 | yes |
| `mx.spymail.one` | 199 | 199 |  |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 676 | 735 |
| `mail.wallywatts.com` | 676 | 735 |
| `mx4.beavis99.com` | 566 | 567 |
| `mx4.beavis99.net` | 566 | 567 |
| `generator.email` | 414 | 549 |
| `email.gravityengine.cc` | 379 | 379 |
| `email.chatgpt.org.uk` | 340 | 340 |
| `tinyhost.shop` | 311 | 311 |
| `mx.emlhub.com` | 277 | 277 |
| `emailfake.com` | 262 | 299 |
| `aero4.unstablemail.com` | 234 | 234 |
| `srv4.unstablemail.com` | 234 | 234 |
| `mx.spymail.one` | 199 | 199 |
| `mx.emltmp.com` | 174 | 174 |
| `mx.emlpro.com` | 167 | 167 |
| `mx.dropmail.me` | 163 | 163 |
| `mx.freeml.net` | 156 | 156 |
| `mail.casadorock.com` | 138 | 138 |
| `mx37.m1bp.com` | 126 | 126 |
| `mx37.mb5p.com` | 126 | 126 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `78.47.124.133` | 1076 | 1076 |
| `94.130.108.80` | 1076 | 1076 |
| `138.226.240.26` | 685 | 685 |
| `91.196.52.205` | 570 | 742 |
| `116.202.9.167` | 541 | 591 |
| `46.101.111.206` | 541 | 591 |
| `142.132.166.12` | 528 | 579 |
| `188.166.111.252` | 528 | 579 |
| `162.159.205.23` | 441 | 449 |
| `162.159.205.24` | 441 | 449 |
| `162.159.205.25` | 441 | 449 |
| `13.223.25.84` | 438 | 438 |
| `162.159.205.17` | 438 | 447 |
| `162.159.205.18` | 438 | 447 |
| `162.159.205.19` | 438 | 447 |
| `54.243.117.197` | 438 | 438 |
| `162.159.205.11` | 425 | 433 |
| `162.159.205.12` | 425 | 433 |
| `162.159.205.13` | 425 | 433 |
| `188.245.74.208` | 390 | 391 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 209 |
| High-confidence disposable IPs | 458 |
| Promoted to `domains_inferred.txt` | 0 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**1686 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

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


*… and 1,656 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
