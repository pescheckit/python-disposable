# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-11-21 02:19 UTC**.*  
*Last DNS snapshot: **2026-11-21T02:11:54+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 108,824 |
| `domains_strict.txt` | 109,887 |
| `domains_inferred.txt` (opt-in) | 4 |

## Reachability

Of **114,461** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 44,142 | 38.6% |
| A_ONLY | 6,110 | 5.3% |
| NXDOMAIN | 42,818 | 37.4% |
| NO_RECORDS | 1,127 | 1.0% |
| TIMEOUT | 20,264 | 17.7% |

**50,252 domains are mail-reachable today** (43.9%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `generator.email` | 8356 | 8615 |  |
| `route2.mx.cloudflare.net` | 1735 | 1960 | yes |
| `route3.mx.cloudflare.net` | 1735 | 1960 | yes |
| `route1.mx.cloudflare.net` | 1734 | 1959 | yes |
| `mail.wabblywabble.com` | 1609 | 1609 |  |
| `mail.wallywatts.com` | 1609 | 1609 |  |
| `mx4.beavis99.com` | 1225 | 1225 |  |
| `mx4.beavis99.net` | 1224 | 1224 |  |
| `park-mx.above.com` | 1013 | 1141 | yes |
| `email.chatgpt.org.uk` | 843 | 856 |  |
| `aero4.unstablemail.com` | 749 | 750 |  |
| `srv4.unstablemail.com` | 747 | 748 |  |
| `smtp.yopmail.com` | 725 | 734 |  |
| `aspmx.l.google.com` | 643 | 730 | yes |
| `alt1.aspmx.l.google.com` | 632 | 717 | yes |
| `alt2.aspmx.l.google.com` | 627 | 710 | yes |
| `emailfake.com` | 602 | 649 |  |
| `eforward1.registrar-servers.com` | 530 | 578 | yes |
| `eforward2.registrar-servers.com` | 530 | 578 | yes |
| `eforward3.registrar-servers.com` | 530 | 578 | yes |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `generator.email` | 8356 | 8615 |
| `mail.wabblywabble.com` | 1609 | 1609 |
| `mail.wallywatts.com` | 1609 | 1609 |
| `mx4.beavis99.com` | 1225 | 1225 |
| `mx4.beavis99.net` | 1224 | 1224 |
| `email.chatgpt.org.uk` | 843 | 856 |
| `aero4.unstablemail.com` | 749 | 750 |
| `srv4.unstablemail.com` | 747 | 748 |
| `smtp.yopmail.com` | 725 | 734 |
| `emailfake.com` | 602 | 649 |
| `mx.emlhub.com` | 484 | 484 |
| `tinyhost.shop` | 444 | 444 |
| `mx.spymail.one` | 384 | 384 |
| `mx.emltmp.com` | 373 | 373 |
| `mx.emlpro.com` | 352 | 352 |
| `mx.dropmail.me` | 331 | 331 |
| `email.gravityengine.cc` | 327 | 327 |
| `mx.freeml.net` | 316 | 316 |
| `smtp.215.im` | 310 | 314 |
| `mx156.hostedmxserver.com` | 307 | 489 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `91.196.52.205` | 8165 | 8445 |
| `78.47.124.133` | 3012 | 3012 |
| `94.130.108.80` | 3012 | 3012 |
| `162.159.205.17` | 1535 | 1755 |
| `162.159.205.18` | 1535 | 1755 |
| `162.159.205.19` | 1535 | 1755 |
| `162.159.205.23` | 1535 | 1754 |
| `162.159.205.24` | 1535 | 1754 |
| `162.159.205.25` | 1535 | 1754 |
| `162.159.205.11` | 1527 | 1746 |
| `162.159.205.12` | 1527 | 1746 |
| `162.159.205.13` | 1527 | 1746 |
| `116.202.9.167` | 1513 | 1513 |
| `46.101.111.206` | 1513 | 1513 |
| `142.132.166.12` | 1485 | 1485 |
| `188.166.111.252` | 1485 | 1485 |
| `188.245.74.208` | 1202 | 1202 |
| `195.201.18.63` | 1193 | 1193 |
| `158.101.127.66` | 1139 | 1139 |
| `13.223.25.84` | 1112 | 1118 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 412 |
| High-confidence disposable IPs | 1,038 |
| Promoted to `domains_inferred.txt` | 4 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**5685 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

| Listed disposable | MX (shared infra) |
|---|---|
| `0-30-24.com` | `alt1.aspmx.l.google.com` |
| `0-mail.com` | `park-mx.above.com` |
| `000476.com` | `park-mx.above.com` |
| `000728.xyz` | `route1.mx.cloudflare.net` |
| `001041.xyz` | `route1.mx.cloudflare.net` |
| `001218.xyz` | `route1.mx.cloudflare.net` |
| `005005.xyz` | `route1.mx.cloudflare.net` |
| `0055betplataforma.com` | `route1.mx.cloudflare.net` |
| `0058.ru` | `alt1.aspmx.l.google.com` |
| `0066bet32.info` | `park-mx.above.com` |
| `0066betapp.info` | `park-mx.above.com` |
| `007bet.info` | `park-mx.above.com` |
| `007gamecasino.net` | `park-mx.above.com` |
| `007jlbu.com` | `route1.mx.cloudflare.net` |
| `007jlkw.com` | `route1.mx.cloudflare.net` |
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
| `02bet.info` | `park-mx.above.com` |
| `041998.xyz` | `mx1.alias.proton.me` |
| `0500betvip.com` | `route1.mx.cloudflare.net` |
| `057gmail.com` | `route1.mx.cloudflare.net` |
| `0ak.org` | `mx00.ionos.com` |


*… and 5,655 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
