import sqlite3
import pandas as pd

# Connect to database
connection = sqlite3.connect("database/bluestock_mf.db")
# List of SQL queries
queries = [
    ("Total Transactions",
     "SELECT COUNT(*) AS Total_Transactions FROM investor_transactions;"),

    ("Total Transaction Amount",
     "SELECT SUM(amount_inr) AS Total_Amount FROM investor_transactions;"),

    ("Average Transaction Amount",
     "SELECT AVG(amount_inr) AS Average_Amount FROM investor_transactions;"),

    ("Transactions by Type",
     """
     SELECT transaction_type,
            COUNT(*) AS Total
     FROM investor_transactions
     GROUP BY transaction_type;
     """),

    ("Investment by Transaction Type",
     """
     SELECT transaction_type,
            SUM(amount_inr) AS Total_Investment
     FROM investor_transactions
     GROUP BY transaction_type;
     """),

    ("Top 10 Schemes by AUM",
     """
     SELECT scheme_name,
            aum_crore
     FROM scheme_performance
     ORDER BY aum_crore DESC
     LIMIT 10;
     """),

    ("Average Expense Ratio",
     """
     SELECT AVG(expense_ratio_pct) AS Average_Expense_Ratio
     FROM scheme_performance;
     """),

    ("Top 5 Highest 1-Year Returns",
     """
     SELECT scheme_name,
            return_1yr_pct
     FROM scheme_performance
     ORDER BY return_1yr_pct DESC
     LIMIT 5;
     """),

    ("Schemes by Risk Grade",
     """
     SELECT risk_grade,
            COUNT(*) AS Total_Schemes
     FROM scheme_performance
     GROUP BY risk_grade;
     """),

    ("NAV Statistics",
     """
     SELECT
     COUNT(*) AS Total_NAV_Records,
     MAX(nav) AS Highest_NAV,
     MIN(nav) AS Lowest_NAV,
     AVG(nav) AS Average_NAV
     FROM nav_history;
     """)
]

# Execute queries
for title, query in queries:
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)

    result = pd.read_sql_query(query, connection)
    print(result)

connection.close()

print("\nAll SQL Queries Executed Successfully!")