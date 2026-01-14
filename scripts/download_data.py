import kagglehub
import shutil
from pathlib import Path

# Resolve project root (one level above scripts/)
PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"
DATA_DIR.mkdir(exist_ok=True)

# Download dataset (cached by kagglehub)
dataset_path = Path(
    kagglehub.dataset_download(
        "rashikrahmanpritom/data-science-job-posting-on-glassdoor"
    )
)

# Target file name
target_file = "uncleaned_DS_jobs.csv"

source_file = dataset_path / target_file
destination_file = DATA_DIR / target_file

if not source_file.exists():
    raise FileNotFoundError(f"{target_file} not found in dataset")

shutil.copy2(source_file, destination_file)

print("Copied:", destination_file)

