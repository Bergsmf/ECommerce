from pathlib import Path

import pandas as pd
import pandera.pandas as pa

from ecommerce.pipeline.extract import Extract
from ecommerce.schema import SalesSchema


def extract_file(file_path: str) -> pd.DataFrame:
    extract = Extract(file_path)
    df_sales = extract.read_file()
    return df_sales


def validate_sales(df_sales: pd.DataFrame) -> pd.DataFrame:
    try:
        df_validated = SalesSchema.validate(df_sales, lazy=True)
        return df_validated
    except pa.errors.SchemaErrors as exc:
        bad_rows = exc.failure_cases['index'].dropna().unique()
        df_clean = df_sales.drop(index=bad_rows)
        return df_clean


if __name__ == '__main__':
    file_path = Path.cwd() / 'data/data.csv'
    df_sales = extract_file(file_path)
    df_sales = validate_sales(df_sales)
