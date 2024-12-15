# Using ZIP method

import csv
import os

file = r'../score.csv'


portfolio = []
with open(file, 'rt') as f:
    rows = csv.reader(f)
    headers = next(rows)
    for row in rows:
        d = dict(zip(headers, row))
        portfolio.append(d)

print('#########################################################'*5)
for d in portfolio:
    if int(d['Mathematics']) > 80:
        print(d['Name'])

