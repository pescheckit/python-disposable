# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-10-11 02:33 UTC**.*  
*Last DNS snapshot: **2026-10-11T02:24:58+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 97,215 |
| `domains_strict.txt` | 98,447 |
| `domains_inferred.txt` (opt-in) | 2 |

## Reachability

Of **100,295** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 44,455 | 44.3% |
| A_ONLY | 5,643 | 5.6% |
| NXDOMAIN | 42,106 | 42.0% |
| NO_RECORDS | 962 | 1.0% |
| TIMEOUT | 7,129 | 7.1% |

**50,098 domains are mail-reachable today** (50.0%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `route2.mx.cloudflare.net` | 2677 | 2749 | yes |
| `route1.mx.cloudflare.net` | 2676 | 2748 | yes |
| `route3.mx.cloudflare.net` | 2675 | 2747 | yes |
| `mail.wabblywabble.com` | 1960 | 1961 |  |
| `mail.wallywatts.com` | 1960 | 1961 |  |
| `generator.email` | 1440 | 1567 |  |
| `aero4.unstablemail.com` | 1292 | 1293 |  |
| `srv4.unstablemail.com` | 1291 | 1292 |  |
| `mx4.beavis99.com` | 1235 | 1235 |  |
| `mx4.beavis99.net` | 1234 | 1234 |  |
| `aspmx.l.google.com` | 1007 | 1089 | yes |
| `alt1.aspmx.l.google.com` | 989 | 1069 | yes |
| `alt2.aspmx.l.google.com` | 985 | 1063 | yes |
| `park-mx.above.com` | 932 | 967 | yes |
| `eforward1.registrar-servers.com` | 910 | 928 | yes |
| `eforward2.registrar-servers.com` | 910 | 928 | yes |
| `eforward3.registrar-servers.com` | 910 | 928 | yes |
| `eforward4.registrar-servers.com` | 910 | 928 | yes |
| `eforward5.registrar-servers.com` | 910 | 928 | yes |
| `smtp.google.com` | 793 | 814 | yes |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 1960 | 1961 |
| `mail.wallywatts.com` | 1960 | 1961 |
| `generator.email` | 1440 | 1567 |
| `aero4.unstablemail.com` | 1292 | 1293 |
| `srv4.unstablemail.com` | 1291 | 1292 |
| `mx4.beavis99.com` | 1235 | 1235 |
| `mx4.beavis99.net` | 1234 | 1234 |
| `email.chatgpt.org.uk` | 762 | 762 |
| `emailfake.com` | 694 | 705 |
| `mx.emlhub.com` | 461 | 461 |
| `smtp.yopmail.com` | 435 | 444 |
| `email.gravityengine.cc` | 423 | 423 |
| `mail.cleantempmail.com` | 418 | 418 |
| `tinyhost.shop` | 381 | 382 |
| `mx.spymail.one` | 373 | 373 |
| `mail.h-email.net` | 369 | 427 |
| `mx2.timeweb.ru` | 362 | 368 |
| `mx1.timeweb.ru` | 361 | 367 |
| `mx.emltmp.com` | 358 | 358 |
| `mx.emlpro.com` | 342 | 342 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `162.159.205.23` | 2681 | 2753 |
| `162.159.205.24` | 2681 | 2753 |
| `162.159.205.25` | 2681 | 2753 |
| `78.47.124.133` | 2676 | 2676 |
| `94.130.108.80` | 2676 | 2676 |
| `162.159.205.17` | 2670 | 2742 |
| `162.159.205.18` | 2670 | 2742 |
| `162.159.205.19` | 2670 | 2742 |
| `162.159.205.11` | 2650 | 2721 |
| `162.159.205.12` | 2650 | 2721 |
| `162.159.205.13` | 2650 | 2721 |
| `91.196.52.205` | 2333 | 2470 |
| `116.202.9.167` | 1936 | 1937 |
| `46.101.111.206` | 1936 | 1937 |
| `142.132.166.12` | 1919 | 1920 |
| `188.166.111.252` | 1919 | 1920 |
| `138.226.240.26` | 1538 | 1538 |
| `146.190.212.90` | 1269 | 1270 |
| `146.190.223.124` | 1263 | 1264 |
| `195.123.189.142` | 1221 | 1227 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 451 |
| High-confidence disposable IPs | 1,144 |
| Promoted to `domains_inferred.txt` | 2 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**8377 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

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
| `007jlbu.com` | `route1.mx.cloudflare.net` |
| `007jlphp.com` | `route1.mx.cloudflare.net` |
| `00gmail.com` | `park-mx.above.com` |
| `010608.xyz` | `route1.mx.cloudflare.net` |
| `010hb.com` | `route1.mx.cloudflare.net` |
| `012356.xyz` | `route1.mx.cloudflare.net` |
| `012pg.bet` | `route1.mx.cloudflare.net` |
| `01g.cloud` | `alt1.aspmx.l.google.com` |
| `01p.co.jp` | `01p-co-jp.mail.protection.outlook.com` |
| `020307.xyz` | `route1.mx.cloudflare.net` |
| `041998.xyz` | `mx1.alias.proton.me` |
| `099833.xyz` | `park-mx.above.com` |
| `0ak.org` | `mx00.ionos.com` |
| `0hcow.com` | `mxa.mailgun.org` |
| `0hio.net` | `aspmx1.migadu.com` |
| `0nce.net` | `route1.mx.cloudflare.net` |
| `0rg.fr` | `mx1.mail.ovh.net` |
| `0sp.me` | `eforward1.registrar-servers.com` |
| `0ut.online` | `smtp.google.com` |
| `0x7121.com` | `park-mx.above.com` |
| `0xmiikee.com` | `eforward1.registrar-servers.com` |


*… and 8,347 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
