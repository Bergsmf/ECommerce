from pipeline.extract import ReadSells

if __name__ == "__main__":
    file_path = "data/ecommerce-data.csv"
    sells = ReadSells()
    sells.read_file(file_path)