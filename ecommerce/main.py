from pipeline.extract import ReadSells


def main():
    file_path = 'data/ecommerce-data.csv'
    sells = ReadSells()
    sells.read_file(file_path)
    return True


if __name__ == '__main__':
    main()
    print('Testa CI')
