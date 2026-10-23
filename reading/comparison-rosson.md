# Baudouin-Desportes, 22 July 1593 (BnF fr. 3984 ff. 186, 189): our independent re-reading compared with Paolo Rosson's first reading

> **First reading: Paolo Rosson, 1 Oct 2026 (GitHub pangoleen/desportes-1593, `reading/f189.md`, `reading/f186.md`, version 0.2; repository head 33c854a, 6 Oct 2026), acknowledged by Tomokiyo 3-4 Oct 2026.** Ours ([f189-french.md](f189-french.md), [f186-french.md](f186-french.md)) was written before his text was opened and was not changed after. His files were read on 18 Oct 2026; they are not reproduced here, and only short passages are quoted.
>
> **Status of our pages:** f. 189: three reader passes voted on all 33 lines (the level measured at 0.90 per sign on known text). f. 186 verso: one full pass plus a second on lines 1-11, no vote (about 0.88 per sign for a single pass). f. 186 recto: one pass (last line two-thirds unread), a second on lines 12-17, no vote; clear text read by Claude.

## How the comparison was made

- **Sign classes, not letters.** Each of his letters was mapped back to the published key's sign class (a/n, b/o, ..., u/v and i/j merged); his clear passages `{..}` and editorial brackets `[..]` were removed. Ours: the final sign classes in [../data/](../data/), word signs (que, qui, pour, et) spelt out, code and unread signs left out. Per line: difflib agreement of the two class strings, and on the matched classes how often the letter chosen inside the pair is the same (numbers in [../data/compare-rosson/](../data/compare-rosson/)).
- His line numbering is the same as ours (recto 0-51 and verso 0-32 in his file = our lines 1-52 and 1-33; f. 189 his 1-33 = ours 1-33).
- Where they differ, a handful of places were looked at in the image (crops of the straightened pages) by Claude. Most were not looked at; the table says only how far the readings agree.

## Result in plain words

- **The two readings are the same text.** At the level of signs they agree on 95.9 % (f. 189), 93.1 % (f. 186 recto) and 93.8 % (f. 186 verso) of the classes, read independently by different methods (his: a line recogniser and lexicon decoder with every line checked on the image; ours: Claude reading signs against a reference sheet, voted over passes, key applied mechanically).
- **Where the signs agree, the letter chosen inside the pair agrees 93-94 % of the time.** The rest are our 5-gram model choosing the wrong member of a pair where his word-level reading picks the right one: e.g. our *lachesar* for his *la chesne* (same signs: a/n, e/r), our *tersur* for his *trefve* (same signs).
- **Our reader's main error is systematic: a/n read as c/p.** Of the sign substitutions between the two readings, the largest group by far is our c/p where he has a/n (10 on f. 189, 17 on the recto, 20 on the verso), then our g/t where he has f/s. This is the confusion already seen on known text (stage B: "a/n read as c/p"). In this hand the a/n hook often nearly closes, so the image alone is often not decisive; in every case looked at, his a/n gives French and ours does not.
- **His reading is the better one** wherever we looked: it resolves the stretches that are garbled in ours (e.g. f. 189 l. 4 "sans l'avoir rien espargné", l. 28 "l'Espagnol", f. 186 verso l. 8 "leur dessein vain, il ne manque"), reads clear words inside the cipher that we missed or misread (f. 189 l. 17 a clear "part[iculi]er" that our span took as cipher; f. 186 recto "V.S.Ill.me" and "M[aist]re" where we read "S. S. Illme" and "Mta"), and identifies most code signs from the sister letters, which we left as {code}.
- **What ours adds:** an independent check that the published key reads both letters and that his sign readings are right in about 19 classes of 20; the decode data (key with the letter chosen at every occurrence; [../decode/decode.py](../decode/decode.py) reproduces the literal stream) and the shuffled-sign controls (French at 2.7 bits/letter against 4.1-4.3 for shuffled signs).

## Places looked at in the image

| page, line (ours) | ours | his | what the crop shows | image supports |
|---|---|---|---|---|
| f. 189, 5 (start) | `spas lauoir` (c/p) | "sans l'avoir" (a/n) | f/s, then a figure 4 whose foot curls left and almost closes, a second figure 4 with open hook, f/s, l/y | his (sense; the first sign is borderline) |
| f. 189, 29 (start) | `urir et pat pol` | "vrir l'Espagnol" | after *urir*: an l/y bracket, e/r, f/s bar (not g/t), c/p, a/n, g/t, a heavy figure 4, b/o, l/y | his: the l/y and f/s signs are there; our reader missed the first and misread the second |
| f. 189, 17 (middle) | `ccorbede` | clear "part[iculi]er" | clear letters "par" with a superscript, written in the cipher line | his: it is clear text, not cipher |
| f. 189, 5 (third) | `espart d` | "espargne" | a blot over one sign | not decidable from the image; his fits the sense |
| f. 186 verso, 9 | `desfri pu pi cila emp` | "dessein vain il ne man" | four figure-4 signs with a hook that nearly closes | his by sense; the image is borderline for each sign |
| f. 186 recto, 23 (end) | `dimpac` | "diman-c" | three figure-4 signs, the last with a closed loop | his: hooks, then a closed loop (a/n, a/n, c/p) |
| f. 186 recto, 18 (clear) | "mal aisé il conte[?] deux[?] a ung benignité[?]" | "mal aisé de contredire a ung bruit" | the clear words | his (our reading of the clear text was wrong) |
| f. 186 recto, 14 (clear) | "il nous[?] [?] & passions" | "de nos humeurs et passions" | the clear words | his |
| f. 186 recto, 13 (clear) | "qu'icy vostre" | "qui icy reste" (Tomokiyo "en reste") | the clear word after *icy* | not decided |

The glyph at the start of our cipher span in recto l. 18 (and l. 13), which looks like "Sr", is the cipher sign for *et*: his reading has "Et de soy mesme" there, as ours does.

## Per line agreement

**f. 189**: sign-class agreement 0.959; same letter where the classes agree 0.935.

| our line | his line | our classes | his classes | class agreement | same letter on matched |
|---|---|---|---|---|---|
| 1 | 1 | 72 | 71 | 0.993 | 0.97 |
| 2 | 2 | 70 | 70 | 1.0 | 0.93 |
| 3 | 3 | 70 | 69 | 0.993 | 0.99 |
| 4 | 4 | 79 | 79 | 1.0 | 0.99 |
| 5 | 5 | 61 | 62 | 0.927 | 0.84 |
| 6 | 6 | 69 | 72 | 0.965 | 0.91 |
| 7 | 7 | 66 | 65 | 0.992 | 0.98 |
| 8 | 8 | 65 | 67 | 0.97 | 1.0 |
| 9 | 9 | 72 | 69 | 0.979 | 0.9 |
| 10 | 10 | 70 | 70 | 1.0 | 0.96 |
| 11 | 11 | 34 | 34 | 0.941 | 0.97 |
| 12 | 12 | 66 | 66 | 0.955 | 0.86 |
| 13 | 13 | 71 | 73 | 0.972 | 0.94 |
| 14 | 14 | 73 | 71 | 0.958 | 0.96 |
| 15 | 15 | 72 | 72 | 0.958 | 0.97 |
| 16 | 16 | 71 | 72 | 0.965 | 0.93 |
| 17 | 17 | 63 | 69 | 0.924 | 0.8 |
| 18 | 18 | 74 | 74 | 0.946 | 0.96 |
| 19 | 19 | 69 | 71 | 0.986 | 0.91 |
| 20 | 20 | 69 | 70 | 0.964 | 0.93 |
| 21 | 21 | 65 | 66 | 0.992 | 0.98 |
| 22 | 22 | 64 | 68 | 0.97 | 0.92 |
| 23 | 23 | 66 | 66 | 1.0 | 0.98 |
| 24 | 24 | 74 | 74 | 0.986 | 0.93 |
| 25 | 25 | 64 | 66 | 0.954 | 0.9 |
| 26 | 26 | 66 | 64 | 0.969 | 0.87 |
| 27 | 27 | 60 | 60 | 0.983 | 0.9 |
| 28 | 28 | 60 | 65 | 0.928 | 0.95 |
| 29 | 29 | 61 | 60 | 0.909 | 0.91 |
| 30 | 30 | 62 | 61 | 0.959 | 0.95 |
| 31 | 31 | 62 | 64 | 0.984 | 0.94 |
| 32 | 32 | 63 | 62 | 0.944 | 1.0 |
| 33 | 33 | 38 | 38 | 1.0 | 0.89 |

**f. 186 recto**: sign-class agreement 0.931; same letter where the classes agree 0.943.

| our line | his line | our classes | his classes | class agreement | same letter on matched |
|---|---|---|---|---|---|
| 12 | 11 | 34 | 37 | 0.901 | 0.97 |
| 13 | 12 | 66 | 60 | 0.921 | 0.91 |
| 14 | 13 | 29 | 34 | 0.889 | 0.93 |
| 15 | 14 | 74 | 71 | 0.952 | 0.93 |
| 16 | 15 | 23 | 26 | 0.816 | 0.95 |
| 17 | 16 | 68 | 69 | 0.978 | 0.99 |
| 18 | 17 | 50 | 52 | 0.941 | 0.98 |
| 19 | 18 | 69 | 70 | 0.978 | 0.96 |
| 20 | 19 | 74 | 71 | 0.979 | 0.93 |
| 21 | 20 | 66 | 69 | 0.963 | 0.98 |
| 22 | 21 | 73 | 73 | 0.973 | 0.97 |
| 23 | 22 | 67 | 69 | 0.941 | 0.92 |
| 24 | 23 | 67 | 67 | 1.0 | 0.91 |
| 25 | 24 | 66 | 65 | 0.992 | 0.89 |
| 26 | 25 | 68 | 67 | 0.933 | 0.87 |
| 27 | 26 | 68 | 68 | 0.971 | 0.94 |
| 28 | 27 | 70 | 70 | 0.986 | 0.99 |
| 29 | 28 | 66 | 68 | 0.925 | 0.94 |
| 30 | 29 | 72 | 72 | 1.0 | 0.99 |
| 31 | 30 | 71 | 71 | 0.972 | 0.93 |
| 32 | 31 | 71 | 68 | 0.978 | 0.91 |
| 33 | 32 | 63 | 63 | 0.984 | 0.98 |
| 34 | 33 | 66 | 66 | 0.985 | 0.97 |
| 35 | 34 | 63 | 65 | 0.953 | 0.92 |
| 36 | 35 | 65 | 66 | 0.947 | 0.92 |
| 37 | 36 | 72 | 72 | 0.917 | 0.89 |
| 38 | 37 | 68 | 70 | 0.942 | 0.94 |
| 39 | 38 | 71 | 74 | 0.966 | 0.94 |
| 40 | 39 | 68 | 67 | 0.978 | 0.92 |
| 41 | 40 | 66 | 66 | 0.985 | 0.97 |
| 42 | 41 | 60 | 63 | 0.927 | 0.91 |
| 43 | 42 | 62 | 62 | 0.952 | 0.97 |
| 44 | 43 | 66 | 68 | 0.925 | 0.87 |
| 45 | 44 | 71 | 67 | 0.957 | 0.98 |
| 46 | 45 | 74 | 67 | 0.922 | 0.94 |
| 47 | 46 | 74 | 73 | 0.98 | 0.97 |
| 48 | 47 | 70 | 71 | 0.95 | 0.94 |
| 49 | 48 | 69 | 69 | 0.986 | 0.99 |
| 50 | 49 | 73 | 73 | 0.986 | 0.94 |
| 51 | 50 | 71 | 70 | 0.965 | 0.97 |
| 52 | 51 | 25 | 69 | 0.447 | 0.9 |

**f. 186 verso**: sign-class agreement 0.938; same letter where the classes agree 0.938.

| our line | his line | our classes | his classes | class agreement | same letter on matched |
|---|---|---|---|---|---|
| 1 | 0 | 73 | 75 | 0.959 | 0.93 |
| 2 | 1 | 68 | 70 | 0.928 | 0.8 |
| 3 | 2 | 67 | 64 | 0.947 | 0.9 |
| 4 | 3 | 72 | 66 | 0.928 | 0.94 |
| 5 | 4 | 69 | 68 | 0.978 | 0.91 |
| 6 | 5 | 77 | 76 | 0.967 | 0.95 |
| 7 | 6 | 73 | 72 | 0.966 | 0.96 |
| 8 | 7 | 68 | 70 | 0.942 | 0.97 |
| 9 | 8 | 71 | 68 | 0.878 | 0.92 |
| 10 | 9 | 67 | 67 | 0.97 | 0.85 |
| 11 | 10 | 70 | 71 | 0.965 | 0.94 |
| 12 | 11 | 67 | 69 | 0.971 | 0.94 |
| 13 | 12 | 76 | 76 | 0.895 | 0.84 |
| 14 | 13 | 67 | 66 | 0.992 | 0.97 |
| 15 | 14 | 62 | 64 | 0.937 | 0.93 |
| 16 | 15 | 62 | 65 | 0.929 | 0.97 |
| 17 | 16 | 19 | 20 | 0.974 | 1.0 |
| 18 | 17 | 70 | 70 | 0.971 | 0.94 |
| 19 | 18 | 65 | 70 | 0.963 | 0.97 |
| 20 | 19 | 68 | 67 | 0.933 | 1.0 |
| 21 | 20 | 66 | 68 | 0.94 | 0.98 |
| 22 | 21 | 69 | 68 | 0.978 | 0.94 |
| 23 | 22 | 64 | 65 | 0.992 | 0.94 |
| 24 | 23 | 71 | 71 | 0.986 | 0.93 |
| 25 | 24 | 68 | 67 | 0.978 | 0.94 |
| 26 | 25 | 38 | 38 | 1.0 | 0.97 |
| 27 | 26 | 16 | 18 | 0.882 | 0.93 |
| 28 | 27 | 66 | 63 | 0.837 | 0.98 |
| 29 | 28 | 66 | 66 | 1.0 | 0.98 |
| 30 | 29 | 63 | 64 | 0.961 | 0.98 |
| 31 | 30 | 63 | 62 | 0.96 | 0.97 |
| 32 | 31 | 72 | 72 | 0.917 | 0.92 |
| 33 | 32 | 70 | 66 | 0.912 | 0.94 |

Low lines: f. 186 recto line 52 (0.45) is our last line, two thirds unread; recto 16 (0.82) and verso 26-28 hold clear passages and code signs that the two readings treat differently.

## What this means

- Our reading confirms Rosson's at the sign level and is weaker than his in letters; it should be cited as an independent confirmation, not as a reading in its own right.
- The systematic a/n -> c/p error of our reader is the first thing to fix in any further machine reading of this cipher (a sheet with more a/n examples whose hook nearly closes, or a word-level decoder that may swap a/n and c/p where a reader is known to confuse them).
