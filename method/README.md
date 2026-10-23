# How the signs were read and measured

This folder explains how the sign readings in `../data/` were made, and how far they can be trusted. The full working code is not published here: it depends on our own tools and language models. What is here is enough to see what was done, to check the measured numbers on the known text, and to reproduce the decode exactly (`../decode/`).

## The cipher in one paragraph

The letters use the Catholic League polyphonic cipher of 1592-1593, as published by Satoshi Tomokiyo ([mayenne.htm](https://cryptiana.web.fc2.com/code/mayenne.htm)). Eleven signs each stand for **two** letters: a/n, b/o, c/p, d/q, e/r, f/s, g/t, h/u, i/x, l/y, m/z. Four signs stand for words or syllables: *que*, *qui*, *pour* and (in this hand) *et*. A few further signs stand for names or words that the published key does not give; we write them `code`. There are no word divisions in the cipher. Reading a page is therefore two separate jobs: (1) say which sign is written at each position, and (2) choose, for each pair sign, which of its two letters is meant.

## Step 1: a known-answer page (stage A)

The sister letter of the same date, f. 188 (Gallica views 351-352), has cipher passages on its verso, and a decipherment made at the time survives on f. 185 (views 343-345). That decipherment was read by Claude ([../data/known-text/f185-decipherment.txt](../data/known-text/f185-decipherment.txt)), took the passages that correspond to the cipher ([../data/known-text/f188v-cipher-passage.txt](../data/known-text/f188v-cipher-passage.txt)), and aligned the known text to the signs of f. 188v line by line with a forced-alignment model (line starts read from the image by Claude). That gave 1245 aligned signs; a confidence filter kept 858 ([../data/known-text/f188v-labels.json](../data/known-text/f188v-labels.json), pixel positions on the full Gallica image).

Check: a seeded random sample of 120 kept labels was looked at sign by sign, in crops, by Claude: 116 were right (96.7 %); this check comes from the same model that reads the signs. The per-label verdicts of that check were not saved in a file; the count is from our working notes.

## Step 2: the reference sheet

From the labelled signs we cut a reference sheet: up to five examples of each sign, one row per sign, with the sign's name in red ([sheet-v2.png](sheet-v2.png), [sheet-v3.png](sheet-v3.png); `sheet-v*.json` lists which labelled signs were used, as indices into [sheet-labels-f188v.json](sheet-labels-f188v.json)).

- **Sheet v2** was cut only from lines that were *not* used for the measurement below (it leaves out lines 14-17 and 20 of f. 188v). It has no `code` row. It is the sheet the measurement was made with.
- **Sheet v3** adds a `code` row (three code signs) and changes some examples; it leaves out the confirmation lines (6, 10-13). It is the sheet used on the target pages ff. 189 and 186.

Image source: crops of BnF, Français 3984, f. 188 verso, from Gallica (ark:/12148/btv1b9060633d, view 352). Source gallica.bnf.fr / Bibliothèque nationale de France. Gallica allows free non-commercial reuse with this source line; commercial reuse needs the BnF's permission. The sheet images and the example input image are under those terms, not under this repository's CC BY licence.

## Step 3: Claude reads the signs

Each manuscript line was cut into pieces at low-ink columns, enlarged, and placed under the reference sheet in one image. Claude (model `claude-opus-5-5`, Anthropic API, one call per image) was asked to name every sign in the strip, left to right, using the names on the sheet. The answer is a single line of sign names; where the model was torn between two it could give both (`e/r|b/o`), and `?` for a sign it could not make out. The answer was treated as data only and parsed into sign classes.

Three passes were made with different cuts and magnifications, so that a sign split by a cut in one pass is whole in another:

| pass | piece width | enlargement |
|---|---|---|
| a | about 1150 px | 1.5x |
| b | about 500 px | 2.0x |
| c | about 600 px | 1.8x, first cut offset by 250 px |

## Step 4: the vote

The passes of a line are aligned with each other sign by sign. Where at least two of three agree, that sign is taken. Where all three differ, every class some pass saw is kept as a candidate, and the decoder (step 6) chooses among those candidates only. A position that only one pass saw as a sign (the others saw nothing there) is dropped when two passes saw nothing. With two passes, agreement is taken and a disagreement keeps both candidates; with one pass, that pass stands. Only passes that read every piece of a line take part in that line's vote. `../data/<page>/reading.json` records, for every sign, the votes, any tied candidates and the class finally used.

## Step 5: the correction pass (only where the image supports it)

Code proposed corrections: the 10 windows of 8 signs per page whose decoded letters the period French model found least likely, each with the single sign change that would most improve that window. Each proposal was then looked at in a crop of the page image, by Claude, and **applied only if the image shows the proposed sign**. Most proposals were rejected because the image shows the sign as first read. Applied: 1 on f. 189, 1 on f. 186 verso, none on f. 186 recto. Every proposal, decision and what was seen is in `../data/<page>/corrections.json`.

## Step 6: from signs to letters

The published key is applied to the signs. For each pair sign, the letter at each occurrence (a or n, b or o, ...) was chosen by a 5-gram character model of period French (an exact Viterbi search; code and unread signs break the context). The choice is the only thing the language model decides, and every choice is recorded in `../data/<page>/key.json` under `choices`, so the decode itself is mechanical and anyone can repeat it with [../decode/decode.py](../decode/decode.py). The model is built from our own period corpora and is not published here; changing a recorded choice changes one letter and nothing else.

## Step 7: word breaks (Normalised text)

The Normalised text in `../reading/*-french.md` adds word breaks by code, never by hand or by a language model: a Viterbi segmentation of each run of letters into words of a period French dictionary (cost = minus log2 of the word's frequency; a stretch no dictionary word covers is kept as one unknown chunk at a fixed cost per letter, and marked `[?]`). No letter is changed, added or removed; the only additions are spaces, a hyphen at a line end, and an editorial apostrophe after elided l, d, qu, s, n, c, m. The files were checked when written: the letters of Normalised equal the letters of Literal.

## Measurement on known text (stage B)

The readers were measured on five held-out lines of f. 188v (lines 14-17 and 20, 294 known signs) that the reference sheet (v2) was not cut from. Sign accuracy = 1 - (edit distance between the classes read and the known classes) / known signs. All the data are in [../data/known-text/stageB-heldout.json](../data/known-text/stageB-heldout.json), and [score_heldout.py](score_heldout.py) recomputes the numbers (Python 3, standard library):

```
$ python3 method/score_heldout.py
pass_a   36 edits / 294 known signs -> sign accuracy 0.8776
pass_b   33 edits / 294 known signs -> sign accuracy 0.8878
pass_c   36 edits / 294 known signs -> sign accuracy 0.8776
vote     29 edits / 294 known signs -> sign accuracy 0.9014
```

`python3 method/score_heldout.py --align` prints the sign-by-sign alignment of the vote against the known text (saved in [../data/known-text/stageB-heldout-alignment.txt](../data/known-text/stageB-heldout-alignment.txt)). The decode's letter accuracy (0.826 for the vote; 0.930 when the known signs themselves are decoded, which is the ceiling set by the 5-gram letter choice) and the bits per letter need the language model; they are in [../data/known-text/scores/](../data/known-text/scores/).

A second set of lines (6 and 10-13, 312 signs, read with sheet v3) scored lower, 0.792 per sign, but there the known answer is partly at fault: the decipherment differs from the cipher in places (spellings, and code signs where the decipherer wrote words out). Looked at by Claude, most of those disagreements were not reader errors; we did not keep a record of that adjudication, so 0.792 is the only recorded number.

The reader's main confusion is between a/n and c/p (both a figure 4; c/p has a closed loop below, a/n an open hook that in this hand often nearly closes).

## Controls (shuffled signs decoded the same way)

A decoder with a language model makes almost anything look a little like its language. So each page was also decoded after shuffling its signs into a random order (seeds 1, 2, 3), with the same key and the same decoder. Real pages cost about 2.7 bits per letter under the period French model; the shuffled controls about 4.1-4.3, and a much smaller share of their letters falls in dictionary words. The last fifth of each page, decoded on its own, stays close to the whole page (2.66-2.89 bits per letter) and far from the controls. Numbers per page: `../data/<page>/controls.json`.

## What this does not show

- It is a machine reading. About one sign in ten is wrong on known text even with the vote, and f. 186 was not voted.
- It awaits a palaeographer's reading.
- The 5-gram choice of letter within a pair is sometimes wrong where a word-level reading would get it right.
- Code signs are left as `{code}`; we did not identify them.
