import sqlite3
import pandas as pd

# Connect to database
connection = sqlite3.connect("database/bluestock_mf.db")
# Check nav_history table
print("========== NAV HISTORY ==========")
query = "SELECT COUNT(*) AS Total_Rows FROM nav_history"
print(pd.read_sql(query, connection))

# Check investor_transactions table
print("\n========== INVESTOR TRANSACTIONS ==========")
query = "SELECT COUNT(*) AS Total_Rows FROM investor_transactions"
print(pd.read_sql(query, connection))

# Check scheme_performance table
print("\n========== SCHEME PERFORMANCE ==========")
query = "SELECT COUNT(*) AS Total_Rows FROM scheme_performance"
print(pd.read_sql(query, connection))

connection.close()