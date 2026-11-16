# MeshCore Links

All checked 2026-11-15. Offline copies are noted. MeshCore is the firmware, protocol and apps this kit runs.

## Flash and configure

| Link | What | Offline copy |
|---|---|---|
| <https://flasher.meshcore.io> | Official web flasher (Chrome/Edge): flash, erase, DFU, serial Console | `offline-flasher/` → <http://localhost:8080> |
| <https://config.meshcore.io> | Repeater / Room Server USB setup tool | `offline-flasher/config-site/` → <http://localhost:8080/config/> |
| <https://github.com/meshcore-dev/MeshCore/releases> | All firmware releases (current stable: **v1.18.0**, 2026-10-15) | `firmware/meshcore-v1.18.0/` |
| <https://blog.meshcore.io/2026/10/15/release-1-18-0> | v1.18.0 release notes | — |
| <https://blog.meshcore.io/2026/04/06/otafix-bootloader> | Why the OTAFIX bootloader matters for Bluetooth updates | bootloaders in `firmware/flasher-static/` |
| <https://www.youtube.com/watch?v=ems9_XvdPX8> | Flasher video tutorial (linked from the flasher) | — |

## Apps (install on phones *before* you need them)

| Link | What | Offline copy |
|---|---|---|
| <https://apps.apple.com/nz/app/meshcore/id6742354151> | MeshCore for iPhone/iPad | none possible (App Store only) |
| <https://play.google.com/store/apps/details?id=com.liamcottle.meshcore.android> | MeshCore for Android | `offline-extras/…-android.apk` (with `--apps`) |
| <https://files.liamcottle.net/MeshCore/v1.51.1/> | Direct downloads: Android APK, macOS, Windows, Linux, web (v1.51.1) | `offline-extras/` (with `--apps`) |
| <https://app.meshcore.nz> | Web app (browser client) | <http://localhost:8080/app/> (with `--apps`) |

## Learn and look things up

| Link | What | Offline copy |
|---|---|---|
| <https://meshcore.io> | Project home | — |
| <https://docs.meshcore.io> | Documentation | `sources/meshcore-docs/` (Markdown) |
| <https://docs.meshcore.io/radio_presets/> | Radio presets explained | `sources/meshcore-docs/radio_presets.md` |
| <https://api.meshcore.nz/api/v1/config> | Live preset list (USA 910.525 MHz; Southern California 927.875 MHz) | table in GUIDE F-0 |
| <https://github.com/meshcore-dev/MeshCore> | Source code (MIT) | `firmware/source/` |
| `sources/meshcore-docs/cli_commands.md` | Every repeater/room-server command | in repo |
| `sources/meshcore-docs/faq.md` | FAQ | in repo |
| <https://map.meshcore.dev> | Map of nodes: find your local mesh | — |

## Related tools

| Link | What |
|---|---|
| <https://github.com/meshcore-dev/config.meshcore.io> | Source of the config tool (MIT) |
| <https://github.com/oltaco> | OTAFIX bootloader author |
| <https://github.com/recrof/QSPIFlash-Formatter> | XIAO nRF52840 flash-erase tool (MIT) |
| <https://areyoumeshingwith.us/docs/meshcore/installation/> | openHop: MeshCore repeater on a Raspberry Pi + SX1262 HAT |
