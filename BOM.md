# Bill of Materials

These are the parts BFC links from his Printables pages and web store, the ones used in the videos. Machine-readable version: [`bom/bom.csv`](bom/bom.csv). Prices were checked **2026-11-14** unless marked *verify* (the store blocked automated checks; snapshot or estimate shown) or *estimate*. Shipping and tax are extra.

**Batch shopping list for any mix:**

```sh
python3 scripts/bom_calc.py --companions 6 --repeaters 4            # parts only
python3 scripts/bom_calc.py -c 6 -r 4 --optional --tools --markdown  # + extras & tools, as Markdown
```

The script rounds each line up to the real pack sizes (8-pack holders, 10-pack switches, 15-pair pigtails…) and picks the cheapest tier mix. For example, 6 antennas becomes a 4-pack plus 2 singles.

## Shared by both builds

| Part | Per radio | Price | Where |
|---|---|---|---|
| Seeed Studio **XIAO nRF52840 & Wio-SX1262 Kit** | 1 | $13.49 | [Seeed](https://www.seeedstudio.com/XIAO-nRF52840-Wio-SX1262-Kit-for-Meshtastic-p-6400.html) |
| Solder + flux | batch | ~$12 | any |

## People's Companion: per unit ≈ $31 (≈ $27 at 10-pack antenna pricing)

| ID | Part | Qty | Pack price → per unit | Where |
|---|---|---|---|---|
| C1 | XIAO nRF52840 & Wio-SX1262 Kit | 1 | $13.49 | [Seeed](https://www.seeedstudio.com/XIAO-nRF52840-Wio-SX1262-Kit-for-Meshtastic-p-6400.html) |
| C2 | BFC 915 MHz whip (SMA male) **+ 10 cm SMA-to-IPEX cable** | 1 | $9 · 4 for $32 · 10 for $70 | [BFC store](https://blackflagcivilian.bigcartel.com/product/bfc-915-mhz-lora-antenna) |
| C3 | 18650 holder with wire leads (Art&Beauty) | 1 | $6.69 / 8 → $0.84 | [Amazon B07KD9JLH3](https://www.amazon.com/dp/B07KD9JLH3) |
| C4 | Mini 10×15 mm SPST rocker switch | 1 | $5.98 / 10 → $0.60 | [Amazon B079JC8HKH](https://www.amazon.com/dp/B079JC8HKH) |
| C5 | 18650 cell: EVE 25P 2500 mAh (designer's pick) | 1 | $1.85–5.99, often sold out | [18650 Battery Store](https://www.18650batterystore.com/products/eve-18650-25p) |
| C6 | Printed Enclosure + Cap, PETG (≤ 49 g) | 1 set | ~$1 filament | `stl/companion/` |
| C7 | Heat shrink (optional) | batch | ~$7 | any |

**Shortcut:** BFC sells a **Companion Builder Kit** (everything except the 18650) for $37.99, 2 for $71.99, or 4 for $135.99, in 8 colors: [store](https://blackflagcivilian.bigcartel.com/product/the-peoples-companion-mesh-radio-builder-kit). The printed housing alone is $11.99, 4 for $39.99, or 10 for $89.99.

## People's Repeater: per unit ≈ $36–41 (light on sale vs. regular)

| ID | Part | Qty | Pack price → per unit | Where |
|---|---|---|---|---|
| R1 | **Harbor Breeze 60 lm 1 W black solar LED spot light** | 1 | $14.98 reg. (often $9.98 on sale) | [Lowe's](https://www.lowes.com/pd/Harbor-Breeze-60-Lumens-1-Watt-Black-Warm-White-Solar-LED-Spot-light/5018244381) |
| R2 | XIAO nRF52840 & Wio-SX1262 Kit | 1 | $13.49 | [Seeed](https://www.seeedstudio.com/XIAO-nRF52840-Wio-SX1262-Kit-for-Meshtastic-p-6400.html) |
| R3 | HiLetgo **CN3065** mini solar charger board | 1 | $6.49 / 2 → $3.25 | [Amazon B082F7X8WS](https://www.amazon.com/dp/B082F7X8WS) |
| R4 | Tenmory 915 MHz 3 dBi antenna + 15 cm U.FL→SMA bulkhead | 1 | $11.99 / 2 → $6.00 | [Amazon B0CTXL61LY](https://www.amazon.com/dp/B0CTXL61LY) |
| R5 | JST **PH2.0** pigtails, 15 pairs (use **3 male** each) | 3 | $7.99 / 15 → $1.60 | [Amazon B088NFRNZ2](https://www.amazon.com/dp/B088NFRNZ2) |
| R6 | Hillman **1/4" × 5/8" bonded sealing washer** | 1 | ~$8 / 75 *verify* | [Lowe's](https://www.lowes.com/pd/Hillman-75-Count-1-4-in-x-5-8-in-Neoprene-Bonded-Sealing-Washer/3036264) |
| R7 | Printed Hub + Mount, ASA (≤ 74 g) | 1 set | ~$1.50 filament | `stl/repeater/` |
| R8 | 2 screws or 2 UV zip ties | 2 | pennies | any |
| R9/R10 | *Optional* button-top upgrade cell: EVE 26V 2550 mAh or Samsung 35E 3500 mAh | 1 | ~$5 / ~$6–9 *verify* | [EVE 26V](https://www.18650batterystore.com/products/eve-26v-18650-button-top-battery) · [35E](https://www.18650batterystore.com/products/samsung-35e-button-top) |

The light **includes an 18650.** Upgrades must be **button-top**. The EVE 25P listing (C5) isn't labeled button-top (likely flat-top), so keep it for companions unless you confirm otherwise.

**Printed hub & mount** are also sold ready-made: $14.99, 4 for $53.99, or 10 for $119.99 ([store](https://blackflagcivilian.bigcartel.com/product/3d-printed-peoples-repeater-hub-mount)).

## Tools

| Tool | Companion | Repeater | Notes |
|---|:-:|:-:|---|
| Soldering iron + solder (+ flux) | ✔ | ✔ | A $12 iron works. Workshop: 1 per 2–3 people. |
| Wire stripper / small flush cutters | ✔ | ✔ | |
| Large side cutters | | ✔ | Cuts the light's housing |
| Small adjustable wrench | ✔ | ✔ | SMA nuts |
| Phillips screwdriver | | ✔ | |
| Needle-nose pliers, tweezers | helpful | ✔ | |
| Safety glasses | ✔ | **✔** | Brittle plastic shards |
| **Multimeter** | recommended | recommended | Polarity checks save boards |
| Heat gun / lighter | optional | | Heat shrink |
| USB-C **data** cable + Chrome/Edge computer | ✔ | ✔ | Flashing |
| Micro-USB cable | | optional | Bench-charge via CN3065 |
| Stand-alone 18650 charger | optional | | Swap-and-go for companion owners |

## Example: Shopping list: 6 companion(s) + 4 repeater(s)

| ID | Item | Need | Buy | Est. cost | Price checked | Where |
|---|---|---:|---|---:|---|---|
| C1 | Seeed Studio XIAO nRF52840 & Wio-SX1262 Kit for Meshtastic | 6 | 6 x single | $80.94 | 2026-11-14 | [Seeed Studio](https://www.seeedstudio.com/XIAO-nRF52840-Wio-SX1262-Kit-for-Meshtastic-p-6400.html) |
| C2 | BFC 915 MHz whip antenna (SMA male) + 10 cm SMA-female-to-IPEX cable | 6 | 1 x 4-pack + 2 x single | $50.00 | 2026-11-14 | [Black Flag Civilian store](https://blackflagcivilian.bigcartel.com/product/bfc-915-mhz-lora-antenna) |
| C3 | Art&Beauty single 18650 battery holder with wire leads (8-pack) | 6 | 1 x 8-pack | $6.69 | 2026-11-14 | [Amazon (ASIN B07KD9JLH3)](https://www.amazon.com/dp/B07KD9JLH3) |
| C4 | Mini 10x15 mm 2-pin SPST on/off rocker switch (10-pack) | 6 | 1 x 10-pack | $5.98 | 2026-11-14 | [Amazon (ASIN B079JC8HKH)](https://www.amazon.com/dp/B079JC8HKH) |
| C5 | EVE 25P 18650 2500 mAh cell | 6 | 6 x single | $35.94 | verify | [18650 Battery Store](https://www.18650batterystore.com/products/eve-18650-25p) |
| C6 | People's Companion housing: Enclosure + Cap (PETG, ~49 g max) | 6 | 6 x single | $6.00 | estimate | [Print it yourself (stl/companion)](https://www.printables.com/model/1832924) |
| R1 | Harbor Breeze 60-lumen 1 W black solar LED spot light (Lowe's) | 4 | 4 x single | $59.92 | 2026-11-14 (search) | [Lowe's](https://www.lowes.com/pd/Harbor-Breeze-60-Lumens-1-Watt-Black-Warm-White-Solar-LED-Spot-light/5018244381) |
| R2 | Seeed Studio XIAO nRF52840 & Wio-SX1262 Kit for Meshtastic | 4 | 4 x single | $53.96 | 2026-11-14 | [Seeed Studio](https://www.seeedstudio.com/XIAO-nRF52840-Wio-SX1262-Kit-for-Meshtastic-p-6400.html) |
| R3 | HiLetgo CN3065 mini solar LiPo charger board (2-pack) | 4 | 2 x 2-pack | $12.98 | 2026-11-14 | [Amazon (ASIN B082F7X8WS)](https://www.amazon.com/dp/B082F7X8WS) |
| R4 | Tenmory 915 MHz 3 dBi SMA antenna + 15 cm U.FL-to-SMA-female bulkhead cable (2-pack) | 4 | 2 x 2-pack | $23.98 | 2026-11-14 | [Amazon (ASIN B0CTXL61LY)](https://www.amazon.com/dp/B0CTXL61LY) |
| R5 | JST PH2.0 2-pin pigtails, 100 mm, 15 male/female pairs | 12 | 1 x 15-pack | $7.99 | 2026-11-14 | [Amazon (ASIN B088NFRNZ2)](https://www.amazon.com/dp/B088NFRNZ2) |
| R6 | Hillman 1/4 in x 5/8 in neoprene bonded sealing washer (Lowe's, 75-count) | 4 | 1 x 75-pack | $8.00 | verify | [Lowe's](https://www.lowes.com/pd/Hillman-75-Count-1-4-in-x-5-8-in-Neoprene-Bonded-Sealing-Washer/3036264) |
| R7 | People's Repeater Hub + Mount (ASA, ~74 g max) | 4 | 4 x single | $6.00 | estimate | [Print it yourself (stl/repeater)](https://www.printables.com/model/1768397) |
| R8 | Mounting hardware: 2 wood/deck screws OR 2 UV-rated zip ties | 8 | 1 x 100-pack | $8.00 | estimate | Any hardware store |
| S1 | Rosin-core solder (thin, 0.6–0.8 mm) + flux pen | 1 | 1 x single | $12.00 | estimate | Any |
| S2 | Small piece of electrical or Kapton tape | 1 | 1 x single | $4.00 | estimate | Any |

**Estimated total: $382.38** plus shipping and tax. Rows marked `verify` or `estimate` need a live price check.
