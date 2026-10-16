# card spec: write a technique card

You turn raw notes into technique cards for the `app_exploration` skill. The skill's whole goal: take a complex web app apart into its functions, and each function into its HTTP requests and parameters. Understanding the app, not attacking it. A card teaches one technique so the reader can do it on a new app.

## inputs the spawn gives you

- your home slices: the note files you own (e.g. `source/notes/c01_v5.md`). You must account for every note id in them.
- your cards: 2 or 3 card names to write.
- the full card list (titles only), so you can cross-link with `see [other-card]`.

Read only your home slice files. Do not read the transcripts or other slices. The notes are your source.

## what a card is

One file per card: `references/techniques/<NN>-<card-name>.md`. The `<NN>` order is in your spawn. Shape:

```
# <card title>

**what**: one line. the technique, in plain words.
**when**: the point in exploring an app where you reach for it.
**why it works**: the property of web apps that makes it pay off. first principles, not a recipe.

## steps
1. ...  (imperative. the real steps from the notes. name the tool he used: Burp, Caido, gau, waymore, GAP/Gap, crt.sh, SecurityTrails, Notepad++. a tool is an example, not a requirement.)

## what it gives the map
the function, request, parameter, or signal this adds to the app model. this is the point of the card.

## signals to read
the things that tell you something: a header, a status code, a response length, a URL shape, a path name, a parameter name, a GUID vs int id, an error. one line each.

## when it does not apply
the default, defense, or app shape that makes this technique quiet or useless.

## his example
one concrete case from the notes (Bugcrowd, Etsy, T-Mobile/TFB targets). cite the note id.

notes: c01_v5.03, c01_v5.07, ...   <- every note id this card draws from
```

## rules

1. Voice: `twin/voice.md`. Short declaratives. Define by contrast. Name the failure. No hype. Lowercase body is fine.
2. Ground every claim in a note id. A claim with no note is cut. Do not invent steps, tools, or payloads the notes do not have.
3. The line between this skill and attacking: exploration maps the app (functions, requests, parameters, signals). Where a note is an attack step (IDOR swap, payload, bypass), keep it only as **where the map goes**: name the hypothesis the map enables, in one line, no payload, no exploit steps. The skill explores; it does not exploit.
4. Account for every note id in your home slices. Each must appear in some card's `notes:` line. A note that is purely an attack action with no mapping value goes under a `## where the map goes` line in the nearest card, still cited.
5. Authorized targets only (PortSwigger, HTB, his own machine, an in-scope program). Say it where it fits, once.
6. Budget: a card is one screen. 400 words at most. Cut history and second examples first.
7. Write only your card files. Do not edit any other file.

## reply (under 100 words)

the card files you wrote, and for each: its note-id count. then: any note id in your home slices you could NOT place, and why.
