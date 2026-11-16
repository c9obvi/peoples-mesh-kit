#!/usr/bin/env python3
"""Render the guide + handouts to self-contained HTML for printing to PDF.

Used by scripts/build_pdf.sh. Needs the `markdown` package (the shell script
installs it into .build/venv).
"""
import base64
import os
import re
import sys

import markdown

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
REPO_URL = "https://github.com/c9obvi/peoples-mesh-kit/blob/main/"

CSS = """
@page { size: Letter; margin: 0.6in 0.6in 0.7in; }
body { font: 10.5pt/1.45 -apple-system, "Helvetica Neue", Arial, sans-serif; color: #111; }
h1 { font-size: 20pt; border-bottom: 3px solid #111; padding-bottom: 4px; }
h2 { font-size: 15pt; margin-top: 1.4em; border-bottom: 1px solid #999; break-after: avoid; }
h3 { font-size: 12pt; break-after: avoid; }
table { border-collapse: collapse; width: 100%; margin: 0.6em 0; font-size: 9pt; break-inside: avoid; }
th, td { border: 1px solid #bbb; padding: 3px 6px; vertical-align: top; text-align: left; }
th { background: #eee; }
blockquote { border-left: 4px solid #c00; margin: 0.6em 0; padding: 0.2em 0.8em; background: #fff5f5; }
code { font-size: 9pt; background: #f2f2f2; padding: 0 3px; border-radius: 3px; word-break: break-all; }
pre code { display: block; padding: 6px; white-space: pre-wrap; }
img { max-width: 60%; max-height: 3.6in; display: block; margin: 0.6em auto 0.2em; border-radius: 6px; }
p > em:only-child { display: block; text-align: center; font-size: 8.5pt; color: #555; }
a { color: #0645ad; text-decoration: none; }
hr { border: 0; border-top: 1px dashed #aaa; margin: 1.2em 0; }
.page-break { break-before: page; }
li { margin: 0.15em 0; }
"""


PLAIN_CSS = """
body { font: 11pt/1.45 Georgia, "Times New Roman", serif; color: #000; }
h1, h2, h3 { font-family: Arial, sans-serif; color: #000; }
img, p > em:only-child { display: none; }
blockquote { border-left: 3px solid #000; background: none; }
th { background: #ddd; }
a { color: #000; text-decoration: none; }
a[href^="http"]::after { content: " <" attr(href) ">"; font-size: 8pt; word-break: break-all; }
td a[href^="http"]::after { font-size: 7pt; }
"""


def inline_images(html, base_dir):
    def repl(m):
        src = m.group(1)
        if re.match(r"^[a-z]+:", src):
            return m.group(0)
        path = os.path.normpath(os.path.join(base_dir, src))
        with open(path, "rb") as f:
            data = base64.b64encode(f.read()).decode()
        return f'src="data:image/jpeg;base64,{data}"'
    return re.sub(r'src="([^"]+)"', repl, html)


def link_to_repo(html, base_dir):
    """Point relative links at GitHub so PDFs never embed local file paths."""
    def repl(m):
        href = m.group(1)
        if re.match(r"^([a-z]+:|#)", href):
            return m.group(0)
        path, _, frag = href.partition("#")
        rel = os.path.relpath(os.path.normpath(os.path.join(base_dir, path)), ROOT)
        return f'href="{REPO_URL}{rel}{"#" + frag if frag else ""}"'
    return re.sub(r'href="([^"]+)"', repl, html)


def render(md_paths, title, plain=False):
    parts = []
    for i, rel in enumerate(md_paths):
        path = os.path.join(ROOT, rel)
        text = open(path, encoding="utf-8").read()
        text = re.sub(r"^- \[ \] ", "- ☐ ", text, flags=re.M)
        text = re.sub(r"^- \[x\] ", "- ☑ ", text, flags=re.M)
        body = markdown.markdown(text, extensions=["tables", "fenced_code", "sane_lists", "toc"])
        body = re.sub(r"<img[^>]*>", "", body) if plain else inline_images(body, os.path.dirname(path))
        body = link_to_repo(body, os.path.dirname(path))
        parts.append(('<div class="page-break"></div>' if i else "") + body)
    extra = PLAIN_CSS if plain else ""
    return f"<!doctype html><html><head><meta charset='utf-8'><title>{title}</title><style>{CSS}{extra}</style></head><body>{''.join(parts)}</body></html>"


if __name__ == "__main__":
    out_dir = sys.argv[1]
    os.makedirs(out_dir, exist_ok=True)
    jobs = {
        "peoples-mesh-kit-guide": (["README.md", "GUIDE.md", "BOM.md", "docs/hardware-options.md", "docs/printing.md", "docs/workshop.md", "firmware/README.md", "offline-flasher/README.md", "docs/meshcore-links.md", "docs/sources.md"], "People's Mesh Kit: Complete Guide", False),
        "plain-instructions": (["GUIDE.md", "BOM.md", "docs/hardware-options.md", "docs/printing.md", "firmware/README.md", "offline-flasher/README.md", "docs/meshcore-links.md"], "People's Mesh Kit: Plain Printable Instructions", True),
        "handouts": (["handouts/companion-build-card.md", "handouts/repeater-build-card.md", "handouts/recipient-card.md"], "People's Mesh Kit: Handouts", False),
    }
    for name, (files, title, plain) in jobs.items():
        with open(os.path.join(out_dir, name + ".html"), "w", encoding="utf-8") as f:
            f.write(render(files, title, plain))
        print(os.path.join(out_dir, name + ".html"))
