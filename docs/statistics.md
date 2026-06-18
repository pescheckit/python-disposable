# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-06-18 03:28 UTC**.*  
*Last DNS snapshot: **2026-06-18T03:12:07+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 73,765 |
| `domains_strict.txt` | 73,796 |
| `domains_inferred.txt` (opt-in) | 2 |

## Reachability

Of **74,251** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 21,889 | 29.5% |
| A_ONLY | 5,150 | 6.9% |
| NXDOMAIN | 39,581 | 53.3% |
| NO_RECORDS | 690 | 0.9% |
| TIMEOUT | 6,941 | 9.3% |

**27,039 domains are mail-reachable today** (36.4%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `mail.wabblywabble.com` | 1345 | 1368 |  |
| `mail.wallywatts.com` | 1345 | 1368 |  |
| `mx4.beavis99.com` | 984 | 985 |  |
| `mx4.beavis99.net` | 983 | 984 |  |
| `generator.email` | 804 | 944 |  |
| `route1.mx.cloudflare.net` | 784 | 791 | yes |
| `route2.mx.cloudflare.net` | 784 | 791 | yes |
| `route3.mx.cloudflare.net` | 782 | 789 | yes |
| `park-mx.above.com` | 620 | 621 | yes |
| `mx.emlhub.com` | 462 | 462 |  |
| `aspmx.l.google.com` | 443 | 444 | yes |
| `alt1.aspmx.l.google.com` | 434 | 435 | yes |
| `alt2.aspmx.l.google.com` | 430 | 431 | yes |
| `emailfake.com` | 427 | 466 |  |
| `aero4.unstablemail.com` | 423 | 423 |  |
| `srv4.unstablemail.com` | 422 | 422 |  |
| `mx.emltmp.com` | 354 | 354 |  |
| `mx.spymail.one` | 349 | 349 |  |
| `mx.emlpro.com` | 336 | 336 |  |
| `eforward1.registrar-servers.com` | 332 | 333 | yes |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 1345 | 1368 |
| `mail.wallywatts.com` | 1345 | 1368 |
| `mx4.beavis99.com` | 984 | 985 |
| `mx4.beavis99.net` | 983 | 984 |
| `generator.email` | 804 | 944 |
| `mx.emlhub.com` | 462 | 462 |
| `emailfake.com` | 427 | 466 |
| `aero4.unstablemail.com` | 423 | 423 |
| `srv4.unstablemail.com` | 422 | 422 |
| `mx.emltmp.com` | 354 | 354 |
| `mx.spymail.one` | 349 | 349 |
| `mx.emlpro.com` | 336 | 336 |
| `tinyhost.shop` | 318 | 318 |
| `mx.dropmail.me` | 314 | 314 |
| `mx.freeml.net` | 298 | 298 |
| `mx37.m1bp.com` | 255 | 255 |
| `mx37.mb5p.com` | 255 | 255 |
| `mx.yomail.info` | 242 | 242 |
| `mx156.hostedmxserver.com` | 221 | 221 |
| `mx195.m1bp.com` | 217 | 218 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `78.47.124.133` | 2475 | 2475 |
| `94.130.108.80` | 2475 | 2475 |
| `116.202.9.167` | 1333 | 1352 |
| `46.101.111.206` | 1333 | 1352 |
| `142.132.166.12` | 1319 | 1339 |
| `188.166.111.252` | 1319 | 1339 |
| `91.196.52.205` | 1303 | 1485 |
| `13.223.25.84` | 1066 | 1066 |
| `54.243.117.197` | 1066 | 1066 |
| `188.245.74.208` | 965 | 966 |
| `195.201.18.63` | 950 | 951 |
| `162.159.205.17` | 798 | 804 |
| `162.159.205.18` | 798 | 804 |
| `162.159.205.19` | 798 | 804 |
| `162.159.205.23` | 796 | 802 |
| `162.159.205.24` | 796 | 802 |
| `162.159.205.25` | 796 | 802 |
| `162.159.205.11` | 794 | 800 |
| `162.159.205.12` | 794 | 800 |
| `162.159.205.13` | 794 | 800 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 290 |
| High-confidence disposable IPs | 754 |
| Promoted to `domains_inferred.txt` | 2 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**3173 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

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
| `10inbox.online` | `route1.mx.cloudflare.net` |
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


*… and 3,143 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
