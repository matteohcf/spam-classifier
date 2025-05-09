import os
from pathlib import Path

# Percorsi base
PROJECT_ROOT = Path(__file__).parent.resolve()
DATASET_DIR = PROJECT_ROOT / "service" / "classifier" / "datasets"
SPAM_HAM_DATASET_PATH = DATASET_DIR / "spam_ham_dataset.csv"