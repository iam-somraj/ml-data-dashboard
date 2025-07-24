import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('daily-data.csv')

plt.figure(figsize=(10, 6))
plt.scatter(data['New_cases'], data['New_deaths'])
plt.xlabel('New cases')
plt.ylabel('New deaths')
plt.title('Scatter Plot: New Cases vs New Deaths')
plt.show()
