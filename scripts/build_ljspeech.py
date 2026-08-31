"""Build the reduced LJSpeech-1.1 release asset: about 300 clips out of 13100.

Source:  https://keithito.com/LJ-Speech-Dataset/
Licence: public domain. The recordings come from LibriVox and the texts from
         Project Gutenberg, both public domain. No attribution required, no
         restriction on commercial use. It is the zero-risk dataset of Module 5.

The full archive is 2.75 GB, which is a lot of classroom minutes on Colab. We
keep one clip every STEP, in filename order, so the sample spreads across all
the source books instead of sitting in the first chapter. Deterministic: same
input, same output.

The audio is left exactly as it comes: 22050 Hz, mono, 16-bit PCM. No
resampling, no trimming, no normalisation, because that is what a TTS pipeline
expects to be handed.
"""

import io
import tarfile

from common import OUT, WORK, download, report

URL = "https://data.keithito.com/data/speech/LJSpeech-1.1.tar.bz2"
STEP = 43  # 13100 / 43 -> about 305 clips

LEGGIMI = """LJSpeech-1.1 — sottoinsieme per il corso ZCS
============================================

Fonte:   https://keithito.com/LJ-Speech-Dataset/
Licenza: PUBBLICO DOMINIO. Registrazioni da LibriVox, testi da Project
         Gutenberg. Nessuna attribuzione obbligatoria, nessun vincolo
         commerciale.

Cosa e' cambiato rispetto all'archivio ufficiale
------------------------------------------------
Solo una clip ogni {step} delle 13.100, in ordine di nome: il campione si
distribuisce su tutti i libri di partenza invece di stare nel primo capitolo.
Nient'altro: l'audio e' quello originale, 22050 Hz mono 16 bit, e metadata.csv
ha lo stesso formato, filtrato alle clip presenti.

metadata.csv non ha intestazione, il separatore e' la barra verticale e le
colonne sono tre: id della clip, trascrizione originale, trascrizione
normalizzata (numeri e abbreviazioni scritti per esteso).

    import pandas as pd
    df = pd.read_csv("metadata.csv", sep="|", header=None, quoting=3,
                     names=["id", "testo", "testo_normalizzato"])

Una sola voce, femminile, circa 24 ore nel dataset intero. Mono-speaker per
costruzione: serve a spiegare la sintesi di una voce, non la clonazione di una
voce diversa.

Per l'archivio intero, lo script che ha prodotto questo e' scripts/build_ljspeech.py
nella repo del corso.
"""


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    src = download(URL, "LJSpeech-1.1.tar.bz2")

    estratto = WORK / "LJSpeech-1.1"
    if not estratto.exists():
        print("estraggo l'archivio ufficiale (~3,6 GB su disco), qualche minuto")
        with tarfile.open(src, "r:bz2") as t:
            t.extractall(WORK)

    # L'ordine dentro il tar ufficiale non e' quello dei nomi: va riordinato qui,
    # altrimenti "una ogni STEP" darebbe un campione arbitrario invece che sparso.
    wavs = sorted((estratto / "wavs").glob("*.wav"))
    tenuti = wavs[::STEP]
    ids = {p.stem for p in tenuti}
    print(f"{len(wavs)} clip nell'originale, {len(tenuti)} tenute "
          f"(da {tenuti[0].stem} a {tenuti[-1].stem})")

    righe = [r for r in (estratto / "metadata.csv").read_text().splitlines()
             if r.split("|", 1)[0] in ids]
    assert len(righe) == len(tenuti), \
        f"{len(righe)} righe di metadata per {len(tenuti)} clip"

    archivio = OUT / "ljspeech-ridotto.tar.bz2"
    with tarfile.open(archivio, "w:bz2") as t:
        for w in tenuti:
            t.add(w, arcname=f"LJSpeech-ridotto/wavs/{w.name}")
        for nome, testo in (("LJSpeech-ridotto/metadata.csv", "\n".join(righe) + "\n"),
                            ("LJSpeech-ridotto/LEGGIMI.txt", LEGGIMI.format(step=STEP))):
            dati = testo.encode("utf-8")
            info = tarfile.TarInfo(nome)
            info.size = len(dati)
            t.addfile(info, io.BytesIO(dati))

    report(archivio)


if __name__ == "__main__":
    main()
