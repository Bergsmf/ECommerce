import pandas as pd


class Transform:
    def __init__(self, df_sales: pd.DataFrame):
        self.df_sales = df_sales

    def calculate_total_row(self) -> pd.DataFrame:
        self.df_sales['Total'] = (
            self.df_sales['Quantity'] * self.df_sales['UnitPrice']
        )
        self.df_sales['MonthSale'] = (
            self.df_sales['InvoiceDate'].dt.to_period('M').dt.to_timestamp()
        )
        return self.df_sales
