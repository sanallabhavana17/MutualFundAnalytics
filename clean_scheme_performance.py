import pandas as pd

# ==========================================================
# STEP 1: Read CSV
# ==========================================================

df = pd.read_csv("Data/Raw/drive-download-20260724T173806Z-1-001/07_scheme_performance.csv")

print("========== ORIGINAL DATA ==========\n")
print(df.head())

# ==========================================================
# STEP 2: Check Data Types
# ==========================================================

print("\n========== DATA TYPES ==========\n")
print(df.dtypes)

# ==========================================================
# STEP 3: Check Duplicate Rows
# ==========================================================

duplicate_rows = df.duplicated().sum()

print("\n========== DUPLICATE CHECK ==========")
print("Duplicate Rows Found :", duplicate_rows)

df = df.drop_duplicates()

print("Duplicate Rows After Cleaning :", df.duplicated().sum())

# ==========================================================
# STEP 4: Check Missing Values
# ==========================================================

print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

# Fill missing numeric values
numeric_columns = df.select_dtypes(include=["int64", "float64"]).columns

for col in numeric_columns:
    df[col] = df[col].fillna(df[col].median())

# ==========================================================
# STEP 5: Validate AUM
# ==========================================================

invalid_aum = df[df["aum_crore"] <= 0]

print("\n========== AUM VALIDATION ==========")
print("Invalid AUM Records :", len(invalid_aum))

df = df[df["aum_crore"] > 0]

# ==========================================================
# STEP 6: Validate Expense Ratio
# ==========================================================

invalid_expense = df[df["expense_ratio_pct"] < 0]

print("\n========== EXPENSE RATIO VALIDATION ==========")
print("Invalid Expense Ratio Records :", len(invalid_expense))

df = df[df["expense_ratio_pct"] >= 0]

# ==========================================================
# STEP 7: Validate Morningstar Rating
# ==========================================================

invalid_rating = df[
    (df["morningstar_rating"] < 1) |
    (df["morningstar_rating"] > 5)
]

print("\n========== RATING VALIDATION ==========")
print("Invalid Ratings :", len(invalid_rating))

# ==========================================================
# STEP 8: Save Cleaned Dataset
# ==========================================================

output_file = "Data/processed/scheme_performance_cleaned.csv"

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