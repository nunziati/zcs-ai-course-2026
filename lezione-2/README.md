# Lezione 2 — venerdì 4 settembre 2026, ore 9:00–13:00

**Modulo 2 — Dati tabellari clinici, explainability e incertezza**

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/nunziati/zcs-ai-course-2026/blob/main/lezione-2/lezione-2.ipynb)

Clicca il badge qui sopra: non c'è niente da installare, serve solo il tuo account Google.
Il notebook si esegue dall'alto in basso e la prima cella scarica i dati da sola.

Questo notebook **non usa la GPU**: il modello più lento impiega una decina di secondi
su CPU. Non serve cambiare il tipo di runtime.

## Cosa c'è dentro

Tre celle sono marcate `PUNTO DI VARIAZIONE`: contengono una costante che modifichiamo
insieme in aula e rieseguiamo. Il resto è già scritto e va solo eseguito.

Il notebook arriva con tutti gli output già dentro, quindi si legge anche senza eseguirlo.

Dodici celle di codice, una cosa per cella. Si parte dai valori mancanti, si sale dalla
regressione logistica al gradient boosting e all'EBM, e si arriva a un AUC di 0,997 —
che poi viene smontato: da dove viene quel numero, quando due modelli sono davvero
diversi, e cosa succede alle probabilità quando cambia il centro di provenienza.

## Le slide

- [`lezione-2.html`](https://nunziati.github.io/zcs-ai-course-2026/lezione-2/lezione-2.html)
  — la versione da schermo, si apre nel browser e funziona anche senza rete.
- [`lezione-2.pdf`](./lezione-2.pdf) — 73 pagine, per leggere e annotare.

## I dati

UCI Thyroid Disease, task `sick`, dalla release
[`dati-thyroid`](https://github.com/nunziati/zcs-ai-course-2026/releases/tag/dati-thyroid).
2.800 righe di training e 972 di test, 29 attributi, licenza CC BY 4.0.

Torna al [README](../README.md) per le indicazioni generali.
