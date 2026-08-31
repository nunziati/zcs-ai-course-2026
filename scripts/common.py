"""Shared helpers for the dataset build scripts.

Not needed by course participants: see scripts/README.md.
"""

import hashlib
import pathlib
import sys
import urllib.request

WORK = pathlib.Path(__file__).resolve().parent / "work"
OUT = pathlib.Path(__file__).resolve().parent / "out"


def download(url, name):
    """Download url into work/name, skipping if the file is already there."""
    WORK.mkdir(parents=True, exist_ok=True)
    dest = WORK / name
    if dest.exists():
        print(f"already downloaded: {dest} ({dest.stat().st_size} bytes)")
        return dest
    print(f"downloading {url}")
    with urllib.request.urlopen(url) as r, open(dest, "wb") as f:
        while chunk := r.read(1 << 20):
            f.write(chunk)
    print(f"got {dest} ({dest.stat().st_size} bytes)")
    return dest


def report(path):
    """Print the size and sha256 of a built artifact, and warn over 100 MB."""
    size = path.stat().st_size
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while chunk := f.read(1 << 20):
            h.update(chunk)
    print(f"\n{path.name}")
    print(f"  size   {size} bytes ({size / 1048576:.1f} MB)")
    print(f"  sha256 {h.hexdigest()}")
    if size > 100 * 1024 * 1024:
        print("  WARNING: over the 100 MB budget", file=sys.stderr)
    return size
