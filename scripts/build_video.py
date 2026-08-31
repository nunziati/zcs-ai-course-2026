"""Fetch the clean-licence video clip for the tracking module.

Source:  https://github.com/opencv/opencv, samples/data/vtest.avi
Licence: Apache 2.0 (the licence of the opencv/opencv repository).

Pedestrians from a fixed camera. Dated and low resolution, but legally clean and
always available, which is why it is the guaranteed fallback rather than the
first choice. The Pexels clip that goes alongside it is picked by the Module 4
syllabus and downloaded by hand from the browser: the Pexels site answers 403 to
automated requests.
"""

import shutil

from common import OUT, download, report

URL = "https://raw.githubusercontent.com/opencv/opencv/master/samples/data/vtest.avi"


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    src = download(URL, "vtest.avi")
    archive = OUT / "vtest.avi"
    shutil.copy(src, archive)
    report(archive)


if __name__ == "__main__":
    main()
