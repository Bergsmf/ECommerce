import pandas as pd

class ReadSells:
    def __init__(self):
        self.df = None
    
    def read_file(self, path: str):
        df_sells = pd.read_csv(path, delimiter = ",", encoding="ISO-8859-1")
        print(df_sells)