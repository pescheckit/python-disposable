# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-09-30 02:33 UTC**.*  
*Last DNS snapshot: **2026-09-30T02:27:10+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 78,045 |
| `domains_strict.txt` | 78,082 |
| `domains_inferred.txt` (opt-in) | 2 |

## Reachability

Of **79,089** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 22,269 | 28.2% |
| A_ONLY | 4,965 | 6.3% |
| NXDOMAIN | 38,347 | 48.5% |
| NO_RECORDS | 807 | 1.0% |
| TIMEOUT | 12,701 | 16.1% |

**27,234 domains are mail-reachable today** (34.4%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `mail.wabblywabble.com` | 1199 | 1278 |  |
| `mail.wallywatts.com` | 1199 | 1278 |  |
| `mx4.beavis99.com` | 1069 | 1070 |  |
| `mx4.beavis99.net` | 1069 | 1070 |  |
| `route1.mx.cloudflare.net` | 901 | 914 | yes |
| `route2.mx.cloudflare.net` | 901 | 914 | yes |
| `route3.mx.cloudflare.net` | 899 | 912 | yes |
| `generator.email` | 656 | 762 |  |
| `email.chatgpt.org.uk` | 518 | 518 |  |
| `park-mx.above.com` | 466 | 471 | yes |
| `aero4.unstablemail.com` | 452 | 452 |  |
| `srv4.unstablemail.com` | 452 | 452 |  |
| `emailfake.com` | 451 | 476 |  |
| `mx.emlhub.com` | 439 | 439 |  |
| `aspmx.l.google.com` | 420 | 423 | yes |
| `alt1.aspmx.l.google.com` | 408 | 411 | yes |
| `alt2.aspmx.l.google.com` | 406 | 409 | yes |
| `email.gravityengine.cc` | 361 | 361 |  |
| `mx.spymail.one` | 351 | 351 |  |
| `mx.emltmp.com` | 341 | 341 |  |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 1199 | 1278 |
| `mail.wallywatts.com` | 1199 | 1278 |
| `mx4.beavis99.com` | 1069 | 1070 |
| `mx4.beavis99.net` | 1069 | 1070 |
| `generator.email` | 656 | 762 |
| `email.chatgpt.org.uk` | 518 | 518 |
| `aero4.unstablemail.com` | 452 | 452 |
| `srv4.unstablemail.com` | 452 | 452 |
| `emailfake.com` | 451 | 476 |
| `mx.emlhub.com` | 439 | 439 |
| `email.gravityengine.cc` | 361 | 361 |
| `mx.spymail.one` | 351 | 351 |
| `mx.emltmp.com` | 341 | 341 |
| `tinyhost.shop` | 339 | 339 |
| `mx.emlpro.com` | 324 | 324 |
| `mx.dropmail.me` | 295 | 295 |
| `mx.freeml.net` | 291 | 291 |
| `mx37.m1bp.com` | 238 | 238 |
| `mx37.mb5p.com` | 238 | 238 |
| `mx.yomail.info` | 215 | 215 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `78.47.124.133` | 2584 | 2584 |
| `94.130.108.80` | 2584 | 2584 |
| `116.202.9.167` | 1169 | 1239 |
| `46.101.111.206` | 1169 | 1239 |
| `142.132.166.12` | 1163 | 1234 |
| `188.166.111.252` | 1163 | 1234 |
| `91.196.52.205` | 1136 | 1269 |
| `188.245.74.208` | 1042 | 1043 |
| `195.201.18.63` | 1033 | 1034 |
| `13.223.25.84` | 994 | 996 |
| `54.243.117.197` | 994 | 996 |
| `162.159.205.23` | 899 | 910 |
| `162.159.205.24` | 899 | 910 |
| `162.159.205.25` | 899 | 910 |
| `162.159.205.17` | 890 | 902 |
| `162.159.205.18` | 890 | 902 |
| `162.159.205.19` | 890 | 902 |
| `162.159.205.11` | 877 | 888 |
| `162.159.205.12` | 877 | 888 |
| `162.159.205.13` | 877 | 888 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 306 |
| High-confidence disposable IPs | 801 |
| Promoted to `domains_inferred.txt` | 2 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**3079 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

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


*… and 3,049 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
