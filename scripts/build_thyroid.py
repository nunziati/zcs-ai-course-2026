"""Build the UCI Thyroid Disease release asset.

Source:  https://archive.ics.uci.edu/dataset/102/thyroid+disease
Licence: CC BY 4.0.
No reduction: the whole thing is under 700 KB. The script exists so the release
can be rebuilt if the UCI URLs move, which they have before.
"""

import zipfile

from common import OUT, download, report

BASE = "https://archive.ics.uci.edu/ml/machine-learning-databases/thyroid-disease/"
FILES = ["sick.data", "sick.test", "sick.names",
         "allhypo.data", "allhypo.test", "allhypo.names"]

COLUMNS = """age sex on_thyroxine query_on_thyroxine on_antithyroid_medication sick
pregnant thyroid_surgery I131_treatment query_hypothyroid query_hyperthyroid
lithium goitre tumor hypopituitary psych TSH_measured TSH T3_measured T3
TT4_measured TT4 T4U_measured T4U FTI_measured FTI TBG_measured TBG
referral_source target""".split()

READ_ME = f"""UCI Thyroid Disease — sottoinsieme del corso
============================================

Fonte:   https://archive.ics.uci.edu/dataset/102/thyroid+disease
Licenza: CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/)
Dati raccolti dal Garavan Institute e da J. Ross Quinlan, 1987.

I file sono quelli ufficiali, non modificati. Nessuna riduzione: pesano meno di 700 KB.

I .data non hanno riga di intestazione, i valori mancanti sono '?', e l'ultima
colonna unisce la classe e l'id del record con una barra verticale
(per esempio "negative.|3733"). Da qui:

    import pandas as pd
    cols = {COLUMNS}
    df = pd.read_csv("sick.data", header=None, names=cols, na_values="?")
    df["target"] = df["target"].str.split("|").str[0].str.rstrip(".")

Sei esami di laboratorio (TSH, T3, TT4, T4U, FTI, TBG) hanno ciascuno accanto il
proprio flag *_measured: e' il missing-by-design su cui lavora la lezione.
TBG non e' mai misurato in questa release.
"""


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    paths = [download(BASE + name, "thyroid-" + name) for name in FILES]
    archive = OUT / "uci-thyroid.zip"
    with zipfile.ZipFile(archive, "w", zipfile.ZIP_DEFLATED) as z:
        for path in paths:
            z.write(path, "thyroid/" + path.name.removeprefix("thyroid-"))
        z.writestr("thyroid/LEGGIMI.txt", READ_ME)
    report(archive)


if __name__ == "__main__":
    main()
