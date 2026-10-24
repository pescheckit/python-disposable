# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-10-24 02:19 UTC**.*  
*Last DNS snapshot: **2026-10-24T02:14:13+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 98,488 |
| `domains_strict.txt` | 99,720 |
| `domains_inferred.txt` (opt-in) | 4 |

## Reachability

Of **102,337** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 47,124 | 46.0% |
| A_ONLY | 6,061 | 5.9% |
| NXDOMAIN | 42,907 | 41.9% |
| NO_RECORDS | 1,163 | 1.1% |
| TIMEOUT | 5,082 | 5.0% |

**53,185 domains are mail-reachable today** (52.0%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `route2.mx.cloudflare.net` | 2711 | 2857 | yes |
| `route1.mx.cloudflare.net` | 2710 | 2856 | yes |
| `route3.mx.cloudflare.net` | 2710 | 2856 | yes |
| `mail.wabblywabble.com` | 2012 | 2013 |  |
| `mail.wallywatts.com` | 2012 | 2013 |  |
| `generator.email` | 1445 | 1661 |  |
| `aero4.unstablemail.com` | 1328 | 1329 |  |
| `srv4.unstablemail.com` | 1326 | 1327 |  |
| `mx4.beavis99.com` | 1251 | 1251 |  |
| `mx4.beavis99.net` | 1250 | 1250 |  |
| `smtp.yopmail.com` | 1097 | 1105 |  |
| `park-mx.above.com` | 1039 | 1114 | yes |
| `aspmx.l.google.com` | 969 | 1052 | yes |
| `alt1.aspmx.l.google.com` | 952 | 1033 | yes |
| `alt2.aspmx.l.google.com` | 947 | 1026 | yes |
| `eforward1.registrar-servers.com` | 915 | 943 | yes |
| `eforward2.registrar-servers.com` | 915 | 943 | yes |
| `eforward3.registrar-servers.com` | 915 | 943 | yes |
| `eforward4.registrar-servers.com` | 915 | 943 | yes |
| `eforward5.registrar-servers.com` | 915 | 943 | yes |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 2012 | 2013 |
| `mail.wallywatts.com` | 2012 | 2013 |
| `generator.email` | 1445 | 1661 |
| `aero4.unstablemail.com` | 1328 | 1329 |
| `srv4.unstablemail.com` | 1326 | 1327 |
| `mx4.beavis99.com` | 1251 | 1251 |
| `mx4.beavis99.net` | 1250 | 1250 |
| `smtp.yopmail.com` | 1097 | 1105 |
| `email.chatgpt.org.uk` | 776 | 777 |
| `emailfake.com` | 767 | 779 |
| `tinyhost.shop` | 520 | 520 |
| `mx.emlhub.com` | 485 | 485 |
| `mail.cleantempmail.com` | 394 | 419 |
| `mx.spymail.one` | 389 | 389 |
| `mail.h-email.net` | 378 | 438 |
| `email.gravityengine.cc` | 371 | 384 |
| `mx.emltmp.com` | 370 | 370 |
| `mx156.hostedmxserver.com` | 367 | 467 |
| `mx.emlpro.com` | 356 | 356 |
| `mx2-hosting.jellyfish.systems` | 352 | 361 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `78.47.124.133` | 3149 | 3149 |
| `94.130.108.80` | 3149 | 3149 |
| `162.159.205.23` | 2704 | 2847 |
| `162.159.205.24` | 2704 | 2847 |
| `162.159.205.25` | 2704 | 2847 |
| `162.159.205.17` | 2700 | 2842 |
| `162.159.205.18` | 2700 | 2842 |
| `162.159.205.19` | 2700 | 2842 |
| `162.159.205.11` | 2681 | 2824 |
| `162.159.205.12` | 2681 | 2824 |
| `162.159.205.13` | 2681 | 2824 |
| `91.196.52.205` | 2485 | 2708 |
| `116.202.9.167` | 1981 | 1982 |
| `46.101.111.206` | 1981 | 1982 |
| `142.132.166.12` | 1962 | 1963 |
| `188.166.111.252` | 1962 | 1963 |
| `138.226.240.26` | 1511 | 1550 |
| `146.190.212.90` | 1300 | 1301 |
| `146.190.223.124` | 1274 | 1275 |
| `188.245.74.208` | 1231 | 1231 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 460 |
| High-confidence disposable IPs | 1,163 |
| Promoted to `domains_inferred.txt` | 4 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**8516 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

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


*… and 8,486 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
