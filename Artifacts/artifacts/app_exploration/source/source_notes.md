# source notes: app exploration class, all slices

built by twin/notes_merge.py. ids are cNN_vN.NN. do not edit here, edit the slice file and re-merge.


## v5 5. sub recon.mp4

### c01_v5 00:01-19:51

- c01_v5.01 [00:16] principle: before touching traffic, learn what exists at a target. why: you cannot study what you have not found. http: -. frame: -
- c01_v5.02 [00:44] principle: only in-scope hosts may be studied; one host in scope means only that host. why: authorization sets the boundary. http: -. frame: -
- c01_v5.03 [01:14] principle: he favors wildcard scope (*.target). why: most realistic, broader coverage than the main site. http: -. frame: -
- c01_v5.04 [01:44] signal: employee or third-party subdomains (e.g. admin.target) can host admin panels. why: internal tooling lives off the main site. http: Host. frame: -
- c01_v5.05 [02:31] tool: Shodan and Censys (censys.io) back into subdomain data for large recon; not shown. why: extra coverage, small gain for the time. http: -. frame: -
- c01_v5.06 [03:18] signal: TLS certs name the hosts a server serves; an IP over HTTPS can return a cert listing accepted names. why: certs leak domain info. http: TLS SAN. frame: -
- c01_v5.07 [03:35] technique: enumeration pipeline: two sources, merge, dedupe, then check which are alive. why: he runs it on every target. http: -. frame: -
- c01_v5.08 [03:59] principle: accept a fast method covering most (98%(?)) hosts over a perfect slow one. why: find bugs quickly, spend time well. http: -. frame: -
- c01_v5.09 [04:48] tool: crt.sh, a certificate transparency search; type a domain, get cert-logged names. why: certs leak subdomains. http: GET crt.sh/?q=etsy.com. frame: 04:58 browser loading crt.sh
- c01_v5.10 [05:13] warning: crt.sh often crashes on big targets; rerun, or toggle expired vs unexpired certs. why: scale. his script retries until a clean response. http: -. frame: -
- c01_v5.11 [05:40] example: etsy.com returns a huge list, many Fastly names, explaining the fastly.net seen earlier. why: cert names show CDN layout. http: -. frame: 08:13 crt.sh table columns ID, logged, not before/after, common name, matching identities, issuer; names like api-origin.etsy.com, *.etsy.com.map.fastly.net
- c01_v5.12 [05:40] signal: one host in scope but hundreds in certs means scope is narrower than the real footprint. why: compare the two. http: -. frame: -
- c01_v5.13 [06:06] signal: names containing "origin" (api-origin) may point at the server behind a CDN/WAF. why: naming hints at the stack. http: Host. frame: 08:13 api-origin.etsy.com rows
- c01_v5.14 [06:31] principle: the path is client, then WAF, then origin IP; the origin is the server holding the content. why: understand the layers. http: Host, IP. frame: -
- c01_v5.15 [07:54] offensive: he notes recon can surface an origin IP to reach a server directly, past the fronting layer. why: shows why host mapping matters. http: Host, IP. frame: -
- c01_v5.16 [08:16] example: crt.sh output even returned stray email addresses for Etsy. why: logs leak more than hostnames. http: -. frame: -
- c01_v5.17 [08:38] tool: securitytrails.com, second source; he logs in with a burner account and API key. why: two sources beat one. http: -. frame: -
- c01_v5.18 [09:08] example: SecurityTrails reports Etsy has over 10,000 subdomains. why: shows scale of a large target. http: -. frame: -
- c01_v5.19 [09:35] principle: huge counts are mostly noise (customer store names); separate company hosts from customer ones. why: focus on what the org runs. http: -. frame: -
- c01_v5.20 [10:24] signal: an Okta subdomain (okta.target) signals internal/employee authentication, so internal apps likely live there. why: Okta is an auth platform. http: Host. frame: 10:35 SecurityTrails cert list: openapi/api/www/image/*.etsy.com rows, issuer DigiCert
- c01_v5.21 [10:50] signal: names like secrets.target, "open API", "API origin", CDN hint at what runs where. why: read names to model the app. http: Host. frame: 10:35 api.etsy.com, openapi.etsy.com visible
- c01_v5.22 [11:20] example: bugcrowd.com has a reasonable ~99 subdomains; he switches to it as a smaller teaching target. why: Etsy is too big to work through live. http: -. frame: 11:06 SecurityTrails cert table for etsy.com
- c01_v5.23 [11:46] technique: use SecurityTrails "historical data" to find an origin IP from before a WAF was added. why: old records predate the current fronting. http: -. frame: -
- c01_v5.24 [12:16] signal: historical data shows each IP with first-seen and duration, revealing provider changes. why: timeline of hosting. http: -. frame: -
- c01_v5.25 [12:44] example: bugcrowd.com moved from Amazon IPs to Cloudflare around 2013-2014 per history. why: shows the switch is visible. http: -. frame: -
- c01_v5.26 [13:10] example: files.bugcrowd.com looks important; its history is all Fastly, earlier Cloudflare. why: per-host history shows infra moves. why: -. http: Host. frame: 14:48 SecurityTrails files.bugcrowd.com subdomains page, hosting provider Fastly, 1 result
- c01_v5.27 [13:40] principle: inspect individual subdomains, not just the list, for anything that stands out. why: the interesting host is in the detail. http: -. frame: -
- c01_v5.28 [14:05] tool: his Python 3 script "get subdomains" calls both sources; needs the requests library via pip. why: automates the pipeline. http: -. frame: -
- c01_v5.29 [14:34] tool: the SecurityTrails API key is set in the script; a free key caps results at ~2000. why: know the limit before trusting output. http: API key. frame: -
- c01_v5.30 [15:00] signal: crt.sh has no 2000 cap, so it can exceed the SecurityTrails free limit on big targets. why: pick the source for the target size. http: -. frame: -
- c01_v5.31 [15:26] step: run `python get_subdomains bugcrowd.com` from the hack files folder. why: demo the tool. http: -. frame: -
- c01_v5.32 [15:52] step: script pulls SecurityTrails first (fast), then unexpired certs from crt.sh. why: combine both before dedupe. http: -. frame: -
- c01_v5.33 [16:17] example: 115 unique subdomains result; crt.sh added names SecurityTrails' 99 missed. why: two sources widen coverage. http: -. frame: -
- c01_v5.34 [16:17] signal: output written to bugcrowd.txt, a plain host list. why: feed to the next step. http: -. frame: 16:45 Notepad++ showing bugcrowd.com host list: email.assetinventory, gateway-admin, crowdcontrol.a.bugcrowd.com, etc.
- c01_v5.35 [16:46] tool: he uses Notepad++ (Edit > Line Operations > Sort Lexographically) to order the list. why: alphabetical order is easier to scan. http: -. frame: 16:45 Notepad++ host list
- c01_v5.36 [17:12] step: delete obvious alias/junk entries that explain the count gap. why: clean the list before probing. http: -. frame: -
- c01_v5.37 [17:38] step: rerun the script on etsy.com in the background while explaining. why: keep the demo moving. http: -. frame: -
- c01_v5.38 [17:55] technique: check which hosts are live by copying the list into Burp Suite. why: a returned subdomain is not always responsive. http: -. frame: -
- c01_v5.39 [18:14] tool: send a plain GET request to Burp Intruder, a tool for sending many requests at once. why: iterate the host list. http: GET /. frame: 18:10 Burp Suite Repeater, request/response panes, target https://www.etsy.com, Inspector panel
- c01_v5.40 [18:40] step: strip cookies from the base request to keep it minimal. why: not needed for a liveness check. http: Cookie. frame: -
- c01_v5.41 [19:01] step: set the request protocol to HTTP/1.1. why: more hosts accept 1.1 than 2, avoids rejection. http: HTTP version. frame: -
- c01_v5.42 [19:21] step: mark the host value as the Intruder insertion point and paste the host list as payloads. why: swap each host into the same request. http: Host. frame: -

#### techniques seen
- subdomain enumeration pipeline: c01_v5.07, c01_v5.09, c01_v5.17, c01_v5.28, c01_v5.31, c01_v5.32
- cert transparency recon: c01_v5.06, c01_v5.09, c01_v5.11
- historical-IP / origin discovery: c01_v5.15, c01_v5.23, c01_v5.24, c01_v5.25
- reading host names to model the app: c01_v5.19, c01_v5.20, c01_v5.21, c01_v5.27
- liveness check with Burp Intruder: c01_v5.38, c01_v5.39, c01_v5.41, c01_v5.42

### c02_v5 19:51-39:08

- c02_v5.01 [19:51] tool: Burp Intruder, mark insertion point with "add squiggly" (§ markers); clear squigglies resets positions. why: defines where each payload goes. http: request line. frame: -
- c02_v5.02 [20:16] tool: Intruder resource pool, raise concurrent requests to ~255, delay 0. why: non-responsive internal domains hang, so bulk recon is slow at the default 10. http: -. frame: -
- c02_v5.03 [20:42] tool: Intruder settings, 0 retries on network failure. why: a host that ignores the first try likely ignores the second. http: -. frame: -
- c02_v5.04 [20:42] step: spray the subdomain list as payloads to check which are live. why: liveness check. http: HTTPS GET on port 443. frame: -
- c02_v5.05 [21:05] signal: default scheme/port is HTTPS 443, same as a browser call. why: baseline reachability. http: 443. frame: -
- c02_v5.06 [21:31] technique: sort results by status code and response length. why: one odd value makes a host stand out in a huge list. http: status, Content-Length. frame: -
- c02_v5.07 [22:07] signal: read status codes. 200 ok, 204 ok no content, 301/302 redirect (often to login), 403 forbidden, 400 bad request, 404 not found. why: codes hint at what the host is. http: status codes. frame: -
- c02_v5.08 [22:37] example: 403s trace to Amazon; a Varnish cache server and an XML "access denied" from an S3 bucket. why: fingerprint the stack. http: Server: varnish, S3 XML body. frame: -
- c02_v5.09 [23:04] principle: do not discard 404. root has no default document (default.aspx/.jsp/.php), but paths may still live there. why: gold hides behind 404. http: 404. frame: -
- c02_v5.10 [23:58] principle: no response ≠ down. host may answer on a different port or be fully blocked; 443 alone does not prove not-internet-facing. why: avoid wrong conclusions. http: -. frame: -
- c02_v5.11 [24:28] aside: nmap port scanning on the IP could find other ports; not taught here. why: out of web scope. http: -. frame: -
skip 24:55-24:55: frame 0025 is an Intruder results table (status/length columns), adds no new fact over speech.
- c02_v5.12 [24:56] technique: re-run the same sweep on HTTP to compare. why: HTTP vs HTTPS liveness differs. http: HTTP port 80. frame: -
- c02_v5.13 [25:14] signal: HTTP run yields many 301s redirecting to HTTPS; a few hosts may answer only on 80. why: more surface. http: 301, Location. frame: -
- c02_v5.14 [25:43] signal: 308 permanent redirect spotted, and a "WAAS API"(?) host that responds. why: unusual code is worth noting. http: 308. frame: -
- c02_v5.15 [26:13] technique: Intruder grep-extract to parse the Location header. why: read redirect targets by eye, no scanner. http: Location header. frame: -
- c02_v5.16 [26:39] step: grep-extract start-after "location", delimiter space. why: isolates the redirect URL per response. http: Location value. frame: -
- c02_v5.17 [27:58] example: learn.security-awareness.bugcrowd.com redirects to /platform/login. why: a host wanting auth is a target. http: Location /platform/login. frame: -
- c02_v5.18 [27:58] principle: prefer things that require authentication over open ones. why: access-control and auth-bypass goals live there. http: -. frame: -
skip 29:02-29:21: frames 0026/0028/0029 are Intruder payload/results views, already described by speech.
- c02_v5.19 [28:28] example: Etsy recon found 2,106 subdomains (SecurityTrails(?) claimed ~10,000; many dupes / user shops). why: gauge real surface size. http: -. frame: -
- c02_v5.20 [28:58] step: edit > line operations > sort lexicographically, then clear/paste into Intruder. why: tidy the 2,100-domain list before spraying. http: -. frame: 0029 shows 200-responder rows (actionsrv, addsterminal, careers, community, image, investments) in the results grid.
- c02_v5.21 [29:26] signal: few 200s come back for Etsy; a 200 means the host accepts an anonymous user. why: not-the-norm hosts stand out. http: 200. frame: -
- c02_v5.22 [29:56] principle: always be reading the responses; build a mental knowledge base of the target. why: learning beats blind scanning. http: -. frame: -
- c02_v5.23 [30:26] example: a "Phone2Action"/campaign status page reveals Etsy uses Quorum Phone2Action software. why: known-vuln research pivot. http: response body "campaign". frame: 0030 shows 200 rows action.etsy.com and related subdomains.
- c02_v5.24 [30:53] technique: shift from "is it alive" to "what lives there" (content discovery). why: second recon phase. http: -. frame: -
- c02_v5.25 [31:12] step: Google/DuckDuckGo dork site:action.etsy.com. why: cheap first look at indexed pages. http: -. frame: -
skip 31:00-31:56: frames 0032/0033/0035/0036/0038 track the search-engine attempts; 0038 confirms the site: dork in Google, no extra fact.
- c02_v5.26 [31:39] example: site: dork returns nothing on both engines. why: unindexed host needs another source. http: -. frame: 0038 shows site:action.etsy.com query with command prompt open.
- c02_v5.27 [32:05] tool: gau (GetAllUrls), fetches known URLs from Wayback, Common Crawl, AlienVault OTX, VirusTotal. why: pulls indexed/intercepted links a search engine misses. http: -. frame: 0040 shows gau output of action.etsy.com URLs.
- c02_v5.28 [32:37] tool: Waymore(?) as an alternative to gau, may check extra sources. why: wider link coverage. http: -. frame: 0040 README visible.
- c02_v5.29 [33:06] signal: VirusTotal holds links people scanned; may contain sensitive download URLs. why: source of leaked links. http: -. frame: 0045 shows waymore About page listing VirusTotal source.
- c02_v5.30 [33:35] step: run gau per domain; note exactly which domain was queried. why: hard to track in a big list. http: -. frame: -
- c02_v5.31 [33:49] tool: his own gau_batch.py reads all_domains.txt and runs gau one-at-a-time, slow, to avoid blocks. why: overnight bulk history collection. http: -. frame: 0052 shows Notepad++ "import subprocess, time" and etsy.com.txt output.
- c02_v5.32 [34:15] principle: populate all_domains.txt only with internet-responsive hosts. why: no point pulling history for unreachable ones. http: -. frame: -
- c02_v5.33 [34:55] signal: gau output shows app/, css/, js/, images/ folders. why: standard app makeup = real application present. http: paths. frame: -
- c02_v5.34 [35:22] principle: always load every JavaScript file in the browser; JS can reveal more links and data. why: expands the map. http: .js responses. frame: -
- c02_v5.35 [35:22] signal: seller-dashboard URL carries a ref ID (integer). why: possible seller ID, IDOR/pivot candidate later. http: ?ref=<int>. frame: -
- c02_v5.36 [35:51] example: hitting the seller-dashboard ref URL returns "campaign not active" (dead link). why: content exists but inactive. http: 200/dead. frame: 0052.
- c02_v5.37 [36:19] technique: find+replace to strip https://action.etsy.com (and http) from the URL list, leaving path stems. why: turn full URLs into Intruder payloads. http: request path. frame: 0052/0056.
- c02_v5.38 [36:45] step: copy a logged request to Intruder, mark path as § position, paste the stems as payloads. why: replay every discovered path. http: GET <path>. frame: 0056 shows Intruder payloads list of etsy.com subdomains.
- c02_v5.39 [37:11] tool: against the live target, resource pool to 1 concurrent request, 500 ms delay. why: a WAF is present; avoid getting blocked. http: -. frame: -
- c02_v5.40 [37:40] signal: compare response lengths; same-length cluster = boilerplate, an outlier length or a 200 vs 404 flags something real. why: finds the interesting path. http: status, length. frame: -
- c02_v5.41 [38:10] step: sort by response length descending. why: big responses (JS, live pages) surface first. http: Content-Length. frame: -
- c02_v5.42 [38:38] example: a "signatures" page returned content showing another researcher's injected test ("PJ Hacker bugcrowd Barcelona"); he suspects a stored-input artifact, not clearly sensitive. why: evidence others probed this app. http: response body. frame: -

#### techniques seen
- liveness sweep in Intruder: c02_v5.02, c02_v5.04, c02_v5.12
- status/length triage: c02_v5.06, c02_v5.40, c02_v5.41
- redirect parsing (grep-extract): c02_v5.15, c02_v5.16
- content discovery (dorks + gau/waymore): c02_v5.25, c02_v5.27, c02_v5.30
- URL-list to Intruder payloads: c02_v5.37, c02_v5.38

### c03_v5 39:08-58:12

- c03_v5.01 [39:08] signal: a different response size flags an endpoint worth a look. why: odd size means the app treats that path specially. http: HTTP response Content-Length. frame: -
- c03_v5.02 [39:08] principle: assume you are not the first to look; others have touched the target. why: tempers expectation of easy finds. http: -. frame: -
- c03_v5.03 [39:38] signal: a 302 tells him something lives at that path. why: a redirect means the server knows the resource. http: HTTP 302 redirect. frame: -
- c03_v5.04 [39:38] step: follow the 302; it pointed to another campaign ID, also expired. why: to see where the app routes. http: Location header to a campaign ID. frame: -
- c03_v5.05 [39:53] tool: Burp Suite repeater via right-click send, or the "follow redirection" button in repeater. why: faster than the browser. http: -. frame: -
- c03_v5.06 [40:07] principle: phase one is judging whether a domain is worth deeper time. why: triage before effort. http: -. frame: -
- c03_v5.07 [40:33] signal: an API returning data on odd URLs hints there is something here. why: live data means real functions behind it. http: API URL returning a body. frame: -
- c03_v5.08 [40:33] signal: a reference to login.css implies a login feature exists. why: why ship login styling with no login. http: login.css asset. frame: -
- c03_v5.09 [40:59] step: he opens login.css and sees form/input styling, confirming a hidden login form. why: proof a login page exists. http: GET login.css. frame: -
- c03_v5.10 [40:59] example: /app returned signatures, maybe the app name. why: a path that answers is a lead. http: /app path. frame: -
skip 40:10 window edge: frame 0073 shows Intruder attack on action.etsy.com, same thread as below.
- c03_v5.11 [41:27] technique: move to Burp extensions to process traffic, the next recon phase. why: automate link/param discovery. http: -. frame: -
- c03_v5.12 [41:27] tool: GAP extension (Get All Parameters, links, words). why: lazy but good starting point. http: -. frame: -
- c03_v5.13 [41:56] step: enable GAP under extensions; it takes a moment to run. why: setup before use. http: -. frame: -
- c03_v5.14 [42:18] tool: extension settings need a Jython jar, downloaded and pointed to. why: Jython add-ons will not install without it. http: -. frame 0081: Burp default settings, Python environment, select Jython file.
- c03_v5.15 [42:43] warning: each extension slows Burp; run the minimum. why: too many and it dies. http: -. frame: -
- c03_v5.16 [43:02] tool: his live Burp runs only JSON Web Tokens and GAP. why: he keeps it lean. http: -. frame: -
- c03_v5.17 [43:26] warning: GAP does nothing unless a scope is set in the target dialog. why: it only acts inside scope. http: -. frame: -
- c03_v5.18 [43:26] step: right-click the host, extensions, GAP; an asterisk flags finds. why: run it per host. http: -. frame: -
- c03_v5.19 [43:55] signal: GAP finds little until you have hit real JavaScript. why: it mines JS for links/params. http: -. frame: -
- c03_v5.20 [43:55] example: a static HTML page with JS (smooth-scroll, github cifrin/andy (?)) turned up. why: shows what GAP surfaces. http: JS file. frame: -
- c03_v5.21 [44:49] tool: IPVanish VPN to switch IPs fast during testing. why: avoid getting his real IP blocked. http: source IP. frame: -
- c03_v5.22 [45:33] tool: waymore (?) v7 and GAP by TomNomNom (?) find links from archives and JS. why: coverage of historical URLs. http: -. frame 0103: waymore github "About - v7" page.
- c03_v5.23 [45:36] step: send action.etsy.com root to Intruder, type "test", add payload markers. why: set up directory fuzzing. http: GET / on action.etsy.com. frame: -
- c03_v5.24 [45:36] tool: his supplied hack files wordlist directory. why: ready lists for fuzzing. http: -. frame: -
- c03_v5.25 [46:04] tool: raft directories list (~70k) with payload processing set to lowercase. why: catch case-sensitive paths, mostly lower. http: fuzzed path segment. frame: -
- c03_v5.26 [46:04] step: start with 10 concurrent requests. why: pace the scan. http: -. frame: -
- c03_v5.27 [46:33] signal: not getting blocked suggests the asset is not behind the WAF. why: WAF would throttle. http: -. frame: -
- c03_v5.28 [46:33] signal: this asset ignores the DataDome cookie. why: another sign it is unprotected. http: DataDome cookie. frame: -
- c03_v5.29 [46:33] signal: the single letter "P" caused a 500 server error. why: an error path is worth probing. http: HTTP 500. frame: -
- c03_v5.30 [47:03] signal: a Set-Cookie returned an action-production JWT plus an XSRF token. why: reveals auth scheme, though on every request. http: Set-Cookie, JWT, XSRF token. frame: -
- c03_v5.31 [47:03] technique: paste the cookie into Decoder and decode as base64. why: check for readable data. http: base64 cookie value. frame: -
- c03_v5.32 [47:33] signal: the cookie decoded to gibberish, nothing useful. why: still worth the look. http: -. frame: -
- c03_v5.33 [47:33] offensive: he tests /P and /1 in repeater for a different response. why: probe the 500 trigger. http: GET /P, GET /1. frame: -
- c03_v5.34 [48:02] signal: requests now forbidden; AWS WAF is running after all. why: block kicked in. http: HTTP 403. frame: -
- c03_v5.35 [48:24] principle: analyze Intruder output, do not run and walk away; ~2500 requests got through before the block. why: results after a block are noise. http: -. frame: -
- c03_v5.36 [48:53] example: redirects revealed /vendor, /storage, /packages folders on the server. why: real directories mapped. http: 301/302 to those paths. frame: -
- c03_v5.37 [48:53] example: a /login page was found. why: the hidden login confirmed. http: /login. frame: -
- c03_v5.38 [49:32] signal: /language came back with JSON. why: a live API endpoint. http: JSON response. frame: -
- c03_v5.39 [50:00] signal: the root /vendor path is blocked, so it is a real directory. why: server guards directory roots. http: blocked GET /vendor. frame 0116: Intruder results, /vendor /storage /packages 301s on action.etsy.com.
- c03_v5.40 [50:29] signal: the login page seems deliberately hidden. why: would need peeling back more layers. http: redirect to /login. frame: -
- c03_v5.41 [50:44] principle: keep digging; curiosity about what runs here is the right attitude. why: exploration mindset is the job. http: -. frame: -
- c03_v5.42 [51:12] technique: Google the software, download a trial, or find others running it to learn the campaign link shape. why: infer the target from a known instance. http: campaign link pattern. frame: -
- c03_v5.43 [51:52] tool: crt.sh and securitytrails.com for subdomains. why: good sources to seed targets. http: -. frame: -
- c03_v5.44 [51:52] principle: prefer wildcard programs over single-website scope. why: single-site, many-subdomain scopes are gimmick security. http: -. frame: -
- c03_v5.45 [52:20] tool: get_subdomains.py needs a free securitytrails API key pasted into the file. why: generates clean domain output files. http: -. frame 0123: get_subdomains.py, securitytrails v1/domain subdomains API, apiKey var.
- c03_v5.46 [52:47] step: find which domains are internet-facing, paste responsive ones into all_domains.txt. why: build the working list. http: -. frame: -
- c03_v5.47 [53:06] signal: "responsive" means any domain that returned a status code. why: defines what goes in the list. http: HTTP status code. frame: -
- c03_v5.48 [53:27] step: run all_domains.txt through the gal batch. why: process every responsive domain. http: -. frame: -
- c03_v5.49 [53:27] technique: skim GAL outputs for sensitive or auth-bypass links, especially on fresh targets. why: new targets leak easy wins. http: URLs in GAL output. frame: -
- c03_v5.50 [54:05] principle: log all the easy wins before the hard ones; it only gets harder. why: order of effort. http: -. frame: -
- c03_v5.51 [54:31] signal: shop subdomains 301 to /shop/<name>. why: lets him filter non-shop domains out. http: 301 Location /shop/<name>. frame: -
- c03_v5.52 [54:31] technique: grep-extract the Location header and filter out shop redirects to isolate the rest. why: pull signal from subdomain noise. http: Location response header. frame: -
- c03_v5.53 [55:31] example: "AEM" = Adobe Experience Manager; damn.etsy bounces to a login. why: recognizing known software. http: redirect to login. frame: -
- c03_v5.54 [56:31] example: etsy.binder.com (?) redirected to damn.etsy.com. why: odd entry worth noting. http: redirect Location. frame: -
- c03_v5.55 [56:55] example: an actual login panel, likely AEM. why: confirms the stack. http: login panel page. frame 0136: browser, blank tab (panel not loaded in this capture).
- c03_v5.56 [56:55] technique: parse the Location response header to cut shop noise and spot real panels. why: the header reveals the target fast. http: Location header. frame: -
- c03_v5.57 [57:18] principle: one shop bug means all shops; test only a shop you own. why: avoid harming other sellers. http: -. frame: -
- c03_v5.58 [57:46] aside: random redirects and oddities are worth noting even if shops are not. why: they carry value. http: redirects. frame: -
- c03_v5.59 [58:12] aside: next is deeper recon and finding issues once inside the app via the proxy. why: sets the series direction. http: proxied traffic. frame: -

#### techniques seen
- judge domain interest (phase one): c03_v5.06, c03_v5.07
- read client assets for hidden features: c03_v5.08, c03_v5.09
- Burp extension recon (GAP): c03_v5.11, c03_v5.12, c03_v5.18, c03_v5.22
- Intruder directory fuzzing: c03_v5.23, c03_v5.25, c03_v5.26
- WAF/rate-limit probing: c03_v5.27, c03_v5.34, c03_v5.35
- cookie/JWT inspection: c03_v5.30, c03_v5.31
- identify unknown software: c03_v5.42, c03_v5.53
- subdomain sourcing and triage: c03_v5.43, c03_v5.45, c03_v5.49
- Location-header filtering: c03_v5.51, c03_v5.52, c03_v5.56


## v6 6. intro.mp4

### c04_v6 00:01-17:46

- c04_v6.01 [00:31] principle: pick a live target you do not know and learn it from zero. why: shows the real process of understanding an unknown app. http: -. frame: -
- c04_v6.02 [01:01] step: check the platform has a public program before poking it. why: stay in authorized scope. http: -. frame: frame_0005 shows the Bugcrowd marketing site, not signed in.
- c04_v6.03 [01:23] signal: read the scope list of targets and wildcards. why: know what you may touch. http: -. frame: -
- c04_v6.04 [01:36] signal: a bare domain without www often implies a wildcard; star.sub is a subdomain wildcard. why: judge how wide the scope is. http: -. frame: -
- c04_v6.05 [01:55] warning: if scope is ambiguous, ask the program rather than assume. why: avoid testing out of bounds. http: -. frame: -
- c04_v6.06 [02:08] signal: most subdomains here are marked out of scope. why: must operate inside the brief. http: -. frame: -
- c04_v6.07 [02:33] principle: companies put things out of scope for many reasons; respect it regardless. why: authorization, not guessing. http: -. frame: -
- c04_v6.08 [02:48] step: choose the main platform site (bugcrowd.com), confirmed in scope, as the target. why: it is the app he actually uses. http: -. frame: -
- c04_v6.09 [03:00] principle: narrate what you see as you see it; assume no prior knowledge. why: that is how the exploration process is learned. http: -. frame: -
- c04_v6.10 [03:02] tool: Burp Suite proxy still scoped to Etsy from last class; needs re-scoping. why: stale scope hides new traffic. http: -. frame: frame_0009 shows Burp with an Intruder/attack view.
- c04_v6.11 [03:10] step: set host/IP range scope to "bugcrowd", uncheck Etsy, keep AWS/Amazon/Microsoft/Azure as generic allows. why: capture only the target's traffic. http: -. frame: -
- c04_v6.12 [03:29] step: re-read the brief for any odd in-scope domains before trusting one keyword. why: do not miss a called-out target. http: -. frame: -
- c04_v6.13 [03:34] signal: the word "bugcrowd" catches both bugcrowd.net and bugcrowd.com; no weird extra domains. why: one scope keyword is enough here. http: -. frame: -
- c04_v6.14 [03:52] tool: toggle the Burp site map filters to force it to refresh/update. why: new builds need the toggle to show traffic. http: -. frame: -
- c04_v6.15 [04:11] warning: after a Burp update, scope changes would not apply while running. why: software updates break things. http: -. frame: frame_0020 is the Bugcrowd landing page in Firefox.
- c04_v6.16 [04:17] step: restart Burp, make a new project "bugcrowd", go to Target > Scope, use advanced scope control, Add, type "bugcrowd". why: get scope to actually take. http: -. frame: -
- c04_v6.17 [04:44] step: back in Firefox, refresh to confirm bugcrowd traffic is now proxied. why: verify the fix before moving on. http: -. frame: -
- c04_v6.18 [04:55] warning: sometimes the blocker is just the tool, not your setup; he lost ~5 min to it. why: do not over-diagnose your own work. http: -. frame: -
skip 00:01-00:31: intro and recap of episode 5, nothing new about the app.
- c04_v6.19 [05:12] technique: refresh the site and scan for third-party domains worth caring about. why: separate real app endpoints from noise. http: -. frame: frame_0032 shows Firefox devtools Network tab with many requests.
- c04_v6.20 [05:22] signal: ignore analytics/ads noise (doubleclick, Google Tag Manager, cookie banners). why: bugs do not live there. http: GET to third-party trackers. frame: -
- c04_v6.21 [05:40] signal: flag unknown API hosts like api.mutinyhq.io(?) as worth a look. why: unfamiliar APIs may hold logic. http: calls to api.mutinyhq.io(?). frame: -
- c04_v6.22 [05:57] principle: to test deeply you need an account; the valuable endpoints are authenticated. why: more features = more attack surface. http: -. frame: -
- c04_v6.23 [06:21] step: use the hacker/researcher login and choose "create an account". why: no account yet. http: -. frame: -
- c04_v6.24 [06:27] step: register with a throwaway identity and a disposable email address. why: keep it a junk test account. http: registration form. frame: -
- c04_v6.25 [06:54] example: the signup password field enforced a rule he had to satisfy. why: shows the app's own constraints. http: registration password field. frame: -
- c04_v6.26 [07:04] step: submit sign up; app sends a confirmation email with a link. why: email verification is part of the auth flow. http: -. frame: -
- c04_v6.27 [07:24] step: open the confirm link on a separate device; clicking it confirmed the account. why: works outside the browser session. http: GET confirm-account link. frame: -
skip 07:52-08:14: fumbling with login error, no app insight.
- c04_v6.28 [08:14] tool: in Burp sort HTTP history by time requested, descending. why: see requests in the order they fired. http: -. frame: frame_0042 shows the Researcher portal login page.
- c04_v6.29 [08:30] signal: the app runs on the non-www host; www just redirects. why: test the real origin. http: requests to www vs non-www bugcrowd.com. frame: -
- c04_v6.30 [08:35] signal: CSP responses are repetitive noise he filters out. why: reduce clutter in history. http: Content-Security-Policy response header. frame: -
- c04_v6.31 [08:44] signal: account creation fired a POST (likely a create-user endpoint) that returns the new user id. why: map which request builds the user. http: POST create user. frame: -
- c04_v6.32 [08:57] example: the password was URL-encoded in the request body; he had mis-cased it and verified fast. why: shows how form values appear on the wire. http: POST body password param, URL-encoded. frame: frame_0044 shows "Invalid username or password" on the login page.
- c04_v6.33 [09:10] principle: when testing, click and exercise every feature, including the registration dialog. why: an untested feature is an unexamined attack surface. http: -. frame: -
- c04_v6.34 [09:10] technique: test the avatar upload by actually uploading a file. why: file upload features carry their own bugs. http: upload request to avatar. frame: -
- c04_v6.35 [09:39] tool: use the browser devtools (F12) Network panel to watch the upload calls live. why: convenient inline view of requests. http: -. frame: -
- c04_v6.36 [10:02] signal: saving the avatar makes a PATCH to an avatar endpoint on the bugcrowd domain; clean, few requests. why: easy to map one action to one request. http: PATCH /avatar. frame: frame_0051 shows the "Upload avatar image" profile dialog.
- c04_v6.37 [10:31] step: fill profile fields (hex color, username) while testing. why: exercise each input. http: profile update requests. frame: -
- c04_v6.38 [10:45] example: he sets the username to "idor12345" as a testing marker. why: easy to spot in responses. http: username field. frame: -
- c04_v6.39 [10:58] step: fill the bio using the markdown feature (bold, preview). why: test the rich-text/markdown input. http: bio field. frame: -
- c04_v6.40 [11:10] step: set profile visibility to public. why: exercise the privacy toggle. http: profile visibility setting. frame: -
- c04_v6.41 [11:24] principle: as a hacker, connecting integrations (GitHub, Stack Overflow) is worth it: more linked features = more calls to test. why: skipping them shrinks attack surface. http: OAuth/connect endpoints. frame: -
- c04_v6.42 [11:50] principle: every button or step you skip is a security problem you may miss, especially in APIs. why: coverage is the point of exploration. http: -. frame: -
- c04_v6.43 [12:03] signal: the onboarding tutorial at /h/welcome has many clickable elements to map. why: more features to examine. http: GET /h/welcome. frame: frame_0076 shows the "Welcome to the Crowd!" onboarding page.
- c04_v6.44 [12:19] technique: check whether a path needs authentication by opening it in a separate unauthenticated browser. why: tests for auth-bypass. http: -. frame: -
- c04_v6.45 [12:33] tool: Burp Proxy > Open browser launches Burp's built-in browser (not logged in). why: a clean unauthenticated session to retest paths. http: -. frame: -
- c04_v6.46 [12:47] example: loading /h/welcome in the unauthenticated browser does require auth. why: confirms the page is gated. http: GET /h/welcome unauthenticated. frame: -
- c04_v6.47 [12:49] principle: auth bypass = a page meant to require auth loads without a token/cookie. why: the generic definition. http: missing auth token/cookie. frame: -
- c04_v6.48 [13:05] principle: it means reaching info that should need auth, usually a forgotten token check on a page or API. why: the mechanism behind the bug. http: -. frame: -
- c04_v6.49 [13:26] report: severity of an auth bypass depends on what the unauthenticated page exposes. why: a generic welcome page = near-zero impact. http: -. frame: -
- c04_v6.50 [13:40] step: switch the account UI to dark mode and review profile/account/support menus. why: keep exploring the authenticated dialog. http: -. frame: frame_0092 shows the IDOR12345 profile overview page.
- c04_v6.51 [14:13] signal: hovering the avatar offers an update; re-uploading may reuse the same call. why: predict which request fires. http: PATCH avatar. frame: -
- c04_v6.52 [14:20] principle: a remove button likely uses a different HTTP method than upload. why: methods map to distinct operations. why: -. http: -. frame: -
- c04_v6.53 [14:32] example: clicking remove made a DELETE request to the avatar endpoint. why: confirms method-per-action. http: DELETE /avatar. frame: frame_0094 shows the authenticated profile with avatar controls.
- c04_v6.54 [14:45] example: re-uploading then made the PATCH request again, as predicted. why: ties each UI action to its request. http: PATCH /avatar. frame: -
- c04_v6.55 [14:59] signal: Burp logs each request in order; sort time-requested shows DELETE, then PATCH, then upload, then the full profile fetch. why: reconstruct the action sequence. http: GET profile. frame: -
- c04_v6.56 [15:27] step: right-click the get-profile request and send to Repeater, then send. why: inspect and replay one request in isolation. http: GET profile to Repeater. frame: -
- c04_v6.57 [15:45] signal: the profile response returns username "idor12345" as JSON. why: confirms what the endpoint exposes. http: JSON response body. frame: -
- c04_v6.58 [15:51] principle: JSON uses curly braces with "key": value pairs; arrays use square brackets. why: baseline for reading responses. http: JSON structure. frame: -
- c04_v6.59 [16:10] signal: an unset JSON value is null; an empty string ("") is blank, not null. why: tell absent from empty. http: null vs "" in response. frame: -
- c04_v6.60 [16:35] signal: the user id is a v4 GUID/UUID (third group starts with 4, 8-4-4-4-12 hex). why: identify the id format. http: UUID in profile response. frame: -
- c04_v6.61 [16:50] offensive: he notes a random UUID id makes IDOR enumeration hard, unlike a guessable username. why: id format drives IDOR feasibility. http: object id parameter. frame: -
- c04_v6.62 [17:00] principle: IDORs are never truly impossible; any identifiable key that links objects can leak via broken access control. why: humans design enumerable references. http: object-reference parameters. frame: -

#### techniques seen
- scope the proxy to the target: c04_v6.10, c04_v6.11, c04_v6.16
- filter noise from real endpoints: c04_v6.19, c04_v6.20, c04_v6.21
- register and verify a junk account: c04_v6.24, c04_v6.26, c04_v6.27
- exercise every feature and watch its request: c04_v6.33, c04_v6.34, c04_v6.42, c04_v6.52
- map UI action to HTTP method: c04_v6.36, c04_v6.53, c04_v6.54, c04_v6.55
- auth-bypass check via unauthenticated browser: c04_v6.44, c04_v6.45, c04_v6.46
- inspect a request in Repeater: c04_v6.56, c04_v6.57

### c05_v6 17:46-35:16

- c05_v6.01 [17:46] signal: the profile fetch is GET to profile-service/v1/profile with no username parameter in the URL. why: no user id in the request means no obvious object to swap. http: GET profile-service/v1/profile. frame: -
- c05_v6.02 [18:15] example: the profile response holds his real first name, last name and signup email. why: leaking a hacker's PII would rate about a P2. http: response body with email field. frame: -
- c05_v6.03 [18:44] principle: a parameter the app ignores today could still be read by the server. why: absence of effect now does not prove the param is unused. http: ?username=test. frame: -
- c05_v6.04 [19:04] signal: only the cookies can be authenticating this API, so the session cookie is the auth mechanism. why: nothing else in the request identifies the user. http: Cookie header. frame: -
- c05_v6.05 [19:18] offensive: he notes a hidden ?filter= type param might override the cookie identity. why: devs often let a param stand in for the session user. http: ?filter=. frame: -
- c05_v6.06 [19:47] technique: for access-control testing, send every parameter you found anywhere at the endpoint with value 1 and watch for a different response. why: a changed response means the param is handled, worth investigating. http: appended params =1. frame: -
- c05_v6.07 [20:15] step: delete the _bugcrowd_session cookie and resend to confirm it is the auth token. why: 401 back proves it authenticates. http: removed session cookie, 401 Unauthorized. frame: -
- c05_v6.08 [20:43] technique: strip cookies one by one (Mutiny, Google trackers, crowdcontrol session key, CSRF) and resend to see which matter. why: isolates the single cookie that holds auth. http: Cookie header, each removed in turn. frame: -
- c05_v6.09 [21:11] signal: after stripping, only _bugcrowd_session remains and still authenticates. why: narrows auth to one cookie. http: Cookie: _bugcrowd_session. frame: -
- c05_v6.10 [21:37] signal: the _bugcrowd_session cookie value is a JWT. why: he will pull it apart as the auth lesson. http: cookie value. frame: -
- c05_v6.11 [22:03] principle: know JWTs inside out; auth/authz is today's core. why: foundational for the testing that follows. http: -. frame: -
- c05_v6.12 [22:26] signal: an Authorization header, often with Bearer prefix, is the common OAuth/JWT style. why: recognise where tokens live. http: Authorization: Bearer <token>. frame: -
- c05_v6.13 [22:36] signal: a token starting EY/EYJ with two periods is a JWT in three sections. why: the dead giveaway for spotting one. http: eyJ...header.payload.signature. frame: -
- c05_v6.14 [22:58] tool: JWT.io, a client-side-only viewer, breaks a token into header, payload, signature. why: clearer than reading it raw, though Burp can too. http: -. frame: 0105 jwt.io decoder, three decoded panels
- c05_v6.15 [23:28] principle: the middle section (payload) carries who you are: role, issuer, expiry, issued-at, member id. why: it is everything the server needs about your access. http: JWT payload claims. frame: -
- c05_v6.16 [23:42] example: this token's payload has issuer identity.bugcrowd.com, an iat time, and a server session id. why: shows real claim contents. http: iss, iat, sessionId claims. frame: 0105 payload shows iss https://identity.bugcrowd.com, sessionId guid
- c05_v6.17 [24:09] signal: the server likely maps the session id back to his user record on its side. why: reasons about how auth resolves identity. http: sessionId claim. frame: -
- c05_v6.18 [24:36] step: he checks the session id is not actually the user id by comparing values. why: curiosity about naming vs reality; they differ. http: sessionId vs user GUID. frame: 0102 Burp Inspector decoding selected JWT text
- c05_v6.19 [24:36] signal: the header field shows how the JWT is signed (RS256, HS256, etc). why: signing type drives the attack. http: JWT header alg. frame: 0105 header alg RS256, kid cookie-signing-key-1
- c05_v6.20 [25:05] principle: HS algorithms sign with a secret like a password; RS uses a private certificate/key. why: getting the HS secret or RS private key lets you forge tokens. http: alg HS256/RS256. frame: -
- c05_v6.21 [25:32] offensive: with the signing key you could set role=admin and sign as the server to take over. why: shows the payoff of a leaked key. http: forged payload role claim. frame: -
- c05_v6.22 [25:57] principle: JWT contents are plain sight; anyone with the token sees everything in it. why: the token is readable, not secret. http: base64 payload. frame: -
- c05_v6.23 [26:09] warning: you can see a role claim and want to flip it to admin, but the server rejects an edit unless the signature is unchecked. why: it teases you because viewing is not forging. http: role claim. frame: 0107 Burp Repeater, response body selected
- c05_v6.24 [26:34] tool: the Burp JSON Web Tokens extension from the BApp store; now even scans cookies for JWTs. why: he runs very few add-ons but keeps this one. http: -. frame: 0102 JSON Web Tokens tab in Burp
- c05_v6.25 [26:58] signal: the extension digested the cookie JWT, showing alg RS256 and the claim set. why: confirms the token data in Burp. http: decoded JWT in extension. frame: -
- c05_v6.26 [27:18] offensive: test if the signature is validated at all by deleting a couple of characters off the signature and resending. why: if content still returns, the signature is not checked. http: truncated JWT signature. frame: -
- c05_v6.27 [27:45] warning: a dev who skips signature validation usually did it on many or all APIs, a catastrophic miss. why: one finding often scales across the app. http: -. frame: -
- c05_v6.28 [28:16] offensive: set the alg to none, trying the case variants (none, None, nOnE), since the check may be case-sensitive. why: a blocked set of variants means it is probably validated. http: JWT header alg=none variants. frame: -
- c05_v6.29 [28:42] signal: an alg=none token has only two sections, the signature group gone. why: no signature needed when none is accepted. http: header.payload. with empty signature. frame: -
- c05_v6.30 [29:03] principle: the two first JWT checks are no-signature-validation and alg=none. why: fast, high-impact tests when auth is a JWT. http: -. frame: -
- c05_v6.31 [29:31] principle: authentication is being logged in; authorization is being allowed to hit this endpoint and its data. why: separates the two ideas he hunts. http: 401 vs 403. frame: -
- c05_v6.32 [29:59] example: a hypothetical /admin endpoint taking ?username=test could return any profile if you were admin, else 403. why: illustrates privilege boundary. http: GET /admin ?username=test, 403. frame: -
- c05_v6.33 [30:30] principle: broken access control in his hunting is mostly privilege escalation, reaching an admin-designed endpoint as a non-admin. why: frames what he looks for. http: -. frame: -
- c05_v6.34 [30:55] example: the bank-teller story: handing out $20,000 with no ID check is missing authentication. why: makes authn tangible. http: -. frame: -
- c05_v6.35 [31:29] example: a teller who checks ID but not account ownership is the broken-authorization case. why: authn passed, authz failed on account 54321 vs 12345. why relates to IDOR. http: -. frame: -
- c05_v6.36 [31:57] principle: his whole method is bypass authn+authz, or authenticate then reach data meant for another user. why: sums up his approach. http: -. frame: -
- c05_v6.37 [32:19] principle: an Authorization header inherently mitigates CSRF because browsers do not auto-send it, unlike cookies. why: header-based auth is safer by design. http: Authorization header vs Cookie. frame: -
- c05_v6.38 [32:47] signal: a Basic header carries username:colon:password base64 encoded, an old auth method. why: recognise legacy auth. http: Authorization: Basic base64(user:pass). frame: -
- c05_v6.39 [33:15] warning: Basic creds usually do not expire, so if intercepted, logged, or in a JS file, the real password leaks. why: high impact and persistent. http: Authorization: Basic. frame: -
- c05_v6.40 [33:36] example: he has found Basic creds sitting in JavaScript files at big Fortune 50 companies. why: real leaked-credential cases. http: JS file strings. frame: -
- c05_v6.41 [33:54] technique: grep JS for btoa/atob near the word "basic" or "authorization" as indicators of leaked or encoded credentials. why: builds targeted searches for creds. http: btoa/atob, basic. frame: -
- c05_v6.42 [34:23] signal: sometimes the authorization value is just a bare GUID cookie, one abstraction layer less than a JWT. why: still your whole auth mechanism. http: Authorization cookie = GUID. frame: -
- c05_v6.43 [34:47] principle: whether a GUID session id or a full JWT, anyone who steals the cookie is logged in as you. why: both reduce to possession of the token. http: session cookie / JWT. frame: 0109 jwt.io showing the session id claim

#### techniques seen
- cookie strip to find the auth token: c05_v6.07, c05_v6.08, c05_v6.09
- send every found param =1: c05_v6.06
- JWT signature and alg=none tests: c05_v6.26, c05_v6.28, c05_v6.30
- authn vs authz reasoning: c05_v6.31, c05_v6.33, c05_v6.36
- grep JS for encoded creds: c05_v6.41

### c06_v6 35:16-52:47

- c06_v6.01 [35:40] signal: no numeric object id on the delete-avatar action. why: the app does a server-side lookup from the session, a sign of correct access control. http: DELETE /profile-service/v1/profile/images/avatar, no id param. frame: -
- c06_v6.02 [36:05] principle: when a user can own only one object, the server can resolve it from the session alone, so no object id is needed. why: this blocks broken access control. http: -. frame: -
- c06_v6.03 [36:35] offensive: he tests a numeric object id (delete to 12345) by changing it for broken access control. why: an id you can edit may let you act on another user's object. http: delete request with a guessable numeric id. frame: -
- c06_v6.04 [36:57] warning: do not needlessly delete a real user's object. why: it is malicious. use two of your own accounts to prove the IDOR instead. http: -. frame: -
- c06_v6.05 [37:24] signal: the uploaded avatar file name gets appended into the stored file path. why: a name read server-side can be a vector. http: PATCH /profile-service/v1/profile/images/avatar, file name in path. frame: proxy history shows PATCH avatar.
- c06_v6.06 [37:52] offensive: he notes file upload as an RCE vector, tested by changing content type of a server-executed file when the upload path is known. why: the response gave the exact upload path. http: response returns the full upload URL.
- c06_v6.07 [38:20] signal: a new host, crowdicons.bugcrowdusercontent.com, surfaced from the upload. why: in-scope hosts get picked up because the brief uses the word bugcrowd. http: upload URL on that host. frame: cue 35:50 shows the usercontent host.
- c06_v6.08 [38:31] technique: trim the file off the upload URL and request the directory to check for open directory listing or an open bucket. why: a quick win if the bucket is public. http: GET on the parent path. frame: -
- c06_v6.09 [38:34] step: walk back one more path segment and retry, as a quick extra check. why: sometimes the whole bucket is open. http: GET on the grandparent path. frame: -
- c06_v6.10 [38:56] signal: a performanceStatistics request carries a username/user object. why: an endpoint tied to a user is a broken-access-control candidate; he sends it to Repeater. http: GET /profile-service/v1/profiles/<user>/performanceStatistics. frame: cue 39:40 shows this in Repeater.
- c06_v6.11 [39:26] principle: for broken access control, do not start by changing the id; first learn if the endpoint even needs auth. why: changing ids blindly is pointless. http: -. frame: -
- c06_v6.12 [39:26] step: delete the cookies and resend to see if the response changes. why: tells you whether the endpoint is authenticated. http: same GET with cookies removed, got nothing back (3226 bytes vs empty). frame: -
- c06_v6.13 [39:55] signal: the API takes a plain user id, not the GUID. why: humans build the easy path, so user ids are enumerable; "tess" is a user id. http: user id in the profiles path. frame: -
- c06_v6.14 [40:24] offensive: he requests another user (tess) profile data to test access. why: to see if non-public data returns. http: GET profiles/tess/performanceStatistics returns data. frame: cue 39:40 shows the JSON body.
- c06_v6.15 [40:24] warning: treat returned data as maybe-public; do not log or exploit, assume it was meant to be public until proven otherwise. why: ethics and avoiding false bugs. http: -. frame: -
- c06_v6.16 [40:56] technique: ask "where did this come from?" for any API call name. why: the answer leads to more endpoints; this is how he finds a lot. http: -. frame: -
- c06_v6.17 [41:26] tool: Burp search, scoped to Response body only. why: an API call name must have come back in a loaded response body. http: searched string "performanceStatistics". frame: cue 41:45 shows search with Response body ticked.
- c06_v6.18 [41:53] signal: the search hit a 1.5 MB Bugcrowd JavaScript file loaded in the background. why: big JS bundles hold API endpoints. http: GET /h/assets/index-*.js. frame: cue 43:20 shows the match in index-DPZJv_p6.js.
- c06_v6.19 [42:58] technique: search the JS file for the API path prefix to find sibling endpoints. why: endpoints at the same path are new targets. http: searched /profile-service/v1/profiles/, 10 matches. frame: cue 43:20 shows profiles path matches.
- c06_v6.20 [42:58] example: siblings found: badgeAttainments, connectedApplicationWidgets, Hall of Fame, performanceStatistics. why: candidate endpoints to test, some maybe not meant public. http: GET on those paths. frame: proxy history shows badgeAttainments.
- c06_v6.21 [43:27] step: request connectedApplicationWidgets to see what it returns. why: it sounded interesting; returned empty, no 401/403. http: GET profiles/<user>/connectedApplicationWidgets. frame: -
- c06_v6.22 [44:25] principle: a JS file lists some endpoints, not all; others hide in other JS files, Git, GitHub/GitLab. why: enumeration is never complete from one source. http: -. frame: -
- c06_v6.23 [44:52] signal: the API path is case sensitive; lowercase first letter returns no content. why: you must match casing when enumerating or you miss endpoints. http: performanceStatistics vs performancestatistics. frame: -
- c06_v6.24 [45:00] step: test how path characters behave: trailing slash still works, # ignored, ? ignored. why: to know what the router tolerates. http: path with /, #, ? appended. frame: -
- c06_v6.25 [45:00] signal: %2f is read as a literal string and a URL-encoded ? (%3F) is rejected. why: encoded path tricks will not work here. http: %2f and %3F in path. frame: -
- c06_v6.26 [45:21] tool: Burp Repeater URL-encode shortcut; he wants a hotkey for "URL encode all characters". why: speeds up encoding tests. http: -. frame: -
- c06_v6.27 [45:50] step: strip performanceStatistics and request just tess's profile. why: to compare with the public profile for leaked fields. http: GET profiles/tess. frame: cue 45:00 shows tess path 404.
- c06_v6.28 [45:50] signal: no email or name came back, so likely not a bug. why: leaked email/first/last name would mean a real access-control issue. http: profile response fields. frame: -
- c06_v6.29 [46:10] technique: copy the whole JS file into Notepad++ to bulk-extract every API path. why: a clean list feeds bulk testing. http: -. frame: frame 46:24 shows the JS in Notepad++.
- c06_v6.30 [46:39] step: find-and-replace the path-prefix token with \r\n in extended mode to put each path on its own line. why: splits paths out; 25 replacements. http: -. frame: -
- c06_v6.31 [47:32] step: use triple-pipe markers plus sort lexicographically ascending to group and isolate the path lines. why: makes the endpoints easy to find. http: -. frame: -
- c06_v6.32 [48:32] step: copy the pipe block to a new file, split on method, sort again, then strip the pipes to leave a clean endpoint list. why: ready for Intruder bulk access-control testing. http: -. frame: -
- c06_v6.33 [48:32] tool: Burp Intruder for bulk access-control testing across many endpoints at once. why: "see what wiggles" from a clean list. http: -. frame: -
- c06_v6.34 [49:18] signal: the endpoint seems to need auth cookies yet also behaves public. why: needs research on whether tess's profile leaks anything the public profile does not. http: -. frame: -
- c06_v6.35 [49:48] step: reopen an unauthenticated proxy browser and hit tess's endpoint to see what returns with no session. why: isolates what auth actually gates. http: GET profiles/tess unauthenticated. frame: -
- c06_v6.36 [49:48] signal: the path is profiles (plural) tess, the same endpoint as his own profile. why: confirms it is one shared endpoint, not a separate public one. http: /profile-service/v1/profiles/tess. frame: cue 45:00.
- c06_v6.37 [50:15] signal: removing cookies broke it because the endpoint needs the CSRF token, not only the session. why: explains the earlier empty response. http: CSRF token required. frame: -
- c06_v6.38 [50:47] warning: a confusing failed/passed result traced to his own profile not having propagated yet, not a real finding. why: testing noise; verify before claiming a bug. http: -. frame: -
- c06_v6.39 [51:15] principle: it always comes down to some object; not everything is a bug, but this is the method by which you would find one. why: method matters more than the find. http: user id as the object. frame: cue 39:40.
- c06_v6.40 [52:05] tool: GAP Burp extension, right-click host, Extensions, GAP, to auto-extract URLs and endpoints from JS. why: automates the manual path extraction. http: -. frame: -
- c06_v6.41 [52:24] warning: do not assume GAP always works; some formats (e.g. T-Mobile's API structure) make it fail to pull paths. why: keep the manual method as a fallback. http: -. frame: -

#### techniques seen
- trace an API call name back to its source JS: c06_v6.16, c06_v6.17, c06_v6.18
- find sibling endpoints from a JS path prefix: c06_v6.19, c06_v6.20
- bulk-extract API paths with Notepad++: c06_v6.29, c06_v6.30, c06_v6.31, c06_v6.32
- auth/need check before id tampering: c06_v6.11, c06_v6.12
- directory/bucket walk-back on upload URLs: c06_v6.08, c06_v6.09


## v7 7. basic exploration.mp4

### c07_v7 00:01-25:15

- c07_v7.01 [00:30] principle: to test an app, first gain an authenticated session. why: an authenticated area exposes more features to explore. http: -. frame: -
- c07_v7.02 [00:58] principle: paying for a subscription or product to reach an authenticated area is often worth it. why: most hackers will not, so the access is less tested. http: -. frame: -
- c07_v7.03 [01:19] aside: he resumes from a prior session on Bugcrowd and tidies the screen. why: get back into context. http: -. frame: -
- c07_v7.04 [01:49] example: revisits a request he decided is likely not a security issue but good for API/BAC discussion. why: teaching value. http: the earlier request under review. frame: -
- c07_v7.05 [02:13] step: opens the target's submit-test-report flow to log a practice bug. why: logging a report reveals more app features too. http: -. frame: f0002 shows Burp live audit task, issues from bugcrowd.com, scope Proxy all traffic
- c07_v7.06 [02:42] tool: enables two-factor with an OTP to pass the report gate. why: platform required 2FA before submitting. http: -. frame: -
- c07_v7.07 [03:08] example: frames the chosen request as a hypothetical IDOR by user ID returning PII. why: model the reporting steps. http: a Repeater request to the user endpoint. frame: -
- c07_v7.08 [03:38] signal: no auth token needed on the request, so he reclasses it as an auth bypass. why: unauthenticated access to PII is higher severity. http: request with no auth token, returns PII by username. frame: -
- c07_v7.09 [04:05] principle: fully unauthenticated APIs returning sensitive data by object are common in the wild. why: set expectations. http: -. frame: -
- c07_v7.10 [04:34] report: make the title attention-getting and as severe-sounding as honest. why: severity is a subjective negotiation. http: -. frame: -
- c07_v7.11 [05:29] report: drafts title "unauthenticated internet-facing bulk PII dump by user ID". why: words like bulk, dump, internet-facing raise perceived impact. http: -. frame: f0013 report form, title field, VRT Auth Bypass, URL field
- c07_v7.12 [06:23] report: sets target bugcrowd.com and VRT to auth bypass, which auto-sets P1 triage. why: correct taxonomy drives severity. http: -. frame: f0013 shows VRT Broken Auth and Session Management > Authentication Bypass
- c07_v7.13 [06:51] signal: the injectable point is the last API stem (a username like "Smith"). why: that identifier is the object being swapped. http: GET .../profile-service/v1/profiles/task... with username at the path tail. frame: f0012 Repeater, /profile-service/v1/profiles/task/badgeAttainments
- c07_v7.14 [07:14] technique: swap the trailing identifier value to fetch another user's record. why: confirms the reference is unprotected. http: changes path tail from one username to another. frame: -
- c07_v7.15 [07:41] principle: each API stem with its own BAC flaw can be its own bug, or a duplicate of one root cause. why: depends on program scope policy. http: -. frame: -
- c07_v7.16 [08:22] offensive: he notes testing a different HTTP method on the same endpoint. why: a method-level BAC bypass is its own issue. http: GET vs POST/PUT on one endpoint. frame: -
- c07_v7.17 [08:48] example: MGM-era bypasses via adding a slash, changing the method, or a query filter. why: small mutations defeat access constraints. http: trailing slash, method change, ?filter=. frame: -
- c07_v7.18 [09:17] principle: once a target marks an issue resolved, any bypass of that fix is fair game. why: bypass of a fixed issue is a fresh bug. http: slash, method, parameter, case variants. frame: -
- c07_v7.19 [09:46] report: he deletes Bugcrowd's issue template and uses his own format. why: a fixed, repeated format over 2000 bugs. http: -. frame: -
- c07_v7.20 [10:15] report: starts with a summary a manager grasps in two sentences. why: readers skim for severity. http: -. frame: -
- c07_v7.21 [11:13] report: log the minimum needed to convey the issue. why: long reports waste time if marked duplicate. http: -. frame: -
- c07_v7.22 [11:42] report: add an impact line and numbered replication steps. why: clarity without superfluous detail. http: -. frame: -
- c07_v7.23 [12:04] principle: the easier a bug is to replicate, the higher its real impact. why: show it works right in the browser. http: paste the URL into a browser address bar. frame: f0008 Proxy history, bugcrowd.com GETs to /profile-service and /idp endpoints
- c07_v7.24 [12:32] step: replication step two is "loop over user IDs where it says Smith". why: demonstrate enumeration simply. http: iterate the username path value. frame: -
- c07_v7.25 [13:00] tool: highlights the username, sends to Burp Intruder, loads a usernames wordlist, caps at ~10. why: just enough for a proof screenshot. http: single payload position on the username. frame: f0026 Intruder, loading username_10000.txt wordlist
- c07_v7.26 [13:26] step: screenshots the bulk 200 responses as proof; redact real PII. why: a picture conveys impact. http: multiple 200 responses across usernames. frame: f0024 Intruder results, status 200, varying lengths per username
- c07_v7.27 [13:49] warning: large fast runs get you instantly blocked. why: he got rate-blocked mid-demo. http: many rapid requests trigger a block. frame: -
- c07_v7.28 [14:15] report: optional remediation line: require an auth token and verify that user may access the requested data. why: shows the missing object-level check. http: -. frame: -
- c07_v7.29 [14:43] step: submits the practice report. why: completes the reporting walk-through. http: -. frame: f0013 report form with summary, impact, steps filled
- c07_v7.30 [15:13] aside: plans future episodes on report philosophy and the mindset of bug bounty. why: you lose control once an issue is logged. http: -. frame: -
- c07_v7.31 [16:11] tool: in Burp he hides noise like SVGs and CSP responses. why: keep only data useful to his style. http: filters out image and CSP responses. frame: -
- c07_v7.32 [16:33] signal: GUIDs appearing on the page cue him toward BAC testing. why: object references are where IDOR lives. http: GUID identifiers in responses. frame: -
- c07_v7.33 [17:00] technique: browses submissions and endpoints to pick a good teaching target. why: find a clean object to demonstrate on. http: engagement and submission endpoints. frame: f0027 editor listing API paths: /engagement-service and /profile-service stems
- c07_v7.34 [17:27] principle: focus on the things that matter, ignore the things that do not. why: efficient app exploration. http: -. frame: -
- c07_v7.35 [17:52] signal: notes separate "id" and "engagementId" fields on one endpoint. why: multiple identifiers mean multiple objects to test. http: engagement endpoint with id and engagementId. frame: f0027 .../engagements/${e} and nested stems
- c07_v7.36 [18:22] principle: GUIDs are where many IDORs go to die. why: random v4 GUIDs resist enumeration. http: 32-char GUID, 8-4-4-4-12. frame: -
- c07_v7.37 [18:52] signal: a GUID whose third group does not start with 4 may be v1/v2 and predictable. why: older GUIDs embed timestamp and MAC, so can be reverse-engineered. http: GUID used as an auth token. frame: -
- c07_v7.38 [19:22] step: switches from the changelog endpoint to /api/v1/users/me to teach IDOR. why: a cleaner, common object endpoint. http: GET /api/v1/users/me (?). frame: -
- c07_v7.39 [19:51] principle: an IDOR object is anything used to look up or identify a record. why: name, username, id, image, email, phone can all be objects. http: fields in the user response. frame: -
- c07_v7.40 [20:16] example: lists the response fields that qualify as objects. why: each is a candidate reference to swap. http: first name, last name, username, UUID, image, email, phone. frame: f0027 confirms per-profile stems like images, badgeAttainments
- c07_v7.41 [20:44] principle: a legacy auto-increment primary key (1,2,3...) makes IDORs trivial. why: sequential IDs are guessable. http: /users/1, ?userId=1 style references. frame: -
- c07_v7.42 [21:55] signal: APIs that reference everything by a numeric id signal pervasive IDOR risk. why: the id maps straight to a backend row. http: path or query id used everywhere. frame: -
- c07_v7.43 [22:25] principle: the URL id is parsed and passed into a backend query parameter. why: understand how the object reaches the data layer. http: /api/v1/auth/users/1 maps to a WHERE id = 1 lookup. frame: -
- c07_v7.44 [23:23] principle: BAC is born when code checks only "is authenticated", not "may this user access this record". why: auth is not authorization. http: -. frame: -
- c07_v7.45 [23:53] principle: correct code also checks "does user have access to requested record" before the query. why: object-level authorization. http: -. frame: -
- c07_v7.46 [24:19] principle: proper checks need roles and extra lookups, so devs often skip them. why: cost explains why BAC is common. http: -. frame: -
- c07_v7.47 [24:47] technique: when testing, first check whether the app even has a concept of roles. why: roles (user vs admin, RBAC) shape the access model. http: look for role indicators in responses. frame: -

skip 25:00-25:15: slice edge, mid-sentence on roles, no complete new idea

#### techniques seen
- gain authenticated access first: c07_v7.01, c07_v7.02
- report writing for severity: c07_v7.05, c07_v7.10, c07_v7.11, c07_v7.12, c07_v7.19, c07_v7.20, c07_v7.21, c07_v7.22, c07_v7.28, c07_v7.29
- identifier swap / IDOR: c07_v7.13, c07_v7.14, c07_v7.38, c07_v7.39, c07_v7.40, c07_v7.41
- bypass mutations (slash/method/param): c07_v7.16, c07_v7.17, c07_v7.18
- enumerate with Intruder: c07_v7.25, c07_v7.26
- GUID analysis: c07_v7.36, c07_v7.37
- find things that matter / signals: c07_v7.31, c07_v7.32, c07_v7.33, c07_v7.35, c07_v7.42
- map auth vs authorization: c07_v7.43, c07_v7.44, c07_v7.45, c07_v7.47

### c08_v7 25:15-50:00

- c08_v7.01 [25:15] principle: a JWT can carry custom app roles (dashboard, run reports, query users) that gate access. why: shows where access decisions live. http: Authorization JWT, decoded role claims. frame: -
- c08_v7.02 [25:41] principle: server access flow is authenticated? then has-role? then load data. why: map the order of checks to find the gap. http: - . frame: -
- c08_v7.03 [26:12] principle: broken access control is the whole idea; the gate is often too easy. why: sets the lens for the slice. http: - . frame: -
- c08_v7.04 [26:34] principle: GUIDs get bolted on late via a lookup table or an added user column. why: legacy retrofits leave BAC gaps. http: user GUID field. frame: -
- c08_v7.05 [27:03] example: an API upgrade pastes a GUID into the query, where user_guid = A. why: shows how object refs enter the request. http: GUID request parameter. frame: -
- c08_v7.06 [27:32] principle: a lazy extra branch, if filter present then query by filter else by GUID. why: a late parameter changes behavior. http: filter parameter. frame: -
- c08_v7.07 [28:01] technique: test whether behavior changes when a parameter is present. why: a late check can override the working security logic. http: added request parameter. frame: -
- c08_v7.08 [28:31] principle: server-side order of operations matters; a filter added outside the if-blocks can bypass checks. why: tells where to probe. http: - . frame: -
- c08_v7.09 [29:00] technique: tinker with the path, e.g. trailing slashes, to change which conditions apply. why: path-specific rules can be shifted. http: URI path, trailing slash. frame: screen shows API endpoint list
- c08_v7.10 [29:52] signal: a /me endpoint implies a /<something-else> exists. why: naming hints at sibling object endpoints. http: /api/v1/users/me. frame: -
- c08_v7.11 [30:21] technique: swap the GUID into the /me slot to test for IDOR. why: see if another user's object loads. http: GET /me replaced with GUID, got 302. frame: -
- c08_v7.12 [30:49] step: parse the user object fields from the response (id, email, first, last). why: those become parameters to test. http: user object JSON fields. frame: -
- c08_v7.13 [31:19] tool: Notepad++ find-and-replace to insert \r\n and split the response fast. why: quick way to strip JSON into a field list. http: - . frame: frame_0032 shows JSON with firstName, lastName, username IDOR12345, theme Dark
- c08_v7.14 [31:41] step: sort lines lexographically to clean out junk and keep parameter names. why: builds a tidy param list by hand. http: - . frame: frame_0036 shows sorted fields id, email, firstName, username, avatar
- c08_v7.15 [32:11] technique: send ?param=1 to Intruder and try each response field as a request parameter. why: see if any is read server side. http: ?param=1 query parameter. frame: -
- c08_v7.16 [32:11] tool: Burp Intruder with a resource pool of one. why: controlled, slow blast. http: - . frame: frame_0029 Intruder results, payloads smith/williams/lee, status 200
- c08_v7.17 [32:39] signal: identical response length (1623) means no parameter had impact. why: length is the fast tell for change. http: Response length column. frame: frame_0029 shows Length column
- c08_v7.18 [33:05] technique: keep a running wordlist of params to try, e.g. filter, isAdmin. why: reuse across future bounty targets. http: filter, isAdmin parameters. frame: -
- c08_v7.19 [33:31] signal: use response length or status code to decide if an attempt worked. why: easy pass/fail signal. http: status code, length. frame: -
- c08_v7.20 [33:58] principle: most things in hacking fail; creativity and effort are the only limits. why: mindset for the work. http: - . frame: -
- c08_v7.21 [34:27] technique: guess sibling paths, try /api/v1/users directly. why: discover endpoints beyond /me. http: GET /api/v1/users. frame: -
- c08_v7.22 [34:27] step: search the JS file for the path and find auth routes (getAuthenticatedUser, isAuthenticated). why: source of real endpoints. http: /auth routes in JS. frame: -
- c08_v7.23 [34:56] step: search the JS for /auth and /api strings. why: surface more routes. http: authenticate, re-authenticate, SSO. frame: -
- c08_v7.24 [35:23] signal: a 1.5 MB JS file hides endpoints like device fingerprint, all services. why: big bundles leak structure. http: JS URI strings. frame: -
- c08_v7.25 [35:50] technique: read and scroll the JavaScript for URIs, stems, odd call patterns. why: most is noise; the URIs are the prize. http: - . frame: -
- c08_v7.26 [36:17] technique: look for an open Swagger/API docs endpoint by fuzzing API paths. why: may dump the full structure. http: Swagger/API docs path. frame: -
- c08_v7.27 [36:46] tool: Gap (GAP) Burp extension scans every hit JS file and dumps perceived URIs. why: fast endpoint overview. http: /api/v1/users/me found. frame: frame_0044 GAP mode panel, params and links found
- c08_v7.28 [37:11] signal: Gap output flags a hackne user search endpoint that stands out. why: user search is a high-interest function. http: user search endpoint. frame: frame_0040 scope page, Bugcrowd primary targets
- c08_v7.29 [37:38] principle: context on the target explains odd functions; collaborator tagging needs a user list. why: domain knowledge guides testing. http: - . frame: -
- c08_v7.30 [38:34] example: the user search is reachable, search by username returns real users. why: confirms the function. http: username=test query. frame: -
- c08_v7.31 [38:56] principle: a function that looks admin may be intended; know the app before calling it a bug. why: avoid false positives. http: username=test. frame: -
- c08_v7.32 [39:27] signal: the search response carries many headers and a huge CSP. why: notes the response shape. http: Content-Security-Policy header. frame: -
- c08_v7.33 [39:27] principle: knowing the app has private vs non-private profiles tells you privacy is a thing to attack. why: unknown features cannot be tested. http: private profile setting. frame: -
- c08_v7.34 [40:25] offensive: he tests the username parameter for SSRF and injection. why: any param taking an object is a BAC/SSRF lead. http: username parameter. frame: frame_0040 scope page
- c08_v7.35 [40:25] offensive: he tests username for SQL injection by sending a single quote to see if it errors. why: cheap check for input handling. http: username=' . frame: -
- c08_v7.36 [40:55] offensive: he tests the parameter for path traversal, gets nothing. why: blind result is not proof it is safe. http: username traversal payload. frame: -
- c08_v7.37 [40:55] principle: a blank response does not mean nothing happened; blind issues cost time, deprioritize. why: ROI on testing. http: - . frame: -
- c08_v7.38 [41:27] principle: visit each URI found in files and judge, in app context, whether it would be a bug. why: the core exploration loop. http: discovered URIs. frame: -
- c08_v7.39 [41:57] technique: reason about which profile fields should be private (resume, connected apps, friends). why: targets the privacy attack surface. http: profile service fields. frame: -
- c08_v7.40 [42:26] step: find the friends feature, add a friend by username to trigger API calls. why: generate the requests worth inspecting. http: username=test. frame: frame_0053 GET username request in Repeater
- c08_v7.41 [43:25] signal: add-friend is a POST to profile-service/v1/profile/friends, keyed by auth token. why: shows how the object is referenced. http: POST profile-service/v1/profile/friends. frame: -
- c08_v7.42 [43:25] offensive: he asks whether you can add a friend marked private. why: a BAC test on the friends flow. http: POST friends, username param. frame: -
- c08_v7.43 [43:55] step: unfriend to see the request object; it is just the username. why: map the request body. http: unfriend request, username field. frame: -
- c08_v7.44 [44:24] signal: friends are added by auth token, not by a profile id in the path. why: token-keying blocks IDOR here. http: auth token vs profile id in path. frame: -
- c08_v7.45 [44:24] principle: IDOR would appear if the path held another user ref (profile/test/friends) to delete their friend. why: shows the vulnerable shape. http: hypothetical profile/<user>/friends path. frame: -
- c08_v7.46 [44:53] principle: this app does session control well, so BAC is less likely; that is not the norm in the wild. why: calibrate expectations. http: - . frame: -
- c08_v7.47 [45:22] aside: plan to pivot to a target with weaker access control (Etsy, T-Mobile). why: better ROI for BAC practice. http: - . frame: frame_0057 Burp GAP username wordlist file picker
- c08_v7.48 [46:14] principle: only hunt BAC here; find where object refs pop out, URI paths, params, POST bodies. why: focus the search. http: object parameters in bodies. frame: -
- c08_v7.49 [46:42] principle: skip targets that do session management right; it is a big internet. why: ROI on target choice. http: JWT session, GUIDs. frame: -
- c08_v7.50 [47:36] principle: pick targets with many object identifiers, large scope, more CRUD to test. why: more surface, more bugs. http: object ids in API calls. frame: -
- c08_v7.51 [47:59] principle: old legacy companies are best; technical debt built on ID values. why: legacy IDs are iterable. http: integer/phone/SSN ids. frame: -
- c08_v7.52 [48:44] example: phone numbers and SSNs are easy ids to iterate for BAC. why: concrete object-of-interest cases. http: numeric ids. frame: -
- c08_v7.53 [49:09] aside: only looked at a couple of many Bugcrowd subdomains and three of many functions. why: scope caveat on the verdict. http: - . frame: -
- c08_v7.54 [49:39] aside: next episode demos T-Mobile JS methodology, then Etsy (IDORs out of scope). why: roadmap. http: - . frame: -
- c08_v7.55 [50:00] warning: stay in scope, follow the brief and the law. why: authorized testing only. http: - . frame: -

#### techniques seen
- parameter-presence testing: c08_v7.07, c08_v7.15, c08_v7.18
- path and endpoint guessing: c08_v7.09, c08_v7.10, c08_v7.21
- object ref / IDOR swap: c08_v7.11, c08_v7.42, c08_v7.45
- JS mining for endpoints: c08_v7.22, c08_v7.25, c08_v7.26, c08_v7.27
- response-field extraction: c08_v7.12, c08_v7.13, c08_v7.14
- context-driven function review: c08_v7.29, c08_v7.38, c08_v7.39
- change-signal reading (length/status): c08_v7.17, c08_v7.19
- target selection for BAC: c08_v7.47, c08_v7.49, c08_v7.50, c08_v7.51


## v8 8. exploration.mp4

### c09_v8 00:02-23:13

- c09_v8.01 [00:20] principle: recon stages chain together: IP/DNS, then wildcard subdomains, then archive URLs, then dorking. why: each stage feeds the next with targets. http: -. frame: -
- c09_v8.02 [00:50] tool: Bugcrowd public programs. why: find big, well-funded targets worth time. http: -. frame: -
- c09_v8.03 [01:10] example: picks T-Mobile, a program he is top-ranked on. why: company he knows well, deep prior experience. http: -. frame: -
- c09_v8.04 [01:37] warning: his IP got blocked mid-demo. why: this target blocks easily, watch request volume. http: -. frame: frame_0004 shows blank Bugcrowd page not loading
- c09_v8.05 [01:50] principle: pick targets by signals: known brand, money, past breaches, wide scope. why: motivated, high-payout, lots of surface. http: -. frame: -
- c09_v8.06 [02:29] principle: targets that "use a lot of numbers" attract him. why: numeric IDs hint at broken access control. http: -. frame: -
- c09_v8.07 [03:23] example: wildcard scope means anything at tfb.t-mobile.com is in scope. why: no asterisk needed, broad surface. http: host tfb.t-mobile.com. frame: -
- c09_v8.08 [03:46] technique: open every in-scope site in the browser to see what it is. why: direct look tells you the app's purpose. http: -. frame: -
- c09_v8.09 [03:46] principle: go where fewer people look, not the popular asset. why: less competition on a crowded program. http: -. frame: -
- c09_v8.10 [04:18] signal: tfb.t-mobile.com redirects to a login panel. why: login-gated app, likely a web service needing an account. http: redirect to login URL. frame: frame_0010 shows T-Mobile email/phone login form
- c09_v8.11 [04:34] technique: dork the host with site: on DuckDuckGo. why: fast, free, surfaces indexed pages past the login wall. http: query site:tfb.t-mobile.com. frame: -
- c09_v8.12 [05:04] tool: Burp Suite, opens a fresh project named T-Mobile. why: capture all traffic before poking around. http: -. frame: -
- c09_v8.13 [05:28] tool: Burp advanced scope control, adds "TMO" and "T-Mobile" regex. why: filter sitemap noise to only target assets. http: -. frame: frame_0033/0088 scope + sitemap
- c09_v8.14 [05:58] step: set sitemap to show-only / hide filter, apply. why: strips indexed junk so TFB is easy to find. http: -. frame: -
- c09_v8.15 [06:27] signal: browsing TFB triggered a request to assets/importmap.json. why: one page load pulled a file he never requested. http: GET assets/importmap.json. frame: frame_0033 importmap.json JSON response in Burp
- c09_v8.16 [06:27] example: importmap.json lists many JavaScript file links. why: a map of the app's JS, a roadmap of endpoints. http: JSON body of JS links. frame: -
- c09_v8.17 [06:57] step: manually paste each JS path into the browser (tfb_payment, main.js, tfb_upgrade). why: load them so they enter Burp. http: GET of each .js file. frame: -
- c09_v8.18 [07:22] signal: the JS files are very large (CPU spikes). why: modern apps ship huge bundles full of endpoints. http: large .js responses. frame: -
- c09_v8.19 [07:52] principle: test manually, load everything yourself. why: he distrusts automation to request all files correctly. http: -. frame: -
- c09_v8.20 [08:21] principle: loading JS into Burp keeps a permanent snapshot of the code. why: a frozen record of the JS for later search. http: responses stored in Burp. frame: -
- c09_v8.21 [08:50] signal: one JS file loads other JS files. why: must find those nested paths to pull more code. http: JS referencing more JS paths. frame: -
- c09_v8.22 [09:36] aside: notes they use React/Redux; skips the framework files. why: Redux bundles are not interesting to him. http: -. frame: frame_0062 sitemap with JS
- c09_v8.23 [10:15] signal: Burp passively scanned the JS and surfaced internal subdomains, e.g. care-ahub.tfb.kube.t-mobile. why: JS leaks Kubernetes/internal hosts. http: host *.kube.t-mobile.com. frame: -
- c09_v8.24 [10:41] technique: search the response body for a leaked hostname to find the file it came from. why: trace a finding back to its source JS. http: Burp search of response bodies. frame: -
- c09_v8.25 [11:11] example: JS yields client IDs and a path to OAuth tokens. why: secrets sitting in a 2 MB file. http: client IDs, OAuth token path. frame: -
- c09_v8.26 [11:36] signal: API links sit right under the leaked data in the JS. why: endpoints pair with the tokens/IDs found. http: API link strings. frame: -
- c09_v8.27 [12:02] tool: Burp "filter out JavaScript" toggle. why: hide JS from sitemap so only API/web requests show. http: -. frame: -
- c09_v8.28 [12:20] step: turn the JS filter off to confirm the JS requests are logged. why: verify everything was captured. http: -. frame: -
- c09_v8.29 [12:20] tool: GAP extension to pull links from the JS files. why: auto-extract endpoints, though it misses some. http: -. frame: -
- c09_v8.30 [13:24] step: paste GAP output into Notepad to read it better. why: too much data to read in Burp. http: extracted API paths. frame: frame_0080 Notepad list of npe.adn / kube URLs
- c09_v8.31 [13:49] principle: one page request cascades into endless endpoints. why: importmap referenced files that reference more files. http: chain from tfb.t-mobile.com to importmap.json to many JS. frame: -
- c09_v8.32 [14:17] principle: find every page you can; each unique path may load more. why: coverage is the whole game in exploration. http: -. frame: -
- c09_v8.33 [14:21] example: GAP surfaces usermanagement.tmobile.com and skava stream studio. why: unknown services worth probing. http: path usermanagement/implicit, skava stream. frame: frame_0080
- c09_v8.34 [14:41] technique: run domain recon on leaked hosts to see if they are internet-facing. why: no response may mean internal-only or legacy alias. http: -. frame: -
- c09_v8.35 [15:33] signal: scans GAP output for target-related hosts like shop.tfb. why: confirm which leaked names tie to the target. http: host shop.tfb. frame: -
- c09_v8.36 [15:50] tool: Burp dashboard "live passive crawl from proxy". why: auto-populate discovered URIs as you browse. http: -. frame: -
- c09_v8.37 [15:55] warning: tight scope limits what Burp crawls and populates. why: efficient but you may miss oddly-named or cloud hosts. http: -. frame: -
- c09_v8.38 [16:36] principle: ignore links at other domains you can't get paid for. why: stay on in-scope assets. http: -. frame: -
- c09_v8.39 [17:04] signal: "cube" in a hostname usually means Kubernetes. why: naming hints at the backend platform. http: host *.kube.t-mobile.com. frame: -
- c09_v8.40 [17:23] example: finds an API host npe.adn.t-mobile.com to probe. why: unknown API, test if it is internet-facing. http: host npe.adn.t-mobile.com. frame: frame_0080
- c09_v8.41 [17:30] principle: a 502 bad gateway can lie; do not stop there. why: 502 may be only a routing problem, host still alive. http: 502 response. frame: -
- c09_v8.42 [17:57] step: strip the path and resend; a 302 to "not found" proves the host is alive. why: distinguish dead from misrouted. http: 302 found redirect. frame: frame_0088 Repeater on npe.adn with qlab02
- c09_v8.43 [18:26] step: add a trailing slash after qlab02 and resend, getting a 404 not 502. why: endpoint expects service/env/path structure. http: path .../qlab02/ returns 404. frame: -
- c09_v8.44 [18:53] warning: automation that drops 502s misses live services. why: the 502 only meant a missing slash and path. http: -. frame: -
- c09_v8.45 [18:53] signal: URL shape is service name, then environment, then API path. why: qlab02 is the environment segment. http: service/env/path pattern. frame: -
- c09_v8.46 [19:31] technique: search main.js for the string to decode the host. why: JS names the parts, e.g. "meg endpoint". http: search main.js for "meg endpoint". frame: -
- c09_v8.47 [19:49] signal: second "meg endpoint" match shows env changed to adn prod PRD01. why: confirms the trailing segment is the environment. http: PRD01 vs qlab02. frame: -
- c09_v8.48 [20:14] principle: reading JS a little reveals what endpoint pieces mean. why: code labels the moving parts. http: -. frame: -
- c09_v8.49 [20:44] warning: can't correlate meg endpoint in other response bodies yet. why: app not used yet, so no traffic captured; answered later. http: -. frame: -
- c09_v8.50 [21:13] example: TFBBS ordering-shop-tradein-service-v4 looks like a SaaS API. why: name signals internet-facing API endpoints. http: host tfbbsn-ordering-shop-tradein-service-v4-saas. frame: -
- c09_v8.51 [21:13] offensive: he plans to test whether the endpoint requires an auth token. why: probe for broken access control. http: delete cookies, compare response. frame: -
- c09_v8.52 [21:40] principle: must hit a valid API path before auth/access-control checks trigger. why: no controller, no condition to test. http: valid API path. frame: -
- c09_v8.53 [22:21] principle: in modern web apps the gold lives in the JavaScript. why: SPAs ship every possible request in one big file. http: -. frame: -
- c09_v8.54 [22:43] signal: huge single JS bundles expose all endpoints at once. why: great for the hacker's reconnaissance. http: large JS bundle. frame: -

#### techniques seen
- browse every in-scope site: c09_v8.08, c09_v8.10
- search-engine dorking: c09_v8.11
- scope and filter in Burp: c09_v8.13, c09_v8.14, c09_v8.27, c09_v8.36
- manual JS loading into Burp: c09_v8.17, c09_v8.19, c09_v8.20
- JS link extraction and reading: c09_v8.24, c09_v8.29, c09_v8.46
- probe leaked hosts, decode URL shape: c09_v8.34, c09_v8.42, c09_v8.43, c09_v8.45

### c10_v8 23:13-45:20

- c10_v8.01 [23:13] signal: object-like names in the app (org name, MCC ID) catch his eye as IDOR candidates. why: named objects map to records he can try to swap. http: org name, MCC ID params. frame: -
- c10_v8.02 [23:37] principle: when a term is unknown (MCC ID), go figure it out by using the app, not by guessing. why: you cannot test what you do not understand. http: -. frame: -
- c10_v8.03 [24:07] technique: ask an AI/Google to learn the business domain of the target (what TFB is, how to make an account). why: domain knowledge first, before testing. http: -. frame: -
- c10_v8.04 [24:36] example: TFB = T-Mobile for Business; AI explains sign-up flow. why: confirms account path exists. http: -. frame: -
- c10_v8.05 [25:05] example: MCC ID groups business accounts sharing one tax ID, used for billing/reporting/hierarchy. why: reveals the account hierarchy to attack. http: -. frame: -
- c10_v8.06 [25:35] principle: AI helps with domain context, not with finding bugs in a large complex app. why: set the right tool to the right job. http: -. frame: -
- c10_v8.07 [26:01] technique: create a real account to reach authenticated functions. why: BAC testing needs a logged-in session. http: -. frame: signup page, "Phone number or account number" field (frame_0122).
- c10_v8.08 [26:23] signal: sign-up expects an existing business/phone number; portal registration is separate from account creation. why: shows the real onboarding path. http: -. frame: -
- c10_v8.09 [26:41] example: he drove to a store, registered as sole proprietor, bought a plan to get a business account. why: that access unlocked BAC testing. http: -. frame: -
- c10_v8.10 [27:09] principle: a regional/paid signup barrier shrinks the tester pool, so it is an edge. why: fewer rivals on that attack surface. http: -. frame: -
- c10_v8.11 [27:25] warning: do not create accounts with fake info (e.g. Australian banks); skip targets you cannot legally access. why: stay lawful. http: -. frame: -
- c10_v8.12 [28:16] principle: be willing to spend time and money for access others will not. why: cost is tiny vs a $35k-$55k bug. http: -. frame: -
- c10_v8.13 [28:46] technique: unauthenticated testing is still possible by finding APIs in the JavaScript. why: code is served without login. http: API paths in JS. frame: -
- c10_v8.14 [29:15] signal: huge number of API links and XHR calls pulled from the JS files. why: each is an endpoint to map. http: XHR/API URLs. frame: -
- c10_v8.15 [29:36] signal: BAC-relevant identifiers in paths: org ID, business account number (BAN). why: these are IDOR insertion points. http: org ID, BAN params. frame: -
- c10_v8.16 [30:02] signal: IDs are sequential integers (user ID, org ID, BAN, customer ID). why: guessable IDs mean BAC risk. http: user/org/customer ID params. frame: -
- c10_v8.17 [30:32] step: search the extracted paths for a new value (customer ID, "support search individual") to find its endpoint. why: learn where an object lives. http: endpoint search. frame: -
- c10_v8.18 [31:01] example: resource 645.js is an internal-only API, yet its JS is served on the internet. why: explains unseen paths. http: 645.js. frame: internal URL list (frame_0122 context).
- c10_v8.19 [31:23] offensive: he flags a "hierarchy" internal API as high value if someone pivots to reach it. why: big impact if accessible. http: hierarchy endpoint. frame: -
- c10_v8.20 [31:53] signal: versioned API paths like v4 party-interaction appear in the code. why: version stems help map the API. http: /v4/party-interaction. frame: -
- c10_v8.21 [32:20] principle: the live app exposes more explicit object names than the extracted code. why: use both sources. http: customer IDs, v1 commerce, v1 shopping-cart. frame: -
- c10_v8.22 [32:46] aside: T-Mobile hardened access control over two years; BAC is now much harder. why: target maturity sets expectations. http: -. frame: -
- c10_v8.23 [33:12] step: run a search to tell whether an ID path (billing account ID) is internal or reachable. why: filter by reachability. http: billing account ID. frame: -
- c10_v8.24 [33:26] tool: Burp Suite; plan to drop 645.js from logs and re-run the gap/extraction to remove internal-only noise. why: focus only on reachable endpoints. http: -. frame: -
- c10_v8.25 [33:51] signal: V4 paths he has access to carry known issues; an example org ID is hardcoded in the code. why: ready-made BAC test target. http: /v4 paths, org ID 7000000000000020152 (frame_0146). frame: b2b-experience v1 orgs/<id>/account-orders (frame_0146).
- c10_v8.26 [34:21] signal: a route resembling ACH/credit-card payment appears; developers keep changing routes. why: new routes mean new surface. http: ACHCC route. frame: -
- c10_v8.27 [34:49] principle: read and interpret path names (ACHCC = payments) rather than treat them as random. why: naming reveals function. http: ACHCC URL ignore list, account-orders. frame: -
- c10_v8.28 [35:11] offensive: a content service pulls an internal directory path with content; he would test it for path traversal or SSRF. why: not everything is BAC. http: content service path param. frame: -
- c10_v8.29 [35:43] report: T-Mobile pays well but uses a cumbersome payout spreadsheet/flowchart; read the brief first. why: know the program before investing. http: -. frame: -
- c10_v8.30 [36:13] technique: dumping values from the code reveals useful endpoints (e.g. the content service). why: extraction surfaces hidden functions. http: content-service paths. frame: System Message "link has expired" (frame_0135).
- c10_v8.31 [36:37] signal: web paths load the dashboard, which chains more JS and more functions. why: following flows reveals the app. http: web/app paths. frame: -
- c10_v8.32 [36:50] signal: a leaked report-request ID shows the GUID format; some objects are GUIDs, most still integers. why: know the ID formats in use. http: report request ID (GUID). frame: -
- c10_v8.33 [37:05] example: thousands of endpoints, each tied to customers; every look finds new APIs. why: scale of the attack surface. http: -. frame: -
- c10_v8.34 [37:31] aside: he hunts occasionally, not obsessively; deep target knowledge lets him find a bug in about an hour. why: experience compounds. http: -. frame: -
- c10_v8.35 [38:14] principle: many leads look like a bug but are not; expect to lose hours in rabbit holes. why: set realistic effort expectations. http: -. frame: -
- c10_v8.36 [38:43] principle: part of the game is picking a target rich in objects and IDs vs one with few APIs. why: more surface, more bugs. http: -. frame: -
- c10_v8.37 [38:55] signal: all links shown, many insertion points, legacy IDs everywhere; T-Mobile subdomains are in scope to pivot. why: perfect recipe for BAC. why pivot widens scope. http: subdomain URLs. frame: -
- c10_v8.38 [39:24] example: an insider subdomain and a checkout index link with a cid= param; he got P1s there before. why: index links leak objects. http: checkout index ?cid=. frame: -
- c10_v8.39 [39:53] tool: gau (gal) to pull indexed URLs for checkout.tfb.t-mobile.com, finding indexed shopping-cart links. why: archives expose live links. http: SID/CID params on cart links. frame: -
- c10_v8.40 [40:25] signal: the indexed links now have expiry set; expiries on index links are the wanted mitigation. why: tests whether the links still work. http: CID + SID tokens in link (frame_0146). frame: login URL list incl Microsoft/azure OAuth paths (frame_0100).
- c10_v8.41 [40:52] offensive: a special SID+CID link partially authenticated him and triggered a six-digit email code. why: shows the auth flow. http: SID+CID link, 6-digit code. frame: "Let's confirm it's you" 8-digit code prompt (frame_0158).
- c10_v8.42 [40:52] offensive: he notes that without rate limiting the 2FA code could be brute forced into the victim's cart (PII). why: assess impact. http: 2FA code endpoint. frame: -
- c10_v8.43 [41:22] example: a CID-only link did nothing; the SID param is required to trigger the 2FA prompt. why: isolate the needed parameter. http: CID vs SID params. frame: -
- c10_v8.44 [41:47] technique: gau is part of the process: links find things; re-crawl after hitting new flows (checkout gives Node auth2 v1 JWT tokens, secure-quote-order request). why: each hit yields new endpoints. http: /node-auth2/v1 JWT, secure-quote-order. frame: -
- c10_v8.45 [42:38] aside: next episode moves to Etsy for live authenticated BAC; TFB stays public-info only. why: keeps testing in scope. http: -. frame: -
- c10_v8.46 [42:59] signal: the indexed emails redacted-start are non-sensitive by design. why: judge what truly needs redaction. http: email in link. frame: -
- c10_v8.47 [43:25] technique: compare DuckDuckGo vs gau indexing; search engines skip secure-token links, gau (likely via VirusTotal scans) keeps them. why: pick the source that holds tokened links. http: tokened URLs. frame: -
- c10_v8.48 [43:50] principle: lots of API data is reachable with no auth token, which makes this a good demo target. why: unauth surface is large. http: -. frame: -
- c10_v8.49 [44:18] tool: Burp Intruder tried to speed the manual work; the sheer endpoint count still leaves bugs unfound. why: scale exceeds manual focus. http: -. frame: -
- c10_v8.50 [44:27] signal: static JSON responses / content assets served from REST APIs, maybe unintentionally exposed. why: exposed REST responses are a finding. http: content-assets, rest-apis/*.json (frame_0166). frame: tfb-acctmgmt content-and-assets rest-apis JSON list (frame_0166).
- c10_v8.51 [44:48] offensive: he probes for a WCS token in subscriber/line-detail responses; not present this time. why: tokens enable deeper access. http: WCS token, subscriber-line-detail. frame: -
- c10_v8.52 [45:16] principle: "you see a thing and you have to know" - test each curiosity to learn the app. why: curiosity-driven coverage. http: -. frame: -

#### techniques seen
- learn the business domain first (AI/Google): c10_v8.03, c10_v8.04, c10_v8.05, c10_v8.06
- create real account for authenticated access: c10_v8.07, c10_v8.09, c10_v8.12
- extract APIs/IDs from JavaScript: c10_v8.13, c10_v8.16, c10_v8.17, c10_v8.30
- filter internal vs reachable endpoints in Burp: c10_v8.23, c10_v8.24
- gau archive crawl for indexed links: c10_v8.39, c10_v8.44, c10_v8.47
- read path names to infer function: c10_v8.27, c10_v8.28
- pivot across in-scope subdomains: c10_v8.37, c10_v8.38


## v9 9. more exploration.mp4

### c11_v9 00:01-22:22

- c11_v9.01 [00:23] technique: crawl pages, pull every referenced JavaScript file, keep it to analyze. why: pages load JS that references more JS and endpoints. http: -. frame: -
- c11_v9.02 [01:07] signal: URIs that take parameters, a `$`-marked object or individual ID. why: parameters are what he hunts. http: URI with `$id` path segment. frame: -
- c11_v9.03 [01:36] principle: do not assume a URI takes no object; it may be a POST carrying a JSON body. why: hidden input surface. http: POST with JSON body. frame: -
- c11_v9.04 [01:45] step: open the JS file to read which parameters an endpoint expects. why: params live in JS variables. http: request parameters. frame: -
- c11_v9.05 [02:13] technique: pick a target he actually uses (Etsy). why: real usage reveals the app. http: -. frame: -
- c11_v9.06 [02:19] example: Etsy once had IDORs out of scope; Bugcrowd(?) put them back in scope. why: scope changed the opportunity. http: -. frame: -
- c11_v9.07 [02:42] technique: read the bug bounty brief before testing, know what is allowed. why: briefs hide odd rules. http: -. frame: -
- c11_v9.08 [03:11] signal: brief has bug-class overrides (self-XSS, CSRF excluded). why: shapes what to hunt. http: -. frame: -
- c11_v9.09 [03:40] example: www.etsy.com primary, mobile apps, APIs with docs, Etsy payments; wildcard in scope at lower pay. http: -. frame: -
- c11_v9.10 [03:40] principle: assume the low end of a reward range; ranges are a marketing gimmick, he avoids them. why: they pay P1s low. http: -. frame: -
- c11_v9.11 [04:35] principle: focus areas show what the client pays more for; he hunts unauthenticated access to user PII. http: -. frame: -
- c11_v9.12 [05:01] principle: "unauthenticated" also means an attacker with his own generic account reading other users' info. http: -. frame: -
- c11_v9.13 [05:25] principle: understand the business first; Etsy is a marketplace, sellers and buyers. http: -. frame: -
- c11_v9.14 [05:25] technique: do authenticated testing by buying things to generate traffic, using a $5 Visa gift card as a real card number. http: -. frame: -
- c11_v9.15 [06:25] tool: Burp target scope, Advanced, Add host Etsy, to isolate only in-scope traffic. http: -. frame: 0037 shows Etsy in scope, host list, HSTS-not-enforced issue
- c11_v9.16 [06:54] tool: Burp filter, show only in-scope, hide images and SVGs to cut noise. http: -. frame: -
- c11_v9.17 [07:21] signal: a beacon endpoint spammed the proxy; removed it from scope. why: noise muddies the view. http: beacon request. frame: -
- c11_v9.18 [07:50] step: pre-made two accounts with disposable emails before testing. why: ready for comparison. http: -. frame: -
- c11_v9.19 [08:34] technique: keep a second account to test broken access control safely without harming a real shop. http: -. frame: -
- c11_v9.20 [08:34] signal: login sent a security code (MFA) and account-hacked alerts, triggered by VPN. http: -. frame: -
- c11_v9.21 [09:28] technique: walk the seller flow (create a shop) to surface more API calls. why: unused features hide endpoints. http: -. frame: 0059 shows Etsy seller onboarding "How you'll get paid"
- c11_v9.22 [10:28] signal: shop is addressed by an integer object ID in the URI path. why: integer IDs invite IDOR. http: path with integer shop ID. frame: -
- c11_v9.23 [10:57] principle: integer object IDs throughout likely means IDORs throughout. why: consistent design. http: -. frame: -
- c11_v9.24 [11:23] signal: a form path used country ID 209, another integer. http: path with integer country ID. frame: -
- c11_v9.25 [11:46] principle: driving the live web populates correct request formatting, easier than crafting from JS. http: -. frame: -
- c11_v9.26 [12:15] example: seller onboarding demands PII, DOB, SSN (entered 123456789), address. http: onboarding form fields. frame: 0065 onboarding payments step
- c11_v9.27 [13:15] signal: heavy address validation, likely a soft PII check in the background. http: address validation requests. frame: -
- c11_v9.28 [13:32] tool: F12 network tab to watch background calls while using the app. http: -. frame: -
- c11_v9.29 [13:59] signal: onboarding calls Plaid to link a bank; he adds Plaid to scope for later. http: Plaid get-plaid-link-token, payment-method-enrollment, address/validate. frame: 0068 shows these POSTs in Burp
- c11_v9.30 [14:43] principle: the extra step nobody does (SSN, Plaid) is where the P1s hide. why: low coverage there. http: -. frame: -
- c11_v9.31 [15:13] principle: set up a fully working shop to reach every seller function and its code paths. http: -. frame: -
- c11_v9.32 [16:15] technique: review account settings to map available features. http: -. frame: 0077 tabs Account, Security, Public Profile, Privacy, Addresses, Credit Cards, Notifications
- c11_v9.33 [16:44] warning: address validation noise is unlikely to recur or yield PII bugs. http: -. frame: -
- c11_v9.34 [17:09] technique: look for a generic GET-by-shop endpoint. why: broad read access is high value. http: GET by shop ID. frame: -
- c11_v9.35 [17:38] principle: reason about backend pseudocode, lookup by ID then update, and whether the auth token is checked against the shop ID. http: -. frame: -
- c11_v9.36 [18:00] offensive: he tests the shop GET for broken access control on the shop ID. http: GET shop setting by ID. frame: -
- c11_v9.37 [18:28] example: GET returned name null; shop ID 7 gave "shop does not exist", backspace gave "not authorized", so access control is enforced on that call. http: GET with varied shop ID. frame: -
- c11_v9.38 [18:54] signal: his own shop name came back null, maybe because setup was never completed. http: GET shop name. frame: -
- c11_v9.39 [19:50] offensive: he appends a trailing slash to "name" to test routing bypass; it returned resource not found. http: path "name/". frame: -
- c11_v9.40 [20:11] tool: Burp convert selection, URL-encode all characters (Ctrl+U), to send %2F. http: %2F in path. frame: -
- c11_v9.41 [20:34] signal: %2F treated as a literal string, not URL-decoded; "name/" is not a valid setting. why: tells how the controller routes. http: setting path with %2F. frame: -
- c11_v9.42 [21:02] technique: request the settings endpoint and sort by name to see which settings were actually hit (only "name"). http: GET settings. frame: -
- c11_v9.43 [21:30] technique: traverse the API backwards to understand it, then fuzz or guess other settings, since access control may differ per setting path. http: per-setting paths. frame: -

#### techniques seen
- read JS for endpoints and params: c11_v9.01, c11_v9.04
- read the brief and set scope: c11_v9.07, c11_v9.15, c11_v9.16
- exercise app features to surface API calls: c11_v9.05, c11_v9.21, c11_v9.25, c11_v9.31, c11_v9.32
- second account for safe access-control testing: c11_v9.18, c11_v9.19
- IDOR by integer object ID: c11_v9.22, c11_v9.23, c11_v9.36, c11_v9.37
- routing/encoding tricks on API paths: c11_v9.39, c11_v9.40, c11_v9.41
- backward API traversal and setting enumeration: c11_v9.42, c11_v9.43

### c12_v9 22:22-45:55

- c12_v9.01 [22:22] technique: re-fetch root shop API with an integer, read the returned fields. why: JSON values name the app's data. http: GET shop API returns shop_name, shop_id, currency_code. frame: -
- c12_v9.02 [22:51] technique: treat each response value as a candidate setting, split on the underscore to try every permutation. why: response values give clues to hidden settings. http: shop_name, currency_code, favorites as settings. frame: -
- c12_v9.03 [23:19] signal: endpoint says whether a shop exists before it checks access. why: existence oracle leaks valid IDs. http: integer shop id, exists vs not. frame: -
- c12_v9.04 [23:19] signal: the param is type checked as int; non-numeric returns a type error. why: shows the expected type. http: shop id = "A" rejected, wrong type. frame: -
- c12_v9.05 [23:43] signal: int type check inherently blocks traversal, SQLi, XSS on that param. why: non-ints never reach the sink. http: -. frame: -
- c12_v9.06 [23:43] warning: single or double quote returns "resource not found", not a type error. why: odd branch worth probing. http: shop id = ' or " to 404. frame: -
- c12_v9.07 [24:37] signal: any symbol or a trailing slash reroutes to 404, maybe router code. why: maps input handling. http: symbol / trailing slash to 404. frame: -
- c12_v9.08 [25:04] signal: a pound sign is ignored server side, same URL-encoded as %23. why: fragment stripped before routing. http: shop id with #, %23, still "not authorized". frame: -
- c12_v9.09 [25:31] technique: send # or ? to detect if the value is relayed to another backend API path. why: finds server-side request chaining. http: # or ? appended to the id. frame: -
- c12_v9.10 [25:31] principle: a front API value can land inside a server's request to an internal, non-internet API. why: that insertion point is where SSRF-ish bugs start. http: /api/v1/user?user_id=... relayed to internal /api/users/<id>/details. frame: Notepad sketch of the two API paths.
- c12_v9.11 [26:55] offensive: he tests a # in the relayed value to truncate the appended backend path. why: returns the base resource, not the fixed sub-path. http: id + # drops /details. frame: -
- c12_v9.12 [27:23] offensive: he tests ../ sequences in the value to pivot to other backend roots. why: reach endpoints like payments. http: traversal to /api/payments/<id>. frame: -
- c12_v9.13 [28:02] principle: IDOR and simple SSRF often sit at the same endpoints and return sensitive data. why: one probe finds both. http: -. frame: -
- c12_v9.14 [28:30] principle: from a URI view, # and ? end the path; the rest is fragment or params. why: explains why they break appended paths. http: -. frame: -
- c12_v9.15 [28:42] technique: #, ?, and the backslash trick are the core API fuzz characters. why: cheap, high-signal probes. http: -. frame: -
- c12_v9.16 [29:31] principle: learn the developers' conventions early; first week finds few bugs. why: patterns predict bug classes. http: -. frame: -
- c12_v9.17 [30:00] signal: integer user_id and shop_id everywhere predict IDORs. why: sequential ints are guessable. http: user_id int, shop_id int. frame: -
- c12_v9.18 [30:23] technique: reuse known param names (shop_id, user_id=1) across other endpoints. why: some accept them even when not documented. http: shop_id, user_id params. frame: -
- c12_v9.19 [30:46] technique: keep a running list of high-value parameters. why: focus later testing. http: shop_id across many files. frame: -
- c12_v9.20 [31:15] example: two paths, api/v3/ajax/shop/<n> and api/v3/ajax/bespoke/shop/<n>; bespoke returns far more. why: compare siblings to find the richer one. http: GET ajax/bespoke/shop/<id>. frame: -
- c12_v9.21 [31:41] tool: send the bespoke request to Burp Repeater to learn the API shape. why: iterate on one request. http: PUT shop preferences. frame: Burp Repeater, request and JSON response, Inspector open.
- c12_v9.22 [31:41] principle: use two accounts so IDOR tests never touch a stranger's shop. why: safe, authorized testing. http: his shop 635...118. frame: -
- c12_v9.23 [32:22] step: log out of the creator account, log into a second account (153...993) for its tokens. why: get a second valid session. http: -. frame: -
- c12_v9.24 [32:49] tool: sort Burp history time-descending to grab the latest request. why: find the fresh auth. http: -. frame: -
- c12_v9.25 [32:49] step: grab the cookies and the CSRF token from the POST request. why: both are needed to replay. http: cookies + CSRF token. frame: -
- c12_v9.26 [33:19] step: send the request to Repeater to carry all cookies, then copy the URI. why: less manual setup. http: -. frame: -
- c12_v9.27 [33:49] signal: body content type is x-www-form-urlencoded, not application/json. why: must match to replay. http: Content-Type: x-www-form-urlencoded. frame: -
- c12_v9.28 [33:49] example: replaying account B against shop A returns "not authorized to view this shop". why: confirms access control holds. http: PUT preferences, access denied. frame: -
- c12_v9.29 [34:18] signal: logging out does invalidate the auth token. why: tokens are server-tracked. http: -. frame: -
- c12_v9.30 [34:32] principle: test cross-account access control only between two accounts you own. why: no harm to real users. http: -. frame: -
- c12_v9.31 [34:32] technique: or run two browsers with two cookie sets instead of log in and out. why: faster two-account testing. http: -. frame: -
- c12_v9.32 [35:18] tool: right-click, extensions, GAP to list JavaScript files; ~864 on Etsy. why: JS holds hidden endpoints. http: -. frame: -
- c12_v9.33 [35:48] example: GET ajax/bespoke/member returns "resource not found"; path expects more. why: probe required params. http: GET ajax/bespoke/member to 404. frame: -
- c12_v9.34 [36:45] signal: ajax/member/addresses returns full address, name, and phone. why: PII sink. http: GET ajax/member/addresses. frame: -
- c12_v9.35 [37:09] report: an access control bug on addresses is a likely P2/P3 for PII leak. why: severity tracks data value. http: -. frame: -
- c12_v9.36 [37:09] technique: delineate the most valuable APIs, then focus testing there. why: spend effort where impact is. http: -. frame: -
- c12_v9.37 [37:39] technique: run a real checkout to unlock order, receipt, and saved-card features. why: creates objects to test. http: -. frame: Etsy home, search for stickers.
- c12_v9.38 [38:34] signal: the product page offers make-offer, buy-now, and add-to-cart. why: three cart paths to test. http: -. frame: -
- c12_v9.39 [39:27] signal: payment options PayPal (OAuth/SAML), Google Pay, bank account, gift card each need testing. why: each flow differs. http: -. frame: "Choose a payment method" modal listing PayPal, Google Pay, bank account, gift card.
- c12_v9.40 [39:56] signal: a bad gift-card code made no network call, so a format check runs client side. why: must read JS to pass it. http: gift-card field, no request. frame: -
- c12_v9.41 [40:47] signal: a placed order returns a receipt ID and a cart ID, both integers. why: new IDOR candidates. http: receipt_id, cart_id integers. frame: -
- c12_v9.42 [41:18] technique: on receipt pages click everything; surfaces view-details, full receipt, purchase ID. why: hidden object references. http: order details, purchase_id. frame: Etsy account menu open on "ZeeTwo" over the help page.
- c12_v9.43 [41:47] step: use help-with-order, "I accidentally placed an order", to cancel the test order. why: avoid shipping the item. http: -. frame: -
- c12_v9.44 [42:47] signal: a "$400 null" and a failed action probably tie to captcha. why: explains the missing call. http: -. frame: -
- c12_v9.45 [42:47] technique: on the purchase-by-id help page, decrement the id to test access control. why: check for horizontal access. http: help page ?purchase_id=<n>. frame: -
- c12_v9.46 [43:12] example: lower purchase ids return page-not-found, maybe tied to user id; needs deeper tests. why: don't conclude from one try. http: purchase_id back-steps to 404. frame: -
- c12_v9.47 [43:12] example: receipt_id=8 populates the page, 7 shows nothing; cart_id is moot; show_thank_you=1 just prints. why: finds which param controls rendering. http: root page ?receipt_id, cart_id, show_thank_you_module=1. frame: order confirmation, "Thanks for your order, ZeeTwo", show_thank_you_module=1 in URL.
- c12_v9.48 [44:40] principle: root-URL params change server rendering but it still checks the authenticated session. why: reaching another's receipt is unlikely. http: -. frame: -
- c12_v9.49 [45:03] tool: run gau on www.etsy.com for indexed URIs to pivot into other data. why: find exposed endpoints. http: gau www.etsy.com. frame: -
- c12_v9.50 [45:26] principle: test a checkout request by request, not all at once in retro. why: you miss what each call did. http: -. frame: -

#### techniques seen
- response values as settings: c12_v9.01, c12_v9.02
- fuzz chars (# ? \) to probe routing and relay: c12_v9.09, c12_v9.11, c12_v9.12, c12_v9.15
- reuse known int params across endpoints: c12_v9.18, c12_v9.19
- compare sibling endpoints (shop vs bespoke): c12_v9.20
- two-account safe access control testing: c12_v9.22, c12_v9.23, c12_v9.30, c12_v9.31
- JS and gau for hidden endpoints: c12_v9.32, c12_v9.49
- real checkout to spawn testable objects: c12_v9.37, c12_v9.41, c12_v9.42
- ID / param tampering on receipt pages: c12_v9.45, c12_v9.46, c12_v9.47

### c13_v9 45:55-68:38

- c13_v9.01 [45:55] signal: cart detail response carries his email plus saved data; cards and billing address appear as integer IDs. why: shows how much the cart object exposes. http: cart detail response, card ID / billing address as ints. frame: -
- c13_v9.02 [46:23] principle: Etsy is a good IDOR target but the IDs hide in JavaScript, so read the code slowly. why: numbers do not all surface from active testing. http: -. frame: -
- c13_v9.03 [46:51] technique: resend a cart request after checkout to see if the cart stays queryable. why: tests whether the object persists. http: GET cart by id after a purchase POST. frame: -
- c13_v9.04 [47:18] example: a checked-out cart was still active and queryable. why: a cart should become an order and die. http: -. frame: -
- c13_v9.05 [47:18] signal: going one ID back returned "don't own cart / index doesn't exist". why: ownership validation, the correct access-control pattern. http: cart id param, ownership error. frame: -
- c13_v9.06 [47:47] signal: an alternate endpoint takes cart_id with underscore vs cart id without. why: legacy parameter formats linger. http: cart_id vs cartid param. frame: -
- c13_v9.07 [47:47] signal: a missing-input error names the exact parameter it expects. why: the app leaks expected param names. http: "missing input cart ID" error. frame: -
- c13_v9.08 [48:12] example: an added card was encrypted in transit, then stored linked to user id, card id, address id. why: maps how PII objects reference each other. http: add-card request, user/card/address int IDs. frame: -
- c13_v9.09 [48:38] signal: stored in plaintext: expiry month/year, name, address, zip, last four. why: flags where PII sits client-side. http: card record fields. frame: -
- c13_v9.10 [49:07] offensive: he tests a user id param in Repeater by iterating numbers. why: probe for broken access control. http: user id param, iterated. frame: -
- c13_v9.11 [49:38] signal: iterating produced service-unavailable then a 403 (different responses). why: a changed response can mark something worth digging into. http: 503 then 403. frame: -
- c13_v9.12 [50:05] warning: the odd response was only a CAPTCHA prompt, not a bug. why: rate behaviour mimics a finding. http: CAPTCHA challenge. frame: -
- c13_v9.13 [50:34] principle: BAC testing is tedious; keep lists of endpoints, params, and every param format. why: organization is the real work. http: -. frame: -
- c13_v9.14 [51:02] principle: hardened targets yield more bugs; Etsy fixed past IDORs and put them out of scope. why: the game is finding what they missed. http: -. frame: -
- c13_v9.15 [51:23] technique: hunt deprecated or lingering endpoints through JavaScript. why: missed fixes hide in old code. http: -. frame: -
- c13_v9.16 [52:06] signal: everything is referenced by integer object client-to-server; legacy PHP references visible. why: integer IDs are the attack surface. http: integer object IDs. frame: 0193 order-confirmation page shows an order id and his email on screen.
- c13_v9.17 [52:32] tool: the JS URL scraper has a "show only requested items" toggle; unchecked shows every scraped URI. why: reveals paths not hit in active testing. http: -. frame: -
- c13_v9.18 [53:00] technique: read the scraped URI list slowly to spot structures the eye missed. why: passive reading finds new surface. http: -. frame: -
- c13_v9.19 [53:31] signal: listing paths take integers; also conversation IDs, with_id, referring_receipt_id. why: each ID is a testable object. http: listing/conversation int params. frame: -
- c13_v9.20 [53:55] offensive: he would try conversation IDs to reach another user's private messages. why: tests message access control. http: conversation id param. frame: -
- c13_v9.21 [54:24] principle: the program highlights PII; address, card, orders, checkout all expose PII to the client. why: PII is what they pay for. http: -. frame: -
- c13_v9.22 [55:14] technique: exercise every feature - create a shop, list items, upload images, reviews, comments, likes. why: each feature opens new requests and bugs. http: -. frame: -
- c13_v9.23 [55:38] principle: BAC bugs are simple to swap; the hard part is diligence, organization, creativity. why: sets the mindset for the work. http: -. frame: -
- c13_v9.24 [56:09] tool: he loads the scraped output (~19,000 lines) into Notepad++. why: a text editor to sift URIs. http: -. frame: 0315 Notepad++ full of etsy.com shop/listing URLs with wanzapid params.
- c13_v9.25 [56:38] step: sort lines ascending, then remove duplicate lines to clean the URI list. why: makes the list readable. http: -. frame: -
- c13_v9.26 [57:05] step: Ctrl+F "find all" on "underscore ID" across the scraped output. why: isolates every id-bearing path. http: *_id URI patterns. frame: 0297 Notepad++ search highlights _id matches across many URLs.
- c13_v9.27 [57:05] tool: a GAU-style tool surfaces old index IDs and the places they are used. why: finds valid foreign IDs and forgotten links. http: -. frame: -
- c13_v9.28 [57:33] signal: spotted a section id (new), campaign ids, valid receipt ids, a conversation link. why: new ID types mean new tests. http: section/campaign/receipt ids. frame: -
- c13_v9.29 [57:33] technique: log in, then open each scraped link carrying another user's IDs to see if it works. why: direct access-control check. http: foreign-id links while authenticated. frame: -
- c13_v9.30 [58:02] example: a social-invite link to another shop triggered a verification/CAPTCHA puzzle. why: shows a guarded endpoint. http: social invite link. frame: -
- c13_v9.31 [58:16] aside: a plain Firefox new-tab page appears, not the target. why: context switch, no app fact. http: -. frame: 0224 Firefox new-tab, generic news tiles, nothing about Etsy.
- c13_v9.32 [58:32] example: the social invite returned a 403 then a redirect, so it likely did nothing. why: distinguish real effect from redirect. http: 403 then redirect. frame: -
- c13_v9.33 [59:00] warning: don't trust the browser on odd hits; open Burp to see what actually happened. why: UI hides the real response. http: -. frame: -
- c13_v9.34 [59:00] example: a conversation keyed to an un-purchased receipt id opened the messaging dialog but returned nothing. why: endpoint reachable, data not leaked. http: conversation by receipt id. frame: 0239 Etsy Messages inbox empty, "No conversations to see here".
- c13_v9.35 [59:54] signal: an email-workflow link looks like an encrypted token. why: tokenised links are worth inspecting. http: email workflow token param. frame: -
- c13_v9.36 [60:25] signal: an OAuth connect link redirects to "ship saver" and carries roles. why: OAuth redirects and roles can expose access. http: OAuth connect redirect with roles. frame: -
- c13_v9.37 [61:23] example: a transactions path with an integer returned a plain 404. why: 404 may mean missing or access-denied. http: transactions/<int>, 404. frame: -
- c13_v9.38 [61:23] signal: a page passes order id twice. why: duplication hints at mixed validation. http: order id appears twice. frame: -
- c13_v9.39 [61:45] technique: when an id appears twice, change one or both; maybe only one is validated. why: the unchecked copy may drive the lookup. http: order id params. frame: -
- c13_v9.40 [62:15] example: your/orders/sold showed as a redirect; purchases differs from orders. why: terminology maps to different objects. http: orders vs purchases paths. frame: -
- c13_v9.41 [62:34] principle: learn the app's terminology and history before testing means much. why: without it, responses are ambiguous. http: -. frame: -
- c13_v9.42 [63:05] technique: access control may be checked only at an API root, so a deeper stem can leak. why: test each path segment. http: orders/sold/completed/<id>. frame: -
- c13_v9.43 [63:52] step: keep combing the de-duped URI list for interesting stems. why: methodical coverage. http: -. frame: 0315 same Notepad++ shop-URL list, scanned line by line.
- c13_v9.44 [64:01] principle: getting access denied is the norm. why: sets expectations for the grind. http: -. frame: -
- c13_v9.45 [64:20] principle: one BAC bypass tends to reveal more nearby; bugs spiral out. why: a find teaches the pattern. http: -. frame: -
- c13_v9.46 [64:44] principle: focus on BAC - swap numbers, add ids, insert integers; occasionally SSRF or an injection if it looks susceptible. why: BAC is the main yield. http: -. frame: -
- c13_v9.47 [64:44] principle: a susceptible target usually hides many bugs (20-40); the gold-mining analogy. why: pick ground that has gold. http: -. frame: -
- c13_v9.48 [65:42] technique: pull the app apart in layers - test in the web, then read JS for the weird stem at each API. why: combines active and code review. http: -. frame: -
- c13_v9.49 [66:08] technique: scope a whole session to one path, e.g. /ajax/bespoke, and test it in full. why: depth beats scatter on a big target. http: /ajax/bespoke paths. frame: -
- c13_v9.50 [66:30] step: test every method and endpoint, fuzz, add and remove params, try slashes, #, ?. why: exhaust each endpoint's variants. http: method/param/char variants. frame: -
- c13_v9.51 [66:49] signal: BAC can live in headers, e.g. an is-admin true header. why: not all bypass is id-swapping. http: is-admin header. frame: -
- c13_v9.52 [67:22] technique: read JS, find an is-admin header reference, then add that header. why: code reveals the magic header. http: is-admin request header. frame: -
- c13_v9.53 [67:45] aside: little body/payload param testing done yet; params can be changed in the body too. why: flags an untested surface. http: request body params. frame: -
- c13_v9.54 [68:11] principle: to test payments you must use the features - add PayPal, a bank account, Stripe, card types. why: coverage demands real feature use. http: -. frame: -

#### techniques seen
- read JavaScript / scraped URIs for hidden and deprecated endpoints: c13_v9.15, c13_v9.17, c13_v9.18, c13_v9.26, c13_v9.27, c13_v9.48, c13_v9.52
- replay / swap integer object IDs for access control: c13_v9.03, c13_v9.10, c13_v9.20, c13_v9.29, c13_v9.39
- organize and exhaust endpoints, params, formats, methods: c13_v9.13, c13_v9.22, c13_v9.49, c13_v9.50
- probe id and path structure for leaks: c13_v9.05, c13_v9.06, c13_v9.42, c13_v9.51


## v10 10. conclusion.mp4

### c14_v10 00:02-28:39

- c14_v10.01 [00:54] principle: this is his real broken-access-control method, nothing held back. why: he wants the process explicit. http: -. frame: -
- c14_v10.02 [01:19] principle: BAC hunting has one goal, find stuff, not craft an injection like XSS. why: mindset differs by bug class. http: -. frame: -
- c14_v10.03 [01:48] technique: step one, read the scope and ask what is in scope. why: stay in bounds, keep a good rating. http: -. frame: -
- c14_v10.04 [02:07] technique: subdomain recon, dump every subdomain, find all the apps. why: map the attack surface. http: -. frame: -
- c14_v10.05 [02:32] step: resolve subdomains to see which are internet facing and responsive. why: live ones are easiest to reach. http: -. frame: -
- c14_v10.06 [03:00] tool: search-engine dorking, Wayback/gau(?), GitHub to find what lives at each subdomain. why: history reveals hidden paths. http: -. frame: -
- c14_v10.07 [03:28] tool: fuzz URI paths with his supplied wordlists. why: find content not linked anywhere. http: GET fuzzed path. frame: -
- c14_v10.08 [03:56] technique: browse the app manually, load JavaScript files, find hidden/unknown pages. why: black-box, you do not know what is there. http: -. frame: -
- c14_v10.09 [04:20] technique: register or sign up when auth is required; open a bank/cell/insurance account. why: get inside the authenticated app. http: -. frame: -
- c14_v10.10 [04:50] principle: the secret sauce is willingness to go the extra step to get an account. why: more access, more surface. http: -. frame: -
- c14_v10.11 [05:21] technique: spend money, buy a product, make transactions. why: payment flows open hidden, rarely tested bugs. http: -. frame: -
- c14_v10.12 [06:14] signal: JavaScript holds URI paths you did not know existed. why: you miss what you cannot see. http: JS files. frame: -
- c14_v10.13 [06:14] technique: scan JS with your eyes, do not only keyword-search it. why: interesting things do not match keywords. http: -. frame: -
- c14_v10.14 [06:42] signal: grep JS for secrets, API keys, paths, other domains, object IDs. why: these leak structure and access. http: -. frame: -
- c14_v10.15 [06:42] example: on Etsy he saw user_id and cart_id in JS. why: names reveal object types to swap. http: user_id, cart_id params. frame: -
- c14_v10.16 [07:11] technique: build a list of important object IDs from JS, request and response params. why: a worklist for IDOR testing. http: path params, headers. frame: -
- c14_v10.17 [07:57] offensive: he tests object IDs as params and swaps their values. why: check broken access control. http: swap ID param values. frame: -
- c14_v10.18 [08:21] example: he reviews a gau dump of Etsy.com for interesting URLs. why: triage links worth revisiting. http: -. frame: Burp Repeater, target etsy.com, request 7 of many.
- c14_v10.19 [08:53] principle: use your brain, something looking different is the signal; context matters (why is an email leaked). why: judgment, not rules. http: -. frame: -
- c14_v10.20 [09:19] signal: paths you do not recognize, unseen objects, authed-looking objects reachable from your account. why: these are IDOR candidates. http: -. frame: -
- c14_v10.21 [09:19] signal: encrypted IDs, GUIDs, tokens often return sensitive data. why: owners assume nobody else holds them. http: token/GUID params. frame: -
- c14_v10.22 [10:18] example: a "load web view one bid" old HTTP link with a weird token jumped out. why: unseen param, worth investigating. http: legacy http:// link, bid token. frame: Etsy ActivateNonsense shop, "not currently selling" banner.
- c14_v10.23 [10:43] principle: a request may trigger more on the backend than the one page. why: watch for side effects. http: -. frame: -
- c14_v10.24 [11:03] example: messaging a seller gave him a conversation ID, message ID, and sender/user ID. why: harvest valid IDs to test. http: conversation_id, message_id, sender/user_id. frame: -
- c14_v10.25 [11:32] offensive: he removes the to_user_id param to see if the request still works. why: probe which params are required. http: drop to_user_id. frame: -
- c14_v10.26 [11:32] signal: a letter in the ID gives 503, a wrong number gives 404. why: error type tells if server reads the param. http: 503, 404 responses. frame: -
- c14_v10.27 [11:59] example: changing to_user_id returns a different user "grand ideas", no sensitive leak. why: confirms the swap works. http: to_user_id swap. frame: -
- c14_v10.28 [12:22] offensive: he tests whether an ID endpoint reveals if a user is an admin. why: admin enumeration could be a low-sev bug. http: is-admin field. frame: -
- c14_v10.29 [12:46] principle: you must understand the app to know what "admin" means here (Etsy admin vs shop admin). why: context sets severity. http: -. frame: -
- c14_v10.30 [12:46] example: this is a working IDOR, swapping to_user_id returns another user. why: textbook access-control flaw. http: to_user_id swap. frame: -
- c14_v10.31 [13:14] signal: the param only accepts an integer; user_id 1 is often an admin. why: integer IDs are enumerable. http: user_id integer. frame: -
- c14_v10.32 [13:14] offensive: he walks user_id 1, 11, etc and finds bots are user IDs. why: enumerate the ID space. http: user_id enumeration. frame: -
- c14_v10.33 [13:43] signal: a trailing zero is tolerated, but null or empty is rejected. why: input handling reveals validation. http: user_id value tests. frame: -
- c14_v10.34 [14:12] offensive: he changes referring_id to 11 too and diffs responses. why: learn if that param does anything. http: referring_id swap. frame: -
- c14_v10.35 [14:12] example: referring_id change only alters headers, likely does nothing. why: not every param is live. http: referring_id, response headers. frame: -
- c14_v10.36 [14:41] offensive: he switches the method to POST to see if the endpoint accepts it. why: try all HTTP methods. http: POST to the ID endpoint, not found. frame: -
- c14_v10.37 [15:00] technique: try all methods, all numbers, all parameters, including giving only user_id. why: exhaust the request shape. http: method and param fuzzing. frame: -
- c14_v10.38 [15:00] signal: non-numeric value like X should error if the server reads the param. why: distinguishes used vs ignored params. http: user_id=X. frame: -
- c14_v10.39 [15:27] example: user_id=X returned a 302 redirect, deleted the session, and logged him out. why: unexpected side effect of a param. http: user_id=X, 302, session-key-deleted header. frame: -
- c14_v10.40 [16:35] warning: the account got locked for "suspicious activity" after the odd request. why: aggressive testing trips security. http: account suspended page. frame: Etsy ActivateNonsense shop, sign-in modal, "Password was incorrect".
- c14_v10.41 [17:05] warning: both accounts were killed; expect this pain in bug bounty. why: be ready to pivot. http: -. frame: -
- c14_v10.42 [17:36] tool: make disposable email aliases (name+test1@gmail.com) for accounts. why: one alias blocked, swap to another. http: -. frame: -
- c14_v10.43 [17:54] warning: prior Zwink/Pinterest indicators may flag him; Etsy/Pinterest merge means they know him. why: reputation follows the tester. http: -. frame: -
- c14_v10.44 [18:25] example: the T-Mobile file shows endless offering-configuration APIs across targets. why: API surface is never-ending. http: /commerce/v1/.../offeringConfiguration paths. frame: Notepad++ list of T-Mobile commerce API endpoints with IDs.
- c14_v10.45 [18:53] technique: build a repository of interesting links, then revisit and tinker with each over time. why: calm, unhurried manual work finds bugs. http: -. frame: -
- c14_v10.46 [19:17] principle: once a company does IDs right (numbers everywhere, like Etsy/Pinterest now), issues get hard to find. why: mature targets resist. http: -. frame: -
- c14_v10.47 [19:43] principle: hunt the weird places, not the front door; find the open window (old code, legacy subdomains). why: less-tested surface pays off. http: -. frame: -
- c14_v10.48 [20:12] technique: subdomain recon to find legacy/different subdomains using many object IDs. why: old code is under-tested. http: -. frame: -
- c14_v10.49 [20:12] principle: wildcard-scope targets are better, more to look at. why: bigger surface, more BAC bugs. http: -. frame: -
- c14_v10.50 [20:40] report: once you find a bug, report it on a bug bounty platform. why: start of the reporting flow. http: -. frame: -
- c14_v10.51 [21:06] tool: bug bounty platforms, HackerOne, Intigriti(?), Synack Red Team, Bugcrowd. why: where you log the bug. http: -. frame: -
- c14_v10.52 [21:35] report: prefer programs with short response/triage/payout times. why: long waits kill momentum and interest. http: -. frame: -
- c14_v10.53 [22:16] report: control freaks struggle; severity has high subjectivity, especially for BAC. why: you have little control over the rating. http: -. frame: -
- c14_v10.54 [23:31] report: PII severity varies by program; name, address, phone, DOB, IDs, SSN/tax, payment IDs, email, IP, geo. why: know what counts as sensitive. http: -. frame: -
- c14_v10.55 [25:04] warning: even SSNs get downgraded by claiming they are EINs (business tax IDs). why: severity arguments cut both ways. http: -. frame: -
- c14_v10.56 [25:53] report: triagers are first line, check is-reproducible then is-triage-correct. why: they gatekeep before the client. http: -. frame: -
- c14_v10.57 [26:48] report: after triagers, program owners can also fail to reproduce and re-triage. why: another layer, no control for you. http: -. frame: -
- c14_v10.58 [27:16] report: make the severity argument, there is a sales pitch, but it may not change the outcome. why: set expectations. http: -. frame: -
- c14_v10.59 [27:45] warning: a report can be marked duplicate and pay zero after all the work. why: accept it as part of the game. http: -. frame: -
- c14_v10.60 [28:12] principle: manual BAC hunting rarely gets duplicates, unlike automated XSS/SQLi scanning. why: argues for the manual method. http: -. frame: -

#### techniques seen
- scope and subdomain recon: c14_v10.03, c14_v10.04, c14_v10.05, c14_v10.48
- content discovery (dork, wayback, github, fuzz, JS): c14_v10.06, c14_v10.07, c14_v10.08, c14_v10.12, c14_v10.13, c14_v10.14
- get inside the app (register, pay): c14_v10.09, c14_v10.11
- object-ID worklist and IDOR swapping: c14_v10.16, c14_v10.17, c14_v10.24, c14_v10.25, c14_v10.30, c14_v10.32, c14_v10.34, c14_v10.37
- link repository and revisit: c14_v10.18, c14_v10.45
- hunt the weird/legacy surface: c14_v10.47, c14_v10.48, c14_v10.49
- operational hygiene (email aliases): c14_v10.42
- reporting and triage: c14_v10.50, c14_v10.52, c14_v10.56, c14_v10.57, c14_v10.58

### c15_v10 28:39-51:43

- c15_v10.01 [28:39] principle: hunt manually, not with scanners, to cut duplicates. why: everyone runs the same scanners, so their findings collide. http: -. frame: -
- c15_v10.02 [29:02] report: a program owner can mark your bug "duplicate of internal issue", a dupe of a finding never logged on the platform. why: you get no visibility to confirm or dispute it. http: -. frame: -
skip 30:00-31:46: payout stories and feelings, nothing about the app.
- c15_v10.03 [31:46] report: a batch of P1s was flipped to not-applicable over an out-of-scope note in the brief. why: scope rules beat validity; read the brief first. http: -. frame: -
- c15_v10.04 [32:15] warning: one buried word in a URI path put a finding out of scope. why: a scope exclusion can be a single path token. http: the API link / a word in the URI path. frame: -
- c15_v10.05 [33:26] signal: he opens his Bugcrowd profile. why: sets up his stats. http: -. frame: bugcrowd.com profile URL loading in the address bar.
- c15_v10.06 [33:50] aside: handle "the_IDORminator", formerly "Z-Wink". why: his identity on the platform. http: -. frame: profile header, rank 14th, 100% accuracy.
- c15_v10.07 [34:05] aside: 99th percentile across P1-P5, 1195 vulns. why: shows volume, including unpaid informational bugs. why: -. http: -. frame: performance-stats panel, priority-percentile bars, radar chart.
- c15_v10.08 [34:48] example: 101 bugs in two months by going deep on one call-center product. why: depth on one app pays off. http: -. frame: -
- c15_v10.09 [35:10] principle: choose high-paying programs over hopping between cheap ones. why: same effort, far more reward. http: -. frame: -
skip 35:40-37:20: career history and income arc, nothing about the app.
- c15_v10.10 [37:20] example: T-Mobile for Business (TFB) is the API target they dumped; one P1 ~$55k. why: context for the target. http: -. frame: -
- c15_v10.11 [38:17] principle: go deep on one well-paying program and learn it. why: familiarity surfaces the one bug. http: -. frame: -
- c15_v10.12 [39:10] technique: try a prepared list of parameter names on an endpoint even with no hint to. why: legacy systems may accept undocumented params. http: a customer-search request, added an "SSN"/"tax ID"(?) parameter. frame: -
- c15_v10.13 [39:28] example: endpoint took accountId (1,2,3...); swapping in an SSN parameter ran an SSN search outside access control. why: a parameter swap becomes an IDOR. http: accountId parameter -> SSN parameter. frame: -
- c15_v10.14 [39:45] step: keep a populated wordlist of parameter names to swap in. why: ready creativity beats guessing each time. http: parameter names. frame: -
- c15_v10.15 [40:13] technique: change API paths, see what lives at each, change IDs, try different parameters. why: the core of API access-control exploration. http: paths, IDs, parameters. frame: -
- c15_v10.16 [40:51] signal: Etsy runs a WAF that blocks him; consider a VPN / rotating IP. why: the WAF shapes how he can test. http: -. frame: -
- c15_v10.17 [41:22] technique: reason about what trips the WAF (401s, an X in an ID, a foreign user ID). why: understand the rules to avoid blocks. http: user ID parameter with X / mismatched value. frame: -
- c15_v10.18 [41:51] warning: a robust app may flag the account and re-validate the token when you stuff another user's ID. why: test the user-ID parameter carefully. http: user ID parameter. frame: -
- c15_v10.19 [42:19] warning: make test accounts look real (plausible name, address, Gmail). why: an audit team blocks obviously fake data. http: -. frame: -
skip 42:40-45:08: quitting, taxes, life plans, nothing about the app.
- c15_v10.20 [45:10] principle: hunt high-impact PII: address, phone, DOB, ID/passport, SSN/tax-id, payment, IP, lat/long. why: these set severity. http: -. frame: editor list of those PII data types.
- c15_v10.21 [45:14] signal: NodeHAP(?) API paths he knows well, parameterized like ${attachmentId}, plus auth/token endpoints. why: familiarity flags new entries. http: dumped paths. frame: path dump, e.g. /attachmentManagement/v2/attachment/${attachmentId}/getDownloadURL, /auth/.../openid-connect/token.
- c15_v10.22 [45:25] signal: those paths are almost all POST requests. why: a POST needs a crafted body. http: POST endpoints. frame: -
- c15_v10.23 [45:53] step: dig the JavaScript per endpoint to find and correctly format the POST body. why: you cannot replay a POST without its body. http: POST body sourced from JS. frame: -
- c15_v10.24 [46:21] principle: the method is exploration, manual testing, injection points; no more. why: debunks over-automation. http: -. frame: -
- c15_v10.25 [46:47] principle: no right-click "find all IDORs" tool exists; do the work. why: automation will not do it for you. http: -. frame: -
- c15_v10.26 [48:09] principle: much of it is swapping numbers/IDs, e.g. a purchase ID. why: access-control bugs are often that simple. http: purchase ID. frame: -
- c15_v10.27 [48:31] technique: find a target's unhardened "back door", not the front door; poke for webpages, sites, subdomains. why: a hardened front door wastes effort. http: -. frame: -
- c15_v10.28 [48:56] principle: private invites hold easier bugs than public programs. why: fewer hunters have picked them over. http: -. frame: -
- c15_v10.29 [49:21] aside: practice IDORs on .gov VDP programs on Bugcrowd (unpaid, less hardened). why: realistic practice targets. http: -. frame: -
- c15_v10.30 [50:41] technique: full recap, map the app: enumerate scope, subdomains, dump each, find apps, paths, pages, JavaScript. why: methodical app mapping. http: subdomains, paths, pages, JS. frame: -
- c15_v10.31 [50:52] technique: sign up, get an auth token, swap it, try to break it, switch between two accounts. why: tests access control. http: auth token. frame: -
- c15_v10.32 [51:04] technique: hack the APIs: add/remove numbers, change paths; grep JS for secrets, creds, paths, URIs, domains, identifiers; build a wordlist for Intruder; try parameters and headers. why: turns recon into an attack list. http: API params, headers, JS strings. frame: -

#### techniques seen
- manual over scanners: c15_v10.01, c15_v10.24, c15_v10.25
- parameter swapping / wordlist: c15_v10.12, c15_v10.13, c15_v10.14, c15_v10.32
- path and ID tinkering: c15_v10.15, c15_v10.26, c15_v10.30
- WAF reasoning and stealth: c15_v10.16, c15_v10.17, c15_v10.18, c15_v10.19
- POST body from JS: c15_v10.21, c15_v10.22, c15_v10.23
- target selection: c15_v10.09, c15_v10.11, c15_v10.27, c15_v10.28, c15_v10.29
- access-control / auth token testing: c15_v10.31
