# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-09-15 02:21 UTC**.*  
*Last DNS snapshot: **2026-09-15T02:16:32+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 75,284 |
| `domains_strict.txt` | 75,315 |
| `domains_inferred.txt` (opt-in) | 2 |

## Reachability

Of **76,298** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 22,159 | 29.0% |
| A_ONLY | 5,082 | 6.7% |
| NXDOMAIN | 39,006 | 51.1% |
| NO_RECORDS | 742 | 1.0% |
| TIMEOUT | 9,309 | 12.2% |

**27,241 domains are mail-reachable today** (35.7%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `mail.wabblywabble.com` | 1230 | 1303 |  |
| `mail.wallywatts.com` | 1230 | 1303 |  |
| `mx4.beavis99.com` | 1087 | 1088 |  |
| `mx4.beavis99.net` | 1087 | 1088 |  |
| `route2.mx.cloudflare.net` | 929 | 941 | yes |
| `route1.mx.cloudflare.net` | 928 | 940 | yes |
| `route3.mx.cloudflare.net` | 927 | 939 | yes |
| `generator.email` | 663 | 800 |  |
| `park-mx.above.com` | 481 | 486 | yes |
| `aero4.unstablemail.com` | 449 | 449 |  |
| `srv4.unstablemail.com` | 449 | 449 |  |
| `mx.emlhub.com` | 416 | 416 |  |
| `aspmx.l.google.com` | 415 | 417 | yes |
| `alt1.aspmx.l.google.com` | 407 | 409 | yes |
| `alt2.aspmx.l.google.com` | 403 | 405 | yes |
| `email.chatgpt.org.uk` | 403 | 403 |  |
| `emailfake.com` | 402 | 439 |  |
| `email.gravityengine.cc` | 359 | 359 |  |
| `mx.spymail.one` | 354 | 354 |  |
| `mx.emltmp.com` | 349 | 349 |  |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 1230 | 1303 |
| `mail.wallywatts.com` | 1230 | 1303 |
| `mx4.beavis99.com` | 1087 | 1088 |
| `mx4.beavis99.net` | 1087 | 1088 |
| `generator.email` | 663 | 800 |
| `aero4.unstablemail.com` | 449 | 449 |
| `srv4.unstablemail.com` | 449 | 449 |
| `mx.emlhub.com` | 416 | 416 |
| `email.chatgpt.org.uk` | 403 | 403 |
| `emailfake.com` | 402 | 439 |
| `email.gravityengine.cc` | 359 | 359 |
| `mx.spymail.one` | 354 | 354 |
| `mx.emltmp.com` | 349 | 349 |
| `mx.emlpro.com` | 328 | 328 |
| `mx.dropmail.me` | 307 | 307 |
| `tinyhost.shop` | 298 | 298 |
| `mx.freeml.net` | 296 | 296 |
| `vietxf.com` | 250 | 250 |
| `mx.yomail.info` | 225 | 225 |
| `mail.casadorock.com` | 222 | 222 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `78.47.124.133` | 2418 | 2418 |
| `94.130.108.80` | 2418 | 2418 |
| `116.202.9.167` | 1191 | 1255 |
| `46.101.111.206` | 1191 | 1255 |
| `142.132.166.12` | 1186 | 1251 |
| `188.166.111.252` | 1186 | 1251 |
| `91.196.52.205` | 1122 | 1296 |
| `188.245.74.208` | 1070 | 1071 |
| `195.201.18.63` | 1056 | 1057 |
| `13.223.25.84` | 1030 | 1031 |
| `54.243.117.197` | 1030 | 1031 |
| `162.159.205.23` | 933 | 943 |
| `162.159.205.24` | 933 | 943 |
| `162.159.205.25` | 933 | 943 |
| `162.159.205.17` | 931 | 942 |
| `162.159.205.18` | 931 | 942 |
| `162.159.205.19` | 931 | 942 |
| `162.159.205.11` | 924 | 934 |
| `162.159.205.12` | 924 | 934 |
| `162.159.205.13` | 924 | 934 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 298 |
| High-confidence disposable IPs | 762 |
| Promoted to `domains_inferred.txt` | 2 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**3154 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

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


*… and 3,124 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
