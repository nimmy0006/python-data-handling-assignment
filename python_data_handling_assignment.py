# Python Data Handling Assignment using Pandas and NumPy

import numpy as np
import pandas as pd

# 1. NumPy Array Creation and Operations
arr = np.array([10, 20, 30, 40, 50])
print("Original Array:", arr)
print("Mean:", np.mean(arr))
print("Standard Deviation:", np.std(arr))
print("Array + 10:", arr + 10)

# 2. Creating a Pandas DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 30, 35, np.nan, 28],
    'Score': [85, 90, np.nan, 88, 92]
}
df = pd.DataFrame(data)
print("\nDataFrame:\n", df)

# 3. Data Cleaning
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Score'].fillna(df['Score'].mean(), inplace=True)
print("\nAfter handling missing data:\n", df)

# 4. Selection and Filtering
print("\nStudents with Score > 88:\n", df[df['Score'] > 88])

# 5. Grouping and Aggregation
grouped = df.groupby('Age').agg({'Score': 'mean'})
print("\nGrouped by Age:\n", grouped)

# 6. Merging DataFrames
extra_data = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Grade': ['A', 'B', 'A', 'B', 'A']
})
merged_df = pd.merge(df, extra_data, on='Name')
print("\nMerged DataFrame:\n", merged_df)