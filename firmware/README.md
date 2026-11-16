# Firmware (offline copy)

**MeshCore v1.18.0**, the latest stable release (published 2026-10-15, checked 2026-11-15), for every board in [docs/hardware-options.md](../docs/hardware-options.md). The files come from the [MeshCore releases](https://github.com/meshcore-dev/MeshCore/releases) via flasher.meshcore.io. MeshCore is MIT-licensed. Each folder has a `SHA256SUMS` file. Refresh while online with `python3 scripts/update_offline_flasher.py`.

| Folder | Board | Chip |
|---|---|---|
| `meshcore-v1.18.0/xiao-nrf52840-wio-sx1262/` | **XIAO nRF52840 + Wio-SX1262 kit (the guide's default)** | nRF52840 |
| `meshcore-v1.18.0/rak4631/` | RAK WisBlock 4631 | nRF52840 |
| `meshcore-v1.18.0/heltec-t114/` | Heltec T114 | nRF52840 |
| `meshcore-v1.18.0/promicro-nrf52-faketec/` | ProMicro nRF52840 "faketec" DIY | nRF52840 |
| `meshcore-v1.18.0/xiao-esp32s3-wio-sx1262/` | XIAO ESP32S3 + Wio-SX1262 kit | ESP32-S3 |
| `meshcore-v1.18.0/lilygo-t3s3-sx1262/` | LilyGo T3S3, SX1262 radio | ESP32-S3 |
| `meshcore-v1.18.0/lilygo-t3s3-sx1276/` | LilyGo T3S3, SX1276 radio | ESP32-S3 |
| `meshcore-v1.18.0/heltec-v3/`, `heltec-v4/` | Heltec V3 / V4 | ESP32-S3 |
| `flasher-static/` | nRF52840 **erase tools** and **OTAFIX bootloaders** (by @oltaco, MIT) | nRF52840 |
| `source/` | MeshCore source code of this release (for custom builds) | — |

Each board folder holds three roles: **`companion_radio_ble`** (phone app over Bluetooth: use this for companions), **`companion_radio_usb`** (USB-only clients) and **`repeater`**.

## Easiest: the offline web flasher

`python3 offline-flasher/serve.py`, then open <http://localhost:8080> in Chrome or Edge. It's the same flasher as flasher.meshcore.io, running from this folder. See [offline-flasher/README.md](../offline-flasher/README.md).

## nRF52840 boards with no tools at all (UF2 drag-and-drop)

The bootloader on these boards shows up as a USB drive, so any computer works. No browser or software is needed.

1. Antenna on. Plug in with a USB-C **data** cable.
2. **Double-tap reset.** A drive appears (often named `XIAO-SENSE`, `RAK4631` or similar). Its `INFO_UF2.TXT` names the board and bootloader.
3. Copy the `.uf2` you want onto the drive. It disconnects by itself when done, which is normal.

| To… | Copy this `.uf2` (XIAO kit example) |
|---|---|
| Make a **companion** | `meshcore-v1.18.0/xiao-nrf52840-wio-sx1262/Xiao_nrf52_companion_radio_ble-v1.18.0-81dbae5.uf2` |
| Make a **repeater** | `meshcore-v1.18.0/xiao-nrf52840-wio-sx1262/Xiao_nrf52_repeater-v1.18.0-81dbae5.uf2` |
| **Wipe** old settings (factory reset), then flash again | `flasher-static/Xiao_nrf52_QSPIFlash_Format-v1.2.uf2` (XIAO). RAK/T114/faketec: `FLASH_ERASE_nrf52_softdevice_v6.uf2` |
| Install the **OTAFIX bootloader** (only needed for Bluetooth updates later) | `flasher-static/xiao_nrf52840_ble_bootloader-0.9.2-OTAFIX2.2.uf2`. Use the `_sense_` file only if `INFO_UF2.TXT` says Sense. Other boards have their own file. |

The `.zip` files are the same firmware as DFU packages, for the web flasher's "Custom firmware" button or `adafruit-nrfutil`.

## ESP32-S3 boards

ESP32-S3 boards have no drag-and-drop mode, so use the offline web flasher, or `esptool` if Python is available:

- `…-merged.bin` is a **full image** (wipes settings), written at `0x0`.
- `….bin` (no `merged`) is an **app-only update** that keeps settings. The web flasher handles the address for you.

```sh
python3 -m pip install esptool        # once, while online
# hold BOOT, tap RESET, release BOOT (download mode), then:
python3 -m esptool --chip esp32s3 write_flash 0x0 meshcore-v1.18.0/lilygo-t3s3-sx1262/LilyGo_T3S3_sx1262_repeater-v1.18.0-81dbae5-merged.bin
```

## Building your own (DIY ESP32 + SX1262)

`source/MeshCore-companion-v1.18.0.tar.gz` is the full source of this release. Custom pin maps are a PlatformIO build ([MeshCore repo](https://github.com/meshcore-dev/MeshCore)). PlatformIO downloads its toolchains on first use, so do a test build **while you're online**.
