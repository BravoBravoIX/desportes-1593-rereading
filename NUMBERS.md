# Where the numbers come from

Every number in [README.md](README.md) and [method/README.md](method/README.md), and the file in this repository it is taken from. All were copied from the records written when the work was done (18 October 2026), not typed from memory. Rounded figures in the README are rounded from these.

| number | meaning | source in this repository |
|---|---|---|
| 95.9 %, 93.1 %, 93.8 % | sign-class agreement with Rosson's reading, f. 189 / f. 186 recto / f. 186 verso | `data/compare-rosson/f189.json`, `f186r.json`, `f186v.json`: `total.class_agreement` (0.959, 0.931, 0.938) |
| 93.5 %, 94.3 %, 93.8 % | same letter chosen where the classes agree | same files: `total.letter_agreement_on_matched_classes` (0.935, 0.943, 0.938) |
| 33 lines; three passes voted on f. 189 | lines and passes per line | `data/f189/signs.txt` (33 rows); `data/f189/reading.json` `passes_per_line` |
| f. 186 verso: two passes on lines 1-11, one elsewhere; recto: two passes on 12-17, one elsewhere | passes per line | `data/f186v/reading.json`, `data/f186r/reading.json` `passes_per_line` |
| 1245 aligned signs, 858 kept | stage A alignment of the known text to f. 188v | 858 = number of entries in `data/known-text/f188v-labels.json` `signs`; 1245 from our stage A record (stated in the same file's `note`) |
| 116 of 120 (96.7 %) | stage A check of a seeded sample of labels, by Claude | our stage A record (also in `data/known-text/f188v-labels.json` `note`); the per-label verdicts were not saved (see `method/README.md`) |
| 294 known signs | held-out lines 14-17, 20 of f. 188v | `data/known-text/scores/*.score.json` `signs_truth`; recomputed by `method/score_heldout.py` |
| 0.878 / 0.888 / 0.878 | sign accuracy of passes a / b / c on held-out lines | `data/known-text/scores/heldout-pass-a.score.json`, `-b`, `-c` `sign_acc` (0.8776, 0.8878, 0.8776); recomputed by `method/score_heldout.py` |
| 0.901 | sign accuracy of the three-pass vote | `data/known-text/scores/heldout-vote.score.json` `sign_acc` (0.9014); recomputed by `method/score_heldout.py` (29 edits / 294) |
| 0.826 | letter accuracy of the decode of the vote | `heldout-vote.score.json` `char_acc` (0.8255) |
| 0.930 | letter accuracy when the known signs are decoded (ceiling) | `heldout-known-text.score.json` `char_acc` (0.9295) |
| about 0.88 per sign for a single pass | single-pass level | the three single-pass scores above |
| 0.792 on 312 signs | vote on the confirmation lines 6, 10-13 (sheet v3) | `data/known-text/scores/confirmation-vote.score.json` `sign_acc` (0.7917), `signs_truth` (312) |
| 2.710, 2.724, 2.733 bits/letter | real pages f. 189, f. 186 recto, f. 186 verso | `data/<page>/controls.json` `real.bits_per_letter` |
| 4.194 / 4.231 / 4.273; 4.129 / 4.208 / 4.160; 4.222 / 4.167 / 4.274 | shuffled-sign controls, seeds 1-3, per page | `data/<page>/controls.json` `controls_shuffled[].bits_per_letter` |
| "about 2.7 against 4.2" | summary of the two rows above | as above |
| 2.66-2.89 bits/letter | last fifth of each page decoded alone | `data/<page>/controls.json` `heldout_block.bits_per_letter` (2.729, 2.658, 2.888) |
| 10 windows per page; 2 changes applied (1 on f. 189, 1 on f. 186 verso, 0 on the recto) | correction pass | `data/<page>/corrections.json` (`changes`, `decision`) |
| piece widths 1150 / 500 / 600 px, enlargement 1.5x / 2.0x / 1.8x, offset 250 px | the three reader passes | our reading records; also stated in `reading/f189-french.md` (Method) |
| byte counts in the check output | sizes of `data/<page>/plaintext.txt` and `plaintext-by-line.txt` | `sh decode/check.sh` |
| 1 October 2026 | date of Rosson's first reading | his repository and Tomokiyo's announcement (links in README) |
