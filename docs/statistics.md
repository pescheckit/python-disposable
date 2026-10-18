# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-10-18 02:26 UTC**.*  
*Last DNS snapshot: **2026-10-18T02:14:16+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 97,562 |
| `domains_strict.txt` | 98,794 |
| `domains_inferred.txt` (opt-in) | 4 |

## Reachability

Of **101,099** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 44,755 | 44.3% |
| A_ONLY | 5,732 | 5.7% |
| NXDOMAIN | 42,392 | 41.9% |
| NO_RECORDS | 986 | 1.0% |
| TIMEOUT | 7,234 | 7.2% |

**50,487 domains are mail-reachable today** (49.9%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `route2.mx.cloudflare.net` | 2685 | 2797 | yes |
| `route1.mx.cloudflare.net` | 2684 | 2796 | yes |
| `route3.mx.cloudflare.net` | 2683 | 2795 | yes |
| `mail.wabblywabble.com` | 1974 | 1975 |  |
| `mail.wallywatts.com` | 1974 | 1975 |  |
| `generator.email` | 1368 | 1577 |  |
| `aero4.unstablemail.com` | 1291 | 1297 |  |
| `srv4.unstablemail.com` | 1290 | 1296 |  |
| `mx4.beavis99.com` | 1232 | 1232 |  |
| `mx4.beavis99.net` | 1231 | 1231 |  |
| `aspmx.l.google.com` | 981 | 1065 | yes |
| `alt1.aspmx.l.google.com` | 964 | 1046 | yes |
| `park-mx.above.com` | 962 | 1026 | yes |
| `alt2.aspmx.l.google.com` | 960 | 1040 | yes |
| `eforward1.registrar-servers.com` | 896 | 923 | yes |
| `eforward2.registrar-servers.com` | 896 | 923 | yes |
| `eforward3.registrar-servers.com` | 896 | 923 | yes |
| `eforward4.registrar-servers.com` | 896 | 923 | yes |
| `eforward5.registrar-servers.com` | 896 | 923 | yes |
| `smtp.google.com` | 792 | 817 | yes |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 1974 | 1975 |
| `mail.wallywatts.com` | 1974 | 1975 |
| `generator.email` | 1368 | 1577 |
| `aero4.unstablemail.com` | 1291 | 1297 |
| `srv4.unstablemail.com` | 1290 | 1296 |
| `mx4.beavis99.com` | 1232 | 1232 |
| `mx4.beavis99.net` | 1231 | 1231 |
| `email.chatgpt.org.uk` | 741 | 741 |
| `emailfake.com` | 691 | 701 |
| `mx.emlhub.com` | 482 | 482 |
| `smtp.yopmail.com` | 425 | 434 |
| `mail.cleantempmail.com` | 418 | 418 |
| `email.gravityengine.cc` | 388 | 401 |
| `mx.spymail.one` | 378 | 378 |
| `mail.h-email.net` | 365 | 428 |
| `mx.emltmp.com` | 355 | 355 |
| `mx.emlpro.com` | 353 | 353 |
| `mx156.hostedmxserver.com` | 352 | 426 |
| `mx2-hosting.jellyfish.systems` | 344 | 350 |
| `mx3-hosting.jellyfish.systems` | 344 | 350 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `78.47.124.133` | 2713 | 2713 |
| `94.130.108.80` | 2713 | 2713 |
| `162.159.205.23` | 2668 | 2779 |
| `162.159.205.24` | 2668 | 2779 |
| `162.159.205.25` | 2668 | 2779 |
| `162.159.205.17` | 2660 | 2770 |
| `162.159.205.18` | 2660 | 2770 |
| `162.159.205.19` | 2660 | 2770 |
| `162.159.205.11` | 2649 | 2758 |
| `162.159.205.12` | 2649 | 2758 |
| `162.159.205.13` | 2649 | 2758 |
| `91.196.52.205` | 2250 | 2465 |
| `116.202.9.167` | 1939 | 1940 |
| `46.101.111.206` | 1939 | 1940 |
| `142.132.166.12` | 1911 | 1911 |
| `188.166.111.252` | 1911 | 1911 |
| `138.226.240.26` | 1462 | 1475 |
| `146.190.212.90` | 1252 | 1258 |
| `195.123.189.142` | 1244 | 1256 |
| `146.190.223.124` | 1228 | 1234 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 457 |
| High-confidence disposable IPs | 1,158 |
| Promoted to `domains_inferred.txt` | 4 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**8385 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

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
| `099833.xyz` | `park-mx.above.com` |
| `0ak.org` | `mx00.ionos.com` |
| `0hcow.com` | `mxa.mailgun.org` |
| `0hio.net` | `aspmx1.migadu.com` |
| `0nce.net` | `route1.mx.cloudflare.net` |
| `0rg.fr` | `mx1.mail.ovh.net` |
| `0sp.me` | `eforward1.registrar-servers.com` |


*… and 8,355 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
