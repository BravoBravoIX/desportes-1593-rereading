# Data

Per page (`f189`, `f186r` = f. 186 recto, `f186v` = f. 186 verso):

| file | contents |
|---|---|
| `signs.txt` | the sign classes as read, one manuscript line per row: line number, a tab, the signs separated by spaces. `an` = the a/n sign, `bo` = b/o, ... ; `que`, `qui`, `pour`, `et` = word signs; `code` = a code sign the published key does not give; `?` = a sign not made out |
| `key.json` | Tomokiyo's published key as a table (`pipeline[0].table`), and under `pipeline[0].choices` the letter taken at every occurrence of each pair sign, in reading order. `unknown_render` is how code and unread signs are printed (`[?code]`, `[??]`) |
| `plaintext.txt` | the literal plaintext as one stream, as written by our tool when the reading was made |
| `plaintext-by-line.txt` | the same, one manuscript line per row (`python3 ../decode/decode.py key.json signs.txt --by-line`) |
| `reading.json` | per sign: line, the votes of the reader passes, the voted class, tied candidates where the passes disagreed, and the class and letters finally used (`fields` explains each); `passes_per_line` says which passes took part on each line |
| `corrections.json` | the correction proposals made by code, and for each what was seen in the image and whether it was applied |
| `controls.json` | the page decoded as read and with its signs shuffled (seeds 1-3), bits per letter and dictionary cover; the last fifth decoded on its own |

Line numbers are the manuscript lines as numbered in `../reading/*-french.md`. On f. 186 recto the cipher starts on line 12; lines 1-11 are clear text.

`known-text/`: the material used to measure the reader. `f185-decipherment.txt` is the reading, by Claude, of the decipherment made at the time (f. 185); `f188v-cipher-passage.txt` the passages of it that correspond to the cipher of f. 188v; `f188v-labels.json` the known signs of f. 188v after alignment (stage A); `stageB-heldout.json` the known classes of the held-out lines and the four readings of them (passes a, b, c and the vote), sign by sign; `stageB-heldout-alignment.txt` the vote aligned to the known text; `scores/` the recorded scores, including letter accuracy and bits per letter.

`compare-rosson/`: per-line counts of the comparison with Rosson's reading (no text of his).
