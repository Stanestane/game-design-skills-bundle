#!/usr/bin/env python3
import argparse, json, mimetypes, os, sys
from pathlib import Path
from urllib.parse import urlparse
from urllib.request import Request, urlopen


def guess_ext(url, content_type, fallback='.jpg'):
    path = urlparse(url).path
    ext = Path(path).suffix.lower()
    if ext in {'.jpg', '.jpeg', '.png', '.webp', '.gif', '.bmp'}:
        return ext
    if content_type:
        guessed = mimetypes.guess_extension(content_type.split(';')[0].strip())
        if guessed:
            if guessed == '.jpe':
                return '.jpg'
            return guessed
    return fallback


def main():
    ap = argparse.ArgumentParser(description='Download image URLs listed in a JSON file')
    ap.add_argument('--input', required=True, help='JSON file containing an array of objects with url or source_url')
    ap.add_argument('--output-dir', required=True)
    ap.add_argument('--prefix', default='img')
    args = ap.parse_args()

    items = json.loads(Path(args.input).read_text(encoding='utf-8'))
    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    saved = []

    for idx, item in enumerate(items, start=1):
        url = item.get('url') or item.get('source_url')
        if not url:
            continue
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urlopen(req, timeout=30) as r:
            content_type = r.headers.get('Content-Type', '')
            data = r.read()
        ext = guess_ext(url, content_type)
        name = f"{args.prefix}-{idx:02d}{ext}"
        out_path = out_dir / name
        out_path.write_bytes(data)
        saved.append({'url': url, 'file': str(out_path)})

    print(json.dumps({'downloaded': len(saved), 'files': saved}, indent=2))


if __name__ == '__main__':
    main()
