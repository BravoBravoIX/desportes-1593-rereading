#!/usr/bin/env python3
"""Apply a page's key.json to its signs.txt and print the literal plaintext.

    python3 decode.py ../data/f189/key.json ../data/f189/signs.txt            # one stream
    python3 decode.py ../data/f189/key.json ../data/f189/signs.txt --by-line  # one row per line

Python 3 standard library only. The key is Tomokiyo's published one: eleven signs each stand
for two letters (a/n, b/o, ...), and key.json records which of the two was taken at every
occurrence ("choices", in reading order), so nothing is guessed here. Word signs give their
word; a code sign or an unread sign prints as the key's unknown marker ([?code], [??]).
"""
import argparse
import json
import sys


def read_signs(path):
    rows = []
    with open(path, encoding="utf-8") as f:
        for raw in f:
            if raw.strip() and not raw.startswith("#"):
                line, _, signs = raw.rstrip("\n").partition("\t")
                rows.append((line, signs.split()))
    return rows


def decode(rows, key):
    step = key["pipeline"][0]
    table, choices = step["table"], step.get("choices", {})
    unknown = step.get("unknown_render", "[?{sym}]")
    used = {}
    out = []
    for line, signs in rows:
        text = []
        for s in signs:
            entry = table.get(s) or {}
            value = entry.get("v")
            if entry.get("type") == "polyphone":
                k = used.get(s, 0)
                used[s] = k + 1
                lst = choices.get(s, [])
                value = lst[k] if k < len(lst) else None
                if value is not None and value not in entry["v"]:
                    sys.exit(f"choice {value!r} for {s!r} is not one of {entry['v']}")
            text.append(unknown.replace("{sym}", s) if value is None else value)
        out.append((line, "".join(text)))
    for s, lst in choices.items():
        if used.get(s, 0) != len(lst):
            sys.exit(f"{len(lst)} choices recorded for {s!r}, {used.get(s, 0)} occurrences")
    return out


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("key")
    ap.add_argument("signs")
    ap.add_argument("--by-line", action="store_true")
    a = ap.parse_args()
    with open(a.key, encoding="utf-8") as f:
        key = json.load(f)
    rows = decode(read_signs(a.signs), key)
    if a.by_line:
        for line, text in rows:
            print(f"{line}  {text}")
    else:
        print("".join(text for _, text in rows))
