import sqlite3

# Connect to the database
connection = sqlite3.connect("database/bluestock_mf.db")

# Read SQL file
with open("SQL/schema.sql", "r") as file:
    sql_script = file.read()

# Execute SQL commands
connection.executescript(sql_script)

print("Tables created successfully!")

# Close connection
connection.close()