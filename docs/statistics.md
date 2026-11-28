# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-11-28 02:54 UTC**.*  
*Last DNS snapshot: **2026-11-28T02:48:26+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 109,317 |
| `domains_strict.txt` | 110,380 |
| `domains_inferred.txt` (opt-in) | 4 |

## Reachability

Of **115,373** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 48,086 | 41.7% |
| A_ONLY | 3,260 | 2.8% |
| NXDOMAIN | 26,190 | 22.7% |
| NO_RECORDS | 831 | 0.7% |
| TIMEOUT | 37,006 | 32.1% |

**51,346 domains are mail-reachable today** (44.5%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `generator.email` | 9431 | 9746 |  |
| `route1.mx.cloudflare.net` | 2398 | 2643 | yes |
| `route2.mx.cloudflare.net` | 2398 | 2643 | yes |
| `route3.mx.cloudflare.net` | 2396 | 2641 | yes |
| `mail.wabblywabble.com` | 1483 | 1484 |  |
| `mail.wallywatts.com` | 1483 | 1484 |  |
| `aero4.unstablemail.com` | 1117 | 1119 |  |
| `srv4.unstablemail.com` | 1115 | 1117 |  |
| `park-mx.above.com` | 1106 | 1278 | yes |
| `smtp.yopmail.com` | 845 | 858 |  |
| `emailfake.com` | 818 | 836 |  |
| `mx4.beavis99.com` | 813 | 813 |  |
| `mx4.beavis99.net` | 812 | 812 |  |
| `aspmx.l.google.com` | 795 | 882 | yes |
| `smtp.google.com` | 786 | 839 | yes |
| `alt1.aspmx.l.google.com` | 780 | 865 | yes |
| `alt2.aspmx.l.google.com` | 776 | 859 | yes |
| `email.chatgpt.org.uk` | 770 | 783 |  |
| `eforward1.registrar-servers.com` | 753 | 805 | yes |
| `eforward2.registrar-servers.com` | 753 | 805 | yes |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `generator.email` | 9431 | 9746 |
| `mail.wabblywabble.com` | 1483 | 1484 |
| `mail.wallywatts.com` | 1483 | 1484 |
| `aero4.unstablemail.com` | 1117 | 1119 |
| `srv4.unstablemail.com` | 1115 | 1117 |
| `smtp.yopmail.com` | 845 | 858 |
| `emailfake.com` | 818 | 836 |
| `mx4.beavis99.com` | 813 | 813 |
| `mx4.beavis99.net` | 812 | 812 |
| `email.chatgpt.org.uk` | 770 | 783 |
| `tinyhost.shop` | 387 | 387 |
| `smtp.215.im` | 361 | 365 |
| `mx1.timeweb.ru` | 344 | 376 |
| `mx2.timeweb.ru` | 344 | 376 |
| `void.blackhole.mx` | 323 | 326 |
| `mx2-hosting.jellyfish.systems` | 320 | 336 |
| `mx3-hosting.jellyfish.systems` | 320 | 336 |
| `mx1-hosting.jellyfish.systems` | 319 | 335 |
| `mx.10mail.org` | 298 | 298 |
| `mx.emlhub.com` | 286 | 286 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `91.196.52.205` | 10222 | 10545 |
| `162.159.205.17` | 2333 | 2569 |
| `162.159.205.18` | 2333 | 2569 |
| `162.159.205.19` | 2333 | 2569 |
| `162.159.205.23` | 2327 | 2563 |
| `162.159.205.24` | 2327 | 2563 |
| `162.159.205.25` | 2327 | 2563 |
| `162.159.205.11` | 2326 | 2561 |
| `162.159.205.12` | 2326 | 2561 |
| `162.159.205.13` | 2326 | 2561 |
| `78.47.124.133` | 1794 | 1794 |
| `94.130.108.80` | 1794 | 1794 |
| `201.3.122.6` | 1660 | 1670 |
| `142.132.166.12` | 1384 | 1385 |
| `188.166.111.252` | 1384 | 1385 |
| `116.202.9.167` | 1378 | 1379 |
| `46.101.111.206` | 1378 | 1379 |
| `146.190.223.124` | 1069 | 1071 |
| `146.190.212.90` | 1062 | 1064 |
| `103.224.212.34` | 1039 | 1206 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 416 |
| High-confidence disposable IPs | 1,040 |
| Promoted to `domains_inferred.txt` | 4 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**7545 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

| Listed disposable | MX (shared infra) |
|---|---|
| `0-30-24.com` | `alt1.aspmx.l.google.com` |
| `0-mail.com` | `park-mx.above.com` |
| `000476.com` | `park-mx.above.com` |
| `000728.xyz` | `route1.mx.cloudflare.net` |
| `001041.xyz` | `route1.mx.cloudflare.net` |
| `001218.xyz` | `route1.mx.cloudflare.net` |
| `001310.xyz` | `route1.mx.cloudflare.net` |
| `005005.xyz` | `route1.mx.cloudflare.net` |
| `0055betplataforma.com` | `route1.mx.cloudflare.net` |
| `0058.ru` | `alt1.aspmx.l.google.com` |
| `0066bet32.info` | `park-mx.above.com` |
| `0066betapp.info` | `park-mx.above.com` |
| `007jlbu.com` | `route1.mx.cloudflare.net` |
| `007jlkw.com` | `route1.mx.cloudflare.net` |
| `007jlphp.com` | `route1.mx.cloudflare.net` |
| `008686.xyz` | `route1.mx.cloudflare.net` |
| `00gmail.com` | `park-mx.above.com` |
| `010608.xyz` | `route1.mx.cloudflare.net` |
| `010hb.com` | `route1.mx.cloudflare.net` |
| `012356.xyz` | `route1.mx.cloudflare.net` |
| `01g.cloud` | `alt1.aspmx.l.google.com` |
| `01p.co.jp` | `01p-co-jp.mail.protection.outlook.com` |
| `020307.xyz` | `route1.mx.cloudflare.net` |
| `02bet.info` | `park-mx.above.com` |
| `041998.xyz` | `mx1.alias.proton.me` |
| `0500betvip.com` | `route1.mx.cloudflare.net` |
| `057gmail.com` | `route1.mx.cloudflare.net` |
| `0ak.org` | `mx00.ionos.com` |
| `0hcow.com` | `mxa.mailgun.org` |
| `0hio.net` | `aspmx1.migadu.com` |


*… and 7,515 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
