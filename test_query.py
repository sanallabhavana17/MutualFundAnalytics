import sqlite3
import pandas as pd

connection = sqlite3.connect("database/bluestock_mf.db")

query = """
SELECT COUNT(*) AS Total_Transactions
FROM investor_transactions;
"""

result = pd.read_sql_query(query, connection)
print(result)

connection.close()