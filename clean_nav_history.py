import pandas as pd

# ==========================================================
# STEP 1: Read the CSV file
# ==========================================================

df = pd.read_csv("Data/Raw/drive-download-20260724T173806Z-1-001/02_nav_history.csv")

print("========== ORIGINAL DATA ==========\n")
print(df.head())

# ==========================================================
# STEP 2: Check data types
# ==========================================================

print("\n========== DATA TYPES BEFORE CONVERSION ==========\n")
print(df.dtypes)

# ==========================================================
# STEP 3: Convert 'date' column to datetime
# ==========================================================

df["date"] = pd.to_datetime(df["date"])

print("\n========== DATA TYPES AFTER CONVERSION ==========\n")
print(df.dtypes)

# ==========================================================
# STEP 4: Sort by AMFI Code and Date
# ==========================================================

df = df.sort_values(by=["amfi_code", "date"])

print("\n========== SORTED DATA ==========\n")
print(df.head())

# ==========================================================
# STEP 5: Check Duplicate Rows
# ==========================================================

duplicate_rows = df.duplicated().sum()

print("\n========== DUPLICATE CHECK ==========")
print("Duplicate Rows Found :", duplicate_rows)

# Remove duplicates
df = df.drop_duplicates()

# Verify duplicates again
print("Duplicate Rows After Cleaning :", df.duplicated().sum())

# ==========================================================
# STEP 6: Check Missing Values
# ==========================================================

print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

# Fill missing NAV values using Forward Fill
df["nav"] = df["nav"].ffill()

# ==========================================================
# STEP 7: Validate NAV Values
# ==========================================================

invalid_nav = df[df["nav"] <= 0]

print("\n========== NAV VALIDATION ==========")
print("Invalid NAV Values :", len(invalid_nav))

# Remove invalid NAV rows if any exist
df = df[df["nav"] > 0]

# ==========================================================
# STEP 8: Save Cleaned Dataset
# ==========================================================

output_file = "Data/processed/nav_history_cleaned.csv"

df.to_csv(output_file, index=False)

print("\n========== FILE SAVED ==========")
print("Cleaned file saved successfully!")
print("Location :", output_file)

# ==========================================================
# STEP 9: Final Summary
# ==========================================================

print("\n========== FINAL SUMMARY ==========")
print("Total Rows :", len(df))
print("Total Columns :", len(df.columns))

print("\nColumn Names:")
print(df.columns.tolist())

print("\nFirst 5 Rows:")
print(df.head())