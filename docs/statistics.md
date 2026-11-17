# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-11-17 02:19 UTC**.*  
*Last DNS snapshot: **2026-11-17T02:10:33+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 108,547 |
| `domains_strict.txt` | 109,610 |
| `domains_inferred.txt` (opt-in) | 4 |

## Reachability

Of **114,037** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 54,935 | 48.2% |
| A_ONLY | 5,383 | 4.7% |
| NXDOMAIN | 38,194 | 33.5% |
| NO_RECORDS | 1,120 | 1.0% |
| TIMEOUT | 14,405 | 12.6% |

**60,318 domains are mail-reachable today** (52.9%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `generator.email` | 10332 | 10598 |  |
| `route2.mx.cloudflare.net` | 2711 | 2933 | yes |
| `route1.mx.cloudflare.net` | 2710 | 2932 | yes |
| `route3.mx.cloudflare.net` | 2710 | 2932 | yes |
| `mail.wabblywabble.com` | 1860 | 1860 |  |
| `mail.wallywatts.com` | 1860 | 1860 |  |
| `aero4.unstablemail.com` | 1284 | 1284 |  |
| `srv4.unstablemail.com` | 1282 | 1282 |  |
| `park-mx.above.com` | 1208 | 1337 | yes |
| `mx4.beavis99.com` | 1153 | 1153 |  |
| `mx4.beavis99.net` | 1152 | 1152 |  |
| `aspmx.l.google.com` | 927 | 1014 | yes |
| `alt1.aspmx.l.google.com` | 910 | 995 | yes |
| `alt2.aspmx.l.google.com` | 907 | 990 | yes |
| `smtp.yopmail.com` | 878 | 887 |  |
| `eforward1.registrar-servers.com` | 876 | 923 | yes |
| `eforward2.registrar-servers.com` | 876 | 923 | yes |
| `eforward3.registrar-servers.com` | 876 | 923 | yes |
| `eforward4.registrar-servers.com` | 876 | 923 | yes |
| `eforward5.registrar-servers.com` | 876 | 923 | yes |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `generator.email` | 10332 | 10598 |
| `mail.wabblywabble.com` | 1860 | 1860 |
| `mail.wallywatts.com` | 1860 | 1860 |
| `aero4.unstablemail.com` | 1284 | 1284 |
| `srv4.unstablemail.com` | 1282 | 1282 |
| `mx4.beavis99.com` | 1153 | 1153 |
| `mx4.beavis99.net` | 1152 | 1152 |
| `smtp.yopmail.com` | 878 | 887 |
| `email.chatgpt.org.uk` | 842 | 855 |
| `emailfake.com` | 754 | 768 |
| `mx.emlhub.com` | 443 | 443 |
| `tinyhost.shop` | 434 | 434 |
| `mx1.timeweb.ru` | 356 | 389 |
| `mx2.timeweb.ru` | 356 | 389 |
| `mx.spymail.one` | 345 | 345 |
| `smtp.215.im` | 342 | 346 |
| `mail.h-email.net` | 337 | 415 |
| `mx2-hosting.jellyfish.systems` | 335 | 350 |
| `mx3-hosting.jellyfish.systems` | 335 | 350 |
| `mx1-hosting.jellyfish.systems` | 334 | 349 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `91.196.52.205` | 11217 | 11491 |
| `162.159.205.17` | 2710 | 2928 |
| `162.159.205.18` | 2710 | 2928 |
| `162.159.205.19` | 2710 | 2928 |
| `78.47.124.133` | 2709 | 2709 |
| `94.130.108.80` | 2709 | 2709 |
| `162.159.205.23` | 2702 | 2920 |
| `162.159.205.24` | 2702 | 2920 |
| `162.159.205.25` | 2702 | 2920 |
| `162.159.205.11` | 2697 | 2915 |
| `162.159.205.12` | 2697 | 2915 |
| `162.159.205.13` | 2697 | 2915 |
| `116.202.9.167` | 1806 | 1806 |
| `46.101.111.206` | 1806 | 1806 |
| `142.132.166.12` | 1799 | 1799 |
| `188.166.111.252` | 1799 | 1799 |
| `201.3.122.6` | 1694 | 1703 |
| `146.190.212.90` | 1257 | 1257 |
| `146.190.223.124` | 1247 | 1247 |
| `103.224.212.34` | 1184 | 1311 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 457 |
| High-confidence disposable IPs | 1,160 |
| Promoted to `domains_inferred.txt` | 4 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**8565 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

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
| `0hcow.com` | `mxa.mailgun.org` |


*… and 8,535 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
