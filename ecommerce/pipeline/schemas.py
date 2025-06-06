from datetime import datetime

import pandera.pandas as pa


class data_template(pa.DataFrameModel):
    InvoiceNo: int
    StockCode: str
    Description: str
    Quantity: int
    InvoiceDate: datetime
    UnitPrice: float
    CustomerID: int
    Country: str
