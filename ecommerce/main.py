from pipeline.extract import Extract


def read_file():
    file_path = 'data/data.csv'
    extract = Extract(file_path)
    extract.read_file()


if __name__ == '__main__':
    read_file()