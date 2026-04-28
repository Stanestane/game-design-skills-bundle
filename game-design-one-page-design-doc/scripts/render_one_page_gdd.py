#!/usr/bin/env python3
import argparse
import json
import math
import os
import re
import textwrap
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

PAGE_W = 1654  # ~A4 at 150dpi
PAGE_H = 2339
MARGIN = 80
GUTTER = 40
BG = "white"
FG = "black"
ACCENT = (45, 45, 45)
FONT_REG = r"C:\Windows\Fonts\arial.ttf"
FONT_BOLD = r"C:\Windows\Fonts\arialbd.ttf"

LEFT_SECTIONS = [
    ("Game Identity / Mantra", "identity_mantra"),
    ("Design Pillars", "design_pillars"),
    ("Genre / Story / Mechanics Summary", "summary"),
    ("Features", "features"),
]
RIGHT_SECTIONS = [
    ("Interface", "interface"),
    ("Art Style", "art_style"),
    ("Music / Sound", "music_sound"),
    ("Development Roadmap / Launch Criteria", "roadmap"),
]


def slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return re.sub(r"-+", "-", text).strip("-") or "one-page-gdd"


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    data.setdefault("title", "Untitled Game")
    data.setdefault("identity_mantra", "")
    data.setdefault("design_pillars", [])
    data.setdefault("summary", "")
    data.setdefault("features", [])
    data.setdefault("interface", "")
    data.setdefault("art_style", "")
    data.setdefault("music_sound", "")
    data.setdefault("platform", "")
    data.setdefault("audience", "")
    data.setdefault("milestones", [])
    data.setdefault("launch_day", "TBD")
    return data


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


def font(path, size):
    return ImageFont.truetype(path, size=size)


def wrap_text(draw, text, fnt, width):
    if not text:
        return []
    words = str(text).split()
    lines = []
    current = words[0]
    for word in words[1:]:
        trial = current + " " + word
        if draw.textbbox((0, 0), trial, font=fnt)[2] <= width:
            current = trial
        else:
            lines.append(current)
            current = word
    lines.append(current)
    return lines


def section_lines(draw, heading, value, heading_font, body_font, width):
    out = [("heading", heading)]
    if isinstance(value, list):
        for item in value:
            wrapped = wrap_text(draw, f"• {item}", body_font, width)
            out.extend(("body", line) for line in wrapped)
    else:
        for para in str(value).split("\n"):
            para = para.strip()
            if not para:
                continue
            wrapped = wrap_text(draw, para, body_font, width)
            out.extend(("body", line) for line in wrapped)
    out.append(("spacer", ""))
    return out


def roadmap_value(data):
    lines = []
    if data.get("platform"):
        lines.append(f"Platform: {data['platform']}")
    if data.get("audience"):
        lines.append(f"Audience: {data['audience']}")
    for i, m in enumerate(data.get("milestones", []), start=1):
        lines.append(f"Milestone {i}: {m}")
    lines.append(f"Launch Day: {data.get('launch_day', 'TBD')}")
    return lines


def build_columns(draw, data, heading_font, body_font, col_w):
    left = []
    for heading, key in LEFT_SECTIONS:
        left.extend(section_lines(draw, heading, data.get(key, ""), heading_font, body_font, col_w))
    right = []
    for heading, key in RIGHT_SECTIONS:
        value = roadmap_value(data) if key == "roadmap" else data.get(key, "")
        right.extend(section_lines(draw, heading, value, heading_font, body_font, col_w))
    return left, right


def line_height(draw, fnt):
    b = draw.textbbox((0, 0), "Ag", font=fnt)
    return b[3] - b[1]


def fits(draw, data, title_font, heading_font, body_font):
    col_w = (PAGE_W - 2 * MARGIN - GUTTER) // 2
    left_x = MARGIN
    right_x = MARGIN + col_w + GUTTER
    y_start = MARGIN + 80

    title_h = draw.textbbox((0, 0), data["title"], font=title_font)[3]
    y_start += title_h + 35

    left, right = build_columns(draw, data, heading_font, body_font, col_w)
    h_h = line_height(draw, heading_font) + 8
    b_h = line_height(draw, body_font) + 6

    def calc_height(lines):
        y = y_start
        for kind, _ in lines:
            if kind == "heading":
                y += h_h + 6
            elif kind == "body":
                y += b_h
            else:
                y += 16
        return y

    return max(calc_height(left), calc_height(right)) <= PAGE_H - MARGIN


def render_pdf(data, pdf_path: Path):
    img = Image.new("RGB", (PAGE_W, PAGE_H), BG)
    draw = ImageDraw.Draw(img)

    font_sizes = [34, 31, 29, 27, 25, 23, 21, 19, 17]
    chosen = None
    for body_size in font_sizes:
        title_font = font(FONT_BOLD, body_size + 18)
        heading_font = font(FONT_BOLD, body_size + 4)
        body_font = font(FONT_REG, body_size)
        if fits(draw, data, title_font, heading_font, body_font):
            chosen = (title_font, heading_font, body_font)
            break
    if chosen is None:
        title_font = font(FONT_BOLD, 30)
        heading_font = font(FONT_BOLD, 18)
        body_font = font(FONT_REG, 16)
        chosen = (title_font, heading_font, body_font)

    title_font, heading_font, body_font = chosen
    col_w = (PAGE_W - 2 * MARGIN - GUTTER) // 2
    left_x = MARGIN
    right_x = MARGIN + col_w + GUTTER

    y = MARGIN
    draw.text((MARGIN, y), data["title"], fill=FG, font=title_font)
    y += draw.textbbox((0, 0), data["title"], font=title_font)[3] + 10
    draw.line((MARGIN, y, PAGE_W - MARGIN, y), fill=ACCENT, width=3)
    y += 25

    left, right = build_columns(draw, data, heading_font, body_font, col_w)
    h_h = line_height(draw, heading_font) + 8
    b_h = line_height(draw, body_font) + 6

    def draw_lines(lines, x, start_y):
        y2 = start_y
        for kind, text in lines:
            if kind == "heading":
                draw.text((x, y2), text, fill=FG, font=heading_font)
                y2 += h_h + 6
            elif kind == "body":
                draw.text((x, y2), text, fill=FG, font=body_font)
                y2 += b_h
            else:
                y2 += 16
        return y2

    draw_lines(left, left_x, y)
    draw_lines(right, right_x, y)

    img.save(str(pdf_path), "PDF", resolution=150.0)


def main():
    parser = argparse.ArgumentParser(description="Render one-page game design doc to markdown and PDF")
    parser.add_argument("--input", required=True, help="Path to input JSON")
    parser.add_argument("--md", help="Path to output markdown")
    parser.add_argument("--pdf", help="Path to output PDF")
    args = parser.parse_args()

    in_path = Path(args.input)
    data = load_json(in_path)

    if args.md:
        md_path = Path(args.md)
        md_path.write_text(make_markdown(data), encoding="utf-8")
    if args.pdf:
        pdf_path = Path(args.pdf)
        render_pdf(data, pdf_path)

    print(json.dumps({
        "input": str(in_path),
        "markdown": str(args.md) if args.md else None,
        "pdf": str(args.pdf) if args.pdf else None,
        "slug": slugify(data.get("title", "one-page-gdd"))
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
