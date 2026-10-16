topic: WAHH 2e chapter 4, Mapping the Application
slug: wahh_ch04_mapping_the_application
target: phase1_target.md (book, pp.73-115, Stuttard and Pinto, Wiley 2011)

bitter pill: the book is 2011. The mechanism is right. Many tools and defaults changed. Each node in the mind map says what broke and the 2026 way. A "2026:" sentence marks it.

domains:
  1. Enumerating visible content. Manual browsing, spiders, user-directed spidering, spider limits and danger, dead client tech, dead tools.
  2. Discovering hidden content. What hides, brute force, status codes, name inference, search engines, archives, forum clues, server defaults.
  3. Pages, functional paths, hidden parameters. One URL with many functions, API descriptions, JavaScript mining, parameter guessing.
  4. Entry points for user input. URL path, parameters, odd formats, headers, out-of-band channels.
  5. Fingerprinting server-side technology. Banners, HTTP fingerprints, extensions, cookie names, third-party components.
  6. Server-side functionality and unique behavior. Dissecting requests, REST to internal call, extrapolation, bolted-on parts.
  7. Mapping the attack surface. Map first, core mechanisms, feature to bug class, third-party code check, plan, the EIS example.

anchors (gold badge): 12 HACK STEPS blocks (H1 to H12) and the 5 end questions (Q1 to Q5). Each sits on the node that teaches it.

prerequisites: HTTP basics (request, response, status, headers, cookies). Burp proxy use.

acquired:   (empty. He was not drilled. Resume lines are context only, not proof.)

stuck:
  - A 200 does not mean a page exists. Custom not-found pages answer 200. Source: WAHH p.84-85.
  - Brute force finds nothing on a one-URL app where a parameter picks the function. Source: WAHH p.93-96.
  - A crawler from 2011 sees an empty app when the front end is JavaScript. 2026 issue. Source: katana README, node d1b.
  - Old Google operators now return nothing, with no error. Source: Google operator page, Search Engine Roundtable.
  - Tool flags drift. Cite only flags read in the tool's own docs. Source: each README, node text.
  - A spider can hit delete and admin functions on a live site. Source: WAHH p.77.

order: foundation (d1a, d2a, d4a, d5a, d7a), then core (the techniques), then dive (dead tools, odd formats, extrapolation, EIS walk).

sources (claim, url, grounded, grade by .rules/grounding-and-confidence.md):
  - Flash blocked from 12 Jan 2021 | https://www.adobe.com/products/flashplayer/end-of-life.html | grounded | 5
  - DirBuster inactive, archived, ZAP fork | https://wiki.owasp.org/index.php/DirBuster | grounded | 5
  - ZAP no longer an OWASP project since Aug 2023 | https://www.zaproxy.org/docs/nowaspzap/ | grounded | 5
  - WebScarab archived, ZAP successor | https://en.wikipedia.org/wiki/WebScarab | grounded | 3 (secondary)
  - OSVDB shut down April 2016 | https://www.theregister.com/2016/04/06/open_source_vuln_database_closes/ | grounded | 3 (secondary, no official page exists)
  - OSV.dev, POST /v1/query, OSV-Scanner | https://google.github.io/osv.dev/ | grounded | 5
  - Google cache: operator dead Sept 2024, Wayback link instead | https://seroundtable.com/google-cache-dead-38112.html | grounded | 3 (secondary)
  - Google operator page lists site:, before:, after:, filetype:, not link:/related:/cache: | https://support.google.com/websearch/answer/2466433 | grounded | 4 (absence on an official page)
  - Wayback CDX API (url, matchType, fl, collapse, filter, output) | https://github.com/internetarchive/wayback/tree/master/wayback-cdx-server | grounded | 5
  - gau (Wayback, Common Crawl, OTX, URLScan; --subs, --providers) | https://github.com/lc/gau | grounded | 5
  - waybackurls | https://github.com/tomnomnom/waybackurls | grounded | 5
  - Common Crawl is free crawl data | https://commoncrawl.org/get-started | grounded | 5 (index access not confirmed)
  - katana (-u -jc -d -kf -rl -jsl) | https://github.com/projectdiscovery/katana | grounded | 5
  - httpx (-l -td -sc -title -web-server) | https://github.com/projectdiscovery/httpx | grounded | 5
  - nuclei (-u -t -tags -as -s) | https://github.com/projectdiscovery/nuclei | grounded | 5
  - interactsh (interactsh-client; DNS, HTTP, SMTP, LDAP) | https://github.com/projectdiscovery/interactsh | grounded | 5
  - ffuf (-w -u -mc -fc -fs -recursion -e -ac -rate) | https://github.com/ffuf/ffuf | grounded | 5
  - feroxbuster (-u -x -s) | https://github.com/epi052/feroxbuster | grounded | 5 for those flags. -w, -d not read, not cited.
  - Arjun (-u -m -w -t --stable --passive; 25,890 names) | https://github.com/s0md3v/Arjun/wiki/Usage and README | grounded | 5
  - Param Miner (Guess params/headers, 65,000 names per request) | https://github.com/PortSwigger/param-miner | grounded | 5
  - jsluice extracts URLs and secrets from JS | https://github.com/BishopFox/jsluice | grounded | 5 (CLI syntax not read, not cited)
  - LinkFinder -i URL -o cli | https://github.com/GerbenJavado/LinkFinder | grounded | 4 (maintenance status not confirmed)
  - SecLists, Assetnote wordlists | https://github.com/danielmiessler/SecLists , https://wordlists.assetnote.io/ | grounded | 5 (no file names cited)
  - Burp crawl uses a built-in Chromium browser, login handling | https://portswigger.net/burp/documentation/desktop/automated-scanning/webapp-scans/full-crawl-and-audit | grounded | 5 (JS handling not stated on page)
  - GraphQL introspection lists types and fields | https://graphql.org/learn/introspection/ | grounded | 5
  - OpenAPI Description describes an API's surface | https://spec.openapis.org/oas/latest.html | grounded | 5
  - HTTP/2 binary framing, header compression, multiplexing | https://www.rfc-editor.org/rfc/rfc9113.html | grounded | 5

ungrounded: (grade 2, flagged in the map, never stated as plain fact)
  - CAT, Wikto, IEWatch, httprint, httprecon status. No source opened. Node d1g, d5b.
  - Server banners and session cookie names are often stripped or generic. Nodes d5a, d5d.
  - File extensions are rarer in modern routes. Node d5c.
  - CDN and WAF rate limits, bot protection, and WAF blocks confusing the test. Node d6c. (Also the reason for the rate flags in d1e, which is only a safety tip.)
  - SPA and fetch/XHR make "pages" worse. Stated only through GraphQL (d3a), which is grounded. The general SPA claim has no opened source.
  - Burp Collaborator as the Burp-side OOB tool. Not opened. Left out of the node. interactsh is the grounded one.
  - Burp Content Discovery current status. Not opened.
  - NVD as the replacement database. NVD page opened, but it did not describe itself in the fetched text. Left out of node text.
  - .git folders, API classes, JSON entry points, public repos as the new forum. Memory. Flagged in nodes d2a, d2h, d4a, d4c, d7c.
  - Source-map mining. Not opened. Not cited.
  - Nikto flags (-root, -404) from the book. Not rechecked in 2026.

handoff: explainer not run
