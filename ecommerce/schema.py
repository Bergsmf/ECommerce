import pandera.pandas as pa
from pandera.typing import Series

class SalesSchema(pa.DataFrameModel):
    InvoiceNo: Series[int]
    StockCode: Series[str]
    Description: Series[str]
    Quantity: Series[int]
    InvoiceDate: Series[pa.DateTime]
    UnitPrice: Series[float]
    CustomerID: Series[int]
    Country: Series[str]