# An independent re-reading of the Baudouin-Desportes cipher letters of 22 July 1593

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23470957.svg)](https://doi.org/10.5281/zenodo.23470957)

**BnF, Français 3984, ff. 186 and 189.** Two letters written in Paris on 22 July 1593, in the Catholic League's polyphonic cipher: one to Cardinal Pietro Aldobrandini (f. 186, recto and verso), one to Girolamo Frachetta (f. 189).

> **The first reading of these letters is Paolo Rosson's**, published on 1 October 2026: <https://github.com/pangoleen/desportes-1593>. It was announced by Satoshi Tomokiyo: <https://cryptiana.blogspot.com/2026/10/did-fran-vi-break-polyphonic-cipher.html>.
>
> This repository is a **second, independent reading**, made with a different method before we opened his text, and then compared with it. At the level of signs the two readings agree on 95.9 % (f. 189), 93.1 % (f. 186 recto) and 93.8 % (f. 186 verso). **Where they differ, his reading is the better one** wherever we looked. Ours is best used as an independent check of his.

## Status of each page

| page | what was read | measured level |
|---|---|---|
| f. 189 | three reader passes, voted, on all 33 lines | 0.90 per sign on known text (the voted level) |
| f. 186 verso | one full reader pass, plus a second pass on lines 1-11; no vote | about 0.88 per sign on known text (single pass) |
| f. 186 recto | one reader pass (the last line two-thirds unread, marked `?`), plus a second pass on lines 12-17; no vote. The recto's clear (uncoded) text was read by eye | about 0.88 per sign on known text (single pass) |

## What is here

| folder | contents |
|---|---|
| [reading/](reading/) | The French text of each page (Literal = exactly what the key gives; Normalised = the same letters with word breaks made by code), an English translation of each letter, and the comparison with Rosson's reading |
| [data/](data/) | Per page: the signs as read (`signs.txt`, one manuscript line per row; `reading.json` with the votes for every sign), the key with the letter chosen at every occurrence (`key.json`), the literal plaintext, corrections and controls. Also the known-answer material used to measure the reader (`data/known-text/`) and the per-line comparison counts (`data/compare-rosson/`) |
| [decode/](decode/) | `decode.py`, a short stand-alone script (Python 3 standard library) that applies `key.json` to `signs.txt`, and `check.sh`, which reproduces all three pages byte for byte |
| [method/](method/) | How the signs were read (the prompt given to Claude, the reference sheet of signs, an example input), the vote, the correction rule, word breaks, the controls, and the measurement on known text |
| [NUMBERS.md](NUMBERS.md) | Where every number in this README comes from |

## The letters and the images

All images are on Gallica, BnF Français 3984, ark:/12148/btv1b9060633d:

- f. 186 recto, view 347: <https://gallica.bnf.fr/ark:/12148/btv1b9060633d/f347.item> (clear opening, then cipher with short clear phrases)
- f. 186 verso, view 348: <https://gallica.bnf.fr/ark:/12148/btv1b9060633d/f348.item>
- f. 189, view 353: <https://gallica.bnf.fr/ark:/12148/btv1b9060633d/f353.item>
- the sister letter of the same date, f. 188 recto and verso, views 351-352 (cipher on the verso): <https://gallica.bnf.fr/ark:/12148/btv1b9060633d/f351.item>
- the decipherment of f. 188 made at the time, ff. 184-185, views 343-345: <https://gallica.bnf.fr/ark:/12148/btv1b9060633d/f343.item>

The page images are not copied here. The reference sheet in `method/` is made of small crops of f. 188 verso (see the image terms below).

## The key

The key is the Catholic League polyphonic key reconstructed and published by **Satoshi Tomokiyo**: *A Polyphonic Substitution Cipher of the Catholic League (1592-1593)*, <https://cryptiana.web.fc2.com/code/mayenne.htm>. We did not derive it, and we do not reproduce his key image; please see it on his page. Eleven signs each stand for two letters (a/n, b/o, c/p, d/q, e/r, f/s, g/t, h/u, i/x, l/y, m/z); further signs stand for *que*, *qui*, *pour* and *et*; a few code signs stand for names or words that the published key does not give (we leave those as `{code}`).

## The method in plain words

1. **A page with a known answer.** The sister letter f. 188 has a decipherment written at the time (f. 185). We read that decipherment and lined it up with the cipher signs of f. 188 verso. That gave signs whose meaning is known. A check by eye of 120 of those labels, chosen at random with a fixed seed, found 116 right.
2. **A reference sheet.** From those known signs we cut a sheet showing several examples of each sign.
3. **Claude reads the signs.** Each line of a page was cut into pieces, and each piece was shown to Claude (Anthropic, model Opus 5.5) under the reference sheet, with the instruction to name every sign from left to right. This was done three times with different cuts and magnifications.
4. **Vote.** Where two of the three readings agree, that sign is taken.
5. **Corrections, only where the image supports them.** Code pointed out the 10 least likely stretches of each page; each proposed change was looked at in the image and applied only if the image shows it (2 changes applied in all).
6. **Key applied mechanically.** The published key turns each sign into its two possible letters; a statistical model of period French picks one at each place, and every pick is written into `key.json`. From then on the decode is a lookup that anyone can repeat with `decode/decode.py`.
7. **Word breaks by code** from a period French dictionary, for the Normalised text only. No letter is changed.
8. **Controls.** Every page was also decoded with its signs shuffled into a random order, in the same way. A real page reads as French; a shuffled one does not.

Details are in [method/README.md](method/README.md).

## Measured numbers

**Reader on known text** (f. 188 verso, five held-out lines the reference sheet was not cut from, 294 signs):

| reader | signs right | letters right after decoding |
|---|---|---|
| one pass (a / b / c) | 0.878 / 0.888 / 0.878 | |
| vote of the three passes | **0.901** | 0.826 |
| the known signs themselves (the ceiling set by the letter choice) | 1.000 | 0.930 |

So even with the vote, **about one sign in ten is misread**, and the letter choice within a pair costs a further few per cent. On a second set of lines (312 signs, with the later sheet) the vote scored 0.792; part of that gap is where the old decipherment itself differs from the cipher, but it is the recorded number.

**Controls** (bits per letter under the period French model; lower = more like French):

| page | real page | shuffled signs, seeds 1 / 2 / 3 |
|---|---|---|
| f. 189 | 2.710 | 4.194 / 4.231 / 4.273 |
| f. 186 recto | 2.724 | 4.129 / 4.208 / 4.160 |
| f. 186 verso | 2.733 | 4.222 / 4.167 / 4.274 |

That is, about 2.7 against 4.2 on every page.

**Agreement with Rosson's first reading** (sign classes, read independently): 95.9 % (f. 189), 93.1 % (f. 186 recto), 93.8 % (f. 186 verso). Where the signs agree, the same letter of the pair is chosen 93.5 %, 94.3 % and 93.8 % of the time. The details, and the places looked at in the image, are in [reading/comparison-rosson.md](reading/comparison-rosson.md).

## Limitations

- **This is a machine reading.** About 1 sign in 10 is wrong at the measured level (f. 189), and somewhat more on f. 186, which was not voted.
- **No palaeographer has checked it.** The clear text of f. 186 recto was read by eye by Claude and has doubtful words marked `[?]`.
- **The letter within a pair is chosen by a 5-gram model**, which sometimes picks the wrong one where a word-level reading would not (e.g. *tentilhomme* for *gentilhomme*).
- **Our reader systematically reads some a/n signs as c/p.** In this hand the two look alike.
- **Code signs are not identified** (`{code}`); Rosson identifies most of them from the sister letters.
- **Rosson's reading is better than ours** wherever the two differ and we looked. Use his for the text; use ours as an independent confirmation.
- The English translations are Claude's, from our Normalised French. They are not literal plaintext, and they skip the stretches that do not read as French.

## How to reproduce the decode

Needs only Python 3 (no packages):

```
sh decode/check.sh
```

Expected output:

```
f189 stream: identical to data/f189/plaintext.txt (2248 bytes)
f189 by-line: identical to data/f189/plaintext-by-line.txt (2412 bytes)
f186r stream: identical to data/f186r/plaintext.txt (2794 bytes)
f186r by-line: identical to data/f186r/plaintext-by-line.txt (2998 bytes)
f186v stream: identical to data/f186v/plaintext.txt (2297 bytes)
f186v by-line: identical to data/f186v/plaintext-by-line.txt (2461 bytes)
all pages reproduced exactly
```

`plaintext.txt` was written by our own tool when the reading was made, so the stream check is a test of `decode.py` against an independent implementation. To read one page line by line: `python3 decode/decode.py data/f189/key.json data/f189/signs.txt --by-line`. In the output, `[?code]` is a code sign and `[??]` a sign that was not made out. The measurement on known text can be recomputed with `python3 method/score_heldout.py`.

What cannot be repeated from this repository alone: Claude's sign readings themselves (they are recorded here, not re-run), and the language model and dictionary used for the letter choice, word breaks and bits per letter (built from our own period corpora).

## Credits

- **Paolo Rosson**, for the first reading of these letters (<https://github.com/pangoleen/desportes-1593>). Only a few short quotations from it appear here, in `reading/comparison-rosson.md`.
- **Satoshi Tomokiyo**, for the published key and his catalogue of these letters (<https://cryptiana.web.fc2.com/code/mayenne.htm>), and for announcing Rosson's reading.
- **Bibliothèque nationale de France / Gallica**, for the manuscript images. Source gallica.bnf.fr / BnF.
- **Anthropic's Claude** (model Opus 5.5) was used as the sign reader, for the correction checks, for reading the clear text and the f. 185 decipherment by eye, and for the English translations.

Prepared by Brett Burford, October 2026.

## Licence

- Text and data (everything except `decode/` and the images noted below): [Creative Commons Attribution 4.0 International](LICENSE) (CC BY 4.0).
- `decode/` and `method/score_heldout.py`: [MIT licence](decode/LICENSE).
- Images in `method/` (`sheet-v2.png`, `sheet-v3.png`, `example-input-*.png`) are crops of BnF, Français 3984, f. 188 verso, from Gallica. They are not covered by CC BY: Gallica's terms allow free non-commercial reuse with the source line "Source gallica.bnf.fr / BnF"; commercial reuse needs the BnF's permission.

## How to cite

Burford, B. (2026). Independent re-reading of the Desportes cipher letters of 22 July 1593 (BnF fr. 3984 ff. 186, 189). Zenodo. https://doi.org/10.5281/zenodo.23470957 (this DOI always points to the latest version; each release has its own version DOI on Zenodo).
