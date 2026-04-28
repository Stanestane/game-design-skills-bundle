#!/usr/bin/env python3
"""
render_one_page_gdd.py
Renders a one-page game design document to Markdown and a visually designed PDF.

Usage:
    python render_one_page_gdd.py --input game.json --md game.md --pdf game.pdf

Requires: reportlab  (pip install reportlab)
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path

# ── Colour palette ─────────────────────────────────────────────────────────
DARK_BG    = (15,  17,  26)
PANEL_BG   = (24,  27,  40)
ACCENT     = (0,  200, 160)
ACCENT_DIM = (0,  130, 105)
HEADING_FG = (0,  200, 160)
TITLE_FG   = (255, 255, 255)
BODY_FG    = (210, 215, 230)
TAG_BG     = (38,  46,  66)
DIVIDER    = (48,  56,  78)
FOOTER_FG  = (120, 130, 155)

# ── Font discovery ─────────────────────────────────────────────────────────
FONT_SEARCH_DIRS = [
    "/usr/share/fonts/truetype/google-fonts",
    "/usr/share/fonts/truetype/liberation",
    "/usr/share/fonts/truetype/dejavu",
    "C:/Windows/Fonts",
    os.path.expanduser("~/Library/Fonts"),
    "/Library/Fonts",
    "/System/Library/Fonts",
]
FONT_CANDIDATES = {
    "regular": ["Poppins-Regular.ttf", "LiberationSans-Regular.ttf", "DejaVuSans.ttf", "arial.ttf"],
    "bold":    ["Poppins-Bold.ttf",    "LiberationSans-Bold.ttf",    "DejaVuSans-Bold.ttf", "arialbd.ttf"],
    "light":   ["Poppins-Light.ttf",   "Poppins-Regular.ttf",        "LiberationSans-Regular.ttf", "arial.ttf"],
    "medium":  ["Poppins-Medium.ttf",  "Poppins-Bold.ttf",           "LiberationSans-Bold.ttf", "arialbd.ttf"],
}

def find_font(variant):
    for candidate in FONT_CANDIDATES[variant]:
        for d in FONT_SEARCH_DIRS:
            p = os.path.join(d, candidate)
            if os.path.exists(p):
                return p
    raise FileNotFoundError(
        f"No font found for variant '{variant}'. "
        "Install Poppins from fonts.google.com or Liberation Sans."
    )

def slugify(text):
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return re.sub(r"-+", "-", text).strip("-") or "one-page-gdd"

def rgb01(t):
    return tuple(c / 255.0 for c in t)

def load_json(path):
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    for k, v in {
        "title": "Untitled Game", "identity_mantra": "",
        "design_pillars": [], "summary": "", "features": [],
        "interface": "", "art_style": "", "music_sound": "",
        "platform": "", "audience": "", "milestones": [], "launch_day": "TBD",
    }.items():
        data.setdefault(k, v)
    return data

# ── Markdown ──────────────────────────────────────────────────────────────
def make_markdown(data):
    lines = [f"# {data['title']}", ""]
    lines += ["## Game Identity / Mantra", data["identity_mantra"], ""]
    lines += ["## Design Pillars"]
    for p in data["design_pillars"]:
        lines.append(f"- {p}")
    lines.append("")
    lines += ["## Genre / Story / Mechanics Summary", data["summary"], ""]
    lines += ["## Features"]
    for f in data["features"]:
        lines.append(f"- {f}")
    lines.append("")
    lines += ["## Interface", data["interface"], ""]
    lines += ["## Art Style", data["art_style"], ""]
    lines += ["## Music / Sound", data["music_sound"], ""]
    lines += ["## Development Roadmap / Launch Criteria"]
    lines.append(f"- Platform: {data['platform']}")
    lines.append(f"- Audience: {data['audience']}")
    for i, m in enumerate(data["milestones"], start=1):
        lines.append(f"- Milestone {i}: {m}")
    lines.append(f"- Launch Day: {data['launch_day']}")
    lines.append("")
    return "\n".join(lines)

# ── PDF ───────────────────────────────────────────────────────────────────
def render_pdf(data, pdf_path):
    try:
        from reportlab.pdfgen import canvas as rl_canvas
        from reportlab.lib.pagesizes import A4
        from reportlab.lib.units import mm
        from reportlab.pdfbase import pdfmetrics
        from reportlab.pdfbase.ttfonts import TTFont
    except ImportError:
        print("ERROR: reportlab required. Run: pip install reportlab", file=sys.stderr)
        sys.exit(1)

    pdfmetrics.registerFont(TTFont("GDD-Regular", find_font("regular")))
    pdfmetrics.registerFont(TTFont("GDD-Bold",    find_font("bold")))
    pdfmetrics.registerFont(TTFont("GDD-Light",   find_font("light")))
    pdfmetrics.registerFont(TTFont("GDD-Medium",  find_font("medium")))

    PAGE_W, PAGE_H = A4
    MX  = 22 * mm
    MB  = 16 * mm
    G   = 7 * mm
    HH  = 50 * mm

    c = rl_canvas.Canvas(str(pdf_path), pagesize=A4)

    # Background
    c.setFillColorRGB(*rgb01(DARK_BG))
    c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)

    # Header band
    c.setFillColorRGB(*rgb01(PANEL_BG))
    c.rect(0, PAGE_H - HH, PAGE_W, HH, fill=1, stroke=0)

    # Top accent stripe
    c.setFillColorRGB(*rgb01(ACCENT))
    c.rect(0, PAGE_H - 3 * mm, PAGE_W, 3 * mm, fill=1, stroke=0)

    # Left accent block in header
    c.setFillColorRGB(*rgb01(ACCENT))
    c.rect(0, PAGE_H - HH, 5 * mm, HH - 3 * mm, fill=1, stroke=0)

    # Title
    title_y = PAGE_H - HH + 24 * mm
    c.setFillColorRGB(*rgb01(TITLE_FG))
    c.setFont("GDD-Bold", 28)
    c.drawString(MX + 2 * mm, title_y, data["title"])

    # Mantra
    mantra = str(data.get("identity_mantra", "")).strip()
    if mantra:
        max_w = PAGE_W - 2 * MX
        c.setFont("GDD-Light", 9)
        while c.stringWidth(mantra, "GDD-Light", 9) > max_w and " " in mantra:
            mantra = mantra[:mantra.rfind(" ")] + "…"
        c.setFillColorRGB(*rgb01(BODY_FG))
        c.drawString(MX + 2 * mm, title_y - 9 * mm, mantra)

    # Pillar tags
    pillars = data.get("design_pillars", [])
    if pillars:
        tag_x = MX + 2 * mm
        tag_y = title_y - 20 * mm
        TAG_H = 5.5 * mm
        TAG_PX = 4.5 * mm
        TAG_R = 2.5 * mm
        c.setFont("GDD-Medium", 7)
        for p in pillars[:6]:
            label = str(p).upper()
            tw = c.stringWidth(label, "GDD-Medium", 7) + 2 * TAG_PX
            if tag_x + tw > PAGE_W - MX:
                break
            c.setFillColorRGB(*rgb01(TAG_BG))
            c.roundRect(tag_x, tag_y, tw, TAG_H, TAG_R, fill=1, stroke=0)
            c.setFillColorRGB(*rgb01(ACCENT))
            c.rect(tag_x, tag_y, 2 * mm, TAG_H, fill=1, stroke=0)
            c.roundRect(tag_x, tag_y, 2 * TAG_R, TAG_H, TAG_R, fill=1, stroke=0)
            c.setFillColorRGB(*rgb01(BODY_FG))
            c.drawString(tag_x + TAG_PX, tag_y + 1.7 * mm, label)
            tag_x += tw + 3 * mm

    # Body layout
    body_top = PAGE_H - HH - 4 * mm
    body_bot = MB + 8 * mm
    col_w    = (PAGE_W - 2 * MX - G) / 2
    left_x   = MX
    right_x  = MX + col_w + G

    # Column divider
    div_x = MX + col_w + G / 2
    c.setStrokeColorRGB(*rgb01(DIVIDER))
    c.setLineWidth(0.5)
    c.line(div_x, body_bot, div_x, body_top - 2 * mm)

    SL  = 7
    BS  = 8.5
    LHB = 4.5 * mm
    LHU = 4.3 * mm
    SG  = 6 * mm
    LG  = 2.8 * mm

    def _wrap(text, fname, fsize, max_w):
        words = str(text).split()
        if not words:
            return []
        result, cur = [], words[0]
        for w in words[1:]:
            trial = cur + " " + w
            if c.stringWidth(trial, fname, fsize) <= max_w:
                cur = trial
            else:
                result.append(cur)
                cur = w
        result.append(cur)
        return result

    def draw_section(heading, value, x, y, width):
        y -= SG
        c.setFillColorRGB(*rgb01(ACCENT))
        c.rect(x, y, width, 0.7 * mm, fill=1, stroke=0)
        y -= 4 * mm
        c.setFont("GDD-Medium", SL)
        c.setFillColorRGB(*rgb01(HEADING_FG))
        c.drawString(x, y, heading.upper())
        y -= LG
        c.setFillColorRGB(*rgb01(BODY_FG))
        if isinstance(value, list):
            for item in value:
                s = str(item).strip()
                if not s:
                    continue
                lines = _wrap(s, "GDD-Regular", BS, width - 5.5 * mm)
                first = True
                for line in lines:
                    y -= LHU
                    if first:
                        c.setFont("GDD-Medium", BS)
                        c.setFillColorRGB(*rgb01(ACCENT_DIM))
                        c.drawString(x, y, "›")
                        c.setFont("GDD-Regular", BS)
                        c.setFillColorRGB(*rgb01(BODY_FG))
                        c.drawString(x + 5 * mm, y, line)
                        first = False
                    else:
                        c.setFont("GDD-Regular", BS)
                        c.drawString(x + 5 * mm, y, line)
        else:
            text = str(value).strip()
            if text:
                lines = _wrap(text, "GDD-Regular", BS, width)
                c.setFont("GDD-Regular", BS)
                for line in lines:
                    y -= LHB
                    c.drawString(x, y, line)
        return y

    # Left column
    y_l = body_top
    y_l = draw_section("Genre / Story / Mechanics", data.get("summary", ""),   left_x, y_l, col_w)
    y_l = draw_section("Key Features",              data.get("features", []),  left_x, y_l, col_w)
    y_l = draw_section("Interface & Controls",      data.get("interface", ""), left_x, y_l, col_w)

    # Right column
    y_r = body_top
    y_r = draw_section("Art Style",     data.get("art_style",   ""), right_x, y_r, col_w)
    y_r = draw_section("Music & Sound", data.get("music_sound", ""), right_x, y_r, col_w)

    road = []
    if data.get("platform"):  road.append(f"Platform: {data['platform']}")
    if data.get("audience"):  road.append(f"Audience: {data['audience']}")
    for i, m in enumerate(data.get("milestones", []), start=1):
        road.append(f"M{i}: {m}")
    road.append(f"Launch: {data.get('launch_day', 'TBD')}")
    y_r = draw_section("Roadmap / Launch Criteria", road, right_x, y_r, col_w)

    # Footer
    c.setFillColorRGB(*rgb01(PANEL_BG))
    c.rect(0, 0, PAGE_W, MB + 4 * mm, fill=1, stroke=0)
    c.setFillColorRGB(*rgb01(ACCENT_DIM))
    c.rect(0, MB + 3.5 * mm, PAGE_W, 0.4 * mm, fill=1, stroke=0)
    c.setFont("GDD-Light", 6.5)
    c.setFillColorRGB(*rgb01(HEADING_FG))
    c.drawString(MX, MB, "ONE-PAGE GAME DESIGN DOCUMENT")
    c.setFillColorRGB(*rgb01(FOOTER_FG))
    c.drawRightString(PAGE_W - MX, MB, data["title"].upper())

    c.save()

# ── CLI ───────────────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(description="Render one-page GDD to Markdown and PDF")
    parser.add_argument("--input", required=True)
    parser.add_argument("--md")
    parser.add_argument("--pdf")
    args = parser.parse_args()

    data = load_json(Path(args.input))

    if args.md:
        Path(args.md).write_text(make_markdown(data), encoding="utf-8")
        print(f"Markdown → {args.md}")

    if args.pdf:
        render_pdf(data, Path(args.pdf))
        print(f"PDF → {args.pdf}")

    print(json.dumps({
        "input": args.input, "markdown": args.md, "pdf": args.pdf,
        "slug": slugify(data.get("title", "one-page-gdd")),
    }, ensure_ascii=False))

if __name__ == "__main__":
    main()
