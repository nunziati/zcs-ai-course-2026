# Corso di AI applicata — Zucchetti Centro Sistemi

Cinque lezioni da quattro ore, dal 2 all'11 settembre 2026, ore 9–13, online.
Docente: Giacomo Nunziati.

È la parte di AI applicata del corso Fondimpresa *Digitalizzazione dei processi
aziendali* (ID 4102444). Qui trovi il materiale: notebook, slide e istruzioni.

## Non devi installare niente

I notebook girano su **Google Colab**, dentro al browser. Ti serve solo l'account
Google che usi già.

1. Apri la lezione dalla tabella qui sotto e clicca **Open in Colab**.
2. Esegui le celle dall'alto verso il basso.

La prima cella installa le librerie e scarica i dati: un paio di minuti.

Se vuoi controllare prima che tutto giri, apri il notebook di verifica.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/nunziati/zcs-ai-course-2026/blob/main/verifica-ambiente.ipynb)

Il corso dà per noti alcuni argomenti di machine learning. La lista, con dove
recuperare ciascuno, sta in [PREREQUISITI.md](PREREQUISITI.md).

## Le cinque lezioni

| | Data | Argomento | Notebook |
|---|---|---|---|
| Lezione 1 | mercoledì 2 settembre | [CNN fine-grained e multimodalità immagine più tabellare](lezione-1/) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/nunziati/zcs-ai-course-2026/blob/main/lezione-1/lezione-1.ipynb) |
| Lezione 2 | venerdì 4 settembre | [Dati tabellari clinici, explainability e incertezza](lezione-2/) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/nunziati/zcs-ai-course-2026/blob/main/lezione-2/lezione-2.ipynb) |
| Lezione 3 | lunedì 7 settembre | [Anomaly detection e manutenzione predittiva](lezione-3/) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/nunziati/zcs-ai-course-2026/blob/main/lezione-3/lezione-3.ipynb) |
| Lezione 4 | mercoledì 9 settembre | [Video e computer vision real-time](lezione-4/) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/nunziati/zcs-ai-course-2026/blob/main/lezione-4/lezione-4.ipynb) pipeline<br>[![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/nunziati/zcs-ai-course-2026/blob/main/lezione-4/metodi-lezione-4.ipynb) metodi |
| Lezione 5 | venerdì 11 settembre | [AI generativa multimodale, voce e video](lezione-5/) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/nunziati/zcs-ai-course-2026/blob/main/lezione-5/caso-studio-metropt.ipynb) |

## Se ti tocca la CPU

Colab dà una GPU gratuita, ma non sempre e non a tutti. Nessun notebook la
pretende: quelli che la sfruttano hanno in cima delle costanti già impostate su
valori che girano anche senza, su meno dati e con risultati più grezzi. I notebook
delle Lezioni 2 e 3 e il caso di studio della Lezione 5 non la usano affatto.

I notebook sono pubblicati **con gli output già dentro**. Se una cella è lenta o va
storta, il risultato atteso lo leggi lì, senza aspettare.

Per chiedere la GPU: *Runtime → Cambia tipo di runtime → GPU T4*.

## Come è organizzata la repo

```
lezione-1/ ... lezione-5/   una cartella per lezione: notebook, slide, note
verifica-ambiente.ipynb     controllo rapido di Python, GPU e librerie
PREREQUISITI.md             cosa il corso dà per noto, e dove recuperarlo
```

I dataset **non stanno nella repo**: sono troppo grandi. I sottoinsiemi ridotti usati
a lezione sono pubblicati nelle
[release](https://github.com/nunziati/zcs-ai-course-2026/releases) e li scarica la
prima cella del notebook. Il link alla fonte ufficiale completa sta nella prima cella
di testo del notebook, per chi vuole rifare tutto sui dati interi.

## I dati e le loro licenze

I dataset sono pubblici e ognuno ha la sua licenza, diversa dalla nostra. Le
release riportano fonte, attribuzione e che cosa è stato cambiato rispetto
all'originale.

| Dati | Fonte | Licenza | Release |
|---|---|---|---|
| Uccelli, immagini più attributi | [CUB-200-2011](https://www.vision.caltech.edu/datasets/cub_200_2011/), Caltech | ricerca e didattica **non commerciali** | [`dati-cub`](https://github.com/nunziati/zcs-ai-course-2026/releases/tag/dati-cub) |
| Esami tiroidei | [UCI Thyroid Disease](https://archive.ics.uci.edu/dataset/102/thyroid+disease) | CC BY 4.0 | [`dati-thyroid`](https://github.com/nunziati/zcs-ai-course-2026/releases/tag/dati-thyroid) |
| Turbine, run-to-failure | [NASA C-MAPSS](https://zenodo.org/records/15346912) | dato pubblico USA, CC BY 4.0 su Zenodo | [`dati-cmapss`](https://github.com/nunziati/zcs-ai-course-2026/releases/tag/dati-cmapss) |
| Stalla con otto vitelli, video annotato | [8-Calves](https://huggingface.co/datasets/tonyFang04/8-calves) | CC BY 4.0 | [`dati-video`](https://github.com/nunziati/zcs-ai-course-2026/releases/tag/dati-video) |
| Compressore di un treno in servizio | [UCI MetroPT-3](https://archive.ics.uci.edu/dataset/791/metropt+3+dataset) | CC BY 4.0 | [`dati-metropt`](https://github.com/nunziati/zcs-ai-course-2026/releases/tag/dati-metropt) |

Citazioni obbligatorie:

- **CUB-200-2011** — Wah C., Branson S., Welinder P., Perona P., Belongie S., *The
  Caltech-UCSD Birds-200-2011 Dataset*, Computation & Neural Systems Technical
  Report CNS-TR-2011-001, California Institute of Technology, 2011. I termini della
  fonte limitano l'uso a **ricerca e didattica non commerciali**: qui c'è per il
  corso, non portarlo in un prodotto.
- **UCI Thyroid Disease** — dati del Garavan Institute e di J. Ross Quinlan, 1987,
  via UCI Machine Learning Repository.
- **NASA C-MAPSS** — A. Saxena, K. Goebel, *Turbofan Engine Degradation Simulation
  Data Set*, NASA Prognostics Data Repository, NASA Ames Research Center.
- **8-Calves** — Y. Fang et al., *8-Calves Dataset: Benchmarking Object Detection and
  Identity Classification in Occlusion-Rich Environments*, arXiv:2503.13777.
- **MetroPT-3** — N. Davari, B. Veloso, R. P. Ribeiro, P. M. Pereira, J. Gama, *Predictive
  maintenance based on anomaly detection using deep learning for air production unit in
  the railway industry*, IEEE DSAA 2021, via UCI Machine Learning Repository.

Ogni archivio si scarica da un URL fisso, che non cambia più:

```python
!wget -q https://github.com/nunziati/zcs-ai-course-2026/releases/download/dati-cub/cub-200-2011-20-classi.tgz
!tar xzf cub-200-2011-20-classi.tgz
```

Gli archivi sono **ridotti** dove serve: 20 classi di uccelli su 200, 30 secondi del
video di 8-Calves, i segnali di MetroPT-3 in medie al minuto. Il motivo è il tempo, non
la banda: Colab azzera il disco a ogni sessione e ognuno riscarica tutto ogni volta. Gli
script che hanno costruito le release stanno in [`scripts/`](scripts/), così si vede
esattamente cosa è stato tolto. Fa eccezione l'estratto di 8-Calves, costruito a mano:
le modifiche sono elencate nell'archivio, in `ATTRIBUZIONE.txt`.

## Eseguirlo in locale

Sono `.ipynb` normali: girano anche in locale con VSCode o Jupyter, ma sono pensati
per Colab. In locale servono Python 3.10 o superiore, PyTorch e le librerie elencate
nella prima cella di ogni notebook.

## Licenza

Il materiale è di Giacomo Nunziati, 2026, e puoi riusarlo al lavoro senza chiedere
niente a nessuno. Due licenze, perché testo e codice hanno bisogni diversi:

- **testo, slide e celle di spiegazione**: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.it) — copia, modifica e usa anche in azienda, citando l'autore;
- **codice dei notebook**: [MIT](https://opensource.org/licenses/MIT) — stessa libertà, con la formula standard del software.

I testi integrali stanno in [LICENSE](LICENSE) per il testo e in
[LICENSE-CODE](LICENSE-CODE) per il codice.

**Dataset, pesi dei modelli e librerie di terze parti non sono coperti da questa
licenza**: restano dei rispettivi autori. Ogni notebook dichiara la licenza di quello
che usa, e le release che contengono dati altrui riportano fonte e attribuzione. È una
distinzione che conviene tenere a mente anche fuori da qui: la licenza del codice e
quella dei pesi di un modello spesso non coincidono.
