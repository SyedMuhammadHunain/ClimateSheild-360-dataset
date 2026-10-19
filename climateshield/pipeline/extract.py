"""Extract the source ZIP into data/raw without modifying the archive."""

from __future__ import annotations

import zipfile

from climateshield.config import RAW_DIR, RAW_DATASETS, ZIP_ARCHIVE


def ensure_raw_extracted() -> None:
    if (RAW_DATASETS / "README_DATASETS_CATALOG.md").exists():
        return
    if not ZIP_ARCHIVE.exists():
        raise FileNotFoundError(f"ZIP archive not found: {ZIP_ARCHIVE}")
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(ZIP_ARCHIVE) as archive:
        archive.extractall(RAW_DIR)
