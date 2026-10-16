# WAHH 2e ch.4: Mapping the Application, the 2026 way

> tally: g5 **26** · g4 **7** · g3 **2** · g2 **8** · g1 **0** (HTML counts them live).
> not verified (the g2 nodes): dead-tool status, WAF/CDN effects, forum-to-repo shift, phpBB paths, jsluice flags beyond `urls`.
>
> **authorized scope only**: PortSwigger Academy, HTB, your own machine, or an in-scope bounty. `$TARGET` is a lab URL or `http://127.0.0.1:8080`; `$TARGET_DOMAIN` is its host. Keep the rate flags.

Mapping comes first [book p.73]. The order holds; many tools died. Each node is a trio: 2011 (book), broke, 2026 way with a command.

## 1. Enumerating visible content {d1}

**Parts:** a recording proxy, a crawler. **Condition:** links and forms exist. **When not:** a client-routed page, or links inside dead compiled objects.

**Manual browsing {d1a}.** Follow every link, finish every multistage form. Still the base; Burp's crawler drives a built-in Chromium [burpcrawl]. [g5]

**Spiders {d1b}.** 2011: Burp Spider, WebScarab follow HTML links. Broke: an HTML-only spider sees a JavaScript app as empty. 2026: `katana -u $TARGET -jc -d 3 -rl 50` parses JS endpoints and caps requests/second [katana]. [g5]

**robots.txt and comments {d1c}.** The owner names hidden paths; comments leak more. 2026: `katana -kf robotstxt,sitemapxml` reads the known files (needs depth 3) [katana]. [g5]

**User-directed spidering {d1d} {H1}.** Browse through a proxy that parses every response; you pick the data, so validation passes and delete links stay unused; open what the spider found but you skipped (Burp "Linked From"). 2026: Burp replays recorded logins, including single sign-on (SSO) [burpcrawl]. H1: browse all, review the site map, access the rest by hand, repeat. [g5]

**Limits and danger {d1e}.** Spiders miss script menus, break sessions, and can call delete or admin functions; the authors defaced a live site this way. 2026: exclude first, `katana -cos 'logout|delete|admin' -rl 20` [katana]. [g5]

**Flash, applets, ActiveX {d1f}.** Links inside compiled objects are invisible to a spider. Adobe blocked Flash on 12 January 2021 [flash]; the gap now sits in JavaScript, read with `katana -jsl` or `jsluice urls app.js` [katana][jsluice]. [g5]

**Dead tools in the chapter {d1g}.** WebScarab archived 2024, ZAP replaced it [wscar] [g3]; ZAP left OWASP in 2023 [zapno] [g5]; DirBuster inactive, now a ZAP add-on, use `ffuf` [dirb] [g5]. CAT, Wikto, IEWatch, httprint, httprecon: no source opened, not verified. [g2]

## 2. Discovering hidden content {d2}

**Parts:** a wordlist, a test that tells a real hit from the app's own error page, a source of removed pages. **Condition:** unlinked paths exist. **When not:** one URL picks its function by parameter (section 3).

**What hides, and why {d2a}.** Test and debug functions, backups, old versions, config and include files, comments, logs. 2026: the same, plus `.git` folders and API docs (not verified). [g2]

**Brute-force names {d2b} {H2}.** 2011: Intruder guesses names, sort by status and length. Broke: DirBuster is dead. 2026: `ffuf -w words.txt -u $TARGET/FUZZ -ac -rate 20`; `-ac` calibrates the fake-404 filter [ffuf]. [g5]

**Reading status codes {d2c} {H2} {Q5}.** A 200 can be a custom not-found page; 401 or 403 means closed but present.
```
curl -s -o /dev/null -w '%{http_code} %{size_download}\n' $TARGET/admin.cpf
# 200 4321  (custom 404: size matches)   401 1250  (exists, wants creds)
```
Q5: app A answers 200 with a not-found body on IIS, so it is absent; app B answers 401 with a Basic realm on Apache-Coyote, so it exists. Filter the fake size with `-fs` [ffuf][curl]. [g5]

**Inferring names {d2d} {H3} {Q2}.** `AddDocument` implies `EditDocument`; numbers, dates, backups (`.bak .old .src`), editor leftovers widen the list. 2026: `ffuf ... -e .bak,.old,.tmp`; per-technology lists built monthly [assetnote][seclists]. Q2: `ucp.php?mode=register` suggests phpBB, whose member pages take numeric ids, so fuzz `memberlist.php?...&u=FUZZ` (paths not verified). [g4]

**Automated discovery tools {d2e}.** Burp Content Discovery combined lists, spidering, extrapolation. 2026: `feroxbuster -u $TARGET -x php,html --rate-limit 20` scans recursively; `--rate-limit` caps requests per second per directory [ferox]. [g4]

**Search engines {d2f} {H4}.** 2011: `site:`, `link:`, `related:`, `cache:`. Broke: the operator page lists none of `link:`, `related:`, `cache:` [gsearch]; `cache:` died 24 September 2024 [serc]. 2026: `site:`, quotes, `-` still work; dead ones fail silently. [g4]

**Archives and URL history {d2g} {H4}.** 2011: Google cache, Wayback. 2026: `gau --subs $TARGET_DOMAIN` merges Wayback, Common Crawl, OTX, URLScan [gau]; `echo $TARGET_DOMAIN | waybackurls` [wburls]; the CDX API with `matchType=prefix&collapse=timestamp:10` returns paths [cdx]. A path archived but 404 live is a route the app once served. [g5]

**Names and forum posts {d2h} {H5}.** List developer names and emails, then search each for posts leaking stack, config, logs. 2026: public code repositories are the new forum (not verified); Google still supports quotes, `-`, `site:` [gsearch]. [g2]

**Web server defaults {d2i} {H6}.** Nikto and Wikto test default files, with many false positives; verify by hand. Broke: the book's `-404` is now `-404string`/`-404code` [nikto]. 2026: `nikto -host $TARGET -404string "Not Found" -Pause 1`, then `nuclei -u $TARGET -as -rl 50`, which picks templates from detected technology [nuclei]. [g5]

## 3. Pages, functional paths, hidden parameters {d3}

**Parts:** one URL carries the function in a parameter, or a published API description. **Condition:** routing by value, not path. **When not:** a plain file tree (section 2).

**Pages vs functional paths {d3a} {H7}.** 2011: `POST /bank.jsp?servlet=TransferFunds&method=confirmTransfer`; parameters name the servlet and method; map in two stages, since directory brute force finds nothing here. 2026: GraphQL puts all calls on one URL; introspection asks the server for its schema.
```
curl -s -X POST $TARGET/graphql -H 'Content-Type: application/json' \
  -d '{"query":"{ __schema { queryType { name } } }"}'
```
`__schema` is always on the query root; many servers disable it in production [gql]. [g4]

**API descriptions as the map {d3b}.** Not in the book. An OpenAPI Description (OAD) describes an API's surface, served as `openapi.json` or `openapi.yaml` [oas]. 2026: `curl -s $TARGET/openapi.json`, then read the routes. [g5]

**Mining JavaScript {d3c}.** 2011: review client code for hints. 2026: `katana -jc` parses JS endpoints; `jsluice urls app.js` prints JSON per URL with `url`, `queryParams`, `method` [jsluice]. Bundles name routes the UI never shows. [g5]

**Hidden parameters {d3d} {H8}.** 2011: Intruder cluster-bomb over `debug test hide` and `true yes 1`. 2026: `arjun -u $TARGET/search --stable` (one thread, 6 to 12 second delay) [arjun]; Param Miner tests up to 65,000 names per request and also guesses headers and cookies [pminer]. [g5]

## 4. Entry points for user input {d4}

**Parts:** URL path, query, body, cookies, trusted headers. **Condition:** input reaches server logic. **When not:** a client-side-only field.

**The entry-point list {d4a}.** URL path, query parameters, POST fields, cookies, and some headers (User-Agent, Referer, Host). 2026: add JSON keys and nested fields (not verified). [g2]

**REST-style path parameters {d4b}.** In `/shop/browse/electronics/iPhone3G/` the path parts are data, injected like query values. 2026: API routes are the modern form; an OAD lists them [oas]. [g5]

**Odd parameter formats {d4c}.** Parameters can sit after a semicolon, in a path, or as URL-encoded XML in one value; dissect the format or miss its fields. 2026: JSON bodies are the common case (not verified). Fuzz each name: `ffuf -w paramnames.txt -u "$TARGET/script.php?FUZZ=test_value" -fs 4242 -rate 10`; a different size is a live name [ffuf]. [g5]

**Headers as input {d4d}.** `Referer`, `User-Agent`, `X-Forwarded-For` are trusted; a mobile User-Agent reaches less-tested code. 2026: Param Miner guesses headers [pminer]; HTTP/2 moves to binary framing but keeps HTTP semantics (RFC 9113) [rfc9113], so it changes the format, not what the app reads. [g5]

**Out-of-band channels {d4e}.** Data can arrive by SMTP mail, a server-side fetch, or a mobile API. 2026: OAST (out-of-band application testing) means a server you control logs lookups the target makes.
```
interactsh-client                       # prints c23b2...oast.pro
curl -s -H "X-Forwarded-For: c23b2...oast.pro" $TARGET
# [c23b2...] Received DNS interaction (A) from ...
```
The client prints each DNS, HTTP, or SMTP hit [oast]. A DNS hit proves the server resolved your value though the page shows nothing. [g5]

## 5. Fingerprinting server-side technology {d5}

**Parts:** `Server` header, error pages, cookie and directory names. **Condition:** at least one is not stripped. **When not:** a CDN normalizes them (not verified).

**Banner grabbing {d5a} {H9} {Q4}.** `Server: Apache/1.3.31` names stack and version. Broke: banners are often trimmed (not verified). 2026: `httpx -l hosts.txt -sc -title -td -rl 50` [httpx]; `curl -sI $TARGET` fetches headers only [curl]. Q4: Coyote is Tomcat's connector package, so `Apache-Coyote` names a Java servlet container (Tomcat) [tomcat]. [g5]

**HTTP fingerprinting {d5b} {H9}.** `httprecon` ranked likely servers by their optional spec differences. 2026: `httpx -td` uses the Wappalyzer dataset [httpx]; the status of httprecon and httprint is not verified. [g2]

**Extensions and error pages {d5c} {H9} {Q1} {Q3}.** `.asp`, `.aspx`, `.jsp`, `.php`, `.dll` name a platform; a missing `.aspx` returns an ASP.NET error. Broke: many routes carry no extension now (not verified). 2026: `curl -sI $TARGET/CookieAuth.dll`. Q1: `CookieAuth.dll` is native code on IIS, a cookie-auth filter; Q3: `Address.asp` is classic ASP. [g4]

**Directories and session cookies {d5d} {H9}.** `JSESSIONID`, `ASPSESSIONID`, `PHPSESSID` and paths like `/servlet` name the stack. Broke: cookie names are often renamed or generic (not verified). 2026: `nuclei -as` and `httpx -td` read more signals [nuclei][httpx]. [g2]

**Third-party components {d5e} {H9}.** Find component and version, then research known flaws. 2026: OSV.dev takes a package, ecosystem and version, a commit, or a purl (package URL).
```
curl -d '{"package":{"name":"nokogiri","ecosystem":"RubyGems"},"version":"1.18.2"}' https://api.osv.dev/v1/query
```
An empty answer means no known entry, not no flaw [osv]. [g5]

## 6. Server-side functionality and unique behavior {d6}

**Parts:** parameter names read like a programmer, consistent across the app. **Condition:** names carry meaning. **When not:** opaque tokens.

**Dissecting requests {d6a} {H10} {Q3}.** `calendar.jsp?isExpired=0&OrderBy=name` means Java, a database `ORDER BY`, and a flag to flip. 2026: the same on JSON and GraphQL fields. Q3: read `action=view` like `isExpired`, try `edit`. [g4]

**REST to internal call {d6b} {H10}.** `/pub/media/117/view` maps to a hidden call like `manager?schema=pub&id=117&action=view`; try `edit`, `add`, higher ids. 2026: `ffuf -w ids.txt -u $TARGET/pub/media/FUZZ/view -mc 200 -rate 10` [ffuf]. [g5]

**Extrapolating behavior {d6c} {H10}.** Parts of one app act alike; an echo function shows the global filter; a decode function reveals your cookie scheme. 2026: a block may be a CDN or WAF, not the app (not verified). [g2]

**Unique behavior {d6d} {H11}.** Hunt bolted-on parts (different style, comments, CAPTCHA, tracking, third-party code); they skip standard defenses. 2026: many are third-party scripts from other hosts (not verified); list them with `katana -jc -rl 50 -em js,json` [katana]. [g5]

## 7. Mapping the attack surface {d7}

**Parts:** the content map, the functional map, features matched to bug classes. **Condition:** mapping ends before probing. **When not:** never; no tool maps an app safely alone [book p.114].

**Map first, probe later {d7a}.** Mapping comes before attack; no tool maps fully and safely, so mix manual work with controlled automation. 2026: Burp's Chromium crawl and login handling help but do not finish it [burpcrawl]. [g5]

**Core functions and mechanisms {d7b} {H12}.** Know the core features, session state, access control, authentication, and support flows like recovery. 2026: the same, plus the API behind each screen. [g4]

**Feature to bug class {d7c} {H12}.** Map each feature to its usual bug: upload to path traversal, login to enumeration, redirect to open redirect, email to injection. 2026: add the API classes (not verified). [g2]

**Check third-party code {d7d} {H12}.** Look up each third-party part in a public vulnerability database. Broke: OSVDB closed 2016 [reg]. 2026: use OSV.dev and `nuclei -as` for known exposures [osv][nuclei]. [g5]

**Plan of attack {d7e} {H12}.** Rank the most interesting functions and the worst bug classes. 2026: first probe all hosts, `httpx -l hosts.txt -sc -title -td -rl 50` [httpx]. [g5]

**The EIS example {d7f}.** The book walks one app, `/auth`, `/core/sitestats`, `/gb`, `/home`, `/pub`, `/shop`, each with its likely bug [book p.110]. 2026: practice the same walk on PortSwigger Academy or HTB labs (lab choice not verified). [g3]

## references

[book] WAHH 2e, Stuttard, Pinto, Wiley 2011, ch.4 pp.73-115, https://portswigger.net/web-security/web-application-hackers-handbook, his copy, 2026-10-16, case. 2011 claims.
[burpcrawl] Burp full crawl and audit, https://portswigger.net/burp/documentation/desktop/automated-scanning/webapp-scans/full-crawl-and-audit, 2026-10-16, official. Chromium crawl, SSO.
[katana] katana, https://github.com/projectdiscovery/katana, 2026-10-16, primary. Crawl flags.
[httpx] httpx, https://github.com/projectdiscovery/httpx, 2026-10-16, primary. Probe flags.
[nuclei] nuclei, https://github.com/projectdiscovery/nuclei, 2026-10-16, primary. `-as`.
[nikto] Nikto, https://github.com/sullo/nikto, 2026-10-16, primary. `-404string`.
[ffuf] ffuf, https://github.com/ffuf/ffuf, 2026-10-16, primary. Fuzz flags.
[ferox] feroxbuster, https://github.com/epi052/feroxbuster, 2026-10-16, primary. `-x`, recursive; `--rate-limit` from src/parser.rs, same repo.
[arjun] Arjun Usage, https://github.com/s0md3v/Arjun/wiki/Usage, 2026-10-16, primary. `--stable`.
[pminer] Param Miner, https://github.com/PortSwigger/param-miner, 2026-10-16, primary. 65,000 names.
[jsluice] jsluice, https://github.com/BishopFox/jsluice/tree/main/cmd/jsluice, 2026-10-16, primary. `urls`.
[gau] gau, https://github.com/lc/gau, 2026-10-16, primary. URL sources.
[wburls] waybackurls, https://github.com/tomnomnom/waybackurls, 2026-10-16, primary. stdin domains.
[cdx] Wayback CDX, https://github.com/internetarchive/wayback/tree/master/wayback-cdx-server, 2026-10-16, official. `prefix`, `collapse`.
[oast] interactsh, https://github.com/projectdiscovery/interactsh, 2026-10-16, primary. Client output.
[osv] OSV.dev query, https://google.github.io/osv.dev/post-v1-query/, 2026-10-16, official. Query body.
[curl] curl manual, https://curl.se/docs/manpage.html, 2026-10-16, official. `-I -w -s`.
[gql] GraphQL introspection, https://graphql.org/learn/introspection/, 2026-10-16, official. `__schema`.
[oas] OpenAPI spec, https://spec.openapis.org/oas/latest.html, 2026-10-16, official. OAD, filenames.
[gsearch] Google operators, https://support.google.com/websearch/answer/2466433, 2026-10-16, official. No `cache:`.
[serc] SE Roundtable, https://seroundtable.com/google-cache-dead-38112.html, 2026-10-16, secondary. `cache:` dead 2024.
[flash] Adobe Flash EOL, https://www.adobe.com/products/flashplayer/end-of-life.html, 2026-10-16, official. 12 Jan 2021.
[dirb] OWASP DirBuster, https://wiki.owasp.org/index.php/DirBuster, 2026-10-16, official. Inactive.
[wscar] WebScarab, https://en.wikipedia.org/wiki/WebScarab, 2026-10-16, secondary. Archived 2024.
[zapno] ZAP status, https://www.zaproxy.org/docs/nowaspzap/, 2026-10-16, official. Left OWASP 2023.
[reg] The Register, https://www.theregister.com/2016/04/06/open_source_vuln_database_closes/, 2026-10-16, secondary. OSVDB closed 2016.
[rfc9113] RFC 9113, https://www.rfc-editor.org/rfc/rfc9113.html, 2026-10-16, official. HTTP/2 semantics.
[tomcat] Tomcat 9 connector, https://tomcat.apache.org/tomcat-9.0-doc/config/http.html, 2026-10-16, official. Coyote.
[assetnote] Assetnote lists, https://wordlists.assetnote.io/, 2026-10-16, primary. Monthly lists.
[seclists] SecLists, https://github.com/danielmiessler/SecLists, 2026-10-16, primary. Fuzzing lists.
