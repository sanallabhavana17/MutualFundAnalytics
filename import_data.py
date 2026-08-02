import sqlite3
import pandas as pd

# Connect to SQLite database
connection = sqlite3.connect("database/bluestock_mf.db")

# -------------------------------
# Import NAV History
# -------------------------------
nav = pd.read_csv("Data/processed/nav_history_cleaned.csv")
nav.to_sql("nav_history", connection, if_exists="append", index=False)

print("NAV History imported successfully.")

# -------------------------------
# Import Investor Transactions
# -------------------------------
transactions = pd.read_csv("Data/processed/investor_transactions_cleaned.csv")
transactions.to_sql("investor_transactions", connection, if_exists="append", index=False)

print("Investor Transactions imported successfully.")

# -------------------------------
# Import Scheme Performance
# -------------------------------
scheme = pd.read_csv("Data/processed/scheme_performance_cleaned.csv")
scheme.to_sql("scheme_performance", connection, if_exists="append", index=False)

print("Scheme Performance imported successfully.")

# Close database connection
connection.close()

print("\nAll datasets imported successfully!")