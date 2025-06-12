import pandas as pd
import pytest

from ecommerce.main import extract_file, validate_sales


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


def structure(rows: int, columns: int):
    expected_rows = rows
    expected_columns = columns

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

    return expected_rows, expected_columns, column_names


def test_extract_file(temp_csv):
    # Arrange
    expected_rows, expected_columns, column_names = structure(2, 8)
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
    expected_rows, expected_columns, column_names = structure(1, 8)
    df = temp_csv[0]

    # Act
    df_clean = validate_sales(df)
    rows, cols = df_clean.shape

    # Assert
    assert list(df_clean.columns) == column_names
    assert isinstance(df_clean, pd.DataFrame)
    assert rows == expected_rows
    assert cols == expected_columns
