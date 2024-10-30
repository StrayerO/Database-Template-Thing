import sqlite3

def add_student(student_id, first_name, last_name):
    # Connect to the database
    conn = sqlite3.connect('DatabaseFile.db')
    cursor = conn.cursor()

    # Insert a new student record into the studentInfo table
    cursor.execute('''
    INSERT INTO studentInfo (studentID, firstName, lastName)
    VALUES (?, ?, ?)
    ''', (student_id, first_name, last_name))

    # Commit changes and close the connection
    conn.commit()
    print(f"Student {first_name} {last_name} added with ID {student_id}.")
    conn.close()

# Example usage
add_student(1, 'John', 'Doe')
add_student(2, 'Jane', 'Smith')
