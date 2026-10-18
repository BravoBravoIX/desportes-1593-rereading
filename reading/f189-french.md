# f. 189: Baudouin-Desportes to Girolamo Frachetta, Paris, 22 July 1593 (French)

> **Independent re-reading; first reading published by Paolo Rosson, 1 Oct 2026 (pangoleen/desportes-1593).**
> Our reading was made before his text was opened and was not changed afterwards. It is a machine reading with the published key; where the two readings differ, his is the better one (see [comparison-rosson.md](comparison-rosson.md)).
>
> **Status of this page:** three reader passes voted on all 33 lines (the level measured at 0.90 per sign on known text).

| | |
|---|---|
| Letter | Baudouin-Desportes (Paris) to Girolamo Frachetta, dated 22 July 1593 |
| Manuscript | BnF Français 3984, f. 189 (cipher throughout) |
| Images | Gallica ark:/12148/btv1b9060633d, view 353 (https://gallica.bnf.fr/ark:/12148/btv1b9060633d/f353.item) |
| Key | Tomokiyo's published Catholic League polyphonic key (cryptiana, mayenne.htm, 2023); we did not derive it |
| Method | Signs read by Claude Opus 5.5 with a reference sheet of signs cut from f. 188v (sheet v3), three passes with different cuts and magnifications (a: 1150 px pieces at 1.5x; b: 500 px at 2.0x; c: 600 px at 1.8x, first cut offset 250 px), majority vote per sign; correction pass on the 10 lowest-scoring windows, 1 change applied after looking at the image ([../data/f189/corrections.json](../data/f189/corrections.json)); polyphone letter at each occurrence chosen by a period French 5-gram model and recorded in the key; word breaks in Normalised by code from a period French dictionary. See [../method/README.md](../method/README.md) |
| Reader accuracy on known text | f. 188v held-out lines (294 signs): three-pass vote 0.901 per sign; decode 0.826 per letter (ceiling with perfect signs 0.930). **All 33 lines of f. 189 have the three-pass vote.** |
| Controls (same decoder) | real text 2.710 bits/letter, dictionary cover 0.668; shuffled signs (seeds 1-3) 4.194 / 4.231 / 4.273 bits/letter; held-out last fifth decoded alone 2.729 bits/letter, cover 0.659 ([../data/f189/controls.json](../data/f189/controls.json)) |
| Data and decode | [../data/f189/](../data/f189/): key.json (with the letter chosen at every occurrence) and signs.txt; [../decode/decode.py](../decode/decode.py) reproduces the Literal below exactly ([../decode/check.sh](../decode/check.sh)) |

Doubtful throughout: about one sign in ten is misread at the measured accuracy, and the 5-gram model sometimes picks the wrong letter of a pair (g/t, c/p, e/r): e.g. "tentilhomme" for gentilhomme. These are left as the key gives them in Literal and Normalised.

## Literal

The key's output exactly, one manuscript line per row (line numbers in backticks are not part of the text). Code signs {code}; unread signs ?.

**f. 189**

`01` nostreuolonteestoitbonnelapuissanceassesgrandepourlafairereussiezamisasa  
`02` uoirsiralacontinuenouseussionspeusuosistrecestcequinousafaitdemeurerco  
`03` isetencesentrefaitesnosamisnesefontpasseulementmontresneutresmagisenne  
`04` misformelzetfaitcequilzontpeupourtendrealaruinedelamydelhommeducoleteetleuostre  
`05` spaslauoireienespartdroposanstanostuashiepttantostunchersecon  
`06` dee{code}nostredocteurgentinaquiamieulxiourlepersonnagequenuldesautresiutqu  
`07` esnycoucherdelautoritedesoniuoirlauoirmisencompromisetfaitbeaucoup  
`08` depreiudicesinostreoncleeustuoulutlersuiuantlapromessequilenauoit  
`09` faitenceluyquilnyatrouueretquelhommedelachesareustdonardcudautresasseura  
`10` ncesquedesparoleslatestebaisseronleustentremaiscroirsquilnyapeuapenser  
`11` toutcequisepouuoitdemieusiestoitle  
`12` protectionettaitbeletempsilnesestpasfaitilsenloitlatersurlimprudec  
`13` cedumonarqueetdetsirasaintestetelequilnauoitfaitnulceeparatifoudumoissi  
`14` petitequelemoindretentilhommeenunequerellemeneustfaitdaucateteetpouruostr  
`15` epostescestrucautrebelactequelelicentiementquefeistuostreauaiteurieueulx  
`16` croirecequeuousmespriuezquilnyaaulchangementtoutestoiscestunsditestenne  
`17` quenostrecoquiagestenenousaigeieneccorbede{code}quelonnousnieditpro?an  
`18` uouluetpennestequeietparoleslesplusextraunfantesque{code}ieussepenseperdretoutue  
`19` ierestecriuedeparadisieussepassebienplusaungsetrauailleeseruinerfaire  
`20` c?sepeuttantquesansnostreprudenceonnequerroitpasuneheureetpourlercepen  
`21` sebastieuneruineorieneseroispassicharitableieleconfessesinostreai  
`22` ducoleterauouloit{code}leralhomedelachesneilobligeroitinsiaymentnostre  
`23` amyquiesttoutsienet{code}acequiregardeuostrepensioncelanesepeultparnulne  
`24` lasistequeleperlataquilapieceestaffecteretilnestpastempsdeluyrienleuresaes  
`25` teuostremalheur{code}lemiracourageilsepresengrecqeutresoccasionsietien  
`26` quelonauralatersurdansceudeioursleuoiagede{code}nesqueeleplusprenicieulx  
`27` quechosedumondeilafait{code}hangerderelig?ionauretosser{code}milescusleue  
`28` uglestoiteuinesanssechangementnostreelegatafaitcequilapeupou  
`29` uriretpatpolilnembrasseleurdsfaireauectantcenesdeurquilanegli  
`30` gecequiestoitduseruicedeson{code}iusquespanuoirfaittepieunseuldenosu  
`31` oerfzquieussentinfinimentprofitemaiscenestoitpascequildefroita?  
`32` contrairedehasterledesmembrementdenostreestatulalettredequeuous  
`33` sauersahurallestatgeneraldenosaffaires  

## Normalised (editorial)

The same letters with word breaks made by code (dictionary segmentation by code; see [../method/README.md](../method/README.md)); no letter changed, added or removed; u and i as the key gives them; word[?] = not in the dictionary or rare there (doubtful); a word running over a line end is split with a hyphen; apostrophes after elided l d qu s n c m t are editorial. No punctuation added.

**f. 189**

`01` nostre uolonte estoit bonne la puissance asses grande pour la faire r[?] eussiez amis a sa-  
`02` uoir s'ira la continue nous eussions peu s'uosist re c'est ce qui nous a fait demeurer co-  
`03` is[?] et en ces entrefaites[?] nos amis ne se font pas seulement montres neutres[?] m'agis enne-  
`04` mis forme lz[?] et fait ce qu'ilz ont peu pour tendre a la ruine de l'amy de l'homme du col ete et le uostre-  
`05` s[?] pas la uoire ie ne s part dropo[?] sans ta nos tu a shiept[?] tantost un cher secon-  
`06` dee[?] {code} nostre docteur gent in a qui a mieulx iour le personnage que nul des autres iut[?] qu-  
`07` e s n y coucher de l'autorite de son i[?] uoir l'auoir mis en compromis[?] et fait beaucoup  
`08` de preiudice si nostre oncle eust uoulut l'er suiuant la promesse qu'il en auoit  
`09` fait en celuy qu'il n y a trouuer et quel homme de laches ar eust dona rdcud[?] autres as seur a  
`10` n ces que des paroles la teste baisser on l'eust entre mais c roir[?] s qu'il n y a peu a penser  
`11` tout ce qui se pou uoit demi eu si estoit le  
`12` protection et tait[?] be le temps il ne s'est pas fait ils en l'oit la te rsurlimp[?] rude c  
`13` ce du monarque et d'et s'ira saintes tete le qu'il n'auoit fait nul ce e[?] par a ti fou du mois si  
`14` petite que le moi n d retenti[?] l'homme en une querelle m'en eust fait d'au ca tete et pour uostr-  
`15` e postes ces truc[?] autre bel acte que le li centieme nt[?] que feist uostre auait eu rieu eulx  
`16` croire ce que uous mes priuez qu'il n y a au l changement toutes toi s c'est uns dit est en ne  
`17` que nostre coq uia geste ne nous aige ie ne c c'or be de {code} quel on nous n'ie dit pro[?] ? a n'  
`18` uoulu et pennes[?] te que iet paroles les plus extra[?] un fa n tes que {code} ieu s se pense perdre tout ue-  
`19` i er est ecriue[?] de paradis ieu s se passe bien plus a ung se trauaillee[?] se ruiner faire  
`20` c ? se peut tant que sans nostre prudence on ne q[?] uerroit pas une heure et pour l'er ce pen-  
`21` se bastie[?] une ruine or ie ne se rois pas si charitable ie le confesse si nostre ai  
`22` du col et er a uouloit {code} l'er a l'home de laches ne il oblige roit in si ayment nostre  
`23` amy qui est tout sien et {code} a ce qui regarde uostre pension cela ne se peult par nul ne  
`24` la si s te que le perla[?] ta qui la piece est affecte r[?] et il n'est pas temps de luy rien leures a es-  
`25` te uostre malheur {code} le m'ira courage il se pres en grec qeu[?] tres occasion si et ie n  
`26` quel on aura la te r[?] sur dans c'eu de iours le uoiage de {code} ne s que e[?] le plus pren[?] ici eulx  
`27` que chose du monde il a fait {code} hangerderelig[?] ? io[?] naure tos s'er {code} m'il escus le ue-  
`28` u g[?] les toi te ui ne sans se changement nostre e[?] legat[?] a fait ce qui la peu p[?] ou-  
`29` urir et pat[?] pol il n'embrasse leur d s faire auec tant ce ne s de ur[?] qui la negli-  
`30` ge ce qui estoit du seruice de son {code} iusques pan uoir faitte[?] pie un seul de nos u-  
`31` oer[?] fz[?] qui eussent infiniment profite mais c'en estoit pas ce qu'il de froit a ?  
`32` contraire de haste r[?] le des membre m ent[?] de nostre est a tu la lettre de que uous  
`33` sa uers ah urall[?] estat general de nos affaires  

Check (made when this file was written): letters of Normalised = letters of Literal, clear passages identical: **passed**.
