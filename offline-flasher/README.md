# Offline flasher: flash and set up radios with no internet

Everything needed to turn a blank board into a companion or repeater from a laptop, with the internet down.

```sh
python3 offline-flasher/serve.py      # opens http://localhost:8080
```

| URL | What | Source |
|---|---|---|
| <http://localhost:8080/> | **MeshCore Flasher**, trimmed to this kit's 9 boards: flash, erase, DFU, serial Console | mirror of flasher.meshcore.io (rebuilt locally, not in git; see below) |
| <http://localhost:8080/config/> | **Repeater / Room Server USB setup** (name, location, radio preset, password) | mirror of config.meshcore.io (MIT, [meshcore-dev/config.meshcore.io](https://github.com/meshcore-dev/config.meshcore.io)) |
| <http://localhost:8080/app/> | **MeshCore web app** (chat client), if you ran the refresh with `--apps` | local only, not in git |

Requirements: **Python 3** (no packages) and **Chrome or Edge**. Safari and Firefox have no Web Serial. `localhost` counts as a secure site, so Web Serial and Web Bluetooth work. The server listens on this computer only.

## Before an emergency (while online)

```sh
python3 scripts/update_offline_flasher.py --apps
```

This one command refreshes:

- **The flasher mirror** (`offline-flasher/site/`)
- **The config tool** (`offline-flasher/config-site/`)
- **The release list** (`offline-flasher/releases/`)
- **Latest stable firmware for all 9 boards, plus nRF erase tools and bootloaders** (`firmware/`)
- **MeshCore docs** (`sources/meshcore-docs/`)
- **MeshCore source code** (`firmware/source/`)
- **MeshCore apps** (`offline-extras/`, with `--apps`): the Android APK, macOS DMG, Windows ZIP and web app

**A fresh clone of this repo has no flasher mirror or apps.** Run the command once on each laptop you'll use. Then:

- Install the **MeshCore app** on every phone ahead of time ([iOS](https://apps.apple.com/nz/app/meshcore/id6742354151) / [Android](https://play.google.com/store/apps/details?id=com.liamcottle.meshcore.android)). iPhones can't install apps offline.
- Android phones can install `offline-extras/MeshCore-…-android.apk` directly (allow "install unknown apps").
- Test once: start the server with Wi-Fi off and flash one board.

## Flashing offline

1. `python3 offline-flasher/serve.py` → pick the board → **Companion (Bluetooth)** or **Repeater** → v1.18.0.
2. nRF52840: **Enter DFU mode**. On first install, **Erase Flash**. Then **Flash!** ESP32-S3: **Flash!** (choose "wipe" on first install).
3. No browser? nRF52840 boards also flash by **dragging a `.uf2` onto the board's USB drive**, and ESP32-S3 with `esptool`. See [firmware/README.md](../firmware/README.md).

## Setting up a repeater offline

Use **/config/**, or the flasher's **Console** (type `help`). Common commands, from the MeshCore CLI reference (full list: `sources/meshcore-docs/cli_commands.md`):

```
ver                                  firmware version
set name Rpt-OakSt-Roof              node name
set radio 910.525,62.5,7,5           freq MHz, bandwidth kHz, spreading factor, coding rate (USA preset)
password <new-admin-password>        change the admin password (do this!)
set lat 37.0000                      optional location (it shows on maps)
set lon -122.0000
advert                               announce the node
reboot
```

Check each command against `cli_commands.md` for your firmware version before relying on it, since the syntax can change between releases.

## Why the flasher mirror isn't in git

The bundled libraries (Vue, BeerCSS, esptool-js, zip.js) are open source, but the flasher app itself has no published license that I could find. So it's rebuilt locally by the refresh script, like the closed-source MeshCore apps. If you keep this repo private and just want a personal backup, you may remove the `offline-flasher/site/` line from `.gitignore`. The config tool (MIT), firmware (MIT), bootloaders and erase tools (MIT) and docs (MIT) are all in git.
