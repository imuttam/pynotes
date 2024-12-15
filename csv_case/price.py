import csv

with open('./csv_case/prices.csv') as f:
    rows = csv.reader(f)
    headers = next(rows)

    for row in rows:
        if row:
            print(row)
