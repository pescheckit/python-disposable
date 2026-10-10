# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-10-10 02:35 UTC**.*  
*Last DNS snapshot: **2026-10-10T02:22:58+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 96,296 |
| `domains_strict.txt` | 97,528 |
| `domains_inferred.txt` (opt-in) | 2 |

## Reachability

Of **99,329** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 43,563 | 43.9% |
| A_ONLY | 5,638 | 5.7% |
| NXDOMAIN | 42,104 | 42.4% |
| NO_RECORDS | 961 | 1.0% |
| TIMEOUT | 7,063 | 7.1% |

**49,201 domains are mail-reachable today** (49.5%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `route2.mx.cloudflare.net` | 2614 | 2690 | yes |
| `route1.mx.cloudflare.net` | 2613 | 2689 | yes |
| `route3.mx.cloudflare.net` | 2612 | 2688 | yes |
| `mail.wabblywabble.com` | 1946 | 1953 |  |
| `mail.wallywatts.com` | 1946 | 1953 |  |
| `generator.email` | 1434 | 1514 |  |
| `aero4.unstablemail.com` | 1291 | 1293 |  |
| `srv4.unstablemail.com` | 1290 | 1292 |  |
| `mx4.beavis99.com` | 1235 | 1235 |  |
| `mx4.beavis99.net` | 1234 | 1234 |  |
| `aspmx.l.google.com` | 993 | 1075 | yes |
| `alt1.aspmx.l.google.com` | 975 | 1055 | yes |
| `alt2.aspmx.l.google.com` | 971 | 1049 | yes |
| `park-mx.above.com` | 930 | 965 | yes |
| `eforward1.registrar-servers.com` | 911 | 927 | yes |
| `eforward2.registrar-servers.com` | 911 | 927 | yes |
| `eforward3.registrar-servers.com` | 911 | 927 | yes |
| `eforward4.registrar-servers.com` | 911 | 927 | yes |
| `eforward5.registrar-servers.com` | 911 | 927 | yes |
| `smtp.google.com` | 764 | 783 | yes |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 1946 | 1953 |
| `mail.wallywatts.com` | 1946 | 1953 |
| `generator.email` | 1434 | 1514 |
| `aero4.unstablemail.com` | 1291 | 1293 |
| `srv4.unstablemail.com` | 1290 | 1292 |
| `mx4.beavis99.com` | 1235 | 1235 |
| `mx4.beavis99.net` | 1234 | 1234 |
| `email.chatgpt.org.uk` | 754 | 754 |
| `emailfake.com` | 689 | 699 |
| `mx.emlhub.com` | 461 | 461 |
| `smtp.yopmail.com` | 436 | 443 |
| `mail.cleantempmail.com` | 388 | 388 |
| `email.gravityengine.cc` | 385 | 386 |
| `tinyhost.shop` | 380 | 381 |
| `mx.spymail.one` | 373 | 373 |
| `mx2.timeweb.ru` | 366 | 367 |
| `mx1.timeweb.ru` | 365 | 366 |
| `mx.emltmp.com` | 358 | 358 |
| `mail.h-email.net` | 354 | 411 |
| `mx156.hostedmxserver.com` | 346 | 375 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `78.47.124.133` | 2676 | 2676 |
| `94.130.108.80` | 2676 | 2676 |
| `162.159.205.23` | 2619 | 2695 |
| `162.159.205.24` | 2619 | 2695 |
| `162.159.205.25` | 2619 | 2695 |
| `162.159.205.17` | 2608 | 2684 |
| `162.159.205.18` | 2608 | 2684 |
| `162.159.205.19` | 2608 | 2684 |
| `162.159.205.11` | 2587 | 2662 |
| `162.159.205.12` | 2587 | 2662 |
| `162.159.205.13` | 2587 | 2662 |
| `91.196.52.205` | 2318 | 2409 |
| `116.202.9.167` | 1923 | 1930 |
| `46.101.111.206` | 1923 | 1930 |
| `142.132.166.12` | 1907 | 1914 |
| `188.166.111.252` | 1907 | 1914 |
| `138.226.240.26` | 1463 | 1464 |
| `146.190.212.90` | 1268 | 1270 |
| `146.190.223.124` | 1262 | 1264 |
| `195.123.189.142` | 1219 | 1222 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 444 |
| High-confidence disposable IPs | 1,115 |
| Promoted to `domains_inferred.txt` | 2 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**8251 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

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
| `00gmail.com` | `park-mx.above.com` |
| `010608.xyz` | `route1.mx.cloudflare.net` |
| `010hb.com` | `route1.mx.cloudflare.net` |
| `012356.xyz` | `route1.mx.cloudflare.net` |
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
| `1-2.co.uk` | `12-co-uk0c.mail.protection.outlook.com` |
| `1-8.biz` | `mail.protonmail.ch` |
| `1-box.ru` | `mx.yandex.ru` |


*… and 8,221 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
