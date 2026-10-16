# Sources opened this run (phase 2, WAHH 2e ch.4), 2026-10-16

Each line: URL, what it settled, grade (.rules/grounding-and-confidence.md).

## Book (target)
- user-input-learning-text/wahh-2e/ch04_mapping_the_application.md — his pasted copy of WAHH 2e ch.4 pp.73-115; all 2011 claims, hack steps H1-H12, questions Q1-Q5 — grade 5 (case)

## Tool docs (primary)
- https://github.com/projectdiscovery/katana — `-u -jc -d(3) -rl(150) -cos -kf(all,robotstxt,sitemapxml, depth 3) -hl -em -jsl -o`, verbatim help lines — grade 5
- https://github.com/projectdiscovery/httpx — `-l -sc -title -td(wappalyzer) -server -rl(150)` — grade 5
- https://github.com/projectdiscovery/nuclei — `-u -l -as(wappalyzer->tags) -rl(150)` — grade 5
- https://github.com/ffuf/ffuf — `-w -u -ac -rate(0) -e -fs -mc`, `?FUZZ=test_value -fs 4242` param example — grade 5
- https://github.com/epi052/feroxbuster — `-u -x` multi-ext example, recursive; no rate-limit flag in README — grade 3
- https://github.com/s0md3v/Arjun/wiki/Usage — `--stable` = 1 thread, 6-12s random delay — grade 5
- https://github.com/PortSwigger/param-miner — identifies hidden params; guesses cookies/headers/params; up to 65,000 names/request — grade 5
- https://github.com/BishopFox/jsluice/tree/main/cmd/jsluice — `urls` mode, output keys url/queryParams/method/headers/type — grade 5
- https://github.com/lc/gau — fetches Wayback, Common Crawl, OTX, URLScan; `--subs`, `--blacklist` — grade 5
- https://github.com/tomnomnom/waybackurls — reads line-delimited domains on stdin — grade 5
- https://github.com/projectdiscovery/interactsh — no-flag run prints `.oast.pro` domain; DNS/HTTP/SMTP interaction lines; `-v` verbose — grade 5
- https://github.com/sullo/nikto — `-host -root -Cgidirs -404code -404string -Pause -maxtime`; no plain `-404` (closest `-no404`) — grade 5

## Standards / official
- https://github.com/internetarchive/wayback/tree/master/wayback-cdx-server — base `web.archive.org/cdx/search/cdx`, `matchType=prefix`, `output=json`, `limit`, `collapse=timestamp:10` (one capture/hour) — grade 5
- https://google.github.io/osv.dev/post-v1-query/ — `POST https://api.osv.dev/v1/query`; body by package+ecosystem+version, commit, or purl; `vulns` array — grade 5
- https://curl.se/docs/manpage.html — `-I` headers only, `-H`, `-d`, `-s`, `-o` write to file, `-w` with `%{http_code}`/`%{size_download}` — grade 5
- https://graphql.org/learn/introspection/ — `__schema` always on the query root; introspection commonly disabled in production — grade 5
- https://spec.openapis.org/oas/latest.html — OAD describes an API's surface (4.1.2); entry doc RECOMMENDED `openapi.json`/`openapi.yaml` — grade 5
- https://support.google.com/websearch/answer/2466433 — operators: quotes, `site:`, `-`, `before:`, `after:`, `filetype:`; `link:`/`related:`/`cache:` absent — grade 5
- https://www.rfc-editor.org/rfc/rfc9113.html — HTTP/2 binary framing, field compression; optimized transport for HTTP semantics — grade 5
- https://tomcat.apache.org/tomcat-9.0-doc/config/http.html — `org.apache.coyote.*` connector packages; Coyote is Tomcat's connector — grade 5
- https://portswigger.net/burp/documentation/desktop/automated-scanning/webapp-scans/full-crawl-and-audit — built-in Chromium crawl; application logins and recorded login sequences for SSO — grade 5
- https://www.adobe.com/products/flashplayer/end-of-life.html — Flash content blocked from running 12 January 2021 — grade 5
- https://wiki.owasp.org/index.php/DirBuster — inactive, archived, now a ZAP Marketplace add-on — grade 5
- https://www.zaproxy.org/docs/nowaspzap/ — ZAP not an OWASP project since August 2023 — grade 5
- https://wordlists.assetnote.io/ — wordlists auto-generated on the 28th each month (Commonspeak2) — grade 3 (per-tech file names not confirmed)
- https://github.com/danielmiessler/SecLists — usernames, passwords, URLs, fuzzing payloads, and more — grade 4

## Secondary
- https://seroundtable.com/google-cache-dead-38112.html — `cache:` operator stopped working, confirmed ~24 September 2024 — grade 3
- https://www.theregister.com/2016/04/06/open_source_vuln_database_closes/ — OSVDB shutdown announced 6 April 2016 — grade 3
- https://en.wikipedia.org/wiki/WebScarab — repository archived 4 April 2024; recommends ZAP as successor — grade 3

## Opened but not cited on the page
- https://portswigger.net/web-security/web-application-hackers-handbook — Academy landing page; holds no ch.4 answer key (mdsec.net/wahh redirects here). Q1-Q5 answered by reasoning from the chapter text instead.
- web.archive.org snapshot of mdsec.net/wahh answers — fetch blocked in this environment; not used.
