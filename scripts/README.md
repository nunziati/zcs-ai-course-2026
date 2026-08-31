# Script che costruiscono le release dei dati

**Ai corsisti questi script non servono.** I notebook scaricano i dati già pronti
dalle [release](https://github.com/nunziati/zcs-ai-course-2026/releases). Questa
cartella serve solo a poter rifare le release da zero, e a rendere verificabile
cosa è stato tolto o cambiato rispetto ai dataset originali.

## Come si usano

```bash
cd scripts
python3 build_cub.py        # 20 classi delle 200 di CUB-200-2011   -> 65,0 MB
python3 build_thyroid.py    # UCI Thyroid, intero                   -> 0,1 MB
python3 build_cmapss.py     # NASA C-MAPSS, intero                  -> 11,9 MB
python3 build_ljspeech.py   # 305 clip delle 13.100 di LJSpeech     -> 60,2 MB
python3 build_video.py      # vtest.avi di OpenCV                   ->  7,8 MB
```

Serve solo Pillow, e solo per `build_cub.py`. Ogni script scarica in `work/`,
costruisce in `out/`, e stampa dimensione e sha256 di quello che ha prodotto.
Entrambe le cartelle sono ignorate da git. Scaricare tutto significa 4 GB, e
`work/` arriva a una decina di GB con gli archivi estratti.

## Il budget: 100 MB per archivio

Deciso su [#16](https://github.com/nunziati/corso-zcs/issues/16). I notebook
girano su Colab, che azzera il disco a ogni sessione: ogni corsista riscarica
tutto ogni volta, e il download si mangia minuti d'aula. Ogni script controlla la
soglia e avvisa se la supera.

Dove la fonte è già sotto la soglia non si riduce niente: si ripubblica il file
originale, perché gli URL ufficiali si rompono e una release è un indirizzo
stabile.

## Cosa è stato cambiato, dataset per dataset

| Archivio | Fonte | Riduzione |
|---|---|---|
| `cub-200-2011-20-classi.tgz` | CaltechDATA | 20 classi su 200, immagini ricompresse JPEG q95 |
| `uci-thyroid.zip` | UCI | nessuna |
| `cmapss.zip` | NASA PCoE | nessuna, tolto solo lo zip esterno |
| `ljspeech-ridotto.tar.bz2` | keithito.com | 305 clip su 13.100 |
| `vtest.avi` | opencv/opencv | nessuna |

Ogni archivio contiene un `LEGGIMI.txt` con fonte, licenza, citazione obbligatoria
dove serve, e l'elenco preciso di cosa è cambiato. Il dettaglio delle licenze sta
nel README della repo.

## Due trappole trovate costruendoli

- **Il tar ufficiale di LJSpeech non è ordinato per nome.** Prendere «una clip ogni
  43 in ordine d'archivio» dava un campione arbitrario invece che sparso sui libri
  di partenza. Lo script ordina prima di campionare.
- **Le immagini di CUB non si possono ridimensionare.** Le coordinate delle 15
  parti e i bounding box sono in pixel: cambiare le dimensioni le invaliderebbe.
  Si ricomprime a parità di pixel, e lo script verifica che le dimensioni non
  cambino.
