---
name: game-design-one-page-design-doc
description: Create a concise one-page game design document and export it as both markdown and PDF. Use when a user wants a one-page design doc, one-pager, pitchable design summary, or compact game concept sheet that captures identity, pillars, summary, features, interface, aesthetic direction, sound, audience, platform, and milestone plan on a single page.
---

# Game Design One-Page Design Doc

Create a one-page game design document that is readable, decision-useful, and visually polished — exportable as a PDF that looks like a real product.

Use this skill when the user wants a compact game design summary rather than a bloated GDD. The output is designed to be passed around in meetings, dropped in Slack, or emailed to publishers without embarrassment.

Read `references/family-conventions.md` when you want the shared style and prioritization rules for this game-design skill family.
Read `references/source-notes.md` when you want the distilled takeaways from the reference template and the GDC talk overview.

## Core principle

A one-page design doc is not a small bad GDD. It is a compressed communication tool.

It should:
- state what the game is
- state why it is interesting
- state what feeling or fantasy it is chasing
- state the core features and interaction model
- state enough production framing to make it actionable

It should not:
- try to explain every subsystem
- drown the reader in lore
- use vague slogans instead of specifics
- hide the real game behind marketing fluff

## What to produce

Produce:
1. **One-page PDF** — the shareable, visually designed version
2. **One-page markdown doc** — the editable text version
3. **Structured source JSON** — the intermediate data used for rendering

## Visual design

The PDF renderer (`scripts/render_one_page_gdd.py`) produces a professional dark-theme layout:

- **Dark background** — near-black navy `#0F111A`, with a lighter panel for the header
- **Teal accent colour** — `#00C8A0` for rules, section headings, pillar tag nubs, and bullet markers
- **Pillar tags** — design pillars rendered as pill-shaped labels with a teal left accent in the header
- **Two-column body** — left column for mechanics-heavy content, right column for production/aesthetic content
- **Section rules** — a teal horizontal rule above each section label
- **Poppins typeface** — used when available (falls back to Liberation Sans or DejaVu)
- **Branded footer** — document label on the left, game title on the right

The renderer uses **ReportLab** (vector PDF — real text, not a raster image), making the output searchable, copy-pasteable, and print-sharp.

### Font requirements

The renderer searches for fonts in standard system locations automatically:
- Linux: `/usr/share/fonts/truetype/google-fonts/`, `/usr/share/fonts/truetype/liberation/`
- macOS: `~/Library/Fonts/`, `/Library/Fonts/`
- Windows: `C:/Windows/Fonts/`

Preferred: Poppins (Bold, Medium, Regular, Light) from fonts.google.com  
Fallback: Liberation Sans (included in most Linux systems)

### Dependencies

```bash
pip install reportlab
```

## Default section structure

Left column:
- Genre / Story / Mechanics Summary
- Key Features
- Interface & Controls

Right column:
- Art Style
- Music & Sound
- Roadmap / Launch Criteria (includes platform, audience, milestones, launch date)

Header band:
- Game title
- Identity / Mantra (subtitle)
- Design Pillars (as pill tags)

## Process

### 1. Clarify the design input
Collect or infer the minimum needed:
- game title or working title
- game identity / mantra
- 2 to 3 design pillars
- concise gameplay/story/mechanics summary
- 3 to 6 key features
- input / interface model
- art references or aesthetic direction
- sound direction or emotional audio goals
- platform
- target audience
- milestone plan or launch criteria

If the user gives messy notes, compress them rather than asking endless questions.

### 2. Write for one-page density
Keep each section tight.

Guidelines:
- prefer short bullets over dense paragraphs
- keep pillars punchy (2–4 words each)
- keep the summary to a compact paragraph
- keep features to the strongest few, not every idea
- make roadmap milestones concrete enough to be useful
- write like the doc will be skimmed in under two minutes

### 3. Preserve design clarity over style fluff
If the concept is fuzzy:
- choose clarity over hype
- expose contradictions instead of smoothing them over
- keep claims grounded in actual mechanics or fantasy

### 4. Build the structured source JSON
Write a JSON file matching the renderer schema.

Expected fields:
- `title`
- `identity_mantra`
- `design_pillars` (array, 2–4 items)
- `summary`
- `features` (array, 3–6 items)
- `interface`
- `art_style`
- `music_sound`
- `platform`
- `audience`
- `milestones` (array)
- `launch_day`

See `references/example-input.json` for a worked example.

### 5. Render markdown and PDF

```bash
# Install dependency first if needed:
pip install reportlab

# Render:
python scripts/render_one_page_gdd.py --input <slug>.json --md <slug>.md --pdf <slug>.pdf
```

The renderer auto-discovers fonts. If content is too long, shorten the copy before rerendering — do not try to fit more by cramming.

### 6. Check fit and trim aggressively
Before finalizing, verify:
- the concept is legible at a glance
- the features list is not overstuffed
- the PDF still feels like a one-pager (not wall-to-wall text)
- the roadmap is realistic enough to be useful
- the strongest idea is visible immediately

If the PDF looks crowded, shorten the writing. If there is too much whitespace, the document is probably well-scoped — do not pad it.

## Output expectations

By default, create files in the current working directory or a user-specified target folder:
- `<slug>.json`
- `<slug>.md`
- `<slug>.pdf`

Use a slug based on the game title when naming files.

## Response structure

When using this skill, report:
- where the JSON, markdown, and PDF files were written
- any sections that had to be compressed heavily
- any major ambiguities or contradictions you preserved or surfaced

## References

Read these when useful:
- `references/source-notes.md` for the distilled source principles and section model
- `references/example-input.json` for renderer input shape and field conventions

## Working principle

If a team cannot explain the game on one page, the design is probably not clear enough yet.

Use this skill to produce a one-pager people can actually read, discuss, and pass around.
