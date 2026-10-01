# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-10-01 02:44 UTC**.*  
*Last DNS snapshot: **2026-10-01T02:33:23+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 97,713 |
| `domains_strict.txt` | 98,944 |
| `domains_inferred.txt` (opt-in) | 2 |

## Reachability

Of **98,483** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 41,389 | 42.0% |
| A_ONLY | 5,091 | 5.2% |
| NXDOMAIN | 38,836 | 39.4% |
| NO_RECORDS | 870 | 0.9% |
| TIMEOUT | 12,297 | 12.5% |

**46,480 domains are mail-reachable today** (47.2%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `route1.mx.cloudflare.net` | 2599 | 2603 | yes |
| `route2.mx.cloudflare.net` | 2599 | 2603 | yes |
| `route3.mx.cloudflare.net` | 2596 | 2600 | yes |
| `mail.wabblywabble.com` | 1826 | 1826 |  |
| `mail.wallywatts.com` | 1826 | 1826 |  |
| `generator.email` | 1445 | 1459 |  |
| `aero4.unstablemail.com` | 1255 | 1255 |  |
| `srv4.unstablemail.com` | 1255 | 1255 |  |
| `mx4.beavis99.com` | 1161 | 1161 |  |
| `mx4.beavis99.net` | 1160 | 1160 |  |
| `aspmx.l.google.com` | 1002 | 1004 | yes |
| `alt1.aspmx.l.google.com` | 981 | 983 | yes |
| `alt2.aspmx.l.google.com` | 975 | 977 | yes |
| `park-mx.above.com` | 910 | 914 | yes |
| `eforward1.registrar-servers.com` | 881 | 882 | yes |
| `eforward2.registrar-servers.com` | 881 | 882 | yes |
| `eforward3.registrar-servers.com` | 881 | 882 | yes |
| `eforward4.registrar-servers.com` | 881 | 882 | yes |
| `eforward5.registrar-servers.com` | 881 | 882 | yes |
| `smtp.google.com` | 761 | 762 | yes |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 1826 | 1826 |
| `mail.wallywatts.com` | 1826 | 1826 |
| `generator.email` | 1445 | 1459 |
| `aero4.unstablemail.com` | 1255 | 1255 |
| `srv4.unstablemail.com` | 1255 | 1255 |
| `mx4.beavis99.com` | 1161 | 1161 |
| `mx4.beavis99.net` | 1160 | 1160 |
| `emailfake.com` | 700 | 710 |
| `publicms1.mail2world.com` | 591 | 592 |
| `publicms2.mail2world.com` | 591 | 592 |
| `email.chatgpt.org.uk` | 564 | 564 |
| `smtp.yopmail.com` | 442 | 444 |
| `mx.emlhub.com` | 440 | 440 |
| `mail.cleantempmail.com` | 380 | 380 |
| `email.gravityengine.cc` | 371 | 371 |
| `mail.h-email.net` | 362 | 362 |
| `mx2.timeweb.ru` | 360 | 360 |
| `mx1.timeweb.ru` | 359 | 359 |
| `mx.spymail.one` | 354 | 354 |
| `tinyhost.shop` | 351 | 351 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `78.47.124.133` | 2608 | 2608 |
| `94.130.108.80` | 2608 | 2608 |
| `162.159.205.23` | 2588 | 2592 |
| `162.159.205.24` | 2588 | 2592 |
| `162.159.205.25` | 2588 | 2592 |
| `162.159.205.17` | 2564 | 2568 |
| `162.159.205.18` | 2564 | 2568 |
| `162.159.205.19` | 2564 | 2568 |
| `162.159.205.11` | 2554 | 2558 |
| `162.159.205.12` | 2554 | 2558 |
| `162.159.205.13` | 2554 | 2558 |
| `91.196.52.205` | 2255 | 2281 |
| `116.202.9.167` | 1784 | 1784 |
| `46.101.111.206` | 1784 | 1784 |
| `142.132.166.12` | 1778 | 1778 |
| `188.166.111.252` | 1778 | 1778 |
| `138.226.240.26` | 1245 | 1245 |
| `195.123.189.142` | 1227 | 1227 |
| `146.190.212.90` | 1224 | 1224 |
| `146.190.223.124` | 1204 | 1204 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 445 |
| High-confidence disposable IPs | 1,098 |
| Promoted to `domains_inferred.txt` | 2 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**8211 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

| Listed disposable | MX (shared infra) |
|---|---|
| `0-30-24.com` | `alt1.aspmx.l.google.com` |
| `0-mail.com` | `park-mx.above.com` |
| `000476.com` | `park-mx.above.com` |
| `000728.xyz` | `route1.mx.cloudflare.net` |
| `001218.xyz` | `route1.mx.cloudflare.net` |
| `001250.xyz` | `eforward1.registrar-servers.com` |
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
| `0live.org` | `route1.mx.cloudflare.net` |
| `0nce.net` | `route1.mx.cloudflare.net` |
| `0rg.fr` | `mx1.mail.ovh.net` |
| `0sp.me` | `eforward1.registrar-servers.com` |
| `0ut.online` | `smtp.google.com` |
| `0x7121.com` | `park-mx.above.com` |
| `0xmiikee.com` | `eforward1.registrar-servers.com` |
| `1-2.co.uk` | `12-co-uk0c.mail.protection.outlook.com` |


*… and 8,181 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
