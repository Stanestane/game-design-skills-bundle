# Search Patterns

## Goal

Turn an emotional canvas into image-search terms that reliably surface useful reference images.

## Lane types

Use a mix of these lanes:

1. **Atmosphere lane** - broad emotional environment
2. **Shape lane** - silhouettes, geometry, density, readability
3. **Palette lane** - color, contrast, lighting, glow, haze
4. **Texture lane** - material feel, polish, roughness, toy-like vs industrial
5. **Composition lane** - framing, scale, negative space, overhead pressure
6. **Mechanic-adjacent lane** - imagery that rhymes with the game loop without requiring exact matches
7. **UI/HUD lane** - arcade readability, score language, pickup emphasis
8. **Era/style lane** - retro, cabinet-era, 90s, vapor, toybox, etc.

## Query formula

Combine:

- subject or style anchor
- mood adjective
- visual constraint
- optional medium hint

Template:

`<subject/style> <mood> <visual constraint> <optional medium>`

Examples:

- `retro arcade platformer bright tension clean silhouettes`
- `falling blocks overhead pressure playful industrial shapes concept art`
- `collectible coin glow colorful dark background game art`
- `arcade hud score combo readable high contrast ui`
- `stacked geometry toy-like materials saturated edge light`

## Query heuristics

- Use emotional adjectives, not only nouns.
- Add readability constraints like `clean silhouettes`, `high contrast`, `minimal background`, `simple shapes`.
- Use `concept art`, `poster`, `key art`, `illustration`, `screenshot`, or `photography` depending on the kind of image you need.
- If results are too literal, shift toward atmosphere and materials.
- If results are too vague, add one mechanical anchor like `falling blocks`, `platformer`, `arcade`, or `pickup`.
- If results are too noisy, add `minimal`, `clean`, `limited palette`, or `graphic`.

## Image selection heuristics

Select images that contribute one of these jobs:

- define emotional tone
- define color and light
- define material and texture
- define spatial pressure
- define collectible/readability language
- define motion energy
- define palette relationships worth borrowing directly

Judge picks with actual taste, not keyword guilt. Ask:

- Would I still keep this if it were not topically related?
- Does it look deliberate, polished, and compositionally strong?
- Does it sharpen the board, or just increase image count?
- Does it help the prototype look more readable and more specific?

Reject images that are:

- tiny thumbnails
- near-duplicates of existing picks
- aesthetically strong but emotionally wrong
- visually muddy or over-detailed for the intended prototype
- generic article headers or stock filler
- only mechanically related, but visually weak

## Caption pattern

Keep manifest captions short:

- what this image contributes
- why it fits the feeling

Example:

- `Overhead threat with readable chunky geometry`
- `Bright collectible glow against subdued arena`
- `Arcade urgency without visual clutter`
