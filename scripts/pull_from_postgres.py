import pandas as pd
from sqlalchemy import create_engine, inspect
from pathlib import Path

project_root = Path(__file__).resolve().parents[1]
data_dir = project_root / "data"

password = input("Enter your database password for user 'postgres':\n")

db_url = f"postgresql+psycopg2://postgres:{password}@localhost:5432/postgres"
engine = create_engine(db_url)

inspector = inspect(engine)
tables = inspector.get_table_names()

if not tables:
    raise ValueError("no tables found in the database.")

print("\navailable tables:")
for i, table in enumerate(tables, start=1):
    print(f"{i}. {table}")

# prompt user for table selection
table_name = input("\nenter the table name you want to export:\n").strip()

if table_name not in tables:
    raise ValueError(f"table '{table_name}' does not exist.")

# load table into dataframe
df = pd.read_sql_table(table_name, engine)

# output file path
output_file = data_dir / f"{table_name}.csv"

# save to csv
df.to_csv(output_file, index=False)

print(f"\nexported {len(df):,} rows from '{table_name}' to:")
print(output_file)