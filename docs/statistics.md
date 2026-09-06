# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-09-06 02:22 UTC**.*  
*Last DNS snapshot: **2026-09-06T02:14:33+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 75,260 |
| `domains_strict.txt` | 75,291 |
| `domains_inferred.txt` (opt-in) | 2 |

## Reachability

Of **76,206** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 21,374 | 28.0% |
| A_ONLY | 4,811 | 6.3% |
| NXDOMAIN | 38,298 | 50.3% |
| NO_RECORDS | 688 | 0.9% |
| TIMEOUT | 11,035 | 14.5% |

**26,185 domains are mail-reachable today** (34.4%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `mail.wabblywabble.com` | 1163 | 1227 |  |
| `mail.wallywatts.com` | 1163 | 1227 |  |
| `mx4.beavis99.com` | 1019 | 1020 |  |
| `mx4.beavis99.net` | 1019 | 1020 |  |
| `route2.mx.cloudflare.net` | 882 | 893 | yes |
| `route1.mx.cloudflare.net` | 881 | 892 | yes |
| `route3.mx.cloudflare.net` | 880 | 891 | yes |
| `generator.email` | 707 | 844 |  |
| `tinyhost.shop` | 582 | 582 |  |
| `park-mx.above.com` | 473 | 478 | yes |
| `mx.emlhub.com` | 421 | 421 |  |
| `emailfake.com` | 417 | 454 |  |
| `aero4.unstablemail.com` | 414 | 414 |  |
| `srv4.unstablemail.com` | 414 | 414 |  |
| `aspmx.l.google.com` | 400 | 402 | yes |
| `alt1.aspmx.l.google.com` | 391 | 393 | yes |
| `alt2.aspmx.l.google.com` | 387 | 389 | yes |
| `mx.spymail.one` | 343 | 343 |  |
| `mx.emltmp.com` | 331 | 331 |  |
| `mx.emlpro.com` | 324 | 324 |  |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 1163 | 1227 |
| `mail.wallywatts.com` | 1163 | 1227 |
| `mx4.beavis99.com` | 1019 | 1020 |
| `mx4.beavis99.net` | 1019 | 1020 |
| `generator.email` | 707 | 844 |
| `tinyhost.shop` | 582 | 582 |
| `mx.emlhub.com` | 421 | 421 |
| `emailfake.com` | 417 | 454 |
| `aero4.unstablemail.com` | 414 | 414 |
| `srv4.unstablemail.com` | 414 | 414 |
| `mx.spymail.one` | 343 | 343 |
| `mx.emltmp.com` | 331 | 331 |
| `mx.emlpro.com` | 324 | 324 |
| `email.chatgpt.org.uk` | 323 | 323 |
| `mx.dropmail.me` | 304 | 304 |
| `mx.freeml.net` | 279 | 279 |
| `mx.yomail.info` | 220 | 220 |
| `mx37.m1bp.com` | 213 | 213 |
| `mx37.mb5p.com` | 213 | 213 |
| `mail.casadorock.com` | 212 | 212 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `78.47.124.133` | 2320 | 2320 |
| `94.130.108.80` | 2320 | 2320 |
| `91.196.52.205` | 1173 | 1347 |
| `116.202.9.167` | 1134 | 1189 |
| `46.101.111.206` | 1134 | 1189 |
| `142.132.166.12` | 1132 | 1188 |
| `188.166.111.252` | 1132 | 1188 |
| `188.245.74.208` | 993 | 994 |
| `195.201.18.63` | 984 | 985 |
| `13.223.25.84` | 982 | 982 |
| `54.243.117.197` | 982 | 982 |
| `162.159.205.23` | 879 | 888 |
| `162.159.205.24` | 879 | 888 |
| `162.159.205.25` | 879 | 888 |
| `162.159.205.17` | 876 | 886 |
| `162.159.205.18` | 876 | 886 |
| `162.159.205.19` | 876 | 886 |
| `162.159.205.11` | 875 | 884 |
| `162.159.205.12` | 875 | 884 |
| `162.159.205.13` | 875 | 884 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 285 |
| High-confidence disposable IPs | 771 |
| Promoted to `domains_inferred.txt` | 2 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**3022 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

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
| `11cows.com` | `mxa.mailgun.org` |
| `123gmail.com` | `park-mx.above.com` |
| `12499aaa.com` | `eforward1.registrar-servers.com` |
| `129.in` | `park-mx.above.com` |
| `12storage.com` | `park-mx.above.com` |
| `13dk.net` | `route1.mx.cloudflare.net` |
| `14n.co.uk` | `14n-co-uk.mail.protection.outlook.com` |
| `14p.in` | `eforward1.registrar-servers.com` |
| `15qm-mail.red` | `eforward1.registrar-servers.com` |
| `189.email` | `route1.mx.cloudflare.net` |
| `1987.com` | `park-mx.above.com` |


*… and 2,992 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
