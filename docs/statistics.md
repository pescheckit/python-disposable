# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-09-01 02:28 UTC**.*  
*Last DNS snapshot: **2026-09-01T02:16:59+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 75,248 |
| `domains_strict.txt` | 75,279 |
| `domains_inferred.txt` (opt-in) | 0 |

## Reachability

Of **76,168** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 14,270 | 18.7% |
| A_ONLY | 2,596 | 3.4% |
| NXDOMAIN | 24,042 | 31.6% |
| NO_RECORDS | 365 | 0.5% |
| TIMEOUT | 34,895 | 45.8% |

**16,866 domains are mail-reachable today** (22.1%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `mail.wabblywabble.com` | 787 | 851 |  |
| `mail.wallywatts.com` | 787 | 851 |  |
| `mx4.beavis99.com` | 632 | 633 |  |
| `mx4.beavis99.net` | 632 | 633 |  |
| `route2.mx.cloudflare.net` | 536 | 546 | yes |
| `route1.mx.cloudflare.net` | 535 | 545 | yes |
| `route3.mx.cloudflare.net` | 535 | 545 | yes |
| `tinyhost.shop` | 473 | 473 |  |
| `generator.email` | 467 | 603 |  |
| `email.chatgpt.org.uk` | 384 | 384 |  |
| `email.gravityengine.cc` | 373 | 373 |  |
| `park-mx.above.com` | 292 | 297 | yes |
| `mx.emlhub.com` | 282 | 282 |  |
| `emailfake.com` | 267 | 304 |  |
| `aero4.unstablemail.com` | 259 | 259 |  |
| `srv4.unstablemail.com` | 259 | 259 |  |
| `aspmx.l.google.com` | 254 | 256 | yes |
| `alt1.aspmx.l.google.com` | 252 | 254 | yes |
| `alt2.aspmx.l.google.com` | 250 | 252 | yes |
| `mx.spymail.one` | 224 | 224 |  |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 787 | 851 |
| `mail.wallywatts.com` | 787 | 851 |
| `mx4.beavis99.com` | 632 | 633 |
| `mx4.beavis99.net` | 632 | 633 |
| `tinyhost.shop` | 473 | 473 |
| `generator.email` | 467 | 603 |
| `email.chatgpt.org.uk` | 384 | 384 |
| `email.gravityengine.cc` | 373 | 373 |
| `mx.emlhub.com` | 282 | 282 |
| `emailfake.com` | 267 | 304 |
| `aero4.unstablemail.com` | 259 | 259 |
| `srv4.unstablemail.com` | 259 | 259 |
| `mx.spymail.one` | 224 | 224 |
| `mx.emltmp.com` | 192 | 192 |
| `mx.emlpro.com` | 188 | 188 |
| `mx.dropmail.me` | 163 | 163 |
| `mx.freeml.net` | 162 | 162 |
| `mx37.m1bp.com` | 162 | 162 |
| `mx37.mb5p.com` | 162 | 162 |
| `mail.casadorock.com` | 143 | 143 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `78.47.124.133` | 1161 | 1161 |
| `94.130.108.80` | 1161 | 1161 |
| `138.226.240.26` | 725 | 725 |
| `142.132.166.12` | 673 | 729 |
| `188.166.111.252` | 673 | 729 |
| `116.202.9.167` | 670 | 725 |
| `46.101.111.206` | 670 | 725 |
| `91.196.52.205` | 652 | 825 |
| `13.223.25.84` | 514 | 514 |
| `54.243.117.197` | 514 | 514 |
| `188.245.74.208` | 508 | 509 |
| `195.201.18.63` | 495 | 496 |
| `162.159.205.17` | 466 | 475 |
| `162.159.205.18` | 466 | 475 |
| `162.159.205.19` | 466 | 475 |
| `162.159.205.23` | 462 | 470 |
| `162.159.205.24` | 462 | 470 |
| `162.159.205.25` | 462 | 470 |
| `162.159.205.11` | 456 | 464 |
| `162.159.205.12` | 456 | 464 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 239 |
| High-confidence disposable IPs | 526 |
| Promoted to `domains_inferred.txt` | 0 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**1830 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

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


*… and 1,800 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
