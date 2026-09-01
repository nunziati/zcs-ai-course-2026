# Lezione 1 — mercoledì 2 settembre 2026, ore 9:00–13:00

**Modulo 1 — CNN fine-grained e multimodalità immagine più tabellare**

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/nunziati/zcs-ai-course-2026/blob/main/lezione-1/lezione-1.ipynb)

Clicca il badge qui sopra: non c'è niente da installare, serve solo il tuo account Google.
Il notebook si esegue dall'alto in basso e la prima cella scarica i dati da sola.

**Se hai una GPU a disposizione su Colab, accendila** — *Runtime → Cambia tipo di runtime →
T4*. Non è obbligatorio: senza GPU il notebook gira lo stesso, l'unico passaggio lento
diventa l'estrazione delle feature, che passa da una quindicina di secondi a circa un minuto.

## Cosa c'è dentro

Ci sono **tre celle marcate `PUNTO DI VARIAZIONE`**: sono le uniche che tocchiamo insieme in
aula, cambiando la costante sulla prima riga e rieseguendo. Tutto il resto è già scritto ed è
solo da eseguire.

Il notebook arriva con **tutti gli output già dentro**, quindi puoi leggerlo anche senza
eseguirlo, e se una cella dovesse fallire in aula il risultato resta visibile.

## I dati

CUB-200-2011 ridotto a 20 classi, dalla release
[`dati-cub`](https://github.com/nunziati/zcs-ai-course-2026/releases/tag/dati-cub).
Attribuzione e termini d'uso stanno nella prima cella del notebook e vanno letti: l'uso è
ristretto a ricerca e didattica **non commerciali**.

Torna al [README](../README.md) per le indicazioni generali.
