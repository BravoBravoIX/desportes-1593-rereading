#!/usr/bin/env python3
"""Recompute the stage B sign accuracy from data/known-text/stageB-heldout.json.

    python3 score_heldout.py [--align]

Sign accuracy = 1 - (edit distance between the classes read and the known classes) / known
signs, over the held-out lines 14-17 and 20 of f. 188v. The classes read are the 'final' ones
(at a tie of the vote the decoder's choice among the candidates); the et sign is counted as the
two classes of its letters (e/r g/t), as the known text spells "et". With --align, prints the
per-sign alignment of the vote against the known text. Python 3 standard library only.
"""
import json
import sys
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data" / "known-text" / "stageB-heldout.json"


def classes(signs):
    out = []
    for s in signs:
        c = s["final"]
        if c in (None, "nul", "|"):
            continue
        out += ["er", "gt"] if c == "et" else [c]
    return out


def align(a, b):
    """Levenshtein table and one optimal path: list of (op, read, known)."""
    n, m = len(a), len(b)
    d = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        d[i][0] = i
    for j in range(m + 1):
        d[0][j] = j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            d[i][j] = min(d[i - 1][j] + 1, d[i][j - 1] + 1, d[i - 1][j - 1] + (a[i - 1] != b[j - 1]))
    ops, i, j = [], n, m
    while i or j:
        if i and j and d[i][j] == d[i - 1][j - 1] + (a[i - 1] != b[j - 1]):
            ops.append(("=" if a[i - 1] == b[j - 1] else "x", a[i - 1], b[j - 1]))
            i, j = i - 1, j - 1
        elif i and d[i][j] == d[i - 1][j] + 1:
            ops.append(("+", a[i - 1], "-"))
            i -= 1
        else:
            ops.append(("-", "-", b[j - 1]))
            j -= 1
    return d[n][m], ops[::-1]


if __name__ == "__main__":
    data = json.loads(DATA.read_text())
    for name, per in data["readings"].items():
        edits = total = 0
        for li in data["lines"]:
            known = data["truth"][str(li)]["classes"]
            e, _ = align(classes(per[str(li)]), known)
            edits += e
            total += len(known)
        print(f"{name:7s} {edits:3d} edits / {total} known signs -> sign accuracy {1 - edits / total:.4f}")
    if "--align" in sys.argv:
        print("\nvote against the known text (= same, x substituted, + extra sign read, - known sign missed)")
        for li in data["lines"]:
            _, ops = align(classes(data["readings"]["vote"][str(li)]), data["truth"][str(li)]["classes"])
            print(f"\nline {li}: {data['truth'][str(li)]['text']}")
            print("  " + " ".join(f"{op}{r}/{k}" if op != "=" else k for op, r, k in ops))
