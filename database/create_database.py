import sqlite3

# Create database in the current (database) folder
connection = sqlite3.connect("bluestock_mf.db")

print("Database created successfully!")

connection.close()