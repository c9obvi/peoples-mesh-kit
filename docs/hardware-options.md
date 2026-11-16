# Radio Board Options

Every mesh node is **two parts working together**:

```
  ┌──────────────────────┐   SPI (8–9 wires)   ┌──────────────────────┐
  │  "BRAIN"             │ <─────────────────> │  LoRa RADIO          │ ── antenna (915 MHz)
  │  nRF52840 or ESP32-S3│                     │  SX1262 (or SX1276)  │
  │  Bluetooth to phone, │                     │  the long-range part │
  │  runs MeshCore       │                     │                      │
  └──────────────────────┘                     └──────────────────────┘
```

**Neither the nRF52840 nor the ESP32-S3 can do LoRa by itself.** "Onboard antenna" on a bare XIAO listing means *Bluetooth*. A node needs both halves. What changes from board to board is how they're joined:

| How they're joined | Examples | Effort |
|---|---|---|
| **Stacked kit:** two boards press together on a tiny board-to-board connector | XIAO nRF52840 + Wio-SX1262 · XIAO ESP32S3 + Wio-SX1262 | None (friction fit) |
| **All-in-one:** brain and radio on one board | LilyGo T3S3, Heltec V3/V4, Heltec T114, RAK4631 | None |
| **DIY:** you wire a radio module to a brain board | ESP32 dev board + Core1262 · ProMicro nRF52840 "faketec" | Solder 8–9 wires (+ custom build for ESP32) |
| **Raspberry Pi HAT:** radio plugs onto the Pi's GPIO header | Waveshare SX1262 HAT (SPI version) · MeshAdv-Mini | None (software install) |

All of these run **MeshCore** and talk to each other on one mesh **if they share the same radio preset** (GUIDE F-0).

## Pick by job

| Job | Best choice | Why |
|---|---|---|
| **Solar repeater (People's Repeater)** | **A: XIAO nRF52840 + Wio-SX1262** | Low power, so a 1 W panel keeps it alive year-round |
| Carry-around companion | A, or **B: XIAO ESP32S3 kit**, or **C: T3S3/Heltec** | B and C are fine but need charging every few days |
| Plugged-in relay (window, attic, wall/USB power) | B, C, or **G: Pi + HAT** | Power doesn't matter on wall power |
| Cheapest DIY low-power relay | **E: faketec** | nRF52840 power draw from ~$10 of parts |

---

## A. XIAO nRF52840 + Wio-SX1262 kit *(the guide's default)*

```
   XIAO nRF52840  (USB-C, BAT+/BAT− pads underneath)
   ════════════════  ← presses on (friction fit)
   Wio-SX1262     (IPEX/U.FL antenna socket)
```

- MeshCore flasher name: **Seeed Studio Xiao nRF52 WIO**. Offline firmware: `firmware/meshcore-v1.18.0/xiao-nrf52840-wio-sx1262/`.
- Fits the People's Companion housing and the People's Repeater build exactly.
- **Buy the kit, not the bare XIAO nRF52840** (a bare board has no LoRa).

| Source | Price (checked) | Notes |
|---|---|---|
| [Seeed Studio](https://www.seeedstudio.com/XIAO-nRF52840-Wio-SX1262-Kit-for-Meshtastic-p-6400.html) | $13.49 each (2026-11-14) | The designer's link. Backordered in Nov 2026. |
| [AliExpress: Seeedstudio AI Hardware Store](https://www.aliexpress.us/item/3256808574469954.html) | **$23.02 for "2 PCS" = 2 kits** + $6.55 shipping (2026-11-15) | 4.8★, 441 ratings, 4,000+ sold; reviewers use it for solar nodes and MeshCore repeaters. Pick "2 PCS". Check import charges at checkout. |
| [DigiKey 102010710](https://www.digikey.com/en/products/result?keywords=102010710) | $13.75 (2026-11-15) | 0 in stock, 1 expected 11/17, 4-week standard lead time |

## B. XIAO ESP32S3 + Wio-SX1262 kit *(in-stock alternative)*

```
   XIAO ESP32S3   (USB-C, BAT+/BAT− pads underneath)
   ════════════════  ← presses on
   Wio-SX1262     (same radio board as kit A)
```

- MeshCore flasher name: **Seeed Studio Xiao S3 WIO** (Companion Bluetooth or Repeater). Offline: `firmware/meshcore-v1.18.0/xiao-esp32s3-wio-sx1262/`.
- Same XIAO footprint and same Wio board as kit A, so it **should** fit the companion housing with the same wiring. Test-fit your first one.
- **Power:** draws several times more than the nRF52840. As a companion, expect **days** per 18650 instead of ~2 weeks. **Not recommended for the solar garden-light repeater.** Use it as a plugged-in relay.
- No antenna is listed in the box. The guide's builds use their own antennas anyway.

| Source | Price | Notes |
|---|---|---|
| [DigiKey 102010611](https://www.digikey.com/en/products/detail/seeed-technology-co-ltd/102010611/25835813) | $10.90 (2026-11-15) | **228 in stock** |

## C. All-in-one ESP32-S3 LoRa boards: LilyGo T3S3, Heltec V3/V4

```
   ┌─────────────────────────────────────┐
   │ ESP32-S3 + SX1262 + OLED screen     │ ── SMA or IPEX antenna
   │ USB-C, JST battery plug             │
   └─────────────────────────────────────┘
```

- Flash and go: flasher entries **LilyGo T3 S3 (SX126x)**, **LilyGo T3 S3 (SX127x)**, **Heltec v3**, **Heltec v4**.
- **Check the T3S3 before flashing:**
  - It must be the **915 MHz** version (LilyGo also sells 433/868 MHz versions).
  - Find out which radio chip it has, SX1262 or SX1276. It's printed on the shield, the PCB or the box. Pick the matching flasher entry or file.
  - The **SX1280 (2.4 GHz) version won't work** with 915 MHz meshes.
- Offline: `firmware/meshcore-v1.18.0/lilygo-t3s3-sx1262/` or `…/lilygo-t3s3-sx1276/` (and `heltec-v3/`, `heltec-v4/`).
- Same power note as B: great companions and plugged-in relays.

## D. Other ready-made nRF52840 + LoRa boards (low power, solar-friendly)

All are listed in the MeshCore flasher with Companion and Repeater roles. Firmware for the **T114**, **RAK4631** and **faketec** is in the offline kit (`firmware/meshcore-v1.18.0/`):

- Heltec **T114**, Mesh Node **T1**
- **RAK WisBlock 4631**
- Elecrow **ThinkNode** M1/M3/M4/M6
- LilyGo **T-Echo**
- Seeed **SenseCAP Solar Node P1**: a complete solar repeater, pricier

They don't fit the People's Repeater hub, so they need their own enclosure and solar setup.

## E. DIY nRF52840 "faketec"

```
   ProMicro-style nRF52840 (nice!nano clone)
        │ 8–9 wires (or a faketec carrier PCB)
   SX1262 module (HT-RA62 / Ebyte E22-900M22S / RA-01SH)
```

- Flasher entry **ProMicro nrf52 (faketec)**, so no custom firmware build is needed.
- Has nRF52840 low power, so it works as a solar repeater. Build-it-yourself enclosure.

## F. DIY: any ESP32 dev board + an SX1262 module

```
   ESP32 / ESP32-S3 dev board            SX1262 module (3.3 V only!)
   3V3 ───────────────────────────────── VCC
   GND ───────────────────────────────── GND
   SCK ───────────────────────────────── SCK
   MOSI ──────────────────────────────── MOSI
   MISO ──────────────────────────────── MISO
   GPIO a ────────────────────────────── NSS / CS
   GPIO b ────────────────────────────── RESET
   GPIO c ────────────────────────────── BUSY
   GPIO d ────────────────────────────── DIO1
   (some modules also need RXEN/TXEN, or DIO2 as the RF switch)
```

- Easy-to-wire modules: **Waveshare Core1262-HF** (2.54 mm pins). **Ebyte E22-900M22S** needs an adapter board (tiny 1.27 mm pads). **Heltec HT-RA62**.
- No pins on your board? Solder on the header strip it shipped with, or solder wires straight to the holes or edge pads.
- **Needs a custom MeshCore build** that maps your chosen GPIO pins. It's a PlatformIO project, not a flasher click. Worth it only for tinkering, since the C boards are often about the same price.

## G. Raspberry Pi + SPI SX1262 HAT (home-base relay)

```
   Raspberry Pi (Zero W / 3B+ / 4 / 5)
   ══════════════════  ← HAT on the 40-pin GPIO header, no wiring
   SX1262 HAT (SPI)   ── antenna
   runs openHop Repeater (formerly pyMC_Repeater): MeshCore repeater + web dashboard
```

- Supported radios include the **Waveshare SX1262 HAT** and the **FrequencyLabs MeshAdv-Mini**. ⚠️ Buy the **SPI** version. Waveshare's UART "LoRa HAT" (Ebyte E22-900T, its own firmware) can't be used as a raw radio.
- Waveshare defaults reported by the project: CS GPIO21, RESET GPIO18, BUSY GPIO20, IRQ GPIO16. Enable SPI first, and verify against current docs.
- A Pi draws **2–5 W**, so wall power only. Good for one always-on node by a high window.
- Install docs: <https://areyoumeshingwith.us/docs/meshcore/installation/> · library: <https://pypi.org/project/pymc-core/> · background: <https://blog.meshcore.io/2026/05/12/pymc-intro>
