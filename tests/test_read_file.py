import pandas as pd
import pytest

from ecommerce.main import (
    extract_file,
    total_sales,
    validate_sales,
    insert_data,
    validate_valid_sales,
)


@pytest.fixture
def temp_csv(tmp_path):
    data = {
        'InvoiceNo': [536365, 'C536379'],
        'StockCode': ['85123A', '71053'],
        'Description': ['WHITE HANGING HEART T-LIGHT HOLDER', None],
        'Quantity': [6, 6],
        'InvoiceDate': ['12/1/2010 8:26', '12/1/2010 8:34'],
        'UnitPrice': [2.55, 3.39],
        'CustomerID': [17850.0, None],
        'Country': ['United Kingdom', 'United Kingdom'],
    }
    df = pd.DataFrame(data)

    temp_file = tmp_path / 'temp_data.csv'
    df.to_csv(temp_file, index=False, encoding='ISO-8859-1')
    return df, temp_file


def structure(rows: int, extra_column: int = 0):
    column_names = [
        'InvoiceNo',
        'StockCode',
        'Description',
        'Quantity',
        'InvoiceDate',
        'UnitPrice',
        'CustomerID',
        'Country',
    ]
    extra_columns = {0: [], 1: ['Total', 'MonthSale']}

    full_column_names = column_names + extra_columns.get(extra_column, [])
    expected_rows = rows
    expected_columns = len(full_column_names)

    return expected_rows, expected_columns, full_column_names


def test_extract_file(temp_csv):
    # Arrange
    expected_rows, expected_columns, column_names = structure(2)
    file = temp_csv[1]

    # Act
    extract = extract_file(file)
    rows, cols = extract.shape

    # Arrange
    assert list(extract.columns) == column_names
    assert isinstance(extract, pd.DataFrame)
    assert not extract.empty
    assert rows == expected_rows
    assert cols == expected_columns


def test_validate_sales(temp_csv):
    # Arrange
    expected_rows, expected_columns, column_names = structure(1)
    df = temp_csv[0]

    # Act
    df_clean = validate_sales(df)
    rows, cols = df_clean.shape

    # Assert
    assert list(df_clean.columns) == column_names
    assert isinstance(df_clean, pd.DataFrame)
    assert rows == expected_rows
    assert cols == expected_columns


def test_total_sales(temp_csv):
    # Arrange
    expected_rows, expected_columns, column_names = structure(1, 1)
    df = temp_csv[0]

    # Act
    df_clean = validate_sales(df)
    df_total = total_sales(df_clean)
    rows, cols = df_total.shape

    # Assert
    assert list(df_total.columns) == column_names
    assert isinstance(df_total, pd.DataFrame)
    assert df_total['Total'].equals(
        df_total['Quantity'] * df_total['UnitPrice']
    )
    assert df_total['MonthSale'].equals(
        df_total['InvoiceDate'].dt.to_period('M').dt.to_timestamp()
    )
    assert rows == expected_rows
    assert cols == expected_columns

def test_validate_valid_sales(temp_csv):
    # Arrange
    expected_rows, expected_columns, column_names = structure(1, 1)
    df = temp_csv[0]

    # Act
    df_clean = validate_sales(df)
    df_total = total_sales(df_clean)
    df_valid_total = validate_valid_sales(df_total)
    rows, cols = df_valid_total.shape

    # Assert
    assert list(df_valid_total.columns) == column_names
    assert isinstance(df_valid_total, pd.DataFrame)
    assert df_valid_total['Total'].equals(
        df_valid_total['Quantity'] * df_valid_total['UnitPrice']
    )
    assert df_valid_total['MonthSale'].equals(
        df_valid_total['InvoiceDate'].dt.to_period('M').dt.to_timestamp()
    )
    assert rows == expected_rows
    assert cols == expected_columns

def test_insert_data(temp_csv):
    # Arrange
    expected_rows, expected_columns, column_names = structure(1, 1)
    df = temp_csv[0]

    # Act
    df_clean = validate_sales(df)
    df_total = total_sales(df_clean)
    df_valid_total = validate_valid_sales(df_total)
    df_inserted = insert_data(df_valid_total)
    rows, cols = df_inserted.shape

    # Assert
    assert list(df_inserted.columns) == column_names
    assert isinstance(df_inserted, pd.DataFrame)
    assert df_valid_total.equals(df_inserted)
    assert rows == expected_rows
    assert cols == expected_columns