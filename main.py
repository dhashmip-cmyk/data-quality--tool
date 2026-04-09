print("Hello,Data Quality Tool!")
import pandas as pd

# CSV file load
df = pd.read_csv("data.csv")

# First 5 rows பார்க்க
print("First 5 rows:")
print(df.head())

# Column names
print("\nColumns:")
print(df.columns)

# Missing values check
print("\nMissing values:")
print(df.isnull().sum())

# Basic info
print("\nData Info:")
print(df.info())

# Duplicate rows check
print("\nDuplicate rows:", df.duplicated().sum())
