import pandas as pd

from ecommerce.pipeline.extract import Extract


def test_read_file(tmp_path):
    # Arrange

    EXPECTED_ROWS = 2
    EXPECTED_COLUMNS = 8

    test_data = (
        'InvoiceNo,StockCode,Description,Quantity,InvoiceDate,UnitPrice,'
        'CustomerID,Country\n'
        '36365,85123A,WHITE HANGING HEART T-LIGHT HOLDER,6,12/1/2010 8:26,'
        '2.55,17850,United Kingdom\n'
        '536365,71053,WHITE METAL LANTERN,6,12/1/2010 8:26,3.39,17850,'
        'United Kingdom'
    )
    expected_columns = [
        'InvoiceNo',
        'StockCode',
        'Description',
        'Quantity',
        'InvoiceDate',
        'UnitPrice',
        'CustomerID',
        'Country',
    ]

    # Act
    file_path = tmp_path / 'test_data.csv'
    file_path.write_text(test_data, encoding='ISO-8859-1')
    extract = Extract(file_path)
    extract.read_file()
    rows, cols = extract.df.shape

    # Arrange
    assert list(extract.df.columns) == expected_columns
    assert isinstance(extract.df, pd.DataFrame)
    assert not extract.df.empty
    assert rows == EXPECTED_ROWS
    assert cols == EXPECTED_COLUMNS
