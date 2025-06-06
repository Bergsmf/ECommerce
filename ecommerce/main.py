from pipeline.extract import ReadSells


def le_arquivo():
    file_path = 'data/src/ecommerce-data.csv'
    error_path = 'data/error/error_ecommerce.csv'
    valid_path = 'data/temp/temp_ecommerce.csv'
    sells = ReadSells()
    sells.read_file(file_path)
    sells.validade_file(valid_path, error_path)


if __name__ == '__main__':
    le_arquivo()
