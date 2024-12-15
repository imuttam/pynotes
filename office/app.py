import csv

with open('master_data.csv', 'r') as file:
    rows = csv.reader(file)
    headers = next(rows)
    row1 = next(rows)
  

print(headers)
print(row1)
