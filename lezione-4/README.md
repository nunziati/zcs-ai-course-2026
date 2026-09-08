# Lezione 4 — mercoledì 9 settembre 2026, ore 9:00–13:00

**Modulo 4 — Video e computer vision realtime**

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/nunziati/zcs-ai-course-2026/blob/main/lezione-4/metodi-lezione-4.ipynb)

Clicca il badge qui sopra: serve solo il tuo account Google. La prima cella che esegui
scarica i dati da sola, e quelle che eseguono un detector installano `ultralytics` al
primo uso, una volta sola.

**Questo notebook si esegue in qualsiasi ordine.** Ogni cella è indipendente: importa
quello che le serve, costruisce i propri dati e stampa la propria conclusione. Se ne può
eseguire una sola, o saltarne metà.

Gira anche senza GPU. Con la GPU le celle che misurano un tempo vanno una decina di volte
più veloci; i risultati non cambiano.

## Cosa c'è dentro

Venti sezioni, una per meccanismo: dalla ridondanza fra frame consecutivi alla latenza al
99° percentile, passando per detection, soppressione dei duplicati, tracking e metriche.

Due celle sono marcate `PUNTO DI VARIAZIONE`. La prima è il detector, e vale per tutto il
notebook:

| valore | modello | licenza |
|---|---|---|
| `yolo11n` | YOLO11 nano, 2,6 M parametri | AGPL-3.0 |
| `yolo11s` | YOLO11 small, 9,5 M parametri | AGPL-3.0 |
| `yolo11m` | YOLO11 medium, 20,1 M parametri — è il valore di partenza | AGPL-3.0 |
| `rtdetr` | RT-DETRv2-R18, 20,2 M parametri | Apache 2.0 |

Cambiare quella costante cambia i numeri di mezzo notebook, e in due celle cambia anche la
conclusione. È voluto.

Il notebook arriva con tutti gli output già dentro, quindi si legge anche senza eseguirlo.

## I dati

**8-Calves**, estratto: 600 frame (30 secondi a 20 frame al secondo, 800×600) di una
stalla ripresa dall'alto con otto vitelli, più le annotazioni — un riquadro per vitello per
frame, con l'identità. Dalla release
[`dati-video`](https://github.com/nunziati/zcs-ai-course-2026/releases/tag/dati-video).

> Fang, Y. et al. *8-Calves Dataset: Benchmarking Object Detection and Identity
> Classification in Occlusion-Rich Environments.* arXiv:2503.13777.

Fonte: [huggingface.co/datasets/tonyFang04/8-calves](https://huggingface.co/datasets/tonyFang04/8-calves),
licenza [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). L'estratto è ritagliato
e ricompresso rispetto all'originale; l'archivio contiene l'attribuzione completa.

Torna al [README](../README.md) per le indicazioni generali.
