import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('daily-data.csv')

# Get the count of missing values in each column
missing_values = df.isnull().sum()
print("Missing Values Count:")
print(missing_values)

# Visualize the missing values
plt.figure(figsize=(10, 6))
df.isnull().sum().plot(kind='bar')
plt.title('Missing Values by Column')
plt.xlabel('Column Name')
plt.ylabel('Count of Missing Values')
plt.xticks(rotation=45)  # Added rotation for better readability
plt.tight_layout()  # Added to prevent label cutoff
plt.show()

# Drop columns with more than 50% missing values
df = df.dropna(axis=1, thresh=len(df)*0.5)

# Drop rows with any missing values
df = df.dropna(axis=0, how='any')

# Impute numerical columns with mean
numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns
df[numerical_cols] = df[numerical_cols].fillna(df[numerical_cols].mean())

# Impute categorical columns with mode
categorical_cols = df.select_dtypes(include=['object']).columns
for col in categorical_cols:  # Fixed: Handle each categorical column separately
    if not df[col].empty and df[col].mode().shape[0] > 0:  # Check if mode exists
        df[col] = df[col].fillna(df[col].mode()[0])

numerical_df = df.select_dtypes(include=['int64', 'float64'])

# Store bounds for each column to use later
outlier_bounds = {}  # Added to store bounds for each column

for col in numerical_df.columns:
    Q1 = numerical_df[col].quantile(0.25)
    Q3 = numerical_df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    outlier_bounds[col] = (lower_bound, upper_bound)  # Store bounds
    
    print(f"Outlier bounds for {col}:")
    print(f"Lower bound: {lower_bound}")
    print(f"Upper bound: {upper_bound}")
    
    # Visualize outliers using boxplot
    plt.figure(figsize=(10, 6))
    plt.boxplot(numerical_df[col], vert=False)
    plt.title(f'Boxplot for {col}')
    plt.xlabel('Values')  # Added axis label
    plt.show()

# Fixed: Apply outlier filtering correctly for each column
for col in numerical_cols:
    lower_bound, upper_bound = outlier_bounds[col]  # Use stored bounds
    df = df[(df[col] >= lower_bound) & (df[col] <= upper_bound)]

def cap_values(value, lower_bound, upper_bound):
    if value < lower_bound:
        return lower_bound
    elif value > upper_bound:
        return upper_bound
    else:
        return value

# Apply capping to each numerical column
for col in numerical_cols:
    if col in df.columns:  # Check if column still exists after filtering
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        
        df[col] = df[col].apply(lambda x: cap_values(x, lower_bound, upper_bound))

# Print final dataset info
print(f"\nFinal dataset shape: {df.shape}")
print("Final missing values:")
print(df.isnull().sum())
    
# Save the cleaned DataFrame to a new CSV file
df.to_csv('cleaned_dataset.csv', index=False)

