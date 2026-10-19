"""CLI: python -m climateshield make-data"""

from __future__ import annotations

import argparse
import sys


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="climateshield", description="ClimateShield 360 data pipeline")
    parser.add_argument(
        "command",
        nargs="?",
        default="make-data",
        choices=["make-data", "inventory", "train"],
        help="make-data rebuilds cleaned and processed layers. inventory writes the file inventory. train runs Deliverable 3 ML modeling.",
    )
    args = parser.parse_args(argv)

    if args.command == "train":
        from climateshield.models.train_and_evaluate import check_dependencies, load_data, feature_engineering, train_and_evaluate
        check_dependencies()
        df = load_data()
        df = feature_engineering(df)
        train_and_evaluate(df)
        return 0

    if args.command == "inventory":
        from climateshield.pipeline.extract import ensure_raw_extracted
        from climateshield.inventory import build_initial_quality_report, build_inventory
        from climateshield.quality.rules import rules_payload
        from climateshield.io_utils import write_json
        from climateshield.config import CLEANING_RULES_PATH

        ensure_raw_extracted()
        inventory = build_inventory()
        build_initial_quality_report(inventory)
        write_json(CLEANING_RULES_PATH, rules_payload())
        print(f"Inventory files: {inventory['n_files']}")
        return 0

    from climateshield.pipeline.run import make_data

    make_data()
    return 0


if __name__ == "__main__":
    sys.exit(main())
