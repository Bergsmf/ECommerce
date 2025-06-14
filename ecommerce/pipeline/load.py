import conn_duckdb as cd
import pandas as pd


class Load:
    def __init__(self, df_sales: pd.DataFrame):
        self.df_sales = df_sales

    def load_db(self) -> pd.DataFrame:
        cd.drop_db()
        con = cd.get_conn()
        con.register('curr_sales', self.df_sales)
        con.execute('CREATE TABLE SALES AS SELECT * FROM curr_sales')
        df_saved = con.execute('SELECT * FROM SALES').fetchdf()
        return df_saved
