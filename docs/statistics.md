# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-10-25 02:29 UTC**.*  
*Last DNS snapshot: **2026-10-25T02:28:59+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 98,428 |
| `domains_strict.txt` | 99,660 |
| `domains_inferred.txt` (opt-in) | 4 |

## Reachability

Of **102,420** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 47,203 | 46.1% |
| A_ONLY | 6,095 | 6.0% |
| NXDOMAIN | 42,884 | 41.9% |
| NO_RECORDS | 1,163 | 1.1% |
| TIMEOUT | 5,075 | 5.0% |

**53,298 domains are mail-reachable today** (52.0%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `route2.mx.cloudflare.net` | 2702 | 2859 | yes |
| `route1.mx.cloudflare.net` | 2701 | 2858 | yes |
| `route3.mx.cloudflare.net` | 2701 | 2858 | yes |
| `mail.wabblywabble.com` | 2018 | 2018 |  |
| `mail.wallywatts.com` | 2018 | 2018 |  |
| `generator.email` | 1446 | 1664 |  |
| `aero4.unstablemail.com` | 1331 | 1331 |  |
| `srv4.unstablemail.com` | 1329 | 1329 |  |
| `mx4.beavis99.com` | 1253 | 1253 |  |
| `mx4.beavis99.net` | 1252 | 1252 |  |
| `smtp.yopmail.com` | 1109 | 1117 |  |
| `park-mx.above.com` | 1070 | 1150 | yes |
| `aspmx.l.google.com` | 971 | 1054 | yes |
| `alt1.aspmx.l.google.com` | 954 | 1035 | yes |
| `alt2.aspmx.l.google.com` | 949 | 1028 | yes |
| `eforward1.registrar-servers.com` | 905 | 937 | yes |
| `eforward2.registrar-servers.com` | 905 | 937 | yes |
| `eforward3.registrar-servers.com` | 905 | 937 | yes |
| `eforward4.registrar-servers.com` | 905 | 937 | yes |
| `eforward5.registrar-servers.com` | 905 | 937 | yes |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 2018 | 2018 |
| `mail.wallywatts.com` | 2018 | 2018 |
| `generator.email` | 1446 | 1664 |
| `aero4.unstablemail.com` | 1331 | 1331 |
| `srv4.unstablemail.com` | 1329 | 1329 |
| `mx4.beavis99.com` | 1253 | 1253 |
| `mx4.beavis99.net` | 1252 | 1252 |
| `smtp.yopmail.com` | 1109 | 1117 |
| `email.chatgpt.org.uk` | 768 | 772 |
| `emailfake.com` | 764 | 777 |
| `tinyhost.shop` | 522 | 522 |
| `mx.emlhub.com` | 486 | 486 |
| `mx.spymail.one` | 389 | 389 |
| `mail.h-email.net` | 378 | 439 |
| `email.gravityengine.cc` | 371 | 385 |
| `mx.emltmp.com` | 370 | 370 |
| `mx156.hostedmxserver.com` | 365 | 471 |
| `mx.emlpro.com` | 356 | 356 |
| `mx2-hosting.jellyfish.systems` | 356 | 365 |
| `mx3-hosting.jellyfish.systems` | 356 | 365 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `78.47.124.133` | 3136 | 3136 |
| `94.130.108.80` | 3136 | 3136 |
| `162.159.205.17` | 2704 | 2857 |
| `162.159.205.18` | 2704 | 2857 |
| `162.159.205.19` | 2704 | 2857 |
| `162.159.205.23` | 2698 | 2852 |
| `162.159.205.24` | 2698 | 2852 |
| `162.159.205.25` | 2698 | 2852 |
| `162.159.205.11` | 2693 | 2846 |
| `162.159.205.12` | 2693 | 2846 |
| `162.159.205.13` | 2693 | 2846 |
| `91.196.52.205` | 2503 | 2729 |
| `116.202.9.167` | 1988 | 1988 |
| `46.101.111.206` | 1988 | 1988 |
| `142.132.166.12` | 1981 | 1981 |
| `188.166.111.252` | 1981 | 1981 |
| `138.226.240.26` | 1421 | 1521 |
| `146.190.212.90` | 1310 | 1310 |
| `146.190.223.124` | 1290 | 1290 |
| `188.245.74.208` | 1233 | 1233 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 460 |
| High-confidence disposable IPs | 1,134 |
| Promoted to `domains_inferred.txt` | 4 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**8532 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

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


*… and 8,502 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
