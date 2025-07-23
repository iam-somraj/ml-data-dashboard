#step:0
import pandas as pd
import matplotlib.pyplot as plt

#step:1
data = pd.read_csv('C:/Users/user/Desktop/data/data/daily-data.csv')

#step:2
#using visualizations to spot any unusual data points
plt.figure(figsize=(10, 6))
plt.scatter(data['New_cases'], data['New_deaths'])
plt.xlabel('New cases')
plt.ylabel('New deaths')
plt.title('Scatter Plot: New Cases vs New Deaths')
plt.show()

#step:1
print(data.head())

print(data.info())

print(data.describe())

#step:3
#to identify any missing values
print(data.isnull().sum())

#step:4
print(data.dtypes)
