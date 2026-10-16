# Live chat area — function map

Host: 0a95006b03f30ebf833543780095002f.web-security-academy.net
Capture: captures/03_livechat.json (42 entries)
Cards used: 08-js-mining-for-endpoints, 12-model-objects-and-parameters
Account: none needed (lab chat is unauthenticated). Sent one harmless "hello" to exercise the socket.

---

## Function 1 — Live chat (send message)

- What it does: user types a message; the page opens a WebSocket and streams messages to/from a support bot. Messages render into the chat table.
- Transport (request): WebSocket, `wss://<host>/chat` (form `action` attribute of `#chatForm`). Not a plain HTTP request; frames do not appear in the HTTP buffer.
- Outbound frames:
  - plain text `READY` — sent once on socket open to request history.
  - JSON `{ "message": <string> }` — the submit handler builds FormData from `#chatForm` (textarea `name="message"`, maxlength 500), html-encodes each value, then `JSON.stringify` and `send`.
- Inbound frames:
  - plain text `TYPING` — renders a "[typing...]" row.
  - JSON `{ "user": <string>, "content": <string> }` — a chat line.
  - JSON `{ "error": <string> }` — an error line.
  - sentinel value `user: "CONNECTED"` — connection marker, not cleared from system rows.
- Signal: no HTTP status (socket). Message shape is JSON keyed by `message` out, `user`/`content`/`error` in.
- Card: 08 (socket URL + frame shapes read from chat.js), 12 (message object model).

## Function 2 — View / download transcript

- What it does: client gathers the rendered message rows, POSTs them, server stores a transcript file and redirects the browser to it.
- Requests:
  - `POST /download-transcript` — body is FormData, field `transcript` (shape: string, the message rows joined by `<br/>`). XHR then follows `xhr.responseURL`.
  - `GET /download-transcript/<n>.txt` — the redirect target. Observed `/download-transcript/2.txt` for this session.
- Parameters (names only): `transcript` (string).
- Signal: 200, `text/plain` body; the id lives in the path as `<n>.txt`.
- Card: 08 (path from viewTranscript.js + inline `viewTranscript('/download-transcript')`), 12 (id model).

---

## from JS, not exercised (chat.js, viewTranscript.js, inline script)

- `wss://<host>/chat` — socket; the `READY` and JSON send calls above (only one JSON "hello" was fired by me).
- `POST /download-transcript` — path passed inline as `viewTranscript('/download-transcript')`; I did not POST directly, only via the button.
- `GET /download-transcript/<n>.txt` — sibling-by-id endpoint.
- `window.renderChatMessage(content)` — an optional hook; absent here so `content` renders raw (noted, not tested).

## Object / parameter model (card 12)

- Object: chat transcript. Id: **integer, sequential, in path** — `download-transcript/<int>.txt` (saw `2.txt`). A `1.txt` sibling is implied; other users' transcripts likely sit at other integers. Classic direct-object-reference shape (mapping only, not tested).
- Object: chat message. Keys: `message` (out), `user` + `content` (in), `error` (in). No id on messages.
- Param `transcript`: free string, client-built, server trusts it to write the stored file content.
