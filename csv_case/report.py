import csv


file = r'./data_set/portfolio.csv'

def portfolio_list(filename):

    """portfoilio as list of tuple """
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            portfolio.append((row[0], int(row[1]), float(row[2])))
    return portfolio

print(portfolio_list(file))
sorted_tuple = sorted(portfolio_list(file), key = lambda x : x[1], reverse=True)
print(sorted_tuple)
data = portfolio_list(file)

total = 0.0

for name,share,price in data:
    total += share*price

print(total)
