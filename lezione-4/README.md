# Lezione 4 — mercoledì 9 settembre 2026, ore 9:00–13:00

**Modulo 4 — Video e computer vision realtime**

Ci sono **due notebook**. Servono a cose diverse e si aprono tutti e due da qui: serve solo
il tuo account Google, la prima cella scarica i dati da sola e quelle che eseguono un
detector installano `ultralytics` al primo uso.

## 1. La pipeline, dal frame al numero

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/nunziati/zcs-ai-course-2026/blob/main/lezione-4/lezione-4.ipynb)

`lezione-4.ipynb` — **si esegue dall'alto in basso.** Una pipeline sola, montata uno stadio
alla volta — decodifica, inferenza, post-processing, tracking, regola di evento — e alla
fine misurata per intero: quanto costa ogni stadio, quanti frame al secondo regge, e di
quanto sbaglia il numero che consegna.

La prima cella contiene la configurazione. Cambiarla e rieseguire tutto è l'esercizio della
giornata.

## 2. I metodi, una cella alla volta

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/nunziati/zcs-ai-course-2026/blob/main/lezione-4/metodi-lezione-4.ipynb)

`metodi-lezione-4.ipynb` — **si esegue in qualsiasi ordine.** Ogni cella è indipendente:
importa quello che le serve, costruisce i propri dati e stampa la propria conclusione. Se ne
può eseguire una sola, o saltarne metà.

Venti sezioni, una per meccanismo: dalla ridondanza fra frame consecutivi alla latenza al
99° percentile, passando per detection, soppressione dei duplicati, tracking e metriche.
Ogni sezione mostra il risultato anche sui frame, non solo in numeri.

## Il detector

Tutti e due i notebook hanno una costante `DETECTOR` marcata `PUNTO DI VARIAZIONE`:

| valore | modello | ms per frame, CPU |
|---|---|---|
| `yolo11n` | YOLO11 nano, 2,6 M parametri | ~20 |
| `yolo11s` | YOLO11 small, 9,5 M parametri | ~45 |
| `yolo11m` | YOLO11 medium, 20,1 M parametri — è il valore di partenza | ~115 |
| `rtdetr` | RT-DETRv2-R18, 20,2 M parametri | ~190 |

I tempi sono presi su una CPU a otto thread e servono solo a confrontare i quattro fra loro:
sulla tua macchina saranno altri. Cambiare quella costante cambia i numeri di mezzo notebook,
e in due celle cambia anche la conclusione. È voluto.

Nessuno dei due notebook ha bisogno della GPU. Con la GPU le celle che misurano un tempo
vanno una decina di volte più veloci; i risultati non cambiano.

Tutti e due arrivano con gli output già dentro, quindi si leggono anche senza eseguirli.

## I dati

**8-Calves**, estratto: 600 frame (30 secondi a 20 frame al secondo, 800×600) di una
stalla ripresa dall'alto con otto vitelli, più le annotazioni — un bounding box per vitello
per frame, con l'identità. Dalla release
[`dati-video`](https://github.com/nunziati/zcs-ai-course-2026/releases/tag/dati-video).

> Fang, Y. et al. *8-Calves Dataset: Benchmarking Object Detection and Identity
> Classification in Occlusion-Rich Environments.* arXiv:2503.13777.

Fonte: [huggingface.co/datasets/tonyFang04/8-calves](https://huggingface.co/datasets/tonyFang04/8-calves),
licenza [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). L'estratto è ritagliato
e ricompresso rispetto all'originale; l'archivio contiene l'attribuzione completa.

Torna al [README](../README.md) per le indicazioni generali.
