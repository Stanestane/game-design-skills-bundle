---
name: game-design-one-page-design-doc
description: Create a concise one-page game design document and export it as both markdown and PDF. Use when a user wants a one-page design doc, one-pager, pitchable design summary, or compact game concept sheet that captures identity, pillars, summary, features, interface, aesthetic direction, sound, audience, platform, and milestone plan on a single page.
---

# Game Design One-Page Design Doc

Create a one-page game design document that is actually readable, decision-useful, and exportable as a PDF.

Use this skill when the user wants a compact game design summary rather than a bloated GDD. This skill is inspired by one-page design-document practice: communicate the core idea clearly, fit the essentials on one page, and give the team something they will actually read.

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
1. **One-page markdown doc** - the editable text version
2. **One-page PDF** - the shareable formatted version
3. **Structured source JSON** - the intermediate data used for rendering, when useful for iteration

## Default section structure

Use this structure unless the user asks for a different one:
- Game Identity / Mantra
- Design Pillars
- Genre / Story / Mechanics Summary
- Features
- Interface
- Art Style
- Music / Sound
- Development Roadmap / Launch Criteria

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
- keep pillars punchy
- keep the summary to a compact paragraph
- keep features to the strongest few, not every idea
- make roadmap milestones concrete enough to be useful
- write like the doc will be skimmed in under two minutes

### 3. Preserve design clarity over style fluff
If the concept is fuzzy:
- choose clarity over hype
- expose contradictions instead of smoothing them over
- keep claims grounded in actual mechanics or fantasy

### 4. Build the structured source
Write a JSON file matching the renderer schema used by `scripts/render_one_page_gdd.py`.

Expected fields:
- `title`
- `identity_mantra`
- `design_pillars` (array)
- `summary`
- `features` (array)
- `interface`
- `art_style`
- `music_sound`
- `platform`
- `audience`
- `milestones` (array)
- `launch_day`

### 5. Render markdown and PDF
Use:

```bash
python scripts/render_one_page_gdd.py --input <json> --md <output.md> --pdf <output.pdf>
```

The renderer is optimized for one-page output. If the content is too long, shorten the copy before rerendering instead of letting the document bloat.

### 6. Check fit and trim aggressively
Before finalizing, verify:
- the concept is legible at a glance
- the features list is not overstuffed
- the PDF still feels like a one-pager
- the roadmap is realistic enough to be useful
- the strongest idea is visible immediately

If the PDF looks crowded, shorten the writing. Do not "solve" bad scoping with tiny unreadable text.

## Output expectations

By default, create files in the current working directory or a user-specified target folder:
- `<slug>.json`
- `<slug>.md`
- `<slug>.pdf`

Use a slug based on the game title when naming files.

## Response structure

When using this skill, report:
- where the markdown file was written
- where the PDF file was written
- any sections that had to be compressed heavily
- any major ambiguities or contradictions you preserved or surfaced

## References

Read these when useful:
- `references/source-notes.md` for the distilled source principles and section model
- `references/example-input.json` for renderer input shape

## Working principle

If a team cannot explain the game on one page, the design is probably not clear enough yet.

Use this skill to produce a one-pager people can actually read, discuss, and pass around.