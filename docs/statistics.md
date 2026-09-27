# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-09-27 02:29 UTC**.*  
*Last DNS snapshot: **2026-09-27T02:24:46+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 75,391 |
| `domains_strict.txt` | 75,422 |
| `domains_inferred.txt` (opt-in) | 2 |

## Reachability

Of **76,480** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 21,558 | 28.2% |
| A_ONLY | 4,963 | 6.5% |
| NXDOMAIN | 38,382 | 50.2% |
| NO_RECORDS | 702 | 0.9% |
| TIMEOUT | 10,875 | 14.2% |

**26,521 domains are mail-reachable today** (34.7%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `mail.wabblywabble.com` | 1193 | 1272 |  |
| `mail.wallywatts.com` | 1193 | 1272 |  |
| `mx4.beavis99.com` | 1081 | 1082 |  |
| `mx4.beavis99.net` | 1081 | 1082 |  |
| `route1.mx.cloudflare.net` | 920 | 933 | yes |
| `route2.mx.cloudflare.net` | 920 | 933 | yes |
| `route3.mx.cloudflare.net` | 918 | 931 | yes |
| `generator.email` | 622 | 759 |  |
| `park-mx.above.com` | 465 | 470 | yes |
| `mx.emlhub.com` | 439 | 439 |  |
| `aspmx.l.google.com` | 422 | 425 | yes |
| `aero4.unstablemail.com` | 418 | 418 |  |
| `srv4.unstablemail.com` | 418 | 418 |  |
| `alt1.aspmx.l.google.com` | 411 | 414 | yes |
| `alt2.aspmx.l.google.com` | 408 | 411 | yes |
| `emailfake.com` | 397 | 434 |  |
| `email.gravityengine.cc` | 354 | 354 |  |
| `mx.spymail.one` | 353 | 353 |  |
| `email.chatgpt.org.uk` | 352 | 352 |  |
| `mx.emltmp.com` | 343 | 343 |  |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 1193 | 1272 |
| `mail.wallywatts.com` | 1193 | 1272 |
| `mx4.beavis99.com` | 1081 | 1082 |
| `mx4.beavis99.net` | 1081 | 1082 |
| `generator.email` | 622 | 759 |
| `mx.emlhub.com` | 439 | 439 |
| `aero4.unstablemail.com` | 418 | 418 |
| `srv4.unstablemail.com` | 418 | 418 |
| `emailfake.com` | 397 | 434 |
| `email.gravityengine.cc` | 354 | 354 |
| `mx.spymail.one` | 353 | 353 |
| `email.chatgpt.org.uk` | 352 | 352 |
| `mx.emltmp.com` | 343 | 343 |
| `mx.emlpro.com` | 327 | 327 |
| `tinyhost.shop` | 318 | 318 |
| `mx.dropmail.me` | 297 | 297 |
| `mx.freeml.net` | 291 | 291 |
| `mx37.m1bp.com` | 222 | 222 |
| `mx37.mb5p.com` | 222 | 222 |
| `mx.yomail.info` | 214 | 214 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `78.47.124.133` | 2353 | 2353 |
| `94.130.108.80` | 2353 | 2353 |
| `116.202.9.167` | 1165 | 1235 |
| `46.101.111.206` | 1165 | 1235 |
| `142.132.166.12` | 1159 | 1230 |
| `188.166.111.252` | 1159 | 1230 |
| `91.196.52.205` | 1075 | 1249 |
| `188.245.74.208` | 1060 | 1061 |
| `195.201.18.63` | 1042 | 1043 |
| `13.223.25.84` | 993 | 995 |
| `54.243.117.197` | 993 | 995 |
| `162.159.205.23` | 918 | 929 |
| `162.159.205.24` | 918 | 929 |
| `162.159.205.25` | 918 | 929 |
| `162.159.205.17` | 911 | 923 |
| `162.159.205.18` | 911 | 923 |
| `162.159.205.19` | 911 | 923 |
| `162.159.205.11` | 891 | 902 |
| `162.159.205.12` | 891 | 902 |
| `162.159.205.13` | 891 | 902 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 303 |
| High-confidence disposable IPs | 801 |
| Promoted to `domains_inferred.txt` | 2 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**3096 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

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


*… and 3,066 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
