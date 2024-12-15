# Assuming you are running this script from inside the 'csv_case' directory

import os

# Define the relative path to the score.csv file
relative_path = '../score.csv'

# Verify the path
absolute_path = os.path.abspath(relative_path)
print(f"The absolute path to the score.csv file is: {absolute_path}")

# Read the CSV file using pandas
import pandas as pd

# Read the CSV file
data = pd.read_csv(relative_path)

# Print the first few rows of the dataframe
print(data.head())
