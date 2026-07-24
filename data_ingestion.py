import os
import pandas as pd

# -----------------------------
# Project Paths
# -----------------------------
DATA_FOLDER = "Data/Raw/drive-download-20260724T173806Z-1-001"
REPORT_FOLDER = "Reports"
REPORT_FILE = os.path.join(REPORT_FOLDER, "data_quality_report.txt")

# Create Reports folder if it doesn't exist
os.makedirs(REPORT_FOLDER, exist_ok=True)

# Get all CSV files
csv_files = sorted([f for f in os.listdir(DATA_FOLDER) if f.endswith(".csv")])

print("=" * 70)
print("        MUTUAL FUND ANALYTICS - DATA INGESTION")
print("=" * 70)

report = []

for file in csv_files:

    file_path = os.path.join(DATA_FOLDER, file)

    print("\n" + "=" * 70)
    print(f"Processing: {file}")
    print("=" * 70)

    report.append("=" * 70)
    report.append(f"FILE : {file}")
    report.append("=" * 70)

    try:
        df = pd.read_csv(file_path)

        # Basic Information
        print(f"Rows    : {df.shape[0]}")
        print(f"Columns : {df.shape[1]}")

        report.append(f"Rows    : {df.shape[0]}")
        report.append(f"Columns : {df.shape[1]}")

        print("\nColumn Names:")
        print(df.columns.tolist())

        report.append("\nColumn Names:")
        report.append(str(df.columns.tolist()))

        print("\nData Types:")
        print(df.dtypes)

        report.append("\nData Types:")
        report.append(str(df.dtypes))

        print("\nFirst 5 Rows:")
        print(df.head())

        report.append("\nFirst 5 Rows:")
        report.append(df.head().to_string())

        # Missing Values
        missing = df.isnull().sum()
        total_missing = missing.sum()

        print("\nMissing Values:")
        print(missing)

        report.append("\nMissing Values:")
        report.append(missing.to_string())
        report.append(f"\nTotal Missing Values : {total_missing}")

        # Duplicate Rows
        duplicates = df.duplicated().sum()

        print(f"\nDuplicate Rows : {duplicates}")

        report.append(f"\nDuplicate Rows : {duplicates}")

        # Empty Rows
        empty_rows = df.isna().all(axis=1).sum()

        print(f"Completely Empty Rows : {empty_rows}")

        report.append(f"Completely Empty Rows : {empty_rows}")

        # Summary
        report.append("\nSummary:")

        if total_missing == 0:
            report.append("✔ No missing values found.")
        else:
            report.append(f"⚠ {total_missing} missing values found.")

        if duplicates == 0:
            report.append("✔ No duplicate rows found.")
        else:
            report.append(f"⚠ {duplicates} duplicate rows found.")

        report.append("\n")

    except Exception as e:

        print(f"Error reading {file}")
        print(e)

        report.append(f"Error reading file: {e}")
        report.append("\n")

# Save Report
with open(REPORT_FILE, "w", encoding="utf-8") as f:
    f.write("\n".join(report))

print("\n" + "=" * 70)
print("Data Ingestion Completed Successfully")
print(f"Report saved to: {REPORT_FILE}")
print("=" * 70)