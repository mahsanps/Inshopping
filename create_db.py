import sqlite3

# Create a connection to the database
conn = sqlite3.connect('db.sqlite3')

# Close the connection
conn.close()

print("Database created successfully.")
