import pandas as pd

# Read the CSV files
fund_master = pd.read_csv("Data/Raw/drive-download-20260724T173806Z-1-001/01_fund_master.csv")
nav_history = pd.read_csv("Data/Raw/drive-download-20260724T173806Z-1-001/02_nav_history.csv")

# Get unique AMFI codes
fund_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

# Find missing codes
missing_in_nav = fund_codes - nav_codes
missing_in_fund = nav_codes - fund_codes

print("=" * 60)
print("AMFI CODE VALIDATION")
print("=" * 60)

if len(missing_in_nav) == 0:
    print("✅ All AMFI codes in fund_master.csv exist in nav_history.csv")
else:
    print("❌ Missing in nav_history.csv:")
    print(missing_in_nav)

print()

if len(missing_in_fund) == 0:
    print("✅ No extra AMFI codes in nav_history.csv")
else:
    print("❌ Extra AMFI codes found:")
    print(missing_in_fund)