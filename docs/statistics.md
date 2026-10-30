# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-10-30 02:19 UTC**.*  
*Last DNS snapshot: **2026-10-30T02:13:59+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 98,543 |
| `domains_strict.txt` | 99,775 |
| `domains_inferred.txt` (opt-in) | 4 |

## Reachability

Of **102,706** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 40,951 | 39.9% |
| A_ONLY | 4,245 | 4.1% |
| NXDOMAIN | 31,437 | 30.6% |
| NO_RECORDS | 887 | 0.9% |
| TIMEOUT | 25,186 | 24.5% |

**45,196 domains are mail-reachable today** (44.0%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `route1.mx.cloudflare.net` | 2450 | 2612 | yes |
| `route2.mx.cloudflare.net` | 2450 | 2612 | yes |
| `route3.mx.cloudflare.net` | 2449 | 2611 | yes |
| `mail.wabblywabble.com` | 1615 | 1616 |  |
| `mail.wallywatts.com` | 1615 | 1616 |  |
| `generator.email` | 1257 | 1477 |  |
| `aero4.unstablemail.com` | 1200 | 1201 |  |
| `srv4.unstablemail.com` | 1198 | 1199 |  |
| `smtp.yopmail.com` | 1079 | 1087 |  |
| `mx4.beavis99.com` | 972 | 972 |  |
| `mx4.beavis99.net` | 971 | 971 |  |
| `park-mx.above.com` | 938 | 1029 | yes |
| `aspmx.l.google.com` | 838 | 923 | yes |
| `alt1.aspmx.l.google.com` | 823 | 906 | yes |
| `alt2.aspmx.l.google.com` | 818 | 899 | yes |
| `eforward1.registrar-servers.com` | 814 | 844 | yes |
| `eforward2.registrar-servers.com` | 814 | 844 | yes |
| `eforward3.registrar-servers.com` | 814 | 844 | yes |
| `eforward4.registrar-servers.com` | 814 | 844 | yes |
| `eforward5.registrar-servers.com` | 814 | 844 | yes |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 1615 | 1616 |
| `mail.wallywatts.com` | 1615 | 1616 |
| `generator.email` | 1257 | 1477 |
| `aero4.unstablemail.com` | 1200 | 1201 |
| `srv4.unstablemail.com` | 1198 | 1199 |
| `smtp.yopmail.com` | 1079 | 1087 |
| `mx4.beavis99.com` | 972 | 972 |
| `mx4.beavis99.net` | 971 | 971 |
| `emailfake.com` | 645 | 657 |
| `email.chatgpt.org.uk` | 615 | 619 |
| `tinyhost.shop` | 413 | 413 |
| `mx.emlhub.com` | 367 | 367 |
| `smtp.215.im` | 334 | 337 |
| `mx2-hosting.jellyfish.systems` | 332 | 342 |
| `mx3-hosting.jellyfish.systems` | 332 | 342 |
| `mx1-hosting.jellyfish.systems` | 331 | 341 |
| `mx2.timeweb.ru` | 331 | 362 |
| `mx1.timeweb.ru` | 330 | 361 |
| `mx156.hostedmxserver.com` | 314 | 434 |
| `mail.h-email.net` | 302 | 374 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `162.159.205.23` | 2403 | 2562 |
| `162.159.205.24` | 2403 | 2562 |
| `162.159.205.25` | 2403 | 2562 |
| `162.159.205.17` | 2395 | 2553 |
| `162.159.205.18` | 2395 | 2553 |
| `162.159.205.19` | 2395 | 2553 |
| `162.159.205.11` | 2372 | 2530 |
| `162.159.205.12` | 2372 | 2530 |
| `162.159.205.13` | 2372 | 2530 |
| `78.47.124.133` | 2230 | 2230 |
| `94.130.108.80` | 2230 | 2230 |
| `91.196.52.205` | 2079 | 2306 |
| `116.202.9.167` | 1509 | 1510 |
| `46.101.111.206` | 1509 | 1510 |
| `142.132.166.12` | 1504 | 1504 |
| `188.166.111.252` | 1504 | 1504 |
| `146.190.212.90` | 1153 | 1154 |
| `195.123.189.142` | 1149 | 1209 |
| `146.190.223.124` | 1143 | 1144 |
| `87.98.164.155` | 1137 | 1145 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 430 |
| High-confidence disposable IPs | 1,052 |
| Promoted to `domains_inferred.txt` | 4 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**7614 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

| Listed disposable | MX (shared infra) |
|---|---|
| `0-30-24.com` | `alt1.aspmx.l.google.com` |
| `0-mail.com` | `park-mx.above.com` |
| `000476.com` | `park-mx.above.com` |
| `000728.xyz` | `route1.mx.cloudflare.net` |
| `001218.xyz` | `route1.mx.cloudflare.net` |
| `001310.xyz` | `route1.mx.cloudflare.net` |
| `005005.xyz` | `route1.mx.cloudflare.net` |
| `0055betplataforma.com` | `route1.mx.cloudflare.net` |
| `0058.ru` | `alt1.aspmx.l.google.com` |
| `007bet.info` | `park-mx.above.com` |
| `007gamecasino.net` | `park-mx.above.com` |
| `007jlbu.com` | `route1.mx.cloudflare.net` |
| `007jlphp.com` | `route1.mx.cloudflare.net` |
| `008686.xyz` | `route1.mx.cloudflare.net` |
| `00gmail.com` | `park-mx.above.com` |
| `010608.xyz` | `route1.mx.cloudflare.net` |
| `010hb.com` | `route1.mx.cloudflare.net` |
| `012356.xyz` | `route1.mx.cloudflare.net` |
| `012pg.bet` | `route1.mx.cloudflare.net` |
| `01g.cloud` | `alt1.aspmx.l.google.com` |
| `01p.co.jp` | `01p-co-jp.mail.protection.outlook.com` |
| `020307.xyz` | `route1.mx.cloudflare.net` |
| `041998.xyz` | `mx1.alias.proton.me` |
| `0500betvip.com` | `route1.mx.cloudflare.net` |
| `057gmail.com` | `route1.mx.cloudflare.net` |
| `099833.xyz` | `park-mx.above.com` |
| `0ak.org` | `mx00.ionos.com` |
| `0hcow.com` | `mxa.mailgun.org` |
| `0hio.net` | `aspmx1.migadu.com` |
| `0nce.net` | `route1.mx.cloudflare.net` |


*… and 7,584 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
