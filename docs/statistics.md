# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-09-26 02:27 UTC**.*  
*Last DNS snapshot: **2026-09-26T02:21:54+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 75,388 |
| `domains_strict.txt` | 75,419 |
| `domains_inferred.txt` (opt-in) | 2 |

## Reachability

Of **76,469** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 21,514 | 28.1% |
| A_ONLY | 4,927 | 6.4% |
| NXDOMAIN | 38,290 | 50.1% |
| NO_RECORDS | 705 | 0.9% |
| TIMEOUT | 11,033 | 14.4% |

**26,441 domains are mail-reachable today** (34.6%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `mail.wabblywabble.com` | 1173 | 1250 |  |
| `mail.wallywatts.com` | 1173 | 1250 |  |
| `mx4.beavis99.com` | 1072 | 1073 |  |
| `mx4.beavis99.net` | 1072 | 1073 |  |
| `route2.mx.cloudflare.net` | 932 | 945 | yes |
| `route1.mx.cloudflare.net` | 931 | 944 | yes |
| `route3.mx.cloudflare.net` | 930 | 943 | yes |
| `generator.email` | 631 | 768 |  |
| `park-mx.above.com` | 470 | 475 | yes |
| `mx.emlhub.com` | 439 | 439 |  |
| `aero4.unstablemail.com` | 425 | 425 |  |
| `srv4.unstablemail.com` | 425 | 425 |  |
| `aspmx.l.google.com` | 424 | 427 | yes |
| `alt1.aspmx.l.google.com` | 414 | 417 | yes |
| `alt2.aspmx.l.google.com` | 412 | 415 | yes |
| `emailfake.com` | 402 | 439 |  |
| `mx.spymail.one` | 354 | 354 |  |
| `email.gravityengine.cc` | 353 | 353 |  |
| `mx.emltmp.com` | 349 | 349 |  |
| `email.chatgpt.org.uk` | 345 | 345 |  |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 1173 | 1250 |
| `mail.wallywatts.com` | 1173 | 1250 |
| `mx4.beavis99.com` | 1072 | 1073 |
| `mx4.beavis99.net` | 1072 | 1073 |
| `generator.email` | 631 | 768 |
| `mx.emlhub.com` | 439 | 439 |
| `aero4.unstablemail.com` | 425 | 425 |
| `srv4.unstablemail.com` | 425 | 425 |
| `emailfake.com` | 402 | 439 |
| `mx.spymail.one` | 354 | 354 |
| `email.gravityengine.cc` | 353 | 353 |
| `mx.emltmp.com` | 349 | 349 |
| `email.chatgpt.org.uk` | 345 | 345 |
| `mx.emlpro.com` | 326 | 326 |
| `tinyhost.shop` | 320 | 320 |
| `mx.dropmail.me` | 302 | 302 |
| `mx.freeml.net` | 294 | 294 |
| `mx37.m1bp.com` | 220 | 220 |
| `mx37.mb5p.com` | 220 | 220 |
| `mx.yomail.info` | 219 | 219 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `78.47.124.133` | 2382 | 2382 |
| `94.130.108.80` | 2382 | 2382 |
| `142.132.166.12` | 1147 | 1216 |
| `188.166.111.252` | 1147 | 1216 |
| `116.202.9.167` | 1145 | 1213 |
| `46.101.111.206` | 1145 | 1213 |
| `91.196.52.205` | 1082 | 1256 |
| `188.245.74.208` | 1051 | 1052 |
| `195.201.18.63` | 1035 | 1036 |
| `13.223.25.84` | 989 | 991 |
| `54.243.117.197` | 989 | 991 |
| `162.159.205.23` | 927 | 938 |
| `162.159.205.24` | 927 | 938 |
| `162.159.205.25` | 927 | 938 |
| `162.159.205.17` | 920 | 932 |
| `162.159.205.18` | 920 | 932 |
| `162.159.205.19` | 920 | 932 |
| `162.159.205.11` | 912 | 923 |
| `162.159.205.12` | 912 | 923 |
| `162.159.205.13` | 912 | 923 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 305 |
| High-confidence disposable IPs | 769 |
| Promoted to `domains_inferred.txt` | 2 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**3101 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

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


*… and 3,071 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
