# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-10-17 02:24 UTC**.*  
*Last DNS snapshot: **2026-10-17T02:24:44+00:00**.*

This document is regenerated nightly from the bundled [`resolution.sqlite`](../disposable_email/data/) snapshot.
It captures the live mail infrastructure of the disposable email domains shipped with this package.

## Domain list sizes

| List | Domains |
|---|---|
| `domains.txt` (default) | 97,538 |
| `domains_strict.txt` | 98,770 |
| `domains_inferred.txt` (opt-in) | 4 |

## Reachability

Of **100,990** resolved domains:

| Status | Count | % of resolved |
|---|---|---|
| MX_OK | 44,691 | 44.3% |
| A_ONLY | 5,730 | 5.7% |
| NXDOMAIN | 42,397 | 42.0% |
| NO_RECORDS | 980 | 1.0% |
| TIMEOUT | 7,192 | 7.1% |

**50,421 domains are mail-reachable today** (49.9%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `route2.mx.cloudflare.net` | 2684 | 2793 | yes |
| `route1.mx.cloudflare.net` | 2683 | 2792 | yes |
| `route3.mx.cloudflare.net` | 2682 | 2791 | yes |
| `mail.wabblywabble.com` | 1973 | 1975 |  |
| `mail.wallywatts.com` | 1973 | 1975 |  |
| `generator.email` | 1370 | 1578 |  |
| `aero4.unstablemail.com` | 1299 | 1300 |  |
| `srv4.unstablemail.com` | 1298 | 1299 |  |
| `mx4.beavis99.com` | 1232 | 1232 |  |
| `mx4.beavis99.net` | 1231 | 1231 |  |
| `aspmx.l.google.com` | 983 | 1066 | yes |
| `alt1.aspmx.l.google.com` | 966 | 1047 | yes |
| `alt2.aspmx.l.google.com` | 962 | 1041 | yes |
| `park-mx.above.com` | 948 | 1012 | yes |
| `eforward1.registrar-servers.com` | 895 | 921 | yes |
| `eforward2.registrar-servers.com` | 895 | 921 | yes |
| `eforward3.registrar-servers.com` | 895 | 921 | yes |
| `eforward4.registrar-servers.com` | 895 | 921 | yes |
| `eforward5.registrar-servers.com` | 895 | 921 | yes |
| `smtp.google.com` | 792 | 814 | yes |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `mail.wabblywabble.com` | 1973 | 1975 |
| `mail.wallywatts.com` | 1973 | 1975 |
| `generator.email` | 1370 | 1578 |
| `aero4.unstablemail.com` | 1299 | 1300 |
| `srv4.unstablemail.com` | 1298 | 1299 |
| `mx4.beavis99.com` | 1232 | 1232 |
| `mx4.beavis99.net` | 1231 | 1231 |
| `email.chatgpt.org.uk` | 741 | 741 |
| `emailfake.com` | 688 | 698 |
| `mx.emlhub.com` | 483 | 483 |
| `smtp.yopmail.com` | 424 | 434 |
| `mail.cleantempmail.com` | 418 | 418 |
| `email.gravityengine.cc` | 390 | 403 |
| `mx.spymail.one` | 378 | 378 |
| `mail.h-email.net` | 365 | 425 |
| `mx.emltmp.com` | 355 | 355 |
| `mx.emlpro.com` | 353 | 353 |
| `mx156.hostedmxserver.com` | 352 | 418 |
| `mx2-hosting.jellyfish.systems` | 343 | 349 |
| `mx3-hosting.jellyfish.systems` | 343 | 349 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `78.47.124.133` | 2714 | 2714 |
| `94.130.108.80` | 2714 | 2714 |
| `162.159.205.23` | 2666 | 2775 |
| `162.159.205.24` | 2666 | 2775 |
| `162.159.205.25` | 2666 | 2775 |
| `162.159.205.17` | 2659 | 2766 |
| `162.159.205.18` | 2659 | 2766 |
| `162.159.205.19` | 2659 | 2766 |
| `162.159.205.11` | 2647 | 2754 |
| `162.159.205.12` | 2647 | 2754 |
| `162.159.205.13` | 2647 | 2754 |
| `91.196.52.205` | 2245 | 2459 |
| `116.202.9.167` | 1938 | 1940 |
| `46.101.111.206` | 1938 | 1940 |
| `142.132.166.12` | 1909 | 1911 |
| `188.166.111.252` | 1909 | 1911 |
| `138.226.240.26` | 1463 | 1476 |
| `146.190.212.90` | 1258 | 1259 |
| `195.123.189.142` | 1247 | 1256 |
| `146.190.223.124` | 1234 | 1235 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 456 |
| High-confidence disposable IPs | 1,151 |
| Promoted to `domains_inferred.txt` | 4 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**8372 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

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
| `0ut.online` | `smtp.google.com` |
| `0x7121.com` | `park-mx.above.com` |


*… and 8,342 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
