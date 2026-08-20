#!/usr/bin/env python3
"""
Build a self-contained HTML moodboard from curated image + palette data.

Usage:
    python build_html_moodboard.py board.json output.html

Input JSON schema:
{
  "title": "Coastal Modernism",
  "subtitle": "sun-bleached concrete, salt air, mid-century calm",   // optional
  "font_style": "serif" | "sans" | "script" | "condensed",           // optional, default "sans"
  "palette": [
    {"hex": "#d8cfc0", "name": "Sand"},
    {"hex": "#3c5a63", "name": "Deep Teal"}
  ],
  "images": [
    {
      "url": "https://...",
      "alt": "short description",
      "size": "hero" | "wide" | "tall" | "normal" | "small"
    }
  ]
}

No on-image source links or credit labels are rendered -- keep the board clean.

Layout: a small deterministic JS masonry engine, not CSS Grid or CSS columns.
Both of those looked appealing for mixed tile sizes but have real failure modes:
Grid's `auto-flow: dense` can leave unfillable gaps for certain span-size mixes,
and CSS multi-column's automatic height-balancing (needed to make `column-span: all`
hero banners work) has known browser inconsistencies that can make content vanish
below the calculated column height instead of just reflowing.

Instead, every tile gets an explicit `data-aspect` (width/height) computed from its
`size` role. On load, a short inline script measures the container width, picks a
column count for the viewport, and places each tile into whichever column is
currently shortest -- classic "masonry" bin-packing, done explicitly rather than
left to a browser heuristic. The container height is then set from the actual
computed layout, so nothing can end up outside it. This also means layout doesn't
need to wait for images to finish loading, since height is derived from the
aspect ratio, not the image's natural size.
"""
import json
import sys
import html

FONT_MAP = {
    "serif":     {"display": "Playfair Display", "weight": "600", "body": "Inter"},
    "sans":      {"display": "Space Grotesk",     "weight": "500", "body": "Inter"},
    "script":    {"display": "Caveat",            "weight": "600", "body": "Inter"},
    "condensed": {"display": "Bebas Neue",         "weight": "400", "body": "Inter"},
}

# aspect ratio (width / height) as a float, applied per role, for every image except "hero"
SIZE_ASPECT = {
    "wide":   4 / 3,
    "tall":   3 / 4,
    "normal": 1.0,
    "small":  16 / 9,
}
HERO_ASPECT = 4 / 3


def build(board: dict) -> str:
    title = html.escape(board.get("title", "Moodboard"))
    subtitle = html.escape(board.get("subtitle", ""))
    font_style = board.get("font_style", "sans")
    fonts = FONT_MAP.get(font_style, FONT_MAP["sans"])
    palette = board.get("palette", [])
    images = board.get("images", [])

    google_fonts = (
        f"{fonts['display'].replace(' ', '+')}:wght@{fonts['weight']}"
        f"&family={fonts['body'].replace(' ', '+')}:wght@400;500"
    )

    hero_html = ""
    masonry_tiles = []
    for img in images:
        size = img.get("size", "normal")
        alt = html.escape(img.get("alt", ""))
        url = html.escape(img.get("url", ""), quote=True)

        if size == "hero" and not hero_html:
            hero_html = f'''
        <figure class="tile hero" data-aspect="{HERO_ASPECT}">
          <img src="{url}" alt="{alt}" loading="eager" />
        </figure>'''
            continue

        aspect = SIZE_ASPECT.get(size, SIZE_ASPECT["normal"])
        masonry_tiles.append(f'''
        <figure class="tile" data-aspect="{aspect}">
          <img src="{url}" alt="{alt}" loading="eager" />
        </figure>''')

    swatches = []
    for c in palette:
        hexv = html.escape(c.get("hex", "#cccccc"))
        name = html.escape(c.get("name", ""))
        swatches.append(f'''
          <div class="swatch">
            <div class="swatch-color" style="background:{hexv};"></div>
            <div class="swatch-label">{name}<br><span class="hex">{hexv}</span></div>
          </div>''')

    palette_block = ""
    if swatches:
        palette_block = f'''
    <div class="palette-strip">
      <div class="palette-row">{"".join(swatches)}</div>
    </div>'''

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<title>{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family={google_fonts}&display=swap" rel="stylesheet">
<style>
  :root {{
    --gap: 14px;
    --radius: 6px;
    --bg: #f7f5f1;
    --ink: #1a1a1a;
  }}
  * {{ box-sizing: border-box; }}
  body {{
    margin: 0;
    padding: 48px 5vw 64px;
    background: var(--bg);
    color: var(--ink);
    font-family: '{fonts['body']}', sans-serif;
  }}
  header {{
    max-width: 900px;
    margin: 0 0 32px;
  }}
  h1 {{
    font-family: '{fonts['display']}', serif;
    font-weight: {fonts['weight']};
    font-size: clamp(2.2rem, 5vw, 3.4rem);
    margin: 0 0 8px;
    letter-spacing: 0.01em;
  }}
  .subtitle {{
    color: #555;
    letter-spacing: 0.02em;
    text-transform: uppercase;
    font-size: 0.85rem;
  }}
  .palette-strip {{
    background: #fff;
    display: flex;
    align-items: center;
    padding: 16px 20px;
    border-radius: var(--radius);
    margin-bottom: var(--gap);
  }}
  .palette-row {{
    display: flex;
    gap: 20px;
    width: 100%;
    flex-wrap: wrap;
  }}
  .swatch {{
    display: flex;
    align-items: center;
    gap: 10px;
  }}
  .swatch-color {{
    width: 34px;
    height: 34px;
    border-radius: 50%;
    box-shadow: inset 0 0 0 1px rgba(0,0,0,0.08);
    flex-shrink: 0;
  }}
  .swatch-label {{
    font-size: 0.75rem;
    line-height: 1.2;
    color: #333;
  }}
  .hex {{
    color: #999;
    font-variant-numeric: tabular-nums;
  }}
  .tile {{
    margin: 0;
    position: absolute;
    overflow: hidden;
    border-radius: var(--radius);
    background: #e5e1d8;
    top: 0;
    left: 0;
  }}
  .tile img {{
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
  }}
  .tile.hero {{
    /* still absolutely positioned like other tiles -- JS gives it a 2-column
       span instead of the full board width, so it stays a strong focal point
       without dominating the whole top of the board */
  }}
  .masonry {{
    position: relative;
  }}
  /* Fallback stacking if JS doesn't run: plain single-column flow, nothing hidden */
  .no-js .masonry .tile {{
    position: relative;
    width: 100% !important;
    height: auto !important;
    margin-bottom: var(--gap);
  }}
  .no-js .masonry .tile img {{
    height: auto;
  }}
</style>
</head>
<body class="no-js">
  <header>
    <h1>{title}</h1>
    {f'<div class="subtitle">{subtitle}</div>' if subtitle else ''}
  </header>
  {palette_block}
  <div class="masonry" id="masonry">
    {hero_html}
    {"".join(masonry_tiles)}
  </div>
<script>
(function() {{
  document.body.classList.remove('no-js');
  var container = document.getElementById('masonry');

  function columnsForWidth(w) {{
    if (w <= 600) return 2;
    if (w <= 900) return 3;
    return 4;
  }}

  function layout() {{
    var containerWidth = container.clientWidth;
    var gap = 14;
    var hero = container.querySelector('.tile.hero');
    var tiles = Array.prototype.slice.call(container.querySelectorAll('.tile:not(.hero)'));

    var cols = columnsForWidth(containerWidth);
    var colWidth = (containerWidth - gap * (cols - 1)) / cols;
    var colHeights = new Array(cols).fill(0);

    if (hero) {{
      // Hero spans 2 columns (or all of them, on a 2-column mobile layout) so it
      // reads as the clear focal point without taking over the whole board width.
      var heroSpan = Math.min(2, cols);
      var heroWidth = colWidth * heroSpan + gap * (heroSpan - 1);
      var heroAspect = parseFloat(hero.dataset.aspect) || (4 / 3);
      var heroHeight = heroWidth / heroAspect;
      hero.style.width = heroWidth + 'px';
      hero.style.height = heroHeight + 'px';
      hero.style.transform = 'translate(0px, 0px)';
      for (var h = 0; h < heroSpan; h++) {{
        colHeights[h] = heroHeight + gap;
      }}
    }}

    tiles.forEach(function(tile) {{
      var aspect = parseFloat(tile.dataset.aspect) || 1;
      var tileH = colWidth / aspect;
      var minCol = 0;
      for (var i = 1; i < cols; i++) {{
        if (colHeights[i] < colHeights[minCol]) minCol = i;
      }}
      var x = minCol * (colWidth + gap);
      var y = colHeights[minCol];
      tile.style.width = colWidth + 'px';
      tile.style.height = tileH + 'px';
      tile.style.transform = 'translate(' + x + 'px, ' + y + 'px)';
      colHeights[minCol] = y + tileH + gap;
    }});

    var maxHeight = Math.max.apply(null, colHeights);
    container.style.height = (maxHeight - gap) + 'px';
  }}

  layout();
  window.addEventListener('resize', function() {{
    clearTimeout(window.__moodboardResizeT);
    window.__moodboardResizeT = setTimeout(layout, 120);
  }});
}})();
</script>
</body>
</html>'''


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python build_html_moodboard.py board.json output.html", file=sys.stderr)
        sys.exit(1)
    with open(sys.argv[1], "r", encoding="utf-8") as f:
        board_data = json.load(f)
    out_html = build(board_data)
    with open(sys.argv[2], "w", encoding="utf-8") as f:
        f.write(out_html)
    print(f"Wrote {sys.argv[2]}")
