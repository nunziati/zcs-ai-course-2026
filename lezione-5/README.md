# Lezione 5 — venerdì 11 settembre 2026, ore 9:00–13:00

**Modulo 5 — AI generativa multimodale, voce e video**

Il notebook di questa lezione è un **caso di studio di anomaly detection e manutenzione
predittiva** su dati industriali reali, presentato alla fine della mattina, prima del test.
Si apre da qui: serve solo il tuo account Google, e la prima cella scarica i dati da sola.

## Caso di studio: il compressore di un treno

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/nunziati/zcs-ai-course-2026/blob/main/lezione-5/caso-studio-metropt.ipynb)

`caso-studio-metropt.ipynb` — **le celle devono essere eseguite dall'alto in basso.** Sette
mesi di segnali del compressore di un treno della metropolitana di Porto in servizio, e i
rapporti di manutenzione con quattro guasti. Due detector a confronto sugli stessi dati — una
regola scritta da chi conosce la macchina, e un modello del comportamento normale, Isolation
Forest — valutati come li valuterebbe un reparto di manutenzione: guasto per guasto, con i
falsi alert contati a settimana.

La prima cella contiene le scelte del caso, marcate `PUNTO DI VARIAZIONE`: la durata delle
finestre, il periodo di addestramento, le soglie e il preavviso. Cambiarle e rieseguire tutto
è l'esercizio. L'esecuzione completa richiede pochi secondi, e la GPU non serve.

Il notebook arriva con gli output già dentro, quindi si legge anche senza eseguirlo.

## I dati

**MetroPT-3**: i segnali dell'unità di produzione dell'aria di un treno della metropolitana di
Porto, da febbraio ad agosto 2020, e i quattro guasti riportati dall'azienda di manutenzione.
Dalla release [`dati-metropt`](https://github.com/nunziati/zcs-ai-course-2026/releases/tag/dati-metropt),
con le medie al minuto dei quindici segnali: l'originale ha un campione ogni dieci secondi
circa. L'archivio contiene l'attribuzione completa e l'elenco di che cosa è cambiato.

> Davari, N., Veloso, B., Ribeiro, R. P., Pereira, P. M., Gama, J. *Predictive maintenance
> based on anomaly detection using deep learning for air production unit in the railway
> industry.* IEEE DSAA 2021.

Fonte: [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/791/metropt+3+dataset),
licenza [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

## Le slide

- [`lezione-5.html`](https://nunziati.github.io/zcs-ai-course-2026/lezione-5/lezione-5.html)
  — la versione da schermo, si apre nel browser e funziona anche senza rete.
- [`lezione-5.pdf`](./lezione-5.pdf) — 45 pagine, per leggere e annotare.

Torna al [README](../README.md) per le indicazioni generali.
