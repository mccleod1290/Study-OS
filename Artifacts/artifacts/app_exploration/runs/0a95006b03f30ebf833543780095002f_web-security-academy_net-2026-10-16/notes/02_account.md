# area: account + auth

host: `0a95006b03f30ebf833543780095002f.web-security-academy.net`
capture: `captures/02_account.json`
scope: map only. no credentials submitted, no account made, no test run.

---

## function: my-account (gated entry redirect)

- what it does: the "My account" link opens the per-user account page. with no
  session it does not load; the server bounces the browser to the login page.
- request: `GET /my-account`
- parameters: none in the URL.
- signal: unauthenticated request returns a redirect to `/login` (final URL
  observed in the browser was `/login`). this is the authentication gate: the
  page needs a session before it serves account data.
- card: 07-auth-vs-authz-model. authN gate first; the authZ check (whose account
  you see) only matters once logged in, not recorded here.

## function: login form (authentication)

- what it does: takes a username and password plus an anti-CSRF token and
  submits them to authenticate; on success it would set a session and release
  `/my-account`.
- request: `POST /login` (form `method="POST" action="/login"`)
- parameters (field names + shape; NO values recorded):
  - `csrf` — hidden input, 32-char alphanumeric token, `required`.
  - `username` — text input, `required`.
  - `password` — password input, `required`.
- signal:
  - CSRF token present as a hidden field, so this form expects a per-request
    token (not just a cookie) — points to a synchronizer-token model.
  - page served over the `GET /login` (200) document.
  - session cookie: not directly readable here — the session is set only on a
    successful POST, and PortSwigger's session cookie is httpOnly (pinchtab
    cookie capability is also off). none exposed to the page pre-login. per
    card 07 the cookie is the single thing that would authenticate `/my-account`
    once issued; name to confirm after a legitimate login, outside this map.
- card: 05-proxy-setup-and-accounts (scoped capture, login-reach), 07-auth-vs-authz-model.

---

## auth model (per card 07, recorded not tested)

- authN: `/my-account` is gated; no session -> redirect to `/login`.
- authZ: the IDOR surface of this lab lives past login (per-user object access).
  not in this account/auth area; left to the feature-mapping worker.
