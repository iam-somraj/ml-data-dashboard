#step:0
import pandas as pd
#step:2:a
import matplotlib.pyplot as plt

#step:1
data = pd.read_csv('daily-data.csv')

#step:2:b
#using visualizations to spot any unusual data points
plt.figure(figsize=(10, 6))
plt.scatter(data['New_cases'], data['New_deaths'])
plt.xlabel('New cases')
plt.ylabel('New deaths')
plt.title('Scatter Plot: New Cases vs New Deaths')
plt.show()

#step:1
#to get the datasets information
print(data.head())

print(data.info())

print(data.describe())

#step:3
#to identify any missing values
print(data.isnull().sum())

#step:4
#to get the data types
print(data.dtypes)
