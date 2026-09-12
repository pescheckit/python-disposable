# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-09-12 02:34 UTC**.*  
*Last DNS snapshot: **2026-09-12T02:24:14+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 75,280 |
| `domains_strict.txt` | 75,311 |
| `domains_inferred.txt` (opt-in) | 2 |

## Reachability

Of **76,274** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 22,508 | 29.5% |
| A_ONLY | 5,140 | 6.7% |
| NXDOMAIN | 39,572 | 51.9% |
| NO_RECORDS | 762 | 1.0% |
| TIMEOUT | 8,292 | 10.9% |

**27,648 domains are mail-reachable today** (36.2%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `mail.wabblywabble.com` | 1262 | 1331 |  |
| `mail.wallywatts.com` | 1262 | 1331 |  |
| `mx4.beavis99.com` | 1093 | 1094 |  |
| `mx4.beavis99.net` | 1093 | 1094 |  |
| `route2.mx.cloudflare.net` | 945 | 957 | yes |
| `route1.mx.cloudflare.net` | 944 | 956 | yes |
| `route3.mx.cloudflare.net` | 943 | 955 | yes |
| `generator.email` | 700 | 837 |  |
| `park-mx.above.com` | 483 | 488 | yes |
| `aero4.unstablemail.com` | 448 | 448 |  |
| `srv4.unstablemail.com` | 448 | 448 |  |
| `mx.emlhub.com` | 440 | 440 |  |
| `emailfake.com` | 429 | 466 |  |
| `aspmx.l.google.com` | 420 | 422 | yes |
| `alt1.aspmx.l.google.com` | 412 | 414 | yes |
| `alt2.aspmx.l.google.com` | 408 | 410 | yes |
| `email.chatgpt.org.uk` | 405 | 405 |  |
| `email.gravityengine.cc` | 369 | 369 |  |
| `mx.spymail.one` | 354 | 354 |  |
| `mx.emltmp.com` | 349 | 349 |  |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 1262 | 1331 |
| `mail.wallywatts.com` | 1262 | 1331 |
| `mx4.beavis99.com` | 1093 | 1094 |
| `mx4.beavis99.net` | 1093 | 1094 |
| `generator.email` | 700 | 837 |
| `aero4.unstablemail.com` | 448 | 448 |
| `srv4.unstablemail.com` | 448 | 448 |
| `mx.emlhub.com` | 440 | 440 |
| `emailfake.com` | 429 | 466 |
| `email.chatgpt.org.uk` | 405 | 405 |
| `email.gravityengine.cc` | 369 | 369 |
| `mx.spymail.one` | 354 | 354 |
| `mx.emltmp.com` | 349 | 349 |
| `mx.emlpro.com` | 328 | 328 |
| `mx.dropmail.me` | 308 | 308 |
| `tinyhost.shop` | 304 | 304 |
| `mx.freeml.net` | 296 | 296 |
| `vietxf.com` | 250 | 250 |
| `mx.yomail.info` | 225 | 225 |
| `mail.casadorock.com` | 223 | 223 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `78.47.124.133` | 2450 | 2450 |
| `94.130.108.80` | 2450 | 2450 |
| `116.202.9.167` | 1227 | 1287 |
| `46.101.111.206` | 1227 | 1287 |
| `142.132.166.12` | 1224 | 1285 |
| `188.166.111.252` | 1224 | 1285 |
| `91.196.52.205` | 1194 | 1368 |
| `188.245.74.208` | 1076 | 1077 |
| `195.201.18.63` | 1061 | 1062 |
| `13.223.25.84` | 1035 | 1035 |
| `54.243.117.197` | 1035 | 1035 |
| `162.159.205.23` | 953 | 963 |
| `162.159.205.24` | 953 | 963 |
| `162.159.205.25` | 953 | 963 |
| `162.159.205.17` | 948 | 959 |
| `162.159.205.18` | 948 | 959 |
| `162.159.205.19` | 948 | 959 |
| `162.159.205.11` | 942 | 952 |
| `162.159.205.12` | 942 | 952 |
| `162.159.205.13` | 942 | 952 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 299 |
| High-confidence disposable IPs | 775 |
| Promoted to `domains_inferred.txt` | 2 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**3181 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

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
| `117.yyolf.net` | `route1.mx.cloudflare.net` |
| `11cows.com` | `mxa.mailgun.org` |
| `123gmail.com` | `park-mx.above.com` |
| `12499aaa.com` | `eforward1.registrar-servers.com` |
| `12storage.com` | `route1.mx.cloudflare.net` |
| `13dk.net` | `route1.mx.cloudflare.net` |
| `14n.co.uk` | `14n-co-uk.mail.protection.outlook.com` |
| `14p.in` | `eforward1.registrar-servers.com` |
| `15qm-mail.red` | `eforward1.registrar-servers.com` |
| `189.email` | `route1.mx.cloudflare.net` |
| `1987.com` | `park-mx.above.com` |


*… and 3,151 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
