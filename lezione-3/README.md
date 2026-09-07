# Lezione 3 — lunedì 7 settembre 2026, ore 9:00–13:00

**Modulo 3 — Rilevazione di anomalie e manutenzione predittiva**

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/nunziati/zcs-ai-course-2026/blob/main/lezione-3/lezione-3.ipynb)

Clicca il badge qui sopra: non c'è niente da installare, serve solo il tuo account Google.
Il notebook si esegue dall'alto in basso e la prima cella scarica i dati da sola.

Questo notebook **non usa la GPU** e non installa nulla: girano solo pandas, scikit-learn
e matplotlib, che su Colab ci sono già.

## Cosa c'è dentro

Undici celle di codice, una cosa per cella. Tre sono marcate `PUNTO DI VARIAZIONE`:
contengono una costante che modifichiamo insieme in aula e rieseguiamo.

Il notebook arriva con tutti gli output già dentro, quindi si legge anche senza eseguirlo.

Il filo è uno solo: **in questi dati le anomalie non ci sono**. L'unica cosa registrata è
quanti cicli mancano al guasto. «Anomalia» non è un dato, è una decisione che prendiamo
noi, e da come la prendiamo dipende ogni numero che viene dopo.

## Le slide

- [`lezione-3.html`](https://nunziati.github.io/zcs-ai-course-2026/lezione-3/lezione-3.html)
  — la versione da schermo, si apre nel browser e funziona anche senza rete.
- [`lezione-3.pdf`](./lezione-3.pdf) — 60 pagine, per leggere e annotare.

## I dati

NASA C-MAPSS, sottoinsieme FD001, dalla release
[`dati-cmapss`](https://github.com/nunziati/zcs-ai-course-2026/releases/tag/dati-cmapss).
Cento motori turbofan simulati, ventuno sensori, 20.631 righe. Dato governativo
statunitense non soggetto a copyright; il deposito Zenodo lo dichiara CC BY 4.0.

Torna al [README](../README.md) per le indicazioni generali.
