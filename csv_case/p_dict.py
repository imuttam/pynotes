import csv


file = r'../csv_case/portfolio.csv'

def portfolio_list(filename):

    """portfoilio as list of tuple """
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)

        for row in rows:
            d = {}
            d[headers[0]] = row[0]
            d[headers[1]] = row[1]
            d[headers[2]] = row[2]
            portfolio.append(d)
    return portfolio

data = portfolio_list(file)
print(data)
# for row in data:
#     print(f'{row["name"]:>10s} {int(row["shares"]):10d} {float(row["price"]):10.2f}')

# Using ZIP method
port_list = []
portfolio = []
with open(file, 'rt') as f:
    rows = csv.reader(f)
    headers = next(rows)
    for row in rows:
        d = dict(zip(headers, row))
        tup = list(zip(headers, row))
        portfolio.append(d)
        port_list.append(tup)


print(portfolio)
print(port_list)


