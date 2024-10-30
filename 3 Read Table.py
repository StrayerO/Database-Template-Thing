import sqlite3

def fetch_students():
    # Connect to the database
    conn = sqlite3.connect('DatabaseFile.db')
    cursor = conn.cursor()

    # Execute a query to fetch all records from the studentInfo table
    cursor.execute('SELECT * FROM studentInfo')

    # Fetch all rows from the executed query
    students = cursor.fetchall()

    # Print each student record
    for student in students:
        print(f"ID: {student[0]}, First Name: {student[1]}, Last Name: {student[2]}")

    # Close the connection
    conn.close()

# Example usage
fetch_students()
