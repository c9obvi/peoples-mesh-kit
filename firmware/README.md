# Firmware (offline copy)

Official **MeshCore v1.18.0** builds for **Seeed Studio XIAO nRF52840 + Wio-SX1262** (flasher name: "Seeed Studio Xiao nRF52 WIO"), downloaded 2026-11-14 from the [MeshCore releases](https://github.com/meshcore-dev/MeshCore/releases) (`companion-v1.18.0`, `repeater-v1.18.0`, published 2026-10-15). The bootloader and erase utilities come from <https://flasher.meshcore.io/firmware/>. MeshCore is MIT-licensed. Checksums: `meshcore-v1.18.0/SHA256SUMS`.

| File | Use |
|---|---|
| `Xiao_nrf52_companion_radio_ble-v1.18.0-81dbae5.uf2` | **People's Companion** (Bluetooth, phone app) |
| `Xiao_nrf52_repeater-v1.18.0-81dbae5.uf2` | **People's Repeater** |
| `Xiao_nrf52_companion_radio_usb-v1.18.0-81dbae5.uf2` | Companion over USB only (web/CLI client, no Bluetooth). Not normally wanted. |
| `*.zip` (same names) | DFU packages. Use with the web flasher's "Custom firmware" option or `adafruit-nrfutil`. |
| `xiao_nrf52840_ble_bootloader-0.9.2-OTAFIX2.2.zip` | OTAFIX bootloader. Only needed for Bluetooth OTA updates later. Install it through the flasher. |
| `Xiao_nrf52_QSPIFlash_Format-v1.2.zip` | The flasher's "erase" helper (wipes old settings). |

## Offline UF2 flashing

1. Antenna attached. Plug the XIAO into a computer with a USB-C **data** cable.
2. **Double-tap** the tiny reset button. A USB drive appears.
3. Drag the right `.uf2` onto it. The drive disconnects itself when done, which is normal.
4. UF2 copying does not run the flasher's Erase step. On a board that already has MeshCore settings, use the online flasher's Erase first. New boards don't need it.

Newer firmware: <https://flasher.meshcore.io> always offers the latest. Refresh this folder before an event with the same file names from the newest release.

## ESP32-S3 alternatives (`meshcore-v1.18.0-esp32s3/`)

Full-flash ("merged") images from the same v1.18.0 releases, for the boards in [docs/hardware-options.md](../docs/hardware-options.md) B and C. Checksums: `meshcore-v1.18.0-esp32s3/SHA256SUMS`.

| File | Board / role |
|---|---|
| `Xiao_S3_WIO_companion_radio_ble-…-merged.bin` | XIAO ESP32S3 + Wio-SX1262 kit, Companion (Bluetooth) |
| `Xiao_S3_WIO_repeater-…-merged.bin` | XIAO ESP32S3 + Wio-SX1262 kit, Repeater |
| `LilyGo_T3S3_sx1262_companion_radio_ble-…-merged.bin` / `…_repeater-…` | LilyGo T3S3 with **SX1262** radio |
| `LilyGo_T3S3_sx1276_companion_radio_ble-…-merged.bin` / `…_repeater-…` | LilyGo T3S3 with **SX1276** radio |

**Online (easiest):** <https://flasher.meshcore.io> → pick "Seeed Studio Xiao S3 WIO" or "LilyGo T3 S3 (SX126x / SX127x)" → role → Flash.

**Offline:** these merged images are written at address `0x0` and replace everything on the flash:

```sh
python3 -m pip install esptool
# Hold BOOT, tap RESET, release BOOT to enter download mode, then:
python3 -m esptool --chip esp32s3 write_flash 0x0 Xiao_S3_WIO_repeater-v1.18.0-81dbae5-merged.bin
```

Antenna on before power, as always.
