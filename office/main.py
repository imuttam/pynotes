import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('master_data.csv')

# Convert the 'DATE' column to datetime
df['DATE'] = pd.to_datetime(df['DATE'], format='%d-%m-%Y')

# Convert 'Total DATA Traffic in GB 4G' to numeric, handling non-numeric values as NaN
df['Total DATA Traffic in GB 4G'] = pd.to_numeric(df['Total DATA Traffic in GB 4G'], errors='coerce')

# Extract month and year for grouping
df['Year-Month'] = df['DATE'].dt.to_period('M')

# Group by 'Year-Month' and calculate the sum of 'Total DATA Traffic in GB 4G'
monthly_data_traffic_sum = df.groupby('Year-Month')['Total DATA Traffic in GB 4G'].sum().reset_index()

# Write the result to a new CSV file
monthly_data_traffic_sum.to_csv('monthly_4G_data_traffic.csv', index=False)


# Display the result
print(monthly_data_traffic_sum)
