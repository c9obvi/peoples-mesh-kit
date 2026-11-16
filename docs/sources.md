# Sources

Everything here was collected 2026-11-14 straight from the designer's links.

## Videos (Black Flag Civilian)

- **People's Companion**: <https://youtu.be/RTBM0CscnLI> (30:54). Overview 2:00, range test 5:00–13:00, **parts & tools 14:00**, C-1 15:00, C-2 15:50, C-3 16:20, C-4 18:00, C-5 19:10, C-6 20:00, C-7 24:00, flash 24:50, pair 26:30.
- **People's Repeater**: <https://youtu.be/yAmINEghCOc> (38:43). Overview 2:00, range test 5:30–11:00, water test 11:30–15:30, **build 15:35**: R-2 16:05, R-3 17:20, R-4 18:40, R-5 21:00, R-6 22:10, R-7 23:50, R-8 25:10, R-9 27:00, R-10 28:50, R-11 30:20, R-12 31:20, R-13 33:40.
- Auto-generated transcripts are kept locally in `sources/transcripts/` and git-ignored, since they are the creator's words (YouTube ASR, so expect errors: "Mesh Central" = MeshCore, "Laura" = LoRa, and in the repeater video "Meshtastic" is said where MeshCore steps are shown).

## What the videos point to (all archived)

The video descriptions contain **no separate written guide**. They link to:
1. **Printables** (STLs + text instructions + parts list): archived in `sources/printables/`, files in `stl/`
2. **BFC web store** (builder kit contents, prices): archived in `sources/store/`
3. SubscribeStar (support/Discord)

The descriptions themselves are archived in `sources/youtube/`. The Printables listings have no other files (no G-code, PDFs or extra downloads). The repeater listing also has v1.0 STLs, which are superseded by v1.1.

## Printables (CC0 / public domain)

- Companion: <https://www.printables.com/model/1832924> → `stl/companion/`, listing text in `sources/printables/companion-printables-1832924.md`
- Repeater: <https://www.printables.com/model/1768397> → `stl/repeater/` (v1.1), listing text in `sources/printables/repeater-printables-1768397.md`
- Photos in `images/` come from those listings, resized to 1400 px.

## Store & parts (designer's links)

- BFC store: <https://blackflagcivilian.bigcartel.com> (builder kit, housings, hubs, antennas)
- Amazon short links resolved: `a.co/d/08OOc4oh` → B07KD9JLH3 (18650 holder) · `a.co/d/0eyPYsYW` → B079JC8HKH (rocker) · `a.co/d/04KqRpTD` → B082F7X8WS (CN3065) · `a.co/d/05SnUmph` → B0CTXL61LY (antenna + bulkhead) · `a.co/d/048UcKC9` → B088NFRNZ2 (PH2.0 pigtails)
- Couldn't load automatically (bot-blocked): Lowe's (light, washer) and 18650batterystore.com (cells). Those prices are marked *verify* in `bom/bom.csv`.

## Alternate hardware (checked 2026-11-15)

- AliExpress kit 2-pack: <https://www.aliexpress.us/item/3256808574469954.html> (from a page saved by the user, since automated access redirects to login)
- DigiKey 102010611 (ESP32S3 kit) / 102010710 (nRF52840 kit): see docs/hardware-options.md
- openHop / pyMC Pi repeater: <https://areyoumeshingwith.us/docs/meshcore/installation/>, <https://pypi.org/project/pymc-core/>

## MeshCore

All links: [docs/meshcore-links.md](meshcore-links.md). Offline mirrors are rebuilt by `scripts/update_offline_flasher.py`.


- Web flasher: <https://flasher.meshcore.io>. Device "Seeed Studio Xiao nRF52 WIO"; roles Companion BLE / Companion USB / Repeater / Room Server; OTAFIX recommendation for OTA.
- Releases: <https://github.com/meshcore-dev/MeshCore/releases> (v1.18.0, 2026-10-15), MIT
- Radio presets: <https://api.meshcore.nz/api/v1/config> (USA 910.525/SF7/BW62.5/CR5; SoCal 927.875)
- Docs: <https://docs.meshcore.io> · App: <https://meshcore.io> · Map: <https://map.meshcore.dev>

## Support the designer

SubscribeStar / Discord: <https://www.subscribestar.com/blackflagcivilian>
