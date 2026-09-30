import pandas as pd

# Load the raw telecom customer churn dataset
df = pd.read_csv("data/raw/Telco-Customer-Churn.csv")

# Inspect the dataset structures and columns
print("--- Dataset Shape (Rows, Columns) ---")
print(df.shape)

print("\n--- First 5 Rows of Data ---")
print(df.head())

print("\n--- Column Data Types and Info ---")
print(df.info())

print("\n--- Missing Value Count Per Column ---")
print(df.isna().sum())
