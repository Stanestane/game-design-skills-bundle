---
name: moodboard-generator
description: Build a themed visual moodboard — sources candidate images from the web, curates them for color harmony, composition, and mood fit, and composes a properly designed board (not a plain photo grid) as an HTML artifact and a flattened PNG. Use this any time the user asks for a moodboard, mood board, visual reference board, inspiration board, style board, or aesthetic/color-palette collage for a theme, brand, room, character, game, event, or creative project — even if they just describe a vibe or aesthetic ("something coastal and mid-century", "cyberpunk night market energy") without using the word "moodboard" explicitly. Also use when asked to research visual references for a look, pull a color palette from a theme, or build a reference sheet for design/art direction.
---

# Moodboard Generator

A moodboard is a composition, not a photo dump. The difference between a board that
looks curated and one that looks like a Pinterest search result is entirely in the
steps below: interpreting the brief into a real color/shot-type plan, curating hard,
and laying the board out with deliberate visual hierarchy.

Read `references/composition-principles.md` before curating — it covers hero-image
selection, shot-type variety, color harmony types, and layout balance. Refer back to
it during curation, not just once at the start.

Copyright review of sourced images is handled by a separate skill/process — don't
self-censor source selection on copyright grounds here; just source and curate for
visual fit.

## Workflow

### 1. Interpret the brief

Turn whatever the user gave you — a phrase, a mood, a character, a brand, a room — into
a concrete plan before searching:

- **Mood adjectives** (3-5 words): what should someone feel looking at this?
- **Color harmony** (see reference doc): monochrome / analogous / complementary /
  triadic / neutral+accent — name it explicitly.
- **Subject/shot list**: what specific things, textures, and scenes would embody this
  theme? Aim for the shot-type variety in the reference doc (hero/establishing,
  environment, detail/object, texture/material, human if relevant).
- **Typography style**: serif / sans / script / condensed, matched to mood.

If the brief is vague ("something cozy"), make a confident interpretive choice and
state it rather than asking the user to fill in a spec — moodboards are inherently
about proposing a direction, not executing an exact one.

### 2. Source candidate images — with real, embeddable URLs

This is the step most likely to go wrong, so be deliberate about it: the board needs
actual `https://...` image URLs that will load in a browser, not just images you've
looked at.

The image-search tool is good for a quick visual gut-check but does **not** hand you a
usable URL — don't try to embed anything from it directly into the board.

Instead, source from stock-photo sites via `web_fetch`, which returns their real
`images.pexels.com` / `images.unsplash.com` CDN URLs paired with descriptive captions,
right in the fetched content:

```
web_fetch("https://www.pexels.com/search/<query>/")
web_fetch("https://unsplash.com/s/photos/<query>")
```

(URL-encode multi-word queries, e.g. `sun%20bleached%20concrete`. If `web_fetch`
rejects a guessed URL as unseen, run a quick `web_search` for `<query> pexels` or
`<query> unsplash` first, then fetch the result link — the tool requires a URL to have
appeared in a prior search/fetch.)

Each result gives you a caption ("Detailed close-up of beige wool texture...") next to
its direct CDN image URL — that caption is your composition/color signal; you don't
need to separately view the pixel to judge fit for most images. Pexels URLs also
support size params (`?auto=compress&cs=tinysrgb&w=1200`) and Unsplash ones support
`?w=1200&h=1600&fit=crop&auto=format` — use these to request roughly the aspect ratio
your layout slot needs.

Run several distinct, targeted queries per board — not one broad query. Five to eight
queries covering different shot types from your plan will surface far better variety
than one query repeated. Examples for a "coastal modernism" brief:

- "sun bleached concrete architecture"
- "mid century modern coastal house"
- "linen textile texture natural light"
- "driftwood weathered wood texture"
- "minimalist window ocean view"

Aim to gather roughly 20-40 candidates across all queries before curating — you need a
large enough pool to be selective in the next step.

### 3. Curate

This is the step that actually makes the board good — don't skip to layout, and don't
curate from captions alone. Caption text tells you what a photo is *of*, not whether
it's actually a strong, specific, on-mood shot — generic-sounding captions
("rainy street with neon reflections") often turn out to be generic images. Before
committing to a set, spend a few image-search calls actually looking at the strongest
candidates, especially hero contenders, and prefer iconic/specific subject matter over
generic keyword matches (for a Tokyo brief, "Shibuya crossing at night" and "Shinjuku
izakaya alley" beat five interchangeable "wet street neon" shots). Watch for AI-generated
stock (sites like StockCake label it explicitly, e.g. "stock AI image") and avoid it in
favor of real photography — a moodboard is a material/color/light reference, and
AI-generated images are a weaker reference for that than real photos.

For each candidate, weigh it against the plan from Step 1:

- Does its color story fit the named harmony? (on-palette vs. off-palette)
- What shot type is it (hero/environment/detail/texture)? Do you already have enough
  of that type?
- Composition quality on its own terms — is it a strong, clear image, or cluttered/
  ambiguous?
- Does it actually feel like the mood adjectives, or just technically match the
  keywords?
- Is it specific and iconic to the theme, or a generic stand-in that could belong to
  any similar brief?

Default to 8-16 images that together cover the shot-type checklist and hold a coherent
palette, with one clear standout for the hero slot. If the user asks for a denser or
"maxed out" board, push toward 16-18 and make the mood/detail split explicit: several
wide/tall shots that carry the overall scene, plus a real cluster of small tiles doing
pure macro/texture/detail work — not just more of the same shot type. Cutting a
mediocre or generic image is almost always better than keeping it for volume.

While curating, note 4-6 palette colors (as hex codes) that represent the board's
color story, inferred from the captions and your own knowledge of the theme. Precision
isn't critical, coherence is.

### 4. Assign layout roles

For each curated image, assign:

- `size`: `"hero"` (at most one — optional, see the reference doc; skip it entirely
  if no image is a clear standout), `"wide"` or `"tall"` (matches the image's own
  orientation — don't stretch a portrait shot into a wide slot), `"normal"`, or
  `"small"` for minor supporting/texture shots.
- `alt`: a short description.

Don't add source links or credit labels on the tiles — keep the board visually clean.

Balance sizes so the board has real hierarchy — don't make everything `"normal"`.
A typical 10-image board might be: 1 hero, 2 wide, 2 tall, 3 normal, 2 small.

### 5. Build the board

Write a JSON file matching the schema documented at the top of
`scripts/build_html_moodboard.py`, then run:

```bash
python3 scripts/build_html_moodboard.py board.json board.html
```

This produces a self-contained HTML file with a deterministic JS masonry layout (not
CSS Grid or CSS columns — both have real gap/content-loss failure modes in browsers;
see the comment at the top of the script for why). The hero, if present, spans two
columns as a large focal tile alongside other images — never the full board width,
which crowds out everything else. A palette swatch strip and mood-matched Google Fonts
typography for the title round it out. Open/view it and sanity-check against the Step 6
checklist in the reference doc before moving on — this is cheap to fix now (swap a
JSON entry, rerun) and expensive to fix after PNG export.

Present the HTML as an artifact so the user can review it inline.

### 6. Export PNG

```bash
python3 scripts/render_png.py board.html board.png
```

This tries a headless browser render. If it fails (exit code 2) — most commonly because
the current environment can't reach the internet to install a browser or load the
image/font URLs — tell the user plainly: PNG export isn't available in this environment,
the HTML file is the deliverable, and they can open it in a browser and use the
browser's own screenshot/print-to-image if they need a flat file. Don't present this as
the skill having failed; the HTML board is fully valid and reviewable on its own.

If it succeeds, present both the HTML and PNG files to the user.

## Iterating

If the user wants changes (swap an image, shift the palette, try a different harmony),
edit the JSON and rerun `build_html_moodboard.py` rather than hand-editing the HTML —
keeps the source of truth consistent if they ask for another round after that.
