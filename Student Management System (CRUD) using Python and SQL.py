import sqlite3

# Connect to database (or create it)
conn = sqlite3.connect('students.db')
cursor = conn.cursor()

# Create table if not exists
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    course TEXT
)
''')

# Function to add new student
def add_student(name, age, course):
    cursor.execute("INSERT INTO students (name, age, course) VALUES (?, ?, ?)", (name, age, course))
    conn.commit()
    print("✅ Student added successfully.\n")

# Function to view all students
def view_students():
    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()
    print("\n📋 Student Records:")
    for row in records:
        print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Course: {row[3]}")
    print()

# Function to search student by ID
def search_student(student_id):
    cursor.execute("SELECT * FROM students WHERE id=?", (student_id,))
    record = cursor.fetchone()
    if record:
        print(f"\n📌 Student Found: ID: {record[0]}, Name: {record[1]}, Age: {record[2]}, Course: {record[3]}\n")
    else:
        print("❌ Student not found.\n")

# Function to update student details
def update_student(student_id, name, age, course):
    cursor.execute("UPDATE students SET name=?, age=?, course=? WHERE id=?", (name, age, course, student_id))
    conn.commit()
    if cursor.rowcount:
        print("✅ Student updated successfully.\n")
    else:
        print("❌ Student not found.\n")

# Function to delete student
def delete_student(student_id):
    cursor.execute("DELETE FROM students WHERE id=?", (student_id,))
    conn.commit()
    if cursor.rowcount:
        print("✅ Student deleted successfully.\n")
    else:
        print("❌ Student not found.\n")

# Main Menu
def menu():
    while True:
        print("=== Student Management System ===")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student by ID")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            name = input("Enter student name: ")
            age = int(input("Enter student age: "))
            course = input("Enter student course: ")
            add_student(name, age, course)

        elif choice == '2':
            view_students()

        elif choice == '3':
            student_id = int(input("Enter student ID: "))
            search_student(student_id)

        elif choice == '4':
            student_id = int(input("Enter student ID to update: "))
            name = input("Enter new name: ")
            age = int(input("Enter new age: "))
            course = input("Enter new course: ")
            update_student(student_id, name, age, course)

        elif choice == '5':
            student_id = int(input("Enter student ID to delete: "))
            delete_student(student_id)

        elif choice == '6':
            print("👋 Exiting the program.")
            break

        else:
            print("❌ Invalid choice. Try again.\n")

# Run program
menu()

# Close database connection
conn.close()
