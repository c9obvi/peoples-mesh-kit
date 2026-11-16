#!/usr/bin/env python3
"""Run the MeshCore web flasher locally, with no internet.

    python3 offline-flasher/serve.py          # then open http://localhost:8080 in Chrome or Edge
    python3 offline-flasher/serve.py --port 9000

Serves the mirrored flasher (offline-flasher/site/), the repeater setup tool
(offline-flasher/config-site/ at /config/), the saved release list
(offline-flasher/releases/), and firmware files from firmware/. Web Serial
works on http://localhost because browsers treat it as a secure origin.
Binds to 127.0.0.1 only. Standard library only; refresh with
scripts/update_offline_flasher.py while online.
"""
import argparse
import http.server
import os
import urllib.parse
import webbrowser

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SITE = os.path.join(HERE, "site")
CONFIG_SITE = os.path.join(HERE, "config-site")
RELEASES = os.path.join(HERE, "releases")
FIRMWARE = os.path.join(ROOT, "firmware")
APP = os.path.join(ROOT, "offline-extras", "meshcore-web")  # optional, git-ignored

TYPES = {".js": "text/javascript", ".css": "text/css", ".json": "application/json", ".svg": "image/svg+xml",
         ".html": "text/html; charset=utf-8", ".woff2": "font/woff2", ".bin": "application/octet-stream",
         ".uf2": "application/octet-stream", ".zip": "application/zip", ".hex": "text/plain",
         ".wasm": "application/wasm", ".png": "image/png", ".ico": "image/x-icon", ".otf": "font/otf",
         ".ttf": "font/ttf"}


def firmware_index():
    """Map firmware file name -> path, searched anywhere under firmware/."""
    index = {}
    for dirpath, _, files in os.walk(FIRMWARE):
        for name in files:
            index.setdefault(name, os.path.join(dirpath, name))
    return index


class Handler(http.server.BaseHTTPRequestHandler):
    index = {}

    def send_file(self, path):
        if not path or not os.path.isfile(path):
            self.send_error(404, "Not available offline")
            return
        with open(path, "rb") as f:
            data = f.read()
        if path == os.path.join(APP, "index.html"):
            data = data.replace(b'<base href="/">', b'<base href="/app/">')  # web app lives under /app/
        self.send_response(200)
        self.send_header("Content-Type", TYPES.get(os.path.splitext(path)[1], "application/octet-stream"))
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(data)

    def safe_join(self, base, rel):
        path = os.path.realpath(os.path.join(base, rel.lstrip("/")))
        return path if path.startswith(os.path.realpath(base) + os.sep) or path == os.path.realpath(base) else None

    def do_GET(self):
        url = urllib.parse.urlparse(self.path)
        path = urllib.parse.unquote(url.path)
        query = urllib.parse.parse_qs(url.query)

        if path == "/releases":
            repo = "".join(c for c in query.get("repo", [""])[0] if c.isalnum() or c in "-_")
            return self.send_file(os.path.join(RELEASES, f"{repo}.json"))
        if path.startswith("/releases/download/") or path.startswith("/firmware/"):
            return self.send_file(self.index.get(os.path.basename(path)))
        if path == "/config":
            self.send_response(301); self.send_header("Location", "/config/"); self.end_headers(); return
        if path.startswith("/config/"):
            target = self.safe_join(CONFIG_SITE, path[len("/config"):])
            if target and os.path.isdir(target):
                target = os.path.join(target, "index.html")
            return self.send_file(target)
        if path == "/app" or path.startswith("/app/"):
            rel = path[len("/app"):] or "/"
            target = self.safe_join(APP, rel)
            if target and os.path.isdir(target):
                target = os.path.join(target, "index.html")
            if not (target and os.path.isfile(target)):
                target = os.path.join(APP, "index.html")
            return self.send_file(target)

        target = self.safe_join(SITE, path)
        if target and os.path.isdir(target):
            target = os.path.join(target, "index.html")
        if not (target and os.path.isfile(target)):
            target = os.path.join(SITE, "index.html")  # the flasher's own page routes
        self.send_file(target)

    def log_message(self, fmt, *args):
        if args and str(args[1]) != "200":
            super().log_message(fmt, *args)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--port", type=int, default=8080)
    ap.add_argument("--no-browser", action="store_true")
    args = ap.parse_args()
    if not os.path.isfile(os.path.join(SITE, "index.html")):
        raise SystemExit("The flasher mirror isn't here yet. While online, run once:\n"
                         "    python3 scripts/update_offline_flasher.py --apps")
    Handler.index = firmware_index()
    server = http.server.ThreadingHTTPServer(("127.0.0.1", args.port), Handler)
    url = f"http://localhost:{args.port}/"
    print(f"Offline MeshCore flasher: {url}  ({len(Handler.index)} firmware files)  Ctrl-C to stop")
    print(f"Repeater setup tool:      {url}config/")
    if os.path.isdir(APP):
        print(f"Offline MeshCore web app:  {url}app/")
    if not args.no_browser:
        webbrowser.open(url)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
