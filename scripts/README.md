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
python3 build_metropt.py    # MetroPT-3, medie al minuto            ->  4,1 MB
```

Servono Pillow, solo per `build_cub.py`, e pandas, solo per `build_metropt.py`. Ogni script scarica in `work/`,
costruisce in `out/`, e stampa dimensione e sha256 di quello che ha prodotto.
Entrambe le cartelle sono ignorate da git.

L'estratto di 8-Calves, `8calves-clip.zip` nella release `dati-video`, non ha uno script
qui: è stato costruito a mano, e le modifiche rispetto all'originale sono elencate nella
nota della release e in `ATTRIBUZIONE.txt`, dentro l'archivio.

## Il budget: 100 MB per archivio

I notebook girano su Colab, che azzera il disco a ogni sessione: ogni corsista
riscarica tutto ogni volta, e il download si mangia minuti d'aula. Ogni script
controlla la soglia e avvisa se la supera.

Dove la fonte è già sotto la soglia non si riduce niente: si ripubblica il file
originale, perché gli URL ufficiali si rompono e una release è un indirizzo
stabile.

## Cosa è stato cambiato, dataset per dataset

| Archivio | Fonte | Riduzione |
|---|---|---|
| `cub-200-2011-20-classi.tgz` | CaltechDATA | 20 classi su 200, immagini ricompresse JPEG q95 |
| `uci-thyroid.zip` | UCI | nessuna |
| `cmapss.zip` | NASA PCoE | nessuna, tolto solo lo zip esterno |
| `8calves-clip.zip` | Hugging Face | 600 frame ritagliati dal video originale e ricompressi, più le detection precalcolate |
| `metropt3.zip` | UCI | medie al minuto dei 15 segnali: da 1.516.948 righe a 252.720 |

Gli archivi di CUB, Thyroid e MetroPT-3 contengono un `LEGGIMI.txt` con fonte, licenza,
citazione obbligatoria dove serve, e l'elenco preciso di cosa è cambiato. `cmapss.zip` è
lo zip interno della NASA, ripubblicato così com'è, e l'estratto di 8-Calves ha
`ATTRIBUZIONE.txt`. Il dettaglio delle licenze sta nel README della repo.

## Una trappola trovata costruendoli

**Le immagini di CUB non si possono ridimensionare.** Le coordinate delle 15 parti e i
bounding box sono in pixel: cambiare le dimensioni le invaliderebbe. Si ricomprime a
parità di pixel, e lo script verifica che le dimensioni non cambino.
