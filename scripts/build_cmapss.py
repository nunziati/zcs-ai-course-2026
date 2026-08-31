"""Build the NASA C-MAPSS release asset.

Source:  https://www.nasa.gov/intelligent-systems-division/discovery-and-systems-health/pcoe/pcoe-data-set-repository/
         entry "6. Turbofan Engine Degradation Simulation Data Set"
         mirror https://zenodo.org/records/15346912 (DOI 10.5281/zenodo.15346912)
Licence: US government data, not subject to copyright; the Zenodo deposit states CC BY 4.0.

No reduction: 12 MB. What the script does is unwrap the archive. NASA ships a zip
that contains a single zip inside a folder whose name has spaces and a dot in it,
which is awkward to unpack in a notebook. We republish the inner zip as is, so one
unzip lands the .txt files straight in the working directory.

Careful with the name: entry "17." of the same repository is N-CMAPSS, a different
dataset of 15.7 GB.
"""

import shutil
import zipfile

from common import OUT, WORK, download, report

URL = ("https://phm-datasets.s3.amazonaws.com/NASA/"
       "6.+Turbofan+Engine+Degradation+Simulation+Data+Set.zip")
INNER = "6. Turbofan Engine Degradation Simulation Data Set/CMAPSSData.zip"


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    outer = download(URL, "cmapss-nasa.zip")
    stage = WORK / "cmapss-stage"
    shutil.rmtree(stage, ignore_errors=True)
    with zipfile.ZipFile(outer) as z:
        z.extract(INNER, stage)
    archive = OUT / "cmapss.zip"
    shutil.copy(stage / INNER, archive)
    with zipfile.ZipFile(archive) as z:
        names = z.namelist()
    print(f"{len(names)} file: {', '.join(sorted(names)[:4])} ...")
    report(archive)


if __name__ == "__main__":
    main()
