# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-10-22 02:20 UTC**.*  
*Last DNS snapshot: **2026-10-22T02:16:11+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 97,746 |
| `domains_strict.txt` | 98,978 |
| `domains_inferred.txt` (opt-in) | 4 |

## Reachability

Of **101,436** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 45,027 | 44.4% |
| A_ONLY | 6,016 | 5.9% |
| NXDOMAIN | 42,782 | 42.2% |
| NO_RECORDS | 1,030 | 1.0% |
| TIMEOUT | 6,581 | 6.5% |

**51,043 domains are mail-reachable today** (50.3%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `route2.mx.cloudflare.net` | 2689 | 2825 | yes |
| `route1.mx.cloudflare.net` | 2688 | 2824 | yes |
| `route3.mx.cloudflare.net` | 2688 | 2824 | yes |
| `mail.wabblywabble.com` | 1998 | 2001 |  |
| `mail.wallywatts.com` | 1998 | 2001 |  |
| `generator.email` | 1340 | 1552 |  |
| `aero4.unstablemail.com` | 1298 | 1298 |  |
| `srv4.unstablemail.com` | 1297 | 1297 |  |
| `mx4.beavis99.com` | 1251 | 1251 |  |
| `mx4.beavis99.net` | 1250 | 1250 |  |
| `park-mx.above.com` | 1005 | 1079 | yes |
| `aspmx.l.google.com` | 961 | 1045 | yes |
| `alt1.aspmx.l.google.com` | 945 | 1027 | yes |
| `alt2.aspmx.l.google.com` | 940 | 1020 | yes |
| `eforward1.registrar-servers.com` | 911 | 938 | yes |
| `eforward2.registrar-servers.com` | 911 | 938 | yes |
| `eforward3.registrar-servers.com` | 911 | 938 | yes |
| `eforward4.registrar-servers.com` | 911 | 938 | yes |
| `eforward5.registrar-servers.com` | 911 | 938 | yes |
| `smtp.google.com` | 794 | 821 | yes |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 1998 | 2001 |
| `mail.wallywatts.com` | 1998 | 2001 |
| `generator.email` | 1340 | 1552 |
| `aero4.unstablemail.com` | 1298 | 1298 |
| `srv4.unstablemail.com` | 1297 | 1297 |
| `mx4.beavis99.com` | 1251 | 1251 |
| `mx4.beavis99.net` | 1250 | 1250 |
| `emailfake.com` | 686 | 698 |
| `email.chatgpt.org.uk` | 581 | 581 |
| `mx.emlhub.com` | 484 | 484 |
| `smtp.yopmail.com` | 421 | 431 |
| `mail.cleantempmail.com` | 413 | 413 |
| `tinyhost.shop` | 407 | 407 |
| `mx.spymail.one` | 389 | 389 |
| `mail.h-email.net` | 373 | 435 |
| `mx.emltmp.com` | 370 | 370 |
| `email.gravityengine.cc` | 363 | 376 |
| `mx156.hostedmxserver.com` | 360 | 454 |
| `mx.emlpro.com` | 356 | 356 |
| `mx2-hosting.jellyfish.systems` | 346 | 355 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `78.47.124.133` | 2772 | 2772 |
| `94.130.108.80` | 2772 | 2772 |
| `162.159.205.23` | 2679 | 2812 |
| `162.159.205.24` | 2679 | 2812 |
| `162.159.205.25` | 2679 | 2812 |
| `162.159.205.17` | 2675 | 2807 |
| `162.159.205.18` | 2675 | 2807 |
| `162.159.205.19` | 2675 | 2807 |
| `162.159.205.11` | 2656 | 2789 |
| `162.159.205.12` | 2656 | 2789 |
| `162.159.205.13` | 2656 | 2789 |
| `91.196.52.205` | 2243 | 2462 |
| `116.202.9.167` | 1964 | 1967 |
| `46.101.111.206` | 1964 | 1967 |
| `142.132.166.12` | 1948 | 1950 |
| `188.166.111.252` | 1948 | 1950 |
| `138.226.240.26` | 1310 | 1323 |
| `146.190.212.90` | 1267 | 1267 |
| `195.123.189.142` | 1252 | 1257 |
| `146.190.223.124` | 1240 | 1240 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 455 |
| High-confidence disposable IPs | 1,152 |
| Promoted to `domains_inferred.txt` | 4 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**8449 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

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


*… and 8,419 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
