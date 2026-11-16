#!/usr/bin/env python3
"""Refresh the offline MeshCore flasher and firmware (run while online).

Mirrors https://flasher.meshcore.io into offline-flasher/site/ and the
repeater setup tool https://config.meshcore.io into offline-flasher/config-site/, trims its
device list to the boards this kit uses, saves the release list it needs,
and downloads the latest stable firmware for those boards into
firmware/meshcore-<version>/<board>/. Then `python3 offline-flasher/serve.py`
runs the same flasher on http://localhost with no internet.

    python3 scripts/update_offline_flasher.py            # refresh everything
    python3 scripts/update_offline_flasher.py --dry-run  # show what would change
    python3 scripts/update_offline_flasher.py --apps     # also fetch the MeshCore apps
                                                         # into offline-extras/ (git-ignored)

Also refreshes the MeshCore docs (sources/meshcore-docs/) and the source code
of the current release (firmware/source/), both MIT-licensed.

Standard library only.
"""
import argparse
import hashlib
import json
import os
import re
import shutil
import sys
import urllib.request

BASE = "https://flasher.meshcore.io"
CONFIG_BASE = "https://config.meshcore.io"
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SITE = os.path.join(ROOT, "offline-flasher", "site")
CONFIG_SITE = os.path.join(ROOT, "offline-flasher", "config-site")
RELEASES = os.path.join(ROOT, "offline-flasher", "releases")
FIRMWARE = os.path.join(ROOT, "firmware")
STATIC = os.path.join(FIRMWARE, "flasher-static")

# Flasher device name -> short folder name. Edit this to add or remove boards.
DEVICES = {
    "Seeed Studio Xiao nRF52 WIO": "xiao-nrf52840-wio-sx1262",
    "Seeed Studio Xiao S3 WIO": "xiao-esp32s3-wio-sx1262",
    "LilyGo T3 S3 (SX126x)": "lilygo-t3s3-sx1262",
    "LilyGo T3 S3 (SX127x)": "lilygo-t3s3-sx1276",
    "Heltec v3": "heltec-v3",
    "Heltec v4": "heltec-v4",
    "Heltec T114": "heltec-t114",
    "RAK WisBlock / WisMesh (RAK 4631)": "rak4631",
    "ProMicro nrf52 (faketec)": "promicro-nrf52-faketec",
}
ROLES = {"companionBle", "companionUsb", "repeater"}
FONTS = ["material-symbols-outlined.woff2", "material-symbols-rounded.woff2", "material-symbols-sharp.woff2"]
FONT_CDN = "https://cdn.jsdelivr.net/npm/beercss@3.9.4/dist/cdn/"
GITHUB_API = "https://api.github.com/repos/meshcore-dev/MeshCore"
DOCS = os.path.join(ROOT, "sources", "meshcore-docs")
SOURCE = os.path.join(FIRMWARE, "source")
EXTRAS = os.path.join(ROOT, "offline-extras")


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "peoples-mesh-kit offline mirror"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()


def write(path, data, dry):
    if dry:
        print("  would write", os.path.relpath(path, ROOT), len(data), "bytes")
        return
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as f:
        f.write(data)


def crawl(base, out, start, dry, rewrite=None):
    """Copy a static site's files (HTML, JS, CSS, images), following absolute and relative refs."""
    seen, queue = set(), list(start)
    while queue:
        path = queue.pop(0)
        if path in seen:
            continue
        seen.add(path)
        try:
            data = get(base + path)
        except Exception as e:
            print("  skip", base + path, "-", e)
            continue
        if rewrite:
            data = rewrite(path, data)
        write(os.path.join(out, "index.html" if path.endswith("/") else path.lstrip("/")), data, dry)
        if not re.search(r"\.(js|css|html|mjs)$|/$", path):
            continue
        text = data.decode("utf-8", "ignore")
        here = path if path.endswith("/") else os.path.dirname(path) + "/"
        refs = set()
        for r in re.findall(r"""(?:from\s*|import\s*\(?\s*|src=|href=|url\(\s*)['"]?([^'"\s)`$?#]+)""", text):
            if r.startswith("/") and not r.startswith("//"):
                refs.add(r)
            elif r.startswith(("./", "../")) or (re.match(r"^[\w-]+/[\w./-]+\.\w+$", r) and not r.startswith("http")):
                refs.add(os.path.normpath(os.path.join(here, r)))
        refs |= set(re.findall(r"""['"`](/(?:lib|js|css|img|src)/[^'"`$\s?#]+)['"`]""", text))
        queue += [r for r in refs if not r.startswith(("/releases", "/firmware/")) and r not in seen
                  and re.search(r"\.\w{1,5}$", r)]
    return len(seen)


def flasher_rewrite(path, data):
    if path.endswith("beer.css"):
        data = data.decode().replace(FONT_CDN, "").encode()  # use local font copies
    if path.endswith((".html", ".js")) or path == "/":
        data = data.decode().replace("https://config.meshcore.io", "/config/").encode()  # local Repeater Setup
    return data


def crawl_site(dry):
    n = crawl(BASE, SITE, ["/", "/flasher.js"], dry, flasher_rewrite)
    for font in FONTS:
        write(os.path.join(SITE, "css", font), get(FONT_CDN + font), dry)
    print(f"flasher site: {n} files + {len(FONTS)} fonts")
    n = crawl(CONFIG_BASE, CONFIG_SITE, ["/"], dry,
              lambda path, data: data.decode().replace(FONT_CDN, "").encode() if path.endswith(".css") else data)
    for font in FONTS:
        write(os.path.join(CONFIG_SITE, "lib", "css", font), get(FONT_CDN + font), dry)
    print(f"repeater config site: {n} files + {len(FONTS)} fonts")


def refresh_docs_and_source(tag, dry):
    """MeshCore docs (Markdown) and the release's source tarball, both MIT."""
    listing = json.loads(get(f"{GITHUB_API}/contents/docs?ref={tag}"))
    for item in listing:
        if item["name"].endswith(".md"):
            write(os.path.join(DOCS, item["name"]), get(item["download_url"]), dry)
    write(os.path.join(DOCS, "LICENSE.txt"),
          get(f"https://raw.githubusercontent.com/meshcore-dev/MeshCore/{tag}/license.txt"), dry)
    tarball = os.path.join(SOURCE, f"MeshCore-{tag}.tar.gz")
    if not os.path.exists(tarball):
        if not dry and os.path.isdir(SOURCE):
            for old in os.listdir(SOURCE):
                os.remove(os.path.join(SOURCE, old))
        write(tarball, get(f"https://codeload.github.com/meshcore-dev/MeshCore/tar.gz/refs/tags/{tag}"), dry)
    print(f"docs + source: {tag}")


def refresh_apps(dry):
    """MeshCore app installers (Android APK, macOS, Windows, web) into offline-extras/.

    The app is free but not open source, so these stay out of git.
    """
    import zipfile
    page = get("https://meshcore.io").decode("utf-8", "ignore")
    m = re.search(r"https://files\.liamcottle\.net/MeshCore/(v[0-9.]+)/", page)
    if not m:
        print("apps: could not find the current version on meshcore.io")
        return
    folder_url, version = m.group(0), m.group(1)
    names = sorted(set(re.findall(r'href="\./([^"]+\.(?:apk|dmg|zip|AppImage))"', get(folder_url).decode())))
    for name in names:
        if "linux" in name:
            continue
        dest = os.path.join(EXTRAS, name)
        if not os.path.exists(dest):
            write(dest, get(folder_url + name), dry)
        if name.endswith("-web.zip") and not dry:
            web = os.path.join(EXTRAS, "meshcore-web")
            shutil.rmtree(web, ignore_errors=True)
            with zipfile.ZipFile(dest) as z:
                z.extractall(EXTRAS + "/_web")
            inner = os.path.join(EXTRAS, "_web", "web")
            shutil.move(inner if os.path.isdir(inner) else EXTRAS + "/_web", web)
            shutil.rmtree(EXTRAS + "/_web", ignore_errors=True)
    print(f"apps: {version} ({len(names)} files) in offline-extras/")


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--apps", action="store_true", help="also download MeshCore app installers (local only)")
    args = ap.parse_args()
    dry = args.dry_run

    crawl_site(dry)

    config = json.loads(get(BASE + "/config.json"))
    devices = []
    for device in config["device"]:
        if device["name"] not in DEVICES:
            continue
        device["firmware"] = [fw for fw in device["firmware"]
                              if fw.get("role") in ROLES and fw.get("class") == "community"
                              and any(k.startswith("github") for k in fw)]
        devices.append(device)
    missing = set(DEVICES) - {d["name"] for d in devices}
    if missing:
        print("WARNING: not in the online flasher any more:", ", ".join(sorted(missing)))
    config["device"] = devices
    write(os.path.join(SITE, "config.json"), json.dumps(config, indent=1).encode(), dry)

    # Images the config and app reference (device pictures, chip icons, logo).
    imgs = set(re.findall(r"/img/[\w.-]+\.svg", json.dumps(config)))
    imgs |= {f"/img/{d['type']}.svg" for d in devices} | {"/img/meshcore.svg"}
    for img in sorted(imgs):
        try:
            write(os.path.join(SITE, img.lstrip("/")), get(BASE + img), dry)
        except Exception as e:
            print("  skip", img, "-", e)

    # Release lists: keep the newest stable version of each firmware type,
    # and only the files our devices' patterns match.
    keys = {k for d in devices for fw in d["firmware"] for k in fw if k.startswith("github")}
    downloads = []  # (url, folder, name)
    for key in sorted(keys):
        releases = json.loads(get(f"{BASE}/releases?repo={key}"))
        newest = {}
        for rel in releases:
            newest.setdefault(rel["type"], rel)  # API lists newest first
        kept = []
        for rel in newest.values():
            files = []
            for f in rel["files"]:
                for d in devices:
                    for fw in d["firmware"]:
                        src = fw.get(key)
                        if src and src["type"] == rel["type"] and any(re.search(p, f["name"]) for p in src["files"].values()):
                            folder = os.path.join(FIRMWARE, f"meshcore-{rel['version']}", DEVICES[d["name"]])
                            downloads.append((BASE + f["url"], folder, f["name"]))
                            if f not in files:
                                files.append(f)
            if files:
                kept.append(dict(rel, files=files))
        write(os.path.join(RELEASES, f"{key}.json"), json.dumps(kept, indent=1).encode(), dry)
        print(f"releases[{key}]:", ", ".join(f"{r['type']} {r['version']}" for r in kept))

    # Static helper files (nRF52 erase tool and bootloaders) referenced by our devices.
    for d in devices:
        names = list(d.get("bootloader", []))
        if d.get("erase"):
            names += [d["erase"], d["erase"].replace(".zip", ".uf2")]
        for name in names:
            downloads.append((f"{BASE}{config['staticPath']}/{name}", STATIC, name))

    seen = set()
    for url, folder, name in downloads:
        dest = os.path.join(folder, name)
        if dest in seen:
            continue
        seen.add(dest)
        if os.path.exists(dest):
            continue
        try:
            write(dest, get(url), dry)
        except Exception as e:  # e.g. a .uf2 erase variant that doesn't exist
            print("  skip", name, "-", e)

    if not dry:
        for folder in sorted({os.path.dirname(p) for p in seen if os.path.exists(p)}):
            names = sorted(n for n in os.listdir(folder) if n != "SHA256SUMS")
            with open(os.path.join(folder, "SHA256SUMS"), "w") as f:
                for n in names:
                    f.write(f"{sha256(os.path.join(folder, n))}  {n}\n")
    print(f"firmware: {len(seen)} files under firmware/")

    stable = [r for r in json.loads(get(f"{GITHUB_API}/releases?per_page=10")) if not r["prerelease"]]
    tag = next(r["tag_name"] for r in stable if r["tag_name"].startswith("companion-"))
    refresh_docs_and_source(tag, dry)
    if args.apps:
        refresh_apps(dry)


if __name__ == "__main__":
    sys.exit(main())
