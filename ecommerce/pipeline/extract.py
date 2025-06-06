import pandas as pd
import pandera.pandas as pa
from pandera.errors import SchemaErrors


class ReadSells:
    def __init__(self):
        self.df = None
        self.invalid_df = None
        self.valid_df = None

    def read_file(self, path: str):
        self.df = pd.read_csv(path, delimiter=',', encoding='ISO-8859-1')
        self.df['InvoiceNo'] = pd.to_numeric(
            self.df['InvoiceNo'], errors='coerce'
        ).astype('Int64')
        self.df['Quantity'] = pd.to_numeric(
            self.df['Quantity'], errors='coerce'
        ).astype('Int64')
        self.df['InvoiceDate'] = pd.to_datetime(
            self.df['InvoiceDate'], format='%m/%d/%Y %H:%M', errors='coerce'
        )
        self.df['UnitPrice'] = pd.to_numeric(
            self.df['UnitPrice'], errors='coerce'
        )
        self.df['CustomerID'] = pd.to_numeric(
            self.df['CustomerID'], errors='coerce'
        ).astype('Int64')

    def validade_file(self, valid_path: str, error_path: str):
        schema = pa.DataFrameSchema({
            'InvoiceNo': pa.Column(pa.Int64),
            'StockCode': pa.Column(str),
            'Description': pa.Column(str, nullable=False),
            'Quantity': pa.Column(pa.Int64),
            'InvoiceDate': pa.Column(pa.DateTime),
            'UnitPrice': pa.Column(float),
            'CustomerID': pa.Column(pa.Int64, nullable=False),
            'Country': pa.Column(str),
        })

        try:
            self.valid_df = schema.validate(self.df, lazy=True)
        except SchemaErrors as err:
            invalid_indices = err.failure_cases['index'].dropna().unique()
            self.invalid_df = self.df.loc[invalid_indices]
            self.valid_df = self.df.drop(index=invalid_indices)

        self.invalid_df.to_csv(error_path, index=False)
        self.valid_df.to_csv(valid_path, index=False)
