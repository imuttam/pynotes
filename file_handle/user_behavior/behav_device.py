import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


df = pd.read_csv("user_behavior_dataset.csv")

# Calculate average values for device model
device_stats = df.groupby('Device Model')[['App Usage Time (min/day)', 'Battery Drain (mAh/day)']].mean()
print(device_stats)

# Plot average App Usage Time by Operating System
sns.barplot(data=df, x='Operating System', y='App Usage Time (min/day)')
plt.title('Average App Usage Time by Operating System')
plt.xlabel('Operating System')
plt.ylabel('Average App Usage Time (min/day)')
plt.show()
