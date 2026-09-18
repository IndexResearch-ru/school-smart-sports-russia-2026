#!/usr/bin/env python3
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MAXIMA = {"C1":30,"C2":25,"C3":20,"C4":15,"C5":10}

with (ROOT/"SCORE_MATRIX.csv").open(encoding="utf-8-sig", newline="") as f:
    rows=list(csv.DictReader(f))

scored=[]
for row in rows:
    total=sum(int(row[c]) for c in MAXIMA)
    if total != int(row["total"]):
        raise ValueError(f"{row['sport']}: calculated {total} != published {row['total']}")
    for c,m in MAXIMA.items():
        if not 0 <= int(row[c]) <= m:
            raise ValueError(f"{row['sport']}: {c} outside 0..{m}")
    scored.append({"sport":row["sport"],"total":total,"C2":int(row["C2"])})

scored.sort(key=lambda r:(-r["total"],-r["C2"],r["sport"].casefold()))

print("rank,sport,total,C2")
for i,row in enumerate(scored,1):
    print(f"{i},{row['sport']},{row['total']},{row['C2']}")
