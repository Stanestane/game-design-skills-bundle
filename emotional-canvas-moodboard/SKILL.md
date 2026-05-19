---
name: emotional-canvas-moodboard
description: Turn a game-design emotional canvas into a curated visual moodboard by deriving image-search queries, gathering a candidate pool from the internet, saving the files locally, rejecting weak references, and rendering both an HTML board and a flattened JPG board. Use when a user wants a moodboard from an emotional canvas, wants visual references for a game concept, or wants a reusable workflow that turns emotional direction into search terms, downloaded image files, and a tastefully curated presentation-ready board.
---

# Emotional Canvas Moodboard

Translate a game's emotional direction into a concrete visual board.

Use this skill after `game-design-emotional-canvas` or whenever the user already has enough emotional direction to describe the intended feeling, adjacent feelings, visual tone, no-go elements, and reference-seeking targets.

## What to produce

Produce these artifacts unless the user asks for a smaller output:

1. A short emotional-canvas summary for the current concept
2. A search-plan list with focused image queries
3. A candidate pool of downloaded source images
4. A machine-readable `manifest.json` describing the curated board
5. A rendered `moodboard.html`
6. A rendered flattened `moodboard.jpg`
7. A short curation note explaining strong keeps and weak rejects

## Core rule

This skill is for reference gathering and board assembly.

Do not spend the whole turn writing abstract creative prose. Move quickly from emotional interpretation to query generation, candidate gathering, hard rejection, and board rendering.

A moodboard is curation, not accumulation. If the result looks like a pile of search results, the skill has failed.

## Workflow

### 1. Build or normalize the emotional canvas

If the user already supplied an emotional canvas, normalize it into this shape:

- Target feeling
- Three defining descriptors
- Adjacent feelings
- Contrasting feelings
- Visual references to seek
- Audio references to seek
- Narrative tone
- No-go elements

If the user only supplied a concept, create a compact emotional canvas first using the structure from `game-design-emotional-canvas`.

Keep it brief. The goal is to drive search quality, not to create a long essay.

### 2. Convert the canvas into image-search lanes

Create 6-12 focused search lanes. Each lane should represent one useful visual dimension, for example:

- shape language
- color and lighting
- environment mood
- texture and material feel
- composition and camera distance
- interface or arcade reference style
- character energy or motion language
- period/style anchors

For each lane, write 2-5 search phrases.

Good query pattern:
- `[subject/style] + [mood adjective] + [visual constraint]`

Examples:
- `arcade platformer mockup tense neon minimal background`
- `falling concrete blocks overhead cinematic top light`
- `retro industrial geometry oppressive playful contrast`
- `coins glowing on stacked blocks game art`

### 3. Gather a candidate pool, not a final board

Use web search and normal web access to find suitable visual references.

Prefer strong anchor sources over generic search sludge:
- official game store screenshots
- official key art
- ArtStation / Behance project images
- strong editorial or portfolio images

Avoid using random article headers, generic stock results, empty category pages, or filler photography unless they are genuinely the best aesthetic match.

Save source URLs in the manifest even when the file is downloaded locally.

Do not filter the collection by copyright status in this skill. The purpose here is fast local reference gathering. Copyright review can happen later in a separate workflow.

Build a candidate pool first:
- 16-40 candidates is normal
- mix broad atmosphere references with direct mechanic-adjacent references
- aggressively reject near-duplicates
- reject low-resolution thumbnails when a larger source is reachable

Quality bar for candidates:
- favor strong mood fit over literal mechanic fit
- favor visual authority over weak topical similarity
- prefer sources with clean composition and deliberate art direction

### 4. Curate brutally before rendering

Before rendering, judge each candidate on:
- aesthetic quality
- emotional fit
- readability / silhouette clarity
- color language
- geometric or material relevance
- uniqueness within the set

Then cut hard.

Final-board rule:
- default final board size is 6-12 images
- every image must earn its place
- each image should contribute a distinct job: atmosphere, shape language, color, space, movement, HUD/readability, collectible/reward language, material finish, or palette reference
- reject anything that is merely "related"
- prefer one strong image per anchor source/title over multiple samey screenshots unless a sequence is the point
- when the user wants a cleaner board, bias toward stronger composition and palette images even if they are less explanatory

Write down at least:
- why the strongest 3-5 images were kept
- why several weak candidates were rejected
- what unique job each kept image is doing in the board

### 5. Save files into a dedicated board folder

Use a folder like:

`output/moodboards/<slug>/`

Recommended layout:

- `downloads/` for local image files
- `manifest.json` for curated-board metadata
- `moodboard.html`
- `moodboard.jpg`
- optional `candidate_manifest.json`
- optional `curation-notes.md`

The manifest should contain:

```json
{
  "title": "...",
  "concept": "...",
  "target_feeling": "...",
  "descriptors": ["..."],
  "lanes": [
    {"name": "...", "queries": ["..."]}
  ],
  "images": [
    {
      "file": "downloads/01.jpg",
      "source_url": "https://...",
      "page_url": "https://...",
      "caption": "...",
      "lane": "..."
    }
  ]
}
```

### 6. Render the moodboard

Use `scripts/download_urls.py` when you already have a curated list of image URLs and want local files quickly.

Then use `scripts/render_moodboard.py` to turn the manifest into:

- a tiled JPG board for quick viewing and sharing
- an HTML board that preserves captions and source links

Prefer 16:9 output unless the user asks for another aspect.

### 7. Report like a creative handoff

Return:
- the distilled target feeling
- the 3-5 strongest mood signals in the board
- any obvious gap in the gathered references
- file locations for the HTML and JPG outputs
- a short keep/reject summary that proves curation happened

If helpful, split the result into two smaller companion boards instead of one mixed board:
- **Aesthetic / vibe board** for color, tone, material, and atmosphere
- **Mechanic / readability board** for space, movement, hazard clarity, HUD, and score language

## Using the bundled script

Download URLs into a board folder:

```bash
python scripts/download_urls.py --input <url-list.json> --output-dir <board-folder>/downloads --prefix ref
```

Render the board:

```bash
python scripts/render_moodboard.py --manifest <path-to-manifest.json> --title "Board Title"
```

Optional:

```bash
python scripts/render_moodboard.py --manifest <path> --width 1920 --height 1080 --columns 4
```

## Sample concept seed

For the concept:

> For a long time I had this idea for a mashup of Tetris and a platformer game. Instead of falling blocks, the player would control a character trying to dodge the falling blocks and survive as long as possible while blocks fall faster and faster. The player can collect points by grabbing coins that spawn randomly on blocks that have already landed. Just for fun I would add a bunch of arcade-inspired powerups. I am working alone and want to make a simple playable prototype of this game in Unity.

A good first emotional read is:

- Target feeling: **cheerful pressure**
- Defining descriptors: **arcade urgency**, **playful danger**, **toy-like physicality**
- Adjacent feelings: **nimble improvisation**, **score-chasing greed**, **bright chaos**
- Contrasting feelings to avoid: **grim dread**, **mil-sim harshness**, **muddy visual noise**, **slow ponderous puzzle solemnity**
- Visual references to seek: **chunky falling geometry**, **clean readable silhouettes**, **bright collectible highlights**, **compact arenas**, **retro arcade energy**, **escalating overhead threat**
- Narrative tone: **light, kinetic, and mischievous rather than epic**
- No-go elements: **photoreal gore**, **brown-grey sludge palettes**, **ultra-busy UI**, **realistic debris clutter**

Use that sample as a pattern, not a limit.

## Reference files

Read these only when useful:

- `references/search-patterns.md` for query design and image-lane ideas
- `references/sample-emotional-canvas.md` for a worked example based on the sample game concept

## Working principle

A good moodboard is not a pile of cool pictures. It is a visual argument for the feeling the prototype should deliver.
ment for the feeling the prototype should deliver.
ling the prototype should deliver.
.md` for a worked example based on the sample game concept

## Working principle

A good moodboard is not a pile of cool pictures. It is a visual argument for the feeling the prototype should deliver.
