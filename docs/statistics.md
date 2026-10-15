# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-10-15 02:22 UTC**.*  
*Last DNS snapshot: **2026-10-15T02:15:05+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 97,378 |
| `domains_strict.txt` | 98,610 |
| `domains_inferred.txt` (opt-in) | 2 |

## Reachability

Of **100,695** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 44,769 | 44.5% |
| A_ONLY | 5,705 | 5.7% |
| NXDOMAIN | 42,381 | 42.1% |
| NO_RECORDS | 978 | 1.0% |
| TIMEOUT | 6,862 | 6.8% |

**50,474 domains are mail-reachable today** (50.1%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `route2.mx.cloudflare.net` | 2687 | 2772 | yes |
| `route1.mx.cloudflare.net` | 2686 | 2771 | yes |
| `route3.mx.cloudflare.net` | 2685 | 2770 | yes |
| `mail.wabblywabble.com` | 1968 | 1968 |  |
| `mail.wallywatts.com` | 1968 | 1968 |  |
| `generator.email` | 1377 | 1570 |  |
| `aero4.unstablemail.com` | 1301 | 1301 |  |
| `srv4.unstablemail.com` | 1300 | 1300 |  |
| `mx4.beavis99.com` | 1234 | 1234 |  |
| `mx4.beavis99.net` | 1233 | 1233 |  |
| `aspmx.l.google.com` | 1005 | 1090 | yes |
| `alt1.aspmx.l.google.com` | 987 | 1070 | yes |
| `alt2.aspmx.l.google.com` | 983 | 1064 | yes |
| `park-mx.above.com` | 945 | 1000 | yes |
| `eforward1.registrar-servers.com` | 903 | 928 | yes |
| `eforward2.registrar-servers.com` | 903 | 928 | yes |
| `eforward3.registrar-servers.com` | 903 | 928 | yes |
| `eforward4.registrar-servers.com` | 903 | 928 | yes |
| `eforward5.registrar-servers.com` | 903 | 928 | yes |
| `smtp.google.com` | 798 | 818 | yes |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 1968 | 1968 |
| `mail.wallywatts.com` | 1968 | 1968 |
| `generator.email` | 1377 | 1570 |
| `aero4.unstablemail.com` | 1301 | 1301 |
| `srv4.unstablemail.com` | 1300 | 1300 |
| `mx4.beavis99.com` | 1234 | 1234 |
| `mx4.beavis99.net` | 1233 | 1233 |
| `email.chatgpt.org.uk` | 755 | 755 |
| `emailfake.com` | 694 | 705 |
| `mx.emlhub.com` | 482 | 482 |
| `smtp.yopmail.com` | 440 | 449 |
| `mail.cleantempmail.com` | 416 | 416 |
| `email.gravityengine.cc` | 400 | 400 |
| `mx.spymail.one` | 378 | 378 |
| `mail.h-email.net` | 359 | 425 |
| `mx.emltmp.com` | 355 | 355 |
| `mx.emlpro.com` | 353 | 353 |
| `mx156.hostedmxserver.com` | 353 | 414 |
| `mx2-hosting.jellyfish.systems` | 343 | 349 |
| `mx3-hosting.jellyfish.systems` | 343 | 349 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `78.47.124.133` | 2730 | 2730 |
| `94.130.108.80` | 2730 | 2730 |
| `162.159.205.23` | 2686 | 2771 |
| `162.159.205.24` | 2686 | 2771 |
| `162.159.205.25` | 2686 | 2771 |
| `162.159.205.17` | 2678 | 2761 |
| `162.159.205.18` | 2678 | 2761 |
| `162.159.205.19` | 2678 | 2761 |
| `162.159.205.11` | 2667 | 2750 |
| `162.159.205.12` | 2667 | 2750 |
| `162.159.205.13` | 2667 | 2750 |
| `91.196.52.205` | 2271 | 2471 |
| `116.202.9.167` | 1941 | 1941 |
| `46.101.111.206` | 1941 | 1941 |
| `142.132.166.12` | 1911 | 1911 |
| `188.166.111.252` | 1911 | 1911 |
| `138.226.240.26` | 1484 | 1484 |
| `146.190.212.90` | 1278 | 1278 |
| `146.190.223.124` | 1270 | 1270 |
| `195.123.189.142` | 1217 | 1227 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 455 |
| High-confidence disposable IPs | 1,161 |
| Promoted to `domains_inferred.txt` | 2 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**8411 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

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


*… and 8,381 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
