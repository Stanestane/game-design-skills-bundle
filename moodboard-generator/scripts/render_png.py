#!/usr/bin/env python3
"""
Render a moodboard HTML file to a flattened PNG.

Usage:
    python render_png.py board.html board.png [--width 1600]

Tries, in order:
  1. playwright (headless Chromium) — best quality, handles web fonts + lazy images
  2. wkhtmltoimage CLI, if installed on the system

If neither is available (common in network-restricted sandboxes — Playwright needs to
download a browser binary, which may be blocked), exits with a clear message. In that
case, ship the HTML as the deliverable and tell the user PNG export needs to happen from
an environment with fuller internet access, or by opening the HTML file in a browser and
using the browser's own screenshot / "Save as image" capability.
"""
import subprocess
import sys
import shutil


def try_playwright(html_path: str, png_path: str, width: int) -> bool:
    try:
        from playwright.sync_api import sync_playwright  # noqa
    except ImportError:
        try:
            subprocess.run(
                [sys.executable, "-m", "pip", "install", "--break-system-packages", "-q", "playwright"],
                check=True, timeout=120,
            )
            subprocess.run([sys.executable, "-m", "playwright", "install", "chromium"],
                            check=True, timeout=300)
            from playwright.sync_api import sync_playwright  # noqa
        except Exception as e:
            print(f"[render_png] playwright unavailable: {e}", file=sys.stderr)
            return False

    from playwright.sync_api import sync_playwright
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page(viewport={"width": width, "height": 1000})
            page.goto(f"file://{html_path}")
            page.wait_for_load_state("networkidle", timeout=15000)
            page.screenshot(path=png_path, full_page=True)
            browser.close()
        return True
    except Exception as e:
        print(f"[render_png] playwright render failed: {e}", file=sys.stderr)
        return False


def try_wkhtmltoimage(html_path: str, png_path: str, width: int) -> bool:
    if not shutil.which("wkhtmltoimage"):
        return False
    try:
        subprocess.run(
            ["wkhtmltoimage", "--width", str(width), html_path, png_path],
            check=True, timeout=120,
        )
        return True
    except Exception as e:
        print(f"[render_png] wkhtmltoimage failed: {e}", file=sys.stderr)
        return False


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python render_png.py board.html board.png [--width 1600]", file=sys.stderr)
        sys.exit(1)
    html_path, png_path = sys.argv[1], sys.argv[2]
    width = 1600
    if "--width" in sys.argv:
        width = int(sys.argv[sys.argv.index("--width") + 1])

    import os
    html_abs = os.path.abspath(html_path)

    if try_playwright(html_abs, png_path, width) or try_wkhtmltoimage(html_abs, png_path, width):
        print(f"Wrote {png_path}")
        sys.exit(0)

    print(
        "PNG export not possible in this environment (no headless browser available, "
        "likely due to network restrictions). Deliver the HTML file instead — it renders "
        "the full moodboard — and note that PNG export needs an environment with fuller "
        "internet access, or the user can open the HTML and export/screenshot it manually.",
        file=sys.stderr,
    )
    sys.exit(2)
