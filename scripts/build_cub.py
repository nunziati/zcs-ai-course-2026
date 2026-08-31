"""Build the reduced CUB-200-2011 release asset: 20 classes out of 200.

Source:  https://www.vision.caltech.edu/datasets/cub_200_2011/
         archive https://data.caltech.edu/records/65de6-vp158
Licence: no standard licence. The official terms restrict use to
         "non-commercial research and educational purposes".

Redistributing it is a declared derogation, decided on issue #15 of the design
repository: the terms allow teaching but say nothing about redistribution.
Hence the attribution below is mandatory, in the release notes and in the first
cell of the notebook, and the images must not go into the slide PDF.

Which 20 classes, and why
-------------------------
Three complete genera, no arbitrary truncation: 8 Gulls, 7 Terns, 5 Kingfishers.
Gulls and Terns are white seabirds that look alike within and across the two
genera, which is the whole point of fine-grained classification. The Kingfishers
are the easy contrast that makes the confusion matrix readable.

Everything else is kept: the 312 binary attributes, the 15 part coordinates, the
bounding boxes and the official train/test split, filtered to these classes. The
HuggingFace mirror does not carry the attributes, which is why the build starts
from the official CaltechDATA archive.

Images are re-encoded as JPEG quality 95 to fit the 100 MB budget: the raw 20
classes are 102 MB. Pixel dimensions are unchanged, so every coordinate in
bounding_boxes.txt and parts/ stays valid.
"""

import io
import pathlib
import shutil
import tarfile

from PIL import Image

from common import OUT, WORK, download, report

URL = ("https://data.caltech.edu/records/65de6-vp158/files/"
       "CUB_200_2011.tgz?download=1")
QUALITY = 95

GENERA = ("Gull", "Tern", "Kingfisher")

ATTRIBUZIONE = """CUB-200-2011 — sottoinsieme di 20 classi per il corso ZCS
=========================================================

Fonte:   Caltech-UCSD Birds-200-2011 (CUB-200-2011)
         https://www.vision.caltech.edu/datasets/cub_200_2011/
         archivio ufficiale: https://data.caltech.edu/records/65de6-vp158

Citazione obbligatoria:
  Wah C., Branson S., Welinder P., Perona P., Belongie S.
  "The Caltech-UCSD Birds-200-2011 Dataset."
  Computation & Neural Systems Technical Report, CNS-TR-2011-001.
  California Institute of Technology, 2011.

Termini d'uso della fonte: l'uso e' ristretto a scopi di ricerca e didattica
NON COMMERCIALI ("their use is restricted to non-commercial research and
educational purposes"). Questo sottoinsieme e' redistribuito per la sola
didattica del corso. Non usarlo per scopi commerciali.

Cosa e' cambiato rispetto all'archivio ufficiale
------------------------------------------------
1. Solo 20 classi delle 200: i generi Gull (8), Tern (7) e Kingfisher (5),
   completi. Gli id di classe e di immagine sono quelli originali, quindi NON
   sono contigui: per allenare, rimappa le etichette (per esempio con
   pandas.factorize o con un dizionario costruito da classes.txt).
2. Le immagini sono ricompresse in JPEG qualita' 95. Le dimensioni in pixel non
   cambiano, quindi bounding_boxes.txt e parts/ restano validi.
3. Tutti i file di metadati sono filtrati a queste 20 classi. Nessun campo e'
   stato tolto o rinominato.
4. attributes.txt sta nella radice dell'archivio, fuori da CUB_200_2011/:
   e' cosi' anche nell'originale, e il README ufficiale dice il contrario.

Per rifare tutto sui dati interi, lo script che ha prodotto questo archivio e'
scripts/build_cub.py nella repo del corso.
"""


def scegli_classi(root):
    """Return the class ids and names of the three complete genera."""
    scelte = []
    for riga in (root / "classes.txt").read_text().splitlines():
        cid, nome = riga.split(" ", 1)
        if nome.rsplit("_", 1)[-1] in GENERA:
            scelte.append((cid, nome))
    return scelte


def filtra(src, dst, chiavi, colonna=0):
    """Copy src to dst keeping only the lines whose given column is in chiavi."""
    dst.parent.mkdir(parents=True, exist_ok=True)
    tenute = 0
    with open(src) as fin, open(dst, "w") as fout:
        for riga in fin:
            campi = riga.split()
            if campi and campi[colonna] in chiavi:
                fout.write(riga)
                tenute += 1
    return tenute


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    tgz = download(URL, "CUB_200_2011.tgz")

    estratto = WORK / "CUB_200_2011"
    if not estratto.exists():
        print("estraggo l'archivio ufficiale (~2,5 GB su disco)")
        with tarfile.open(tgz) as t:
            t.extractall(WORK)

    root = estratto
    classi = scegli_classi(root)
    class_ids = {cid for cid, _ in classi}
    print(f"{len(classi)} classi scelte: {', '.join(n for _, n in classi)}")

    # image_id -> relative path, restricted to the chosen classes
    etichetta = {}
    for riga in (root / "image_class_labels.txt").read_text().splitlines():
        iid, cid = riga.split()
        if cid in class_ids:
            etichetta[iid] = cid
    percorso = {}
    for riga in (root / "images.txt").read_text().splitlines():
        iid, rel = riga.split(" ", 1)
        if iid in etichetta:
            percorso[iid] = rel
    print(f"{len(percorso)} immagini")

    stage = WORK / "cub-stage"
    shutil.rmtree(stage, ignore_errors=True)
    base = stage / "CUB_200_2011"
    base.mkdir(parents=True)

    # images, re-encoded at the same pixel size
    entrata = uscita = 0
    for iid, rel in sorted(percorso.items(), key=lambda kv: int(kv[0])):
        src = root / "images" / rel
        dst = base / "images" / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        entrata += src.stat().st_size
        buf = io.BytesIO()
        Image.open(src).convert("RGB").save(
            buf, "JPEG", quality=QUALITY, optimize=True, progressive=True)
        dst.write_bytes(buf.getvalue())
        uscita += dst.stat().st_size
    print(f"immagini: {entrata / 1048576:.1f} MB -> {uscita / 1048576:.1f} MB "
          f"(JPEG q{QUALITY}, Pillow {Image.__version__})")

    image_ids = set(percorso)
    per_immagine = [
        "image_class_labels.txt", "images.txt", "train_test_split.txt",
        "bounding_boxes.txt", "parts/part_locs.txt", "parts/part_click_locs.txt",
        "attributes/image_attribute_labels.txt",
    ]
    for nome in per_immagine:
        n = filtra(root / nome, base / nome, image_ids)
        print(f"  {nome}: {n} righe")

    n = filtra(root / "classes.txt", base / "classes.txt", class_ids)
    print(f"  classes.txt: {n} righe")

    # one row per class, in the order of the full classes.txt: keep by position
    righe = (root / "attributes/class_attribute_labels_continuous.txt"
             ).read_text().splitlines()
    tenute = [righe[int(cid) - 1] for cid, _ in classi]
    (base / "attributes/class_attribute_labels_continuous.txt").write_text(
        "\n".join(tenute) + "\n")
    print(f"  attributes/class_attribute_labels_continuous.txt: {len(tenute)} righe")

    for nome in ("parts/parts.txt", "attributes/certainties.txt", "README"):
        shutil.copy(root / nome, base / nome)
    shutil.copy(WORK / "attributes.txt", stage / "attributes.txt")
    (stage / "LEGGIMI.txt").write_text(ATTRIBUZIONE)

    archivio = OUT / "cub-200-2011-20-classi.tgz"
    with tarfile.open(archivio, "w:gz") as t:
        for p in sorted(stage.rglob("*")):
            t.add(p, arcname=str(p.relative_to(stage)), recursive=False)
    report(archivio)


if __name__ == "__main__":
    main()
