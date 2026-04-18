from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

DATA_RAW       = ROOT / "data" / "raw"
DATA_PROCESSED = ROOT / "data" / "processed"
FIGURES_DIR    = ROOT / "outputs" / "figures"
MODELS_DIR     = ROOT / "outputs" / "models"
REPORTS_DIR    = ROOT / "outputs" / "reports"

MEDIA_COLS = ["tv_spend", "ooh_spend", "print_spend", "facebook_spend", "search_spend"]
MEDIA_LABELS = {
    "tv_spend":       "TV",
    "ooh_spend":      "OOH",
    "print_spend":    "Print",
    "facebook_spend": "Facebook",
    "search_spend":   "Search",
}
MEDIA_COLORS = {
    "tv_spend":       "#4E9AF1",
    "ooh_spend":      "#F5C842",
    "print_spend":    "#6BCB77",
    "facebook_spend": "#FF7043",
    "search_spend":   "#9C5CF5",
}

TARGET_COL = "revenue"
DATE_COL   = "date"

ADSTOCK_DECAY = {
    "tv_spend":       0.65,
    "ooh_spend":      0.40,
    "print_spend":    0.35,
    "facebook_spend": 0.50,
    "search_spend":   0.20,
}

HILL_ALPHA = {
    "tv_spend":       2.0,
    "ooh_spend":      1.5,
    "print_spend":    1.2,
    "facebook_spend": 2.5,
    "search_spend":   1.8,
}
HILL_GAMMA = {
    "tv_spend":       70000,
    "ooh_spend":      30000,
    "print_spend":    20000,
    "facebook_spend": 50000,
    "search_spend":   25000,
}
