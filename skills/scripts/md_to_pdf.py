#!/usr/bin/env python3
"""Markdown → PDF for Notes vault (WeasyPrint). Usage: md_to_pdf.py IN.md -o OUT.pdf"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import markdown
import re
import shutil
import subprocess

try:
    from weasyprint import HTML
except OSError:  # no GTK runtime on Windows: fall back to Edge headless
    HTML = None

CSS = """
@page { margin: 1.5cm; size: A4; }
body { font-family: DejaVu Sans, sans-serif; font-size: 10.5pt; line-height: 1.35; color: #111; }
h1 { font-size: 16pt; border-bottom: 1px solid #333; padding-bottom: 0.3em; }
h2 { font-size: 13pt; margin-top: 1.2em; }
h3 { font-size: 11.5pt; }
code, pre { font-family: DejaVu Sans Mono, monospace; font-size: 9pt; }
pre { background: #f4f4f4; padding: 0.6em; overflow-wrap: break-word; white-space: pre-wrap; }
table { border-collapse: collapse; width: 100%; margin: 0.8em 0; font-size: 9.5pt; }
th, td { border: 1px solid #ccc; padding: 0.35em 0.45em; vertical-align: top; }
th { background: #eee; }
a { color: #0645ad; }
"""


def build_html(md_path: Path) -> str:
    body = markdown.markdown(
        md_path.read_text(encoding="utf-8"),
        extensions=["tables", "fenced_code", "nl2br"],
    )
    parts = re.split(r"(<pre>.*?</pre>|<code>.*?</code>|<svg.*?</svg>)", body, flags=re.S)
    link = re.compile(r'(?<![">=])(https?://[^\s<)]+)')
    body = "".join(
        part if i % 2 else link.sub(r'<a href="\1">\1</a>', part)
        for i, part in enumerate(parts)
    )
    return (
        "<!DOCTYPE html><html><head><meta charset='utf-8'>"
        f"<style>{CSS}</style></head><body>{body}</body></html>"
    )


def find_edge() -> str | None:
    for name in ("msedge", "chrome"):
        found = shutil.which(name)
        if found:
            return found
    for path in (
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    ):
        if Path(path).exists():
            return path
    return None


def convert(md_path: Path, pdf_path: Path, html_path: Path | None = None) -> int:
    html = build_html(md_path)
    html_path = html_path or pdf_path.with_suffix(".html")
    html_path.parent.mkdir(parents=True, exist_ok=True)
    html_path.write_text(html, encoding="utf-8")
    pdf_path.parent.mkdir(parents=True, exist_ok=True)
    if HTML is not None:
        document = HTML(string=html, base_url=str(md_path.resolve().parent)).render()
        document.write_pdf(str(pdf_path))
        return len(document.pages)
    edge = find_edge()
    if not edge:
        print("no PDF engine found; HTML written only", file=sys.stderr)
        return 0
    subprocess.run(
        [edge, "--headless", "--disable-gpu", "--no-pdf-header-footer",
         f"--print-to-pdf={pdf_path.resolve()}", html_path.resolve().as_uri()],
        check=True, capture_output=True, timeout=120,
    )
    return len(re.findall(rb"/Type\s*/Page[^s]", pdf_path.read_bytes()))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("input")
    ap.add_argument("-o", "--output", required=True)
    ap.add_argument("--html", default=None, help="also write the HTML page")
    args = ap.parse_args()
    md_path = Path(args.input)
    pdf_path = Path(args.output)
    html_path = Path(args.html) if args.html else None
    if not md_path.is_file():
        print(f"missing: {md_path}", file=sys.stderr)
        return 1
    pages = convert(md_path, pdf_path, html_path)
    print(pdf_path)
    print(f"pages: {pages}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
