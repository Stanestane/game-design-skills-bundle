#!/usr/bin/env python3
import argparse, json, math, os, textwrap
from pathlib import Path
from PIL import Image, ImageOps, ImageDraw, ImageFont


def load_font(size):
    candidates = [
        'C:/Windows/Fonts/segoeui.ttf',
        'C:/Windows/Fonts/arial.ttf',
    ]
    for path in candidates:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except Exception:
                pass
    return ImageFont.load_default()


def fit_crop(img, target_w, target_h):
    return ImageOps.fit(img.convert('RGB'), (target_w, target_h), method=Image.Resampling.LANCZOS)


def parse_args():
    ap = argparse.ArgumentParser(description='Render moodboard JPG and HTML from manifest.json')
    ap.add_argument('--manifest', required=True)
    ap.add_argument('--title', default=None)
    ap.add_argument('--width', type=int, default=1920)
    ap.add_argument('--height', type=int, default=1080)
    ap.add_argument('--columns', type=int, default=4)
    ap.add_argument('--gutter', type=int, default=20)
    return ap.parse_args()


def rel_to_manifest(manifest_path, maybe_rel):
    p = Path(maybe_rel)
    if p.is_absolute():
        return p
    return Path(manifest_path).parent / p


def render_jpg(data, manifest_path, out_jpg, title, width, height, columns, gutter):
    bg = Image.new('RGB', (width, height), (18, 18, 20))
    draw = ImageDraw.Draw(bg)
    title_font = load_font(46)
    meta_font = load_font(24)
    caption_font = load_font(20)

    margin = 32
    header_h = 150
    footer_h = 24
    body_top = margin + header_h
    body_bottom = height - margin - footer_h
    body_h = body_bottom - body_top
    images = data.get('images', [])
    if not images:
        raise ValueError('manifest has no images')

    rows = math.ceil(len(images) / columns)
    cell_w = int((width - 2 * margin - (columns - 1) * gutter) / columns)
    cell_h = int((body_h - (rows - 1) * gutter) / rows)
    thumb_h = max(80, cell_h - 52)

    draw.text((margin, margin), title, fill=(245, 245, 245), font=title_font)
    feeling = data.get('target_feeling', '')
    desc = ', '.join(data.get('descriptors', [])[:4])
    meta = f"Target feeling: {feeling}" + (f"  |  {desc}" if desc else '')
    draw.text((margin, margin + 64), meta, fill=(190, 190, 190), font=meta_font)

    for i, item in enumerate(images):
        row = i // columns
        col = i % columns
        x = margin + col * (cell_w + gutter)
        y = body_top + row * (cell_h + gutter)
        img_path = rel_to_manifest(manifest_path, item['file'])
        try:
            im = Image.open(img_path)
            tile = fit_crop(im, cell_w, thumb_h)
        except Exception:
            tile = Image.new('RGB', (cell_w, thumb_h), (60, 40, 40))
            td = ImageDraw.Draw(tile)
            td.text((10, 10), 'missing', fill=(255, 255, 255), font=caption_font)
        bg.paste(tile, (x, y))
        lane = item.get('lane', '')
        caption = item.get('caption', '')
        if lane:
            draw.text((x, y + thumb_h + 6), lane, fill=(255, 216, 120), font=caption_font)
        wrapped = textwrap.fill(caption, width=max(18, int(cell_w / 16)))
        draw.multiline_text((x, y + thumb_h + 28), wrapped, fill=(220, 220, 220), font=caption_font, spacing=2)

    bg.save(out_jpg, quality=92)


def render_html(data, manifest_path, out_html, title):
    cards = []
    manifest_dir = Path(manifest_path).parent
    for item in data.get('images', []):
        img_file = item['file'].replace('\\', '/')
        page_url = item.get('page_url', '')
        source_url = item.get('source_url', '')
        lane = item.get('lane', '')
        caption = item.get('caption', '')
        links = []
        if page_url:
            links.append(f"<a href=\"{page_url}\" target=\"_blank\">page</a>")
        if source_url:
            links.append(f"<a href=\"{source_url}\" target=\"_blank\">image</a>")
        links_html = ' · '.join(links)
        cards.append(f"""
        <figure class='card'>
          <img src='{img_file}' loading='lazy'>
          <figcaption>
            <div class='lane'>{lane}</div>
            <div class='caption'>{caption}</div>
            <div class='links'>{links_html}</div>
          </figcaption>
        </figure>
        """)
    feeling = data.get('target_feeling', '')
    desc = ', '.join(data.get('descriptors', []))
    html = f"""<!doctype html>
<html>
<head>
<meta charset='utf-8'>
<meta name='viewport' content='width=device-width, initial-scale=1'>
<title>{title}</title>
<style>
body {{ font-family: Segoe UI, Arial, sans-serif; background:#111; color:#eee; margin:0; padding:24px; }}
h1 {{ margin:0 0 10px; }}
.meta {{ color:#bdbdbd; margin-bottom:24px; }}
.grid {{ display:grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap:18px; }}
.card {{ background:#1b1b1d; border:1px solid #2a2a2d; border-radius:14px; overflow:hidden; margin:0; }}
.card img {{ display:block; width:100%; height:260px; object-fit:cover; background:#222; }}
figcaption {{ padding:12px 14px 16px; }}
.lane {{ color:#ffd878; font-size:13px; text-transform:uppercase; letter-spacing:.08em; margin-bottom:8px; }}
.caption {{ font-size:15px; line-height:1.35; margin-bottom:10px; }}
.links a {{ color:#9ed0ff; text-decoration:none; margin-right:10px; }}
</style>
</head>
<body>
<h1>{title}</h1>
<div class='meta'><b>Target feeling:</b> {feeling}<br><b>Descriptors:</b> {desc}</div>
<div class='grid'>
{''.join(cards)}
</div>
</body>
</html>"""
    Path(out_html).write_text(html, encoding='utf-8')


def main():
    args = parse_args()
    manifest_path = Path(args.manifest)
    data = json.loads(manifest_path.read_text(encoding='utf-8'))
    title = args.title or data.get('title') or manifest_path.parent.name
    out_html = manifest_path.parent / 'moodboard.html'
    out_jpg = manifest_path.parent / 'moodboard.jpg'
    render_jpg(data, manifest_path, out_jpg, title, args.width, args.height, args.columns, args.gutter)
    render_html(data, manifest_path, out_html, title)
    print(json.dumps({
        'manifest': str(manifest_path),
        'html': str(out_html),
        'jpg': str(out_jpg),
        'images': len(data.get('images', []))
    }, indent=2))


if __name__ == '__main__':
    main()
