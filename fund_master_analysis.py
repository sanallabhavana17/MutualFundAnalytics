import pandas as pd

# Read the CSV file
df = pd.read_csv("Data/Raw/drive-download-20260724T173806Z-1-001/01_fund_master.csv")

print("=" * 60)
print("FUND HOUSES")
print("=" * 60)
print(df["fund_house"].unique())

print("\nTotal Fund Houses:", df["fund_house"].nunique())

print("\n" + "=" * 60)
print("CATEGORIES")
print("=" * 60)
print(df["category"].unique())

print("\nTotal Categories:", df["category"].nunique())

print("\n" + "=" * 60)
print("SUB-CATEGORIES")
print("=" * 60)
print(df["sub_category"].unique())

print("\nTotal Sub-Categories:", df["sub_category"].nunique())

print("\n" + "=" * 60)
print("RISK CATEGORIES")
print("=" * 60)
print(df["risk_category"].unique())

print("\nTotal Risk Categories:", df["risk_category"].nunique())