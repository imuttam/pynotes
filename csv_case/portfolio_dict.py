import csv
from pprint import pprint

file = r'./data_set/portfolio.csv'

def portfolio_list(filename):

    """portfoilio as list of tuple """
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            d = dict(zip(headers,row))
            portfolio.append(d)
    return portfolio

# pprint(portfolio_list(file))

data = portfolio_list(file)


for d in data:
   
    print(f"{d['name']:>10s} {d['shares']:>10s} {d['price']:>10s}")