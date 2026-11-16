#!/usr/bin/env python3
"""Shopping list for a batch of People's Companions and People's Repeaters.

Reads bom/bom.csv and rounds each line up to real pack sizes, choosing the
cheapest mix of price tiers (e.g. 4-pack + singles of antennas).

    python3 scripts/bom_calc.py --companions 6 --repeaters 4
    python3 scripts/bom_calc.py -c 10 -r 5 --optional --tools --markdown > my-order.md

Prices are snapshots (see the price_checked column), not quotes. Shipping
and tax are not included.
"""
import argparse
import csv
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))
BOM = os.path.join(HERE, "..", "bom", "bom.csv")


def parse_offers(text):
    """'1=9.00;4=32.00' -> [(1, 9.0), (4, 32.0)]"""
    offers = []
    for part in text.split(";"):
        units, price = part.split("=")
        offers.append((int(units), float(price)))
    return offers


def cheapest(qty, offers):
    """Cheapest combination of offers covering at least qty units.

    Returns (cost, units_bought, {offer_units: count}).
    """
    if qty <= 0:
        return 0.0, 0, {}
    limit = qty + max(u for u, _ in offers)
    best = [math.inf] * (limit + 1)
    pick = [None] * (limit + 1)
    best[0] = 0.0
    for n in range(1, limit + 1):
        for units, price in offers:
            if units <= n and best[n - units] + price < best[n]:
                best[n] = best[n - units] + price
                pick[n] = units
    n = min(range(qty, limit + 1), key=lambda k: (best[k], k))
    cost, bought, combo = best[n], n, {}
    while n > 0:
        combo[pick[n]] = combo.get(pick[n], 0) + 1
        n -= pick[n]
    return cost, bought, combo


def describe(combo):
    parts = []
    for units, count in sorted(combo.items(), reverse=True):
        label = "single" if units == 1 else f"{units}-pack"
        parts.append(f"{count} x {label}")
    return " + ".join(parts)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("-c", "--companions", type=int, default=1)
    ap.add_argument("-r", "--repeaters", type=int, default=1)
    ap.add_argument("--optional", action="store_true", help="include optional items (heat shrink, upgrade cells, clear coat)")
    ap.add_argument("--tools", action="store_true", help="include tools (skip if you already own them)")
    ap.add_argument("--markdown", action="store_true", help="print a Markdown table")
    args = ap.parse_args()

    builds = {"companion": args.companions, "repeater": args.repeaters}
    rows = list(csv.DictReader(open(BOM, newline="", encoding="utf-8")))

    lines, total = [], 0.0
    for row in rows:
        build, req = row["build"], row["required"]
        if build == "tool" and not args.tools:
            continue
        if req == "optional" and not args.optional:
            continue
        per = int(row["qty_per_unit"])
        if build in builds:
            if builds[build] == 0:
                continue
            # qty_per_unit 0 = buy once for the batch (e.g. heat-shrink kit),
            # except optional upgrade cells, which are one per repeater.
            need = per * builds[build] if per else (builds[build] if row["id"] in ("R9", "R10") else 1)
        else:
            need = 1
        cost, bought, combo = cheapest(need, parse_offers(row["offers"]))
        total += cost
        lines.append((row, need, bought, combo, cost))

    title = f"Shopping list: {args.companions} companion(s) + {args.repeaters} repeater(s)"
    if args.markdown:
        print(f"# {title}\n")
        print("| ID | Item | Need | Buy | Est. cost | Price checked | Where |")
        print("|---|---|---:|---|---:|---|---|")
        for row, need, bought, combo, cost in lines:
            where = f"[{row['vendor']}]({row['url']})" if row["url"] else row["vendor"]
            print(f"| {row['id']} | {row['item']} | {need} | {describe(combo)} | ${cost:,.2f} | {row['price_checked']} | {where} |")
        print(f"\n**Estimated total: ${total:,.2f}** plus shipping and tax. Rows marked `verify` or `estimate` need a live price check.")
    else:
        print(title)
        print("=" * len(title))
        for row, need, bought, combo, cost in lines:
            flag = "" if row["price_checked"][:2] == "20" else f"  [{row['price_checked']}]"
            print(f"{row['id']:>4}  need {need:>3}  buy {describe(combo):<28} ${cost:>8,.2f}  {row['item'][:70]}{flag}")
        print(f"\nEstimated total: ${total:,.2f} (+ shipping/tax). [verify]/[estimate] = check live price.")


if __name__ == "__main__":
    main()
