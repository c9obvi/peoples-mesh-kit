# Repeater build card (bag "R")

Full steps: GUIDE.md Part R · Video: youtu.be/yAmINEghCOc from 15:35

**In the bag:** ASA hub + mount · Harbor Breeze light · XIAO kit (pre-flashed **Repeater**) · CN3065 board · antenna + U.FL bulkhead cable · 3 male PH2.0 pigtails · bonded washer · tape · 2 screws/zip ties

- [ ] **2** Bulkhead into the hub → work the **bonded washer** down the threads → nut → snug (don't crack it).
- [ ] **3** Pigtail polarity matches the CN3065 silkscreen? If not, swap red/black in all 3 plugs.
- [ ] **4** **Glasses on.** Harvest the light: keep the panel box + swivel junction + O-ring. Cut between the 4 teeth.
- [ ] **5** Open the panel box (save the screws). Cut the wires. Remove the switch module. **Tape the rubber plug.**
- [ ] **6** Panel: black → pigtail black. **White (+)** → pigtail **red**. One wire at a time.
- [ ] **7** Cell out! Battery box: red → +, black → −.
- [ ] **8** XIAO BAT pads: red → BAT+, black → BAT−. Bend the tips 90°; the wire exits away from the USB-C end.
- [ ] **9** Coax through the junction (thumb screw + captive nut). Snap the hub onto the junction. Twist-test.
- [ ] **10** U.FL onto the Wio: flat, click. **Antenna on now.** Rejoin the boards.
- [ ] **11** CN3065: **SOLAR → BAT → SYS OUT.** Green blink = powered.
- [ ] **12** Flash station: name, location, **new admin password**, group preset.
- [ ] **13** Test station: telemetry login + it shows up in a test message's path. Then pack it in and replace the 4 screws.
