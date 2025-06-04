import pandas as pd

from ecommerce.pipeline.extract import ReadSells


def test_read_file():
    file_path = 'data/ecommerce-data.csv'

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
