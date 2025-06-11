import pandas as pd


class Extract:
    def __init__(self, file_path: str):
        self.df = None
        self.file_path = file_path

    def read_file(self):
        self.df = pd.read_csv(self.file_path, encoding='ISO-8859-1')
