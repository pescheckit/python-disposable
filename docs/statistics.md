# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-09-29 02:22 UTC**.*  
*Last DNS snapshot: **2026-09-29T02:17:52+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 75,600 |
| `domains_strict.txt` | 75,631 |
| `domains_inferred.txt` (opt-in) | 2 |

## Reachability

Of **76,690** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 21,544 | 28.1% |
| A_ONLY | 4,939 | 6.4% |
| NXDOMAIN | 38,135 | 49.7% |
| NO_RECORDS | 688 | 0.9% |
| TIMEOUT | 11,384 | 14.8% |

**26,483 domains are mail-reachable today** (34.5%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `mail.wabblywabble.com` | 1192 | 1271 |  |
| `mail.wallywatts.com` | 1192 | 1271 |  |
| `mx4.beavis99.com` | 1070 | 1071 |  |
| `mx4.beavis99.net` | 1070 | 1071 |  |
| `route1.mx.cloudflare.net` | 897 | 910 | yes |
| `route2.mx.cloudflare.net` | 897 | 910 | yes |
| `route3.mx.cloudflare.net` | 895 | 908 | yes |
| `generator.email` | 606 | 737 |  |
| `email.chatgpt.org.uk` | 505 | 505 |  |
| `park-mx.above.com` | 466 | 471 | yes |
| `mx.emlhub.com` | 437 | 437 |  |
| `aspmx.l.google.com` | 420 | 423 | yes |
| `aero4.unstablemail.com` | 417 | 417 |  |
| `srv4.unstablemail.com` | 417 | 417 |  |
| `alt1.aspmx.l.google.com` | 409 | 412 | yes |
| `alt2.aspmx.l.google.com` | 407 | 410 | yes |
| `emailfake.com` | 395 | 430 |  |
| `email.gravityengine.cc` | 354 | 354 |  |
| `mx.spymail.one` | 353 | 353 |  |
| `mx.emltmp.com` | 342 | 342 |  |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 1192 | 1271 |
| `mail.wallywatts.com` | 1192 | 1271 |
| `mx4.beavis99.com` | 1070 | 1071 |
| `mx4.beavis99.net` | 1070 | 1071 |
| `generator.email` | 606 | 737 |
| `email.chatgpt.org.uk` | 505 | 505 |
| `mx.emlhub.com` | 437 | 437 |
| `aero4.unstablemail.com` | 417 | 417 |
| `srv4.unstablemail.com` | 417 | 417 |
| `emailfake.com` | 395 | 430 |
| `email.gravityengine.cc` | 354 | 354 |
| `mx.spymail.one` | 353 | 353 |
| `mx.emltmp.com` | 342 | 342 |
| `mx.emlpro.com` | 324 | 324 |
| `tinyhost.shop` | 313 | 313 |
| `mx.dropmail.me` | 298 | 298 |
| `mx.freeml.net` | 291 | 291 |
| `mx37.m1bp.com` | 218 | 218 |
| `mx37.mb5p.com` | 218 | 218 |
| `mx.yomail.info` | 215 | 215 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `78.47.124.133` | 2346 | 2346 |
| `94.130.108.80` | 2346 | 2346 |
| `116.202.9.167` | 1163 | 1233 |
| `46.101.111.206` | 1163 | 1233 |
| `142.132.166.12` | 1158 | 1229 |
| `188.166.111.252` | 1158 | 1229 |
| `91.196.52.205` | 1050 | 1216 |
| `188.245.74.208` | 1043 | 1044 |
| `195.201.18.63` | 1035 | 1036 |
| `13.223.25.84` | 993 | 995 |
| `54.243.117.197` | 993 | 995 |
| `162.159.205.23` | 895 | 906 |
| `162.159.205.24` | 895 | 906 |
| `162.159.205.25` | 895 | 906 |
| `162.159.205.17` | 885 | 897 |
| `162.159.205.18` | 885 | 897 |
| `162.159.205.19` | 885 | 897 |
| `162.159.205.11` | 872 | 883 |
| `162.159.205.12` | 872 | 883 |
| `162.159.205.13` | 872 | 883 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 301 |
| High-confidence disposable IPs | 799 |
| Promoted to `domains_inferred.txt` | 2 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**3073 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

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
| `14n.co.uk` | `14n-co-uk.mail.protection.outlook.com` |
| `14p.in` | `eforward1.registrar-servers.com` |
| `15qm-mail.red` | `eforward1.registrar-servers.com` |
| `189.email` | `route1.mx.cloudflare.net` |
| `1987.com` | `park-mx.above.com` |
| `1c-spec.ru` | `mx.yandex.ru` |


*… and 3,043 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
