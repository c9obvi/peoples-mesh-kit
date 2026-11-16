# Printing the parts

Designer settings are from the Printables listings, archived in `sources/printables/`. The Bambu notes after them are for a **P1S with a 0.6 mm hardened-steel nozzle and no AMS**, the printer this kit was first built with. Other printers: use the designer settings.

## Designer settings (verbatim intent)

| | Companion (Enclosure, Cap) | Repeater Hub | Repeater Mount |
|---|---|---|---|
| Material | PETG (ASA/ABS OK, **no PLA/PLA+**) | **ASA** (ABS OK, **no PLA**) | ASA |
| Layer height | 0.2 mm | 0.2 mm | 0.2 mm |
| Line/"layer thickness" | 0.4 mm | 0.4 mm | 0.4 mm |
| Walls | 3–4 | **5–6** | 2–3 |
| Infill | 30–40% | 30–40% | 20–30% |
| Supports | none | none | none |
| Extra | translucent PETG lets the blue LED glow through | bed ~100 °C, enclosure > 40 °C, slow | |

BFC: *"if you print these hubs in ASA with all walls and no infill, the prints come out pretty damn waterproof with no external coatings."* Clear coat is optional extra protection.

## Bambu P1S, 0.6 mm nozzle

- Always use a **"P1S 0.6 nozzle"** process and filament preset. A 0.4 preset on a 0.6 hotend under-extrudes badly.
- **Line width:** the 0.6 default is fine. Set walls by thickness instead of count: 3 walls × 0.6 ≈ the designer's 4 × 0.4, and 4 walls × 0.6 ≈ 6 × 0.4 for the hub. Where the hub's walls are thinner than that, the slicer prints them solid, which is what you want for water resistance.
- **Layer height:** 0.20–0.24 mm.
- **Companion (PETG):** the everyday `Creality CR-PETG @P1S 0.6` preset (245 °C) is fine. Translucent PETG looks best.
- **Repeater (ASA):** use a Bambu/Generic ASA 0.6 preset. Use a textured PEI plate (a glue stick helps). Close the door and preheat the bed for ~10 minutes so the chamber warms. Turn the aux fan down. Lower the outer-wall speed.
- **Fit check first:** a 0.6 nozzle is a little less crisp on small snap-fits. Print one enclosure + cap and one hub, then test the cap snap, switch pocket, SMA hole, and hub ↔ light junction before printing a batch.
- The hub STL is 62 MB (1.25 M triangles, a very fine mesh). Bambu Studio handles it. If slicing gets slow, use *Simplify model* lightly. Don't simplify the junction area much.

## File sizes and bounding boxes

| File | Triangles | Size (mm) | Max solid weight |
|---|---|---|---|
| PeoplesCompanionEnclosureV1.0.stl | 12,914 | 47.6 × 88.6 × 26.0 | 36 g PETG |
| PeoplesCompanionCapV1.0.stl | 5,196 | 41.8 × 87.1 × 3.0 | 13 g PETG |
| PeoplesRepeaterHubV1.1.stl | 1,253,980 | 34.0 × 39.1 × 74.7 | 47 g ASA |
| PeoplesRepeaterMountV1.1.stl | 53,304 | 40.8 × 20.6 × 43.6 | 27 g ASA |

A hub and mount share a plate easily (both ASA), and a 256 mm bed holds several sets of either kind, so batches go quickly. Keep PETG and ASA on separate plates.

## Versions

The repeater listing also has v1.0 files (`Original Version v1.0`). This repo includes only **v1.1** ("Most Recent Version"), the version the guide is written for.
