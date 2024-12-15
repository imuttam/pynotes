import csv 

records = {}
with open('./data_set/portfolio.csv') as file:
    rows = csv.reader(file)
    headers = next(rows)
    for row in rows:
        records[row[0]] = row[-1]

print(records)