# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-09-10 02:29 UTC**.*  
*Last DNS snapshot: **2026-09-10T02:29:36+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 75,262 |
| `domains_strict.txt` | 75,293 |
| `domains_inferred.txt` (opt-in) | 2 |

## Reachability

Of **76,242** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 20,843 | 27.3% |
| A_ONLY | 4,623 | 6.1% |
| NXDOMAIN | 36,818 | 48.3% |
| NO_RECORDS | 682 | 0.9% |
| TIMEOUT | 13,276 | 17.4% |

**25,466 domains are mail-reachable today** (33.4%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `mail.wabblywabble.com` | 1140 | 1209 |  |
| `mail.wallywatts.com` | 1140 | 1209 |  |
| `mx4.beavis99.com` | 999 | 1000 |  |
| `mx4.beavis99.net` | 999 | 1000 |  |
| `route2.mx.cloudflare.net` | 868 | 879 | yes |
| `route1.mx.cloudflare.net` | 867 | 878 | yes |
| `route3.mx.cloudflare.net` | 866 | 877 | yes |
| `generator.email` | 688 | 825 |  |
| `park-mx.above.com` | 453 | 458 | yes |
| `mx.emlhub.com` | 416 | 416 |  |
| `aero4.unstablemail.com` | 405 | 405 |  |
| `srv4.unstablemail.com` | 405 | 405 |  |
| `emailfake.com` | 403 | 440 |  |
| `aspmx.l.google.com` | 382 | 384 | yes |
| `alt1.aspmx.l.google.com` | 373 | 375 | yes |
| `alt2.aspmx.l.google.com` | 369 | 371 | yes |
| `mx.spymail.one` | 339 | 339 |  |
| `tinyhost.shop` | 336 | 336 |  |
| `mx.emltmp.com` | 323 | 323 |  |
| `mx.emlpro.com` | 311 | 311 |  |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 1140 | 1209 |
| `mail.wallywatts.com` | 1140 | 1209 |
| `mx4.beavis99.com` | 999 | 1000 |
| `mx4.beavis99.net` | 999 | 1000 |
| `generator.email` | 688 | 825 |
| `mx.emlhub.com` | 416 | 416 |
| `aero4.unstablemail.com` | 405 | 405 |
| `srv4.unstablemail.com` | 405 | 405 |
| `emailfake.com` | 403 | 440 |
| `mx.spymail.one` | 339 | 339 |
| `tinyhost.shop` | 336 | 336 |
| `mx.emltmp.com` | 323 | 323 |
| `mx.emlpro.com` | 311 | 311 |
| `email.chatgpt.org.uk` | 305 | 305 |
| `mx.dropmail.me` | 295 | 295 |
| `mx.freeml.net` | 278 | 278 |
| `vietxf.com` | 250 | 250 |
| `mail.casadorock.com` | 228 | 228 |
| `mx.yomail.info` | 210 | 210 |
| `mx37.m1bp.com` | 206 | 206 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `78.47.124.133` | 2293 | 2293 |
| `94.130.108.80` | 2293 | 2293 |
| `91.196.52.205` | 1138 | 1312 |
| `116.202.9.167` | 1102 | 1162 |
| `46.101.111.206` | 1102 | 1162 |
| `142.132.166.12` | 1098 | 1159 |
| `188.166.111.252` | 1098 | 1159 |
| `188.245.74.208` | 976 | 977 |
| `195.201.18.63` | 965 | 966 |
| `13.223.25.84` | 934 | 934 |
| `54.243.117.197` | 934 | 934 |
| `162.159.205.23` | 868 | 877 |
| `162.159.205.24` | 868 | 877 |
| `162.159.205.25` | 868 | 877 |
| `162.159.205.17` | 866 | 876 |
| `162.159.205.18` | 866 | 876 |
| `162.159.205.19` | 866 | 876 |
| `162.159.205.11` | 862 | 871 |
| `162.159.205.12` | 862 | 871 |
| `162.159.205.13` | 862 | 871 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 281 |
| High-confidence disposable IPs | 757 |
| Promoted to `domains_inferred.txt` | 2 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**2938 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

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


*… and 2,908 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
