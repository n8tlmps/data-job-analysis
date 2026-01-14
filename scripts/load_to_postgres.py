import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path

project_root = Path(__file__).resolve().parents[1]
file_path = project_root / "data" / "uncleaned_DS_jobs.csv"
password = input("Enter your database password for user 'postgres':\n")

db_url = f"postgresql+psycopg2://postgres:{password}@localhost:5432/postgres"

engine = create_engine(db_url)

df = pd.read_csv(file_path)
df.columns = (
    df.columns.str.strip()
    .str.lower()
    .str.replace(" ", "_")
    .str.replace(r"[^a-z0-9_]+", "", regex=True)
)

table_name = "raw_job_data"
df.to_sql(table_name, engine, if_exists="replace", index=False)
print(f"Loaded {len(df):,} rows into table '{table_name}'")