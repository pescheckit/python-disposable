# Disposable Email Infrastructure — Statistics

*Generated automatically. Last build: **2026-11-19 02:15 UTC**.*  
*Last DNS snapshot: **2026-11-18T02:51:16+00:00**.*

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
| MX_OK | 40,808 | 35.8% |
| A_ONLY | 5,265 | 4.6% |
| NXDOMAIN | 37,476 | 32.9% |
| NO_RECORDS | 1,029 | 0.9% |
| TIMEOUT | 29,459 | 25.8% |

**46,073 domains are mail-reachable today** (40.4%). The remainder are historical: domains that no longer resolve (NXDOMAIN) but are kept on the list because disposable operators frequently re-register such names.

## Top disposable mail backends (MX hosts)

Including shared infrastructure (Cloudflare/Google/etc.):

| MX host | Disposable domains | Total resolved | Shared infra |
|---|---|---|---|
| `generator.email` | 8202 | 8468 |  |
| `route2.mx.cloudflare.net` | 1573 | 1795 | yes |
| `route3.mx.cloudflare.net` | 1573 | 1795 | yes |
| `route1.mx.cloudflare.net` | 1572 | 1794 | yes |
| `mail.wabblywabble.com` | 1379 | 1379 |  |
| `mail.wallywatts.com` | 1379 | 1379 |  |
| `mx4.beavis99.com` | 1084 | 1084 |  |
| `mx4.beavis99.net` | 1083 | 1083 |  |
| `park-mx.above.com` | 906 | 1035 | yes |
| `email.chatgpt.org.uk` | 794 | 807 |  |
| `smtp.yopmail.com` | 715 | 724 |  |
| `aero4.unstablemail.com` | 674 | 674 |  |
| `srv4.unstablemail.com` | 672 | 672 |  |
| `aspmx.l.google.com` | 573 | 660 | yes |
| `emailfake.com` | 570 | 584 |  |
| `alt1.aspmx.l.google.com` | 562 | 647 | yes |
| `alt2.aspmx.l.google.com` | 559 | 642 | yes |
| `eforward1.registrar-servers.com` | 491 | 538 | yes |
| `eforward2.registrar-servers.com` | 491 | 538 | yes |
| `eforward3.registrar-servers.com` | 491 | 538 | yes |


With shared infrastructure excluded (these are the *true* disposable mail backends):

| MX host | Disposable domains | Total resolved |
|---|---|---|
| `generator.email` | 8202 | 8468 |
| `mail.wabblywabble.com` | 1379 | 1379 |
| `mail.wallywatts.com` | 1379 | 1379 |
| `mx4.beavis99.com` | 1084 | 1084 |
| `mx4.beavis99.net` | 1083 | 1083 |
| `email.chatgpt.org.uk` | 794 | 807 |
| `smtp.yopmail.com` | 715 | 724 |
| `aero4.unstablemail.com` | 674 | 674 |
| `srv4.unstablemail.com` | 672 | 672 |
| `emailfake.com` | 570 | 584 |
| `mx.emlhub.com` | 439 | 439 |
| `tinyhost.shop` | 416 | 416 |
| `mx.spymail.one` | 340 | 340 |
| `mx.emltmp.com` | 325 | 325 |
| `mx.emlpro.com` | 321 | 321 |
| `smtp.215.im` | 308 | 312 |
| `email.gravityengine.cc` | 294 | 294 |
| `mx.dropmail.me` | 291 | 291 |
| `mx.freeml.net` | 277 | 277 |
| `mx156.hostedmxserver.com` | 268 | 442 |


## Top mail IPs by disposable domain count

| IP address | Disposable domains | Total resolved |
|---|---|---|
| `91.196.52.205` | 7995 | 8269 |
| `78.47.124.133` | 2686 | 2686 |
| `94.130.108.80` | 2686 | 2686 |
| `162.159.205.17` | 1357 | 1575 |
| `162.159.205.18` | 1357 | 1575 |
| `162.159.205.19` | 1357 | 1575 |
| `162.159.205.23` | 1346 | 1564 |
| `162.159.205.24` | 1346 | 1564 |
| `162.159.205.25` | 1346 | 1564 |
| `162.159.205.11` | 1343 | 1561 |
| `162.159.205.12` | 1343 | 1561 |
| `162.159.205.13` | 1343 | 1561 |
| `116.202.9.167` | 1244 | 1244 |
| `46.101.111.206` | 1244 | 1244 |
| `142.132.166.12` | 1233 | 1233 |
| `188.166.111.252` | 1233 | 1233 |
| `188.245.74.208` | 1055 | 1055 |
| `195.201.18.63` | 1050 | 1050 |
| `158.101.127.66` | 1049 | 1049 |
| `13.223.25.84` | 939 | 945 |


## Inferred candidates pipeline

| Metric | Value |
|---|---|
| High-confidence disposable MX hosts (≥5 disposables, not shared) | 382 |
| High-confidence disposable IPs | 955 |
| Promoted to `domains_inferred.txt` | 4 |


A candidate domain (sourced from Certificate Transparency logs) is promoted to `domains_inferred.txt` when its MX or IP intersects with one of the high-confidence disposable clusters above.

## Possible upstream false positives (phase 3b)

**5181 domains** in `domains.txt` resolve *only* to MX hosts on the shared-infra allowlist (Google Workspace, Microsoft 365, Cloudflare Email Routing, etc.). These may be legitimate businesses incorrectly listed upstream — or shell domains owned by disposable operators who happen to use mainstream mail. Review manually; this script does NOT auto-remove them.

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


*… and 5,151 more. Full list available by querying the SQLite directly.*


---

*This file is auto-generated by `scripts/generate_stats.py`. Do not edit by hand.*
