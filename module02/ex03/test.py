from csvreader import CsvReader

# if __name__ == "__main__":
#     with CsvReader('good.csv') as file:
#         print(file)
#         data = file.getdata()
#         header = file.getheader()
#         print('header:', header)
#         for row in data:
#             print(row)

if __name__ == "__main__":
    with CsvReader('bad.csv') as file:
        print(file)
        if (file is None):
            exit()
        data = file.getdata()
        header = file.getheader()
        print('header:', header)
        for row in data:
            print(row)
