# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-11-20 02:23 UTC**.*  
*Last DNS snapshot: **2026-11-20T02:16:03+00:00**.*

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
| MX_OK | 44,164 | 38.6% |
| A_ONLY | 6,153 | 5.4% |
| NXDOMAIN | 42,788 | 37.4% |
| NO_RECORDS | 1,134 | 1.0% |
| TIMEOUT | 20,222 | 17.7% |

**50,317 domains are mail-reachable today** (44.0%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `generator.email` | 8351 | 8610 |  |
| `route2.mx.cloudflare.net` | 1730 | 1955 | yes |
| `route3.mx.cloudflare.net` | 1730 | 1955 | yes |
| `route1.mx.cloudflare.net` | 1729 | 1954 | yes |
| `mail.wabblywabble.com` | 1606 | 1606 |  |
| `mail.wallywatts.com` | 1606 | 1606 |  |
| `mx4.beavis99.com` | 1228 | 1228 |  |
| `mx4.beavis99.net` | 1227 | 1227 |  |
| `park-mx.above.com` | 1004 | 1132 | yes |
| `email.chatgpt.org.uk` | 845 | 858 |  |
| `aero4.unstablemail.com` | 750 | 751 |  |
| `srv4.unstablemail.com` | 748 | 749 |  |
| `smtp.yopmail.com` | 726 | 735 |  |
| `aspmx.l.google.com` | 643 | 730 | yes |
| `alt1.aspmx.l.google.com` | 632 | 717 | yes |
| `alt2.aspmx.l.google.com` | 627 | 710 | yes |
| `emailfake.com` | 604 | 651 |  |
| `eforward1.registrar-servers.com` | 534 | 582 | yes |
| `eforward2.registrar-servers.com` | 534 | 582 | yes |
| `eforward3.registrar-servers.com` | 534 | 582 | yes |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `generator.email` | 8351 | 8610 |
| `mail.wabblywabble.com` | 1606 | 1606 |
| `mail.wallywatts.com` | 1606 | 1606 |
| `mx4.beavis99.com` | 1228 | 1228 |
| `mx4.beavis99.net` | 1227 | 1227 |
| `email.chatgpt.org.uk` | 845 | 858 |
| `aero4.unstablemail.com` | 750 | 751 |
| `srv4.unstablemail.com` | 748 | 749 |
| `smtp.yopmail.com` | 726 | 735 |
| `emailfake.com` | 604 | 651 |
| `mx.emlhub.com` | 482 | 482 |
| `tinyhost.shop` | 450 | 450 |
| `mx.spymail.one` | 382 | 382 |
| `mx.emltmp.com` | 373 | 373 |
| `mx.emlpro.com` | 352 | 352 |
| `mx.dropmail.me` | 327 | 327 |
| `email.gravityengine.cc` | 326 | 326 |
| `mx.freeml.net` | 313 | 313 |
| `smtp.215.im` | 310 | 314 |
| `mx156.hostedmxserver.com` | 308 | 490 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `91.196.52.205` | 8149 | 8429 |
| `78.47.124.133` | 2998 | 2998 |
| `94.130.108.80` | 2998 | 2998 |
| `162.159.205.17` | 1532 | 1752 |
| `162.159.205.18` | 1532 | 1752 |
| `162.159.205.19` | 1532 | 1752 |
| `162.159.205.23` | 1530 | 1749 |
| `162.159.205.24` | 1530 | 1749 |
| `162.159.205.25` | 1530 | 1749 |
| `162.159.205.11` | 1522 | 1741 |
| `162.159.205.12` | 1522 | 1741 |
| `162.159.205.13` | 1522 | 1741 |
| `116.202.9.167` | 1508 | 1508 |
| `46.101.111.206` | 1508 | 1508 |
| `142.132.166.12` | 1483 | 1483 |
| `188.166.111.252` | 1483 | 1483 |
| `188.245.74.208` | 1208 | 1208 |
| `195.201.18.63` | 1199 | 1199 |
| `158.101.127.66` | 1139 | 1139 |
| `13.223.25.84` | 1116 | 1122 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 414 |
| High-confidence disposable IPs | 1,050 |
| Promoted to `domains_inferred.txt` | 4 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**5677 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

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


*… and 5,647 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
