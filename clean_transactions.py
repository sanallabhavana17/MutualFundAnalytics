import pandas as pd

# ==========================================================
# STEP 1: Read the CSV file
# ==========================================================

df = pd.read_csv("Data/Raw/drive-download-20260724T173806Z-1-001/08_investor_transactions.csv")

print("========== ORIGINAL DATA ==========\n")
print(df.head())

# ==========================================================
# STEP 2: Check Data Types
# ==========================================================

print("\n========== DATA TYPES ==========\n")
print(df.dtypes)

# ==========================================================
# STEP 3: Convert Transaction Date
# ==========================================================

df["transaction_date"] = pd.to_datetime(df["transaction_date"])

print("\nTransaction Date converted successfully.")

# ==========================================================
# STEP 4: Remove Duplicate Rows
# ==========================================================

duplicate_rows = df.duplicated().sum()

print("\n========== DUPLICATE CHECK ==========")
print("Duplicate Rows Found :", duplicate_rows)

df = df.drop_duplicates()

print("Duplicate Rows After Cleaning :", df.duplicated().sum())

# ==========================================================
# STEP 5: Check Missing Values
# ==========================================================

print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

# ==========================================================
# STEP 6: Standardize Transaction Type
# ==========================================================

df["transaction_type"] = df["transaction_type"].str.strip().str.title()

allowed_types = ["Sip", "Lumpsum", "Redemption"]

invalid_transaction = df[~df["transaction_type"].isin(allowed_types)]

print("\n========== TRANSACTION TYPE CHECK ==========")
print("Invalid Transaction Types :", len(invalid_transaction))

# ==========================================================
# STEP 7: Validate Amount
# ==========================================================

invalid_amount = df[df["amount_inr"] <= 0]

print("\n========== AMOUNT VALIDATION ==========")
print("Invalid Amount Rows :", len(invalid_amount))

df = df[df["amount_inr"] > 0]

# ==========================================================
# STEP 8: Validate KYC Status
# ==========================================================

allowed_kyc = ["Verified", "Pending", "Rejected"]

invalid_kyc = df[~df["kyc_status"].isin(allowed_kyc)]

print("\n========== KYC STATUS ==========")
print("Invalid KYC Records :", len(invalid_kyc))

# ==========================================================
# STEP 9: Save Cleaned Dataset
# ==========================================================

output_file = "Data/processed/investor_transactions_cleaned.csv"

df.to_csv(output_file, index=False)

print("\n========== FILE SAVED ==========")
print("Cleaned file saved successfully!")
print("Location :", output_file)

# ==========================================================
# STEP 10: Final Summary
# ==========================================================

print("\n========== FINAL SUMMARY ==========")
print("Total Rows :", len(df))
print("Total Columns :", len(df.columns))

print("\nColumn Names:")
print(df.columns.tolist())

print("\nFirst 5 Rows:")
print(df.head())