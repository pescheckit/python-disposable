# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-10-21 02:39 UTC**.*  
*Last DNS snapshot: **2026-10-21T02:19:17+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 97,727 |
| `domains_strict.txt` | 98,959 |
| `domains_inferred.txt` (opt-in) | 4 |

## Reachability

Of **101,363** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 44,979 | 44.4% |
| A_ONLY | 6,005 | 5.9% |
| NXDOMAIN | 42,767 | 42.2% |
| NO_RECORDS | 1,026 | 1.0% |
| TIMEOUT | 6,586 | 6.5% |

**50,984 domains are mail-reachable today** (50.3%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `route2.mx.cloudflare.net` | 2690 | 2823 | yes |
| `route1.mx.cloudflare.net` | 2689 | 2822 | yes |
| `route3.mx.cloudflare.net` | 2689 | 2822 | yes |
| `mail.wabblywabble.com` | 2000 | 2001 |  |
| `mail.wallywatts.com` | 2000 | 2001 |  |
| `generator.email` | 1342 | 1550 |  |
| `aero4.unstablemail.com` | 1298 | 1298 |  |
| `srv4.unstablemail.com` | 1297 | 1297 |  |
| `mx4.beavis99.com` | 1251 | 1251 |  |
| `mx4.beavis99.net` | 1250 | 1250 |  |
| `park-mx.above.com` | 990 | 1061 | yes |
| `aspmx.l.google.com` | 960 | 1043 | yes |
| `alt1.aspmx.l.google.com` | 944 | 1025 | yes |
| `alt2.aspmx.l.google.com` | 939 | 1018 | yes |
| `eforward1.registrar-servers.com` | 910 | 937 | yes |
| `eforward2.registrar-servers.com` | 910 | 937 | yes |
| `eforward3.registrar-servers.com` | 910 | 937 | yes |
| `eforward4.registrar-servers.com` | 910 | 937 | yes |
| `eforward5.registrar-servers.com` | 910 | 937 | yes |
| `smtp.google.com` | 798 | 821 | yes |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 2000 | 2001 |
| `mail.wallywatts.com` | 2000 | 2001 |
| `generator.email` | 1342 | 1550 |
| `aero4.unstablemail.com` | 1298 | 1298 |
| `srv4.unstablemail.com` | 1297 | 1297 |
| `mx4.beavis99.com` | 1251 | 1251 |
| `mx4.beavis99.net` | 1250 | 1250 |
| `emailfake.com` | 687 | 698 |
| `email.chatgpt.org.uk` | 581 | 581 |
| `mx.emlhub.com` | 484 | 484 |
| `smtp.yopmail.com` | 419 | 431 |
| `mail.cleantempmail.com` | 413 | 413 |
| `tinyhost.shop` | 407 | 407 |
| `mx.spymail.one` | 388 | 388 |
| `mail.h-email.net` | 379 | 435 |
| `mx.emltmp.com` | 370 | 370 |
| `email.gravityengine.cc` | 365 | 378 |
| `mx156.hostedmxserver.com` | 365 | 452 |
| `mx.emlpro.com` | 355 | 355 |
| `mx2-hosting.jellyfish.systems` | 347 | 353 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `78.47.124.133` | 2772 | 2772 |
| `94.130.108.80` | 2772 | 2772 |
| `162.159.205.23` | 2680 | 2810 |
| `162.159.205.24` | 2680 | 2810 |
| `162.159.205.25` | 2680 | 2810 |
| `162.159.205.17` | 2675 | 2805 |
| `162.159.205.18` | 2675 | 2805 |
| `162.159.205.19` | 2675 | 2805 |
| `162.159.205.11` | 2656 | 2786 |
| `162.159.205.12` | 2656 | 2786 |
| `162.159.205.13` | 2656 | 2786 |
| `91.196.52.205` | 2239 | 2454 |
| `116.202.9.167` | 1965 | 1966 |
| `46.101.111.206` | 1965 | 1966 |
| `142.132.166.12` | 1948 | 1949 |
| `188.166.111.252` | 1948 | 1949 |
| `138.226.240.26` | 1311 | 1324 |
| `146.190.212.90` | 1266 | 1266 |
| `195.123.189.142` | 1250 | 1257 |
| `146.190.223.124` | 1239 | 1239 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 455 |
| High-confidence disposable IPs | 1,160 |
| Promoted to `domains_inferred.txt` | 4 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**8440 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

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


*… and 8,410 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
