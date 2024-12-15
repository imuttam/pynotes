import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("user_behavior_dataset.csv")

head = df.head()
columns = df.columns

# Check for missing values in each column
#print(df.isnull().sum())
# Check data types of each column
df.dtypes


# Plot boxplots for quick visualization of outliers
numeric_columns = ['App Usage Time (min/day)', 'Screen On Time (hours/day)', 
                   'Battery Drain (mAh/day)', 'Data Usage (MB/day)']
for col in numeric_columns:
    sns.boxplot(data=df, x=col)
    plt.title(f'Boxplot of {col}')
    plt.show()

print(df.describe())