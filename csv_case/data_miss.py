import csv


file = r'./data_set/missing.csv'

with open(file, 'rt') as f:
    rows = csv.reader(f)
    headers = next(rows)
    for index,row in enumerate(rows):
        try:
            print(f'{index} {row[0]:>10s} {int(row[1]):10d} {float(row[2]):10.2f}')
        except:
            print(f' Couldn not convert: {row}')