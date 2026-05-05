# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-05-05 03:27 UTC**.*  
*Last DNS snapshot: **2026-05-05T03:09:02+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 72,190 |
| `domains_strict.txt` | 72,221 |
| `domains_inferred.txt` (opt-in) | 2 |

## Reachability

Of **72,379** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 22,557 | 31.2% |
| A_ONLY | 5,738 | 7.9% |
| NXDOMAIN | 42,518 | 58.7% |
| NO_RECORDS | 750 | 1.0% |
| TIMEOUT | 816 | 1.1% |

**28,295 domains are mail-reachable today** (39.1%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `mail.wabblywabble.com` | 1557 | 1565 |  |
| `mail.wallywatts.com` | 1557 | 1565 |  |
| `mx4.beavis99.com` | 1005 | 1005 |  |
| `mx4.beavis99.net` | 1004 | 1004 |  |
| `generator.email` | 827 | 912 |  |
| `route2.mx.cloudflare.net` | 794 | 794 | yes |
| `route1.mx.cloudflare.net` | 793 | 793 | yes |
| `route3.mx.cloudflare.net` | 793 | 793 | yes |
| `park-mx.above.com` | 581 | 581 | yes |
| `mx.emlhub.com` | 493 | 493 |  |
| `aero4.unstablemail.com` | 477 | 477 |  |
| `srv4.unstablemail.com` | 476 | 476 |  |
| `aspmx.l.google.com` | 463 | 463 | yes |
| `emailfake.com` | 462 | 503 |  |
| `alt1.aspmx.l.google.com` | 454 | 454 | yes |
| `alt2.aspmx.l.google.com` | 450 | 450 | yes |
| `mx.spymail.one` | 389 | 389 |  |
| `mx.emltmp.com` | 377 | 377 |  |
| `eforward1.registrar-servers.com` | 368 | 368 | yes |
| `eforward2.registrar-servers.com` | 368 | 368 | yes |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 1557 | 1565 |
| `mail.wallywatts.com` | 1557 | 1565 |
| `mx4.beavis99.com` | 1005 | 1005 |
| `mx4.beavis99.net` | 1004 | 1004 |
| `generator.email` | 827 | 912 |
| `mx.emlhub.com` | 493 | 493 |
| `aero4.unstablemail.com` | 477 | 477 |
| `srv4.unstablemail.com` | 476 | 476 |
| `emailfake.com` | 462 | 503 |
| `mx.spymail.one` | 389 | 389 |
| `mx.emltmp.com` | 377 | 377 |
| `mx.emlpro.com` | 364 | 364 |
| `mx.dropmail.me` | 342 | 342 |
| `mx.freeml.net` | 321 | 321 |
| `mx37.m1bp.com` | 288 | 288 |
| `mx37.mb5p.com` | 288 | 288 |
| `mail.casadorock.com` | 256 | 256 |
| `mx.yomail.info` | 254 | 254 |
| `mail.mailerhost.net` | 247 | 247 |
| `mx195.m1bp.com` | 236 | 236 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `78.47.124.133` | 2753 | 2753 |
| `94.130.108.80` | 2753 | 2753 |
| `116.202.9.167` | 1556 | 1564 |
| `46.101.111.206` | 1556 | 1564 |
| `142.132.166.12` | 1555 | 1563 |
| `188.166.111.252` | 1555 | 1563 |
| `91.196.52.205` | 1433 | 1568 |
| `13.223.25.84` | 1168 | 1168 |
| `54.243.117.197` | 1168 | 1168 |
| `188.245.74.208` | 1004 | 1004 |
| `195.201.18.63` | 1004 | 1004 |
| `162.159.205.17` | 817 | 817 |
| `162.159.205.18` | 817 | 817 |
| `162.159.205.19` | 817 | 817 |
| `162.159.205.11` | 815 | 815 |
| `162.159.205.12` | 815 | 815 |
| `162.159.205.13` | 815 | 815 |
| `162.159.205.23` | 815 | 815 |
| `162.159.205.24` | 815 | 815 |
| `162.159.205.25` | 815 | 815 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 306 |
| High-confidence disposable IPs | 791 |
| Promoted to `domains_inferred.txt` | 2 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**3255 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

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


*… and 3,225 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
