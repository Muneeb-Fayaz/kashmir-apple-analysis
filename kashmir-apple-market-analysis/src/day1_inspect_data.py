from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data" / "raw"

def main():
    production_file = DATA_DIR / "apple_production_official_2024_25.csv"
    df = pd.read_csv(production_file)

    print("\\n=== KASHMIR APPLE MARKET ANALYSIS | DAY 1 ===")
    print("\\n1. First five rows:")
    print(df.head())

    print("\\n2. Dataset shape (rows, columns):")
    print(df.shape)

    print("\\n3. Column names:")
    print(df.columns.tolist())

    print("\\n4. Data types and non-null counts:")
    df.info()

    print("\\n5. Missing values:")
    print(df.isna().sum())

    print("\\n6. Production summary (thousand metric tonnes):")
    print(df["apple_production_thousand_mt"].describe())

    print("\\n7. Highest-producing districts:")
    print(
        df.sort_values("apple_production_thousand_mt", ascending=False)
          [["district", "apple_production_thousand_mt"]]
          .to_string(index=False)
    )

    total = df["apple_production_thousand_mt"].sum()
    print(f"\\nTotal Kashmir Division production in this table: {total:,.2f} thousand MT")

if __name__ == "__main__":
    main()
