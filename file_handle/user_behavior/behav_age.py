import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv("user_behavior_dataset.csv")

# Histogram for Age distribution
sns.histplot(data=df, x='Age', bins=10, kde=True)
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# Bar plot for Gender distribution
sns.countplot(data=df, x='Gender')
plt.title('Gender Distribution')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()
