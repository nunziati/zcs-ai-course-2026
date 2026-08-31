# Corso di AI applicata — Zucchetti Centro Sistemi

Cinque lezioni da quattro ore, dal 2 all'11 settembre 2026, ore 9–13, online.
Docente: Giacomo Nunziati.

È la parte di AI applicata del corso Fondimpresa *Digitalizzazione dei processi
aziendali* (ID 4102444). Qui trovi il materiale: notebook, slide e istruzioni.

## Non devi installare niente

I notebook girano su **Google Colab**, dentro al browser. Ti serve solo l'account
Google che usi già.

1. Apri la lezione dalla tabella qui sotto e clicca **Open in Colab**.
2. Esegui le celle dall'alto verso il basso, insieme al docente.

La prima cella installa le librerie e scarica i dati: un paio di minuti. Non devi
preparare niente prima della lezione.

Se vuoi controllare in anticipo che tutto giri, apri il notebook di verifica. Non è
obbligatorio.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/nunziati/zcs-ai-course-2026/blob/main/verifica-ambiente.ipynb)

## Le cinque lezioni

| | Data | Argomento | Notebook |
|---|---|---|---|
| Lezione 1 | mercoledì 2 settembre | [CNN fine-grained e multimodalità immagine più tabellare](lezione-1/) | in arrivo |
| Lezione 2 | venerdì 4 settembre | [Dati tabellari, explainability e incertezza](lezione-2/) | in arrivo |
| Lezione 3 | lunedì 7 settembre | [Anomaly detection e manutenzione predittiva](lezione-3/) | in arrivo |
| Lezione 4 | mercoledì 9 settembre | [Video e computer vision realtime](lezione-4/) | in arrivo |
| Lezione 5 | venerdì 11 settembre | [AI generativa multimodale, voce e video](lezione-5/) | in arrivo |

Il notebook di ogni lezione compare nella sua cartella, di norma la sera prima.

## Se ti tocca la CPU

Colab dà una GPU gratuita, ma non sempre e non a tutti. Ogni notebook ha in cima le
costanti `EPOCHS`, `BATCH_SIZE` e `N_SAMPLES`, già impostate su valori che girano
anche senza GPU: il notebook funziona lo stesso, su meno dati e con risultati più
grezzi.

I notebook sono pubblicati **con gli output già dentro**. Se una cella è lenta o va
storta, il risultato atteso lo leggi lì, senza aspettare, e intanto segui la lezione
sullo schermo condiviso.

Per chiedere la GPU: *Runtime → Cambia tipo di runtime → GPU T4*.

## Come è organizzata la repo

```
lezione-1/ ... lezione-5/   una cartella per lezione: notebook, slide, note
verifica-ambiente.ipynb     controllo rapido di Python, GPU e librerie
```

I dataset **non stanno nella repo**: sono troppo grandi. I sottoinsiemi ridotti usati
a lezione sono pubblicati nelle
[release](https://github.com/nunziati/zcs-ai-course-2026/releases) e li scarica la
prima cella del notebook. Il link alla fonte ufficiale completa resta in una cella
commentata, per chi poi vuole rifare tutto sui dati interi.

## Eseguirlo in locale

Sono `.ipynb` normali: girano anche in locale con VSCode o Jupyter. Durante le lezioni
però l'unico ambiente supportato è Colab. In locale servono Python 3.10 o superiore,
PyTorch e le librerie elencate nella prima cella di ogni notebook.

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
