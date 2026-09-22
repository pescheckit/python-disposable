# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-09-22 02:31 UTC**.*  
*Last DNS snapshot: **2026-09-22T02:20:22+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 75,321 |
| `domains_strict.txt` | 75,352 |
| `domains_inferred.txt` (opt-in) | 2 |

## Reachability

Of **76,381** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 23,777 | 31.1% |
| A_ONLY | 5,482 | 7.2% |
| NXDOMAIN | 42,139 | 55.2% |
| NO_RECORDS | 807 | 1.1% |
| TIMEOUT | 4,176 | 5.5% |

**29,259 domains are mail-reachable today** (38.3%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `mail.wabblywabble.com` | 1315 | 1391 |  |
| `mail.wallywatts.com` | 1315 | 1391 |  |
| `mx4.beavis99.com` | 1156 | 1157 |  |
| `mx4.beavis99.net` | 1156 | 1157 |  |
| `route2.mx.cloudflare.net` | 1007 | 1020 | yes |
| `route1.mx.cloudflare.net` | 1006 | 1019 | yes |
| `route3.mx.cloudflare.net` | 1005 | 1018 | yes |
| `generator.email` | 717 | 854 |  |
| `park-mx.above.com` | 509 | 514 | yes |
| `aero4.unstablemail.com` | 478 | 478 |  |
| `srv4.unstablemail.com` | 478 | 478 |  |
| `mx.emlhub.com` | 464 | 464 |  |
| `aspmx.l.google.com` | 461 | 463 | yes |
| `alt1.aspmx.l.google.com` | 452 | 454 | yes |
| `alt2.aspmx.l.google.com` | 449 | 451 | yes |
| `emailfake.com` | 444 | 481 |  |
| `email.chatgpt.org.uk` | 420 | 420 |  |
| `email.gravityengine.cc` | 382 | 382 |  |
| `mx.spymail.one` | 379 | 379 |  |
| `mx.emltmp.com` | 367 | 367 |  |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 1315 | 1391 |
| `mail.wallywatts.com` | 1315 | 1391 |
| `mx4.beavis99.com` | 1156 | 1157 |
| `mx4.beavis99.net` | 1156 | 1157 |
| `generator.email` | 717 | 854 |
| `aero4.unstablemail.com` | 478 | 478 |
| `srv4.unstablemail.com` | 478 | 478 |
| `mx.emlhub.com` | 464 | 464 |
| `emailfake.com` | 444 | 481 |
| `email.chatgpt.org.uk` | 420 | 420 |
| `email.gravityengine.cc` | 382 | 382 |
| `mx.spymail.one` | 379 | 379 |
| `mx.emltmp.com` | 367 | 367 |
| `mx.emlpro.com` | 350 | 350 |
| `tinyhost.shop` | 334 | 334 |
| `mx.dropmail.me` | 331 | 331 |
| `mx.freeml.net` | 314 | 314 |
| `vietxf.com` | 272 | 272 |
| `mail.casadorock.com` | 242 | 242 |
| `mx.yomail.info` | 242 | 242 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `78.47.124.133` | 2596 | 2596 |
| `94.130.108.80` | 2596 | 2596 |
| `116.202.9.167` | 1295 | 1362 |
| `46.101.111.206` | 1295 | 1362 |
| `142.132.166.12` | 1294 | 1362 |
| `188.166.111.252` | 1294 | 1362 |
| `91.196.52.205` | 1223 | 1397 |
| `188.245.74.208` | 1144 | 1145 |
| `195.201.18.63` | 1128 | 1129 |
| `13.223.25.84` | 1113 | 1114 |
| `54.243.117.197` | 1113 | 1114 |
| `162.159.205.23` | 1014 | 1025 |
| `162.159.205.24` | 1014 | 1025 |
| `162.159.205.25` | 1014 | 1025 |
| `162.159.205.17` | 1010 | 1022 |
| `162.159.205.18` | 1010 | 1022 |
| `162.159.205.19` | 1010 | 1022 |
| `162.159.205.11` | 1002 | 1013 |
| `162.159.205.12` | 1002 | 1013 |
| `162.159.205.13` | 1002 | 1013 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 313 |
| High-confidence disposable IPs | 814 |
| Promoted to `domains_inferred.txt` | 2 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**3382 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

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
| `0live.org` | `route1.mx.cloudflare.net` |
| `0nce.net` | `route1.mx.cloudflare.net` |
| `0regon.org` | `route1.mx.cloudflare.net` |
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
| `12storage.com` | `route1.mx.cloudflare.net` |
| `13dk.net` | `route1.mx.cloudflare.net` |
| `14n.co.uk` | `14n-co-uk.mail.protection.outlook.com` |
| `14p.in` | `eforward1.registrar-servers.com` |
| `15qm-mail.red` | `eforward1.registrar-servers.com` |
| `189.email` | `route1.mx.cloudflare.net` |


*… and 3,352 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
