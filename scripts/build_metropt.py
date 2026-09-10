"""Build the MetroPT-3 release asset: one-minute means of the fifteen signals.

Source:  https://archive.ics.uci.edu/dataset/791/metropt+3+dataset
Licence: CC BY 4.0.
Paper:   Davari, N., Veloso, B., Ribeiro, R. P., Pereira, P. M., Gama, J. Predictive
         maintenance based on anomaly detection using deep learning for air production unit
         in the railway industry. IEEE DSAA 2021, DOI 10.1109/DSAA53316.2021.9564181.

The original CSV is 208 MB: 1,516,948 rows, one sample every ten seconds or so, from
February to August 2020. Colab would spend minutes downloading it. Every minute that has at
least one sample is replaced by the mean of its samples: the analogue signals become
one-minute means, the digital ones the fraction of the minute in which they were active.
Minutes without samples are left out, so the gaps of the original stay visible. About
250,000 rows, 5 MB zipped.

The failure table of the documentation numbers the first two failures #1 and gives the
second a maintenance date a month before the failure itself. LEGGIMI.txt keeps the four
intervals, numbered 1 to 4, and leaves the maintenance dates out. Needs pandas.
"""

import zipfile

import pandas as pd

from common import OUT, download, report

URL = "https://archive.ics.uci.edu/static/public/791/metropt+3+dataset.zip"
CSV = "MetroPT3(AirCompressor).csv"

LEGGIMI = """MetroPT-3, medie al minuto
==========================

Che cos'e'
Sette mesi di segnali dell'unita' di produzione dell'aria (Air Production Unit) di un
treno della metropolitana di Porto in servizio, da febbraio ad agosto 2020: sette segnali
analogici (pressioni, corrente del motore, temperatura dell'olio) e otto digitali (stato
delle valvole e segnali elettrici).

Fonte
UCI Machine Learning Repository, MetroPT-3 Dataset
https://archive.ics.uci.edu/dataset/791/metropt+3+dataset

Citazione
Davari, N., Veloso, B., Ribeiro, R. P., Pereira, P. M., Gama, J. Predictive maintenance
based on anomaly detection using deep learning for air production unit in the railway
industry. 2021 IEEE 8th International Conference on Data Science and Advanced Analytics
(DSAA), pp. 1-10. DOI 10.1109/DSAA53316.2021.9564181

Licenza
Creative Commons Attribution 4.0 International (CC BY 4.0)
https://creativecommons.org/licenses/by/4.0/

Che cosa e' cambiato rispetto all'originale
- L'originale ha un campione ogni dieci secondi circa: 1.516.948 righe, 208 MB.
- Qui ogni minuto con almeno un campione e' sostituito dalla media dei suoi campioni. Per i
  segnali analogici e' la media al minuto; per quelli digitali, che valgono 0 o 1, e' la
  frazione del minuto in cui il segnale era attivo.
- I minuti senza campioni sono omessi: i buchi dell'originale restano.
- La colonna dell'indice originale e' tolta. I nomi delle colonne sono quelli originali,
  compreso DV_eletric.
- I valori sono scritti con quattro cifre significative.

I guasti
Il dataset non ha etichette. La documentazione riporta quattro guasti, dai rapporti
dell'azienda di manutenzione, tutti perdite d'aria (air leak):
  1   18/04/2020 00:00  ->  18/04/2020 23:59
  2   29/05/2020 23:30  ->  30/05/2020 06:00
  3   05/06/2020 10:00  ->  07/06/2020 14:30
  4   15/07/2020 14:30  ->  15/07/2020 19:00
Nella tabella originale i primi due guasti hanno entrambi il numero #1, e il secondo
rimanda a una manutenzione del 30 aprile, un mese prima del guasto stesso. Qui sono
numerati da 1 a 4 e le date di manutenzione sono omesse.
"""


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    src = download(URL, "metropt3-uci.zip")
    with zipfile.ZipFile(src) as z, z.open(CSV) as f:
        d = pd.read_csv(f, index_col=0, parse_dates=["timestamp"])
    print(f"{len(d)} original rows, {d.timestamp.min()} to {d.timestamp.max()}")
    m = d.set_index("timestamp").sort_index().resample("1min").mean().dropna(how="all")
    print(f"{len(m)} minutes with at least one sample")
    archive = OUT / "metropt3.zip"
    with zipfile.ZipFile(archive, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        z.writestr("metropt3-1min.csv", m.to_csv(float_format="%.4g"))
        z.writestr("LEGGIMI.txt", LEGGIMI)
    with zipfile.ZipFile(archive) as z:
        print(f"{len(z.namelist())} file: {', '.join(z.namelist())}")
    report(archive)


if __name__ == "__main__":
    main()
