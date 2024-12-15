import pandas as pd
data = pd.read_csv( 'https://raw.githubusercontent.com/fivethirtyeight/data/master/alcohol-consumption/drinks.csv' )

print(data.head())
# print(alcohol_data.tail())
print(data.columns)

df = data.groupby('country')['total_litres_of_pure_alcohol'].mean()
print(df)