#!/bin/sh
# Decode the three pages with decode.py and compare byte for byte with the files in data/<page>/:
# plaintext.txt (one stream) and plaintext-by-line.txt (one row per manuscript line).
cd "$(dirname "$0")/.." || exit 2
status=0
for page in f189 f186r f186v; do
    for mode in stream by-line; do
        if [ "$mode" = stream ]; then flag=""; want="data/$page/plaintext.txt"
        else flag="--by-line"; want="data/$page/plaintext-by-line.txt"; fi
        if python3 decode/decode.py "data/$page/key.json" "data/$page/signs.txt" $flag | cmp -s - "$want"; then
            echo "$page $mode: identical to $want ($(wc -c < "$want") bytes)"
        else
            echo "$page $mode: DIFFERS from $want"
            status=1
        fi
    done
done
[ $status = 0 ] && echo "all pages reproduced exactly"
exit $status
