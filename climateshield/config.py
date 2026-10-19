"""Project paths, licences, and documented gazetteer lookups."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ZIP_ARCHIVE = ROOT / "Pakistan_MultiSource_Datasets_Collection.zip"
DATA_DIR = ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
RAW_DATASETS = RAW_DIR / "collected_datasets"
CLEANED_DIR = DATA_DIR / "cleaned"
PROCESSED_DIR = DATA_DIR / "processed"
WAREHOUSE_PATH = PROCESSED_DIR / "climateshield.duckdb"
REPORTS_DIR = ROOT / "reports"
MANIFEST_PATH = DATA_DIR / "manifest.csv"
QUALITY_REPORT_PATH = REPORTS_DIR / "quality_report.json"
QUALITY_LOGS_PATH = REPORTS_DIR / "quality_logs.csv"
INVENTORY_PATH = REPORTS_DIR / "dataset_inventory.json"
INITIAL_QUALITY_PATH = REPORTS_DIR / "initial_quality_report.json"
CLEANING_RULES_PATH = REPORTS_DIR / "cleaning_rules.json"

CUSEC_TO_CMS = 0.028316846592  # 1 cubic foot per second -> cubic metres per second
PKT_OFFSET_HOURS = 5

# Documented HDX/COD-style ADM2 prefix -> region. This is a label lookup, not a
# population or hazard estimate.
PCODE_REGION = {
    "PK1": {"region_name": "Gilgit-Baltistan", "region_code": "GB"},
    "PK2": {"region_name": "Balochistan", "region_code": "BA"},
    "PK3": {"region_name": "Azad Jammu and Kashmir", "region_code": "AJK"},
    "PK4": {"region_name": "Islamabad Capital Territory", "region_code": "ICT"},
    "PK5": {"region_name": "Khyber Pakhtunkhwa", "region_code": "KP"},
    "PK6": {"region_name": "Punjab", "region_code": "PB"},
    "PK7": {"region_name": "Sindh", "region_code": "SD"},
}

PROVINCE_LABELS = {
    "KPK": "Khyber Pakhtunkhwa",
    "AJK": "Azad Jammu and Kashmir",
    "Punjab": "Punjab",
    "Sindh": "Sindh",
}

SOURCE_LICENCES = {
    "01_open_meteo_heat_rainfall": {
        "publisher": "Open-Meteo",
        "source_url": "https://open-meteo.com/",
        "licence": "CC-BY-4.0",
        "independence": "Independent weather reanalysis/forecast API (not on the OSM/PBS/NDMA stack).",
    },
    "02_openstreetmap_geofabrik": {
        "publisher": "OpenStreetMap contributors / Geofabrik / oex (HOT-style export)",
        "source_url": "https://www.openstreetmap.org/",
        "licence": "ODbL-1.0",
        "independence": "Volunteer-mapped infrastructure and settlements.",
    },
    "03_ndma_pmd_hazards_warnings": {
        "publisher": "NDMA and Pakistan Meteorological Department",
        "source_url": "https://ndma.gov.pk/ ; https://www.pmd.gov.pk/",
        "licence": "licence_unspecified_official_publication",
        "independence": "Official Pakistani hazard and river-threshold publications.",
    },
    "04_pakistan_bureau_of_statistics": {
        "publisher": "Pakistan Bureau of Statistics",
        "source_url": "https://www.pbs.gov.pk/",
        "licence": "licence_unspecified_official_statistics",
        "independence": "Official census/statistics tables (not on the Open-Meteo track list).",
    },
}

OPEN_METEO_CITIES = {
    "faisalabad": "Faisalabad",
    "gilgit": "Gilgit",
    "gwadar": "Gwadar",
    "hyderabad": "Hyderabad",
    "islamabad": "Islamabad",
    "karachi": "Karachi",
    "lahore": "Lahore",
    "multan": "Multan",
    "peshawar": "Peshawar",
    "quetta": "Quetta",
    "rawalpindi": "Rawalpindi",
    "sukkur": "Sukkur",
}

# Physically implausible bounds for Pakistan 2 m air temperature. Values outside
# this range are flagged, never discarded. Genuine heat (40-54 C) is in range.
TEMP_C_HARD_MIN = -40.0
TEMP_C_HARD_MAX = 55.0
HUMIDITY_MIN = 0.0
HUMIDITY_MAX = 100.0
PRECIP_HARD_MAX_MM = 500.0  # hourly; above this is flagged, not removed
