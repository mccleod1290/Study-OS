# Area: catalog + product detail

Host: 0a95006b03f30ebf833543780095002f.web-security-academy.net
Lab: Insecure direct object references (PortSwigger). Map only, no attack.
Capture: captures/01_catalog.json (56 entries, this host only)

## Function: home / product catalog
- What it does: lists every product as a card with image, title, rating, and a "View details" link. No login needed; it is the public shop front.
- Request: `GET /`
- Parameters: none on the wire.
- Signal: 200, response type text/html (full catalog page). Product cards are server-rendered; each "View details" href carries a productId.
- Card: 06-exercise-features-map-requests

## Function: product detail
- What it does: shows one product's page (title, image, description) when "View details" is clicked. Click fired a navigation to `/product?productId=1`.
- Request: `GET /product?productId=<n>`
- Parameters: `productId` : int, small and sequential (observed 1, 2, 3). Single query parameter; this is the direct object reference. Parameter recorded only; value NOT swapped (that would be an IDOR test = attack, out of my scope).
- Signal: 200, response type text/html. Each id returns a distinct product page (different title/image), so the id selects the object server-side. No JSON, no object id echoed in a body field.
- Card: 06-exercise-features-map-requests, 09-read-response-and-change-signals

## Supporting requests (same host)
- `GET /image/productcatalog/products/<file>` : int/filename for each product thumbnail. 200, image. Path reference worth noting, not exercised beyond load.
- `GET /resources/css/labsEcommerce.css`, `/resources/labheader/css/`, `/resources/labheader/js/labHeader.js` : static assets. 200.

## From JS, not exercised (card 08 pointer, read labHeader.js)
- WebSocket: `ws(s)://<host>/academyLabHeader` — opened by labHeader.js, sends "PING" every 5s, receives lab-status HTML. PortSwigger lab-status channel, not a catalog feature. No HTTP request fired for it in the capture.
