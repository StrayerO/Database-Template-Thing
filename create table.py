import sqlite3

# Connect to the database (will create the database file if it doesn't exist)
conn = sqlite3.connect('DatabaseFile.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create the studentInfo table
cursor.execute('''
CREATE TABLE IF NOT EXISTS studentInfo (
    studentID INTEGER PRIMARY KEY,
    firstName TEXT NOT NULL,
    lastName TEXT NOT NULL
)
''')

# Commit changes and close the connection
conn.commit()
conn.close()
