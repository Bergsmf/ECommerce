from pathlib import Path

import pandas as pd
import pandera.pandas as pa
from pipeline.extract import Extract
from pipeline.load import Load
from pipeline.transform import Transform
from schema import SalesSchema, SalesValidSchema


def extract_file(file_path: str) -> pd.DataFrame:
    extract = Extract(file_path)
    df_sales = extract.read_file()
    return df_sales


def validate_sales(df_sales: pd.DataFrame) -> pd.DataFrame:
    df_sales = SalesSchema.preprocess(df_sales)
    try:
        df_validated = SalesSchema.validate(df_sales, lazy=True)
        return df_validated
    except pa.errors.SchemaErrors as exc:
        bad_rows = exc.failure_cases['index'].dropna().unique()
        df_clean = df_sales.drop(index=bad_rows)
        return df_clean


def total_sales(df_sales: pd.DataFrame) -> pd.DataFrame:
    transform = Transform(df_sales)
    df_sales = transform.calculate_total_row()
    return df_sales


def validate_valid_sales(df_sales: pd.DataFrame) -> pd.DataFrame:
    try:
        df_validated = SalesValidSchema.validate(df_sales, lazy=True)
        return df_validated
    except pa.errors.SchemaErrors as exc:
        print(exc.failure_cases)
        bad_rows = exc.failure_cases['index'].dropna().unique()
        df_clean = df_sales.drop(index=bad_rows)
        return df_clean


def insert_data(df_sales: pd.DataFrame) -> pd.DataFrame:
    load = Load(df_sales)
    df_sales = load.load_db()
    return df_sales


if __name__ == '__main__':
    file_path = Path.cwd() / 'data/data.csv'
    df_sales = extract_file(file_path)
    df_sales = validate_sales(df_sales)
    df_sales = total_sales(df_sales)
    df_sales = validate_valid_sales(df_sales)
    df_sales = insert_data(df_sales)
