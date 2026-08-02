import pandas as pd

# Load cleaned dataset
df = pd.read_csv("Data/processed/investor_transactions_cleaned.csv")

print("="*50)
print("DATASET INFORMATION")
print("="*50)

print(df.info())

print("\n")

print("="*50)
print("DESCRIPTIVE STATISTICS")
print("="*50)

print(df.describe())

print("\n")

print("="*50)
print("MISSING VALUES")
print("="*50)

print(df.isnull().sum())

print("\n")

print("="*50)
print("TRANSACTION TYPES")
print("="*50)

print(df["transaction_type"].value_counts())

print("\n")

print("="*50)
print("PAYMENT MODES")
print("="*50)

print(df["payment_mode"].value_counts())

print("\n")

print("="*50)
print("KYC STATUS")
print("="*50)

print(df["kyc_status"].value_counts())

print("\n")

print("="*50)
print("TOP 10 STATES")
print("="*50)

print(df["state"].value_counts().head(10))