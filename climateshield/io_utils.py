"""Safe I/O helpers. Raw files are read-only."""

from __future__ import annotations

import hashlib
import json
import shutil
from pathlib import Path
from typing import Any

import pandas as pd

from climateshield.config import RAW_DIR


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def assert_not_raw(path: Path) -> None:
    resolved = path.resolve()
    raw_root = RAW_DIR.resolve()
    if resolved == raw_root or raw_root in resolved.parents:
        raise PermissionError(f"Refusing to write inside raw directory: {path}")


def reset_dir(path: Path) -> None:
    assert_not_raw(path)
    if path.exists():
        shutil.rmtree(path)
    path.mkdir(parents=True, exist_ok=True)


def write_json(path: Path, payload: Any) -> None:
    assert_not_raw(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, default=str), encoding="utf-8")


def write_csv(path: Path, frame: pd.DataFrame) -> None:
    assert_not_raw(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    frame.to_csv(path, index=False)


def write_parquet(path: Path, frame: pd.DataFrame) -> None:
    assert_not_raw(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    frame.to_parquet(path, index=False)


def write_table(path_stem: Path, frame: pd.DataFrame, parquet: bool = True, csv: bool = True) -> dict[str, str]:
    written: dict[str, str] = {}
    if csv:
        csv_path = path_stem.with_suffix(".csv")
        write_csv(csv_path, frame)
        written["csv"] = str(csv_path)
    if parquet:
        parquet_path = path_stem.with_suffix(".parquet")
        write_parquet(parquet_path, frame)
        written["parquet"] = str(parquet_path)
    return written
