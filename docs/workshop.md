# Running a "Build Your Own Mesh Radio" Weekend Session

BFC's prepping group built **10 repeaters in one Sunday afternoon** over a barbecue. This is a plan for doing the same with neighbors, friends and family, where most builders have never soldered.

## Format at a glance

| | Companion-only session | Companion + Repeater session |
|---|---|---|
| Builders | 6–12 | 6–10 |
| Length | 3 hours | 5–6 hours (with lunch) |
| Ratio | 1 helper per 4 builders | 1 helper per 3 builders |
| Irons | 1 per 2 builders | 1 per 2 builders |
| Result | everyone leaves with a working companion | + the group installs 1 repeater per household, or 2–3 shared ones |

## 2–3 weeks before

- [ ] **Pick one preset for the whole group** (GUIDE F-0). Find out whether a local MeshCore mesh exists. Check <https://map.meshcore.dev> and ask on the local subreddit/Discord.
- [ ] Collect RSVPs: who builds what? Run `python3 scripts/bom_calc.py -c N -r M --optional --tools` and order. **Seeed ships from overseas**, so order the XIAO kits first. Lithium cells ship by ground.
- [ ] Decide who pays for what: kits at cost, a suggested donation, or gifts.
- [ ] Print every housing, hub and mount, plus **2 spare sets** for broken snaps and mis-prints. Test-fit one of each first.
- [ ] Buy the Harbor Breeze lights in person if you can (Lowe's bulk price: 6+). Check every box is complete.

## The week before: pre-work that saves the day

- [ ] **Flash and bench-test every XIAO kit** on its stock antenna (GUIDE Part 2 / F). Label the bags "C" or "R" and flash the matching role. Dead boards get swapped now, not at the table.
- [ ] Charge every 18650 to storage/full. Put each cell in its own case or bag.
- [ ] **Pre-fix the PH2.0 pigtail polarity** for all repeaters (GUIDE R-3). It's tedious and easy to get wrong in a crowd.
- [ ] Optional: pre-tin the BAT pads on each XIAO. These are the tiniest joints of the day.
- [ ] Pack **one zip bag per build**: printed parts + every component + a printed copy of the Companion or Repeater build card (`handouts/`).
- [ ] Load `firmware/` and this repo onto the flashing laptop. Everything works offline.

## Stations

1. **Welcome / intro (15 min):** what mesh is, why height matters, and the safety brief (below). Show a finished companion and repeater.
2. **Soldering tables:** irons on stands, sponge or brass wool, fume fan or open air, safety glasses, multimeter, flux, solder, tweezers, heat shrink, and a "helper" flag.
3. **Garden-light demolition (repeater builders):** outdoors or on a drop cloth. Glasses on. Large and small cutters, screwdriver, a bin for the junk.
4. **Flash & configure:** a laptop with Chrome/Edge, `firmware/` copied locally, 2 USB-C data cables, and a printed sheet of the agreed preset and naming scheme (e.g. `Smith-Home`, `Rpt-OakSt-Roof`).
5. **Test / hand-off:** a known-good companion and phone in a "test" channel. Confirm each new radio sends and receives, and each repeater shows up in a message's path.

## Run of show (full-day version)

| Time | Block |
|---|---|
| 0:00 | Arrive, coffee, grab your bag, intro + safety (15 min) |
| 0:15 | **Companion build**, GUIDE C-1 → C-7 (45–60 min). Helpers circulate during C-6 soldering. |
| 1:15 | Companion flashing/pairing, phone app install, join the group channel |
| 1:45 | Break / lunch |
| 2:30 | **Repeater build**, R-2 bulkhead and R-4 light harvest first (the hard parts, while fresh) |
| 3:30 | R-6 → R-8 soldering, R-9 → R-11 assembly |
| 4:15 | Flash + configure repeaters, function test (GUIDE Part T), seal them up |
| 4:45 | Walk or drive test: put one repeater up high and send messages around the block |
| 5:15 | Hand-off: recipient cards, plan where each repeater goes, group photo |

## Safety brief (read aloud)

- Irons are **400 °C**: always back in the stand, never set down on the table. Treat burns with cool water.
- **Safety glasses** while cutting the garden lights and while soldering.
- **No batteries in holders until the final step.** Check red = + with the meter before the cell goes in. If anything gets hot, swells or smells, pull the cell and set it outside on concrete.
- Solder fumes: ventilate, keep a fan pulling away from faces, wash hands before eating. Leaded solder: no food at the tables.
- Kids are welcome with a dedicated adult. The companion is a great first-solder project.

## Common day-of snags

- **Stuck U.FL/IPEX plug:** press flat and straight down. Never rock it. Don't remove and re-seat it more than necessary.
- **Bridged BAT pads:** wick or drag the iron through the gap, then check with continuity before the cell goes in.
- **Cap won't close:** coax or wires are bunched. Re-twist the coax into its pocket (C-3).
- **Junction cracked during light harvest:** use a spare light. That's why you bought a spare.
- **Nothing talks to anything:** the preset doesn't match (F-0), or a board was flashed as Companion *USB*.

## After the session

- Give every companion owner the **recipient card** (`handouts/recipient-card.md`).
- Keep a shared list: repeater names, locations, admin passwords (in a password manager, not in this repo), and who maintains each.
- Check repeater telemetry monthly from a companion (Login → Telemetry).
