import pandera.pandas as pa
from pandera.typing import Index, Series


class SalesSchema(pa.DataFrameModel):
    InvoiceNo: Series[int]
    StockCode: Series[str]
    Description: Series[str]
    Quantity: Series[int]
    InvoiceDate: Series[pa.DateTime]
    UnitPrice: Series[float]
    CustomerID: Series[int] = pa.Field(nullable=True)
    Country: Series[str]
    index: Index[int]

    class Config:
        coerce = True
        strict = True
