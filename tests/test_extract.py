import pandas as pd

from ecommerce.pipeline.extract import ReadSells


def test_read_file():
    file_path = 'data/src/ecommerce-data.csv'

    reader = ReadSells()
    reader.read_file(file_path)

    assert reader.df is not None
    assert isinstance(reader.df, pd.DataFrame)
    assert not reader.df.empty
    assert list(reader.df.columns) == [
        'InvoiceNo',
        'StockCode',
        'Description',
        'Quantity',
        'InvoiceDate',
        'UnitPrice',
        'CustomerID',
        'Country',
    ]


def test_validade_file(tmp_path):
    error_path = 'data/error/error_ecommerce.csv'
    valid_path = 'data/temp/temp_ecommerce.csv'

    data = {
        'InvoiceNo': [123456, None],
        'StockCode': ['A100', 'B200'],
        'Description': ['Product A', None],
        'Quantity': [10, 5],
        'InvoiceDate': [
            pd.Timestamp('2023-01-01'),
            pd.Timestamp('2023-01-02'),
        ],
        'UnitPrice': [20.5, 10.0],
        'CustomerID': [12345, None],
        'Country': ['United Kingdom', 'France'],
    }
    df = pd.DataFrame(data)
    reader = ReadSells()
    reader.df = df
    reader.validade_file(valid_path, error_path)
    assert isinstance(reader.valid_df, pd.DataFrame)
    assert isinstance(reader.invalid_df, pd.DataFrame)
    df_valid = pd.read_csv(valid_path)
    df_error = pd.read_csv(error_path)
    assert len(df_valid) == 1
    assert len(df_error) == 1
