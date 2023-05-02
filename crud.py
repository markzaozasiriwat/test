import sqlite3
from tkinter import Tk
from tkinter.filedialog import askopenfilename

conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY,
        name TEXT,
        telephone TEXT,
        address TEXT,
        gender TEXT,
        photo BLOB
    )
''')

def create_employee(name, telephone, address, gender, photo_path):
    with open(photo_path, 'rb') as photo_file:
        photo_data = photo_file.read()

    cursor.execute('''
        INSERT INTO employees (name, telephone, address, gender, photo)
        VALUES (?, ?, ?, ?, ?)
    ''', (name, telephone, address, gender, photo_data))
    conn.commit()
    print("Employee created successfully!")

def read_employees():
    cursor.execute('SELECT * FROM employees')
    rows = cursor.fetchall()
    for row in rows:
        employee_id, name, telephone, address, gender, photo_data = row
        print("Employee ID:", employee_id)
        print("Name:", name)
        print("Telephone:", telephone)
        print("Address:", address)
        print("Gender:", gender)
        with open(f'employee_{employee_id}.jpg', 'wb') as photo_file:
            photo_file.write(photo_data)
        print("Photo saved as employee_{employee_id}.jpg")
        print()

def update_employee(employee_id, name, telephone, address, gender, photo_path):
    with open(photo_path, 'rb') as photo_file:
        photo_data = photo_file.read()

    cursor.execute('''
        UPDATE employees
        SET name = ?, telephone = ?, address = ?, gender = ?, photo = ?
        WHERE id = ?
    ''', (name, telephone, address, gender, photo_data, employee_id))
    conn.commit()
    print("updated successfully!")

def delete_employee(employee_id):
    cursor.execute('DELETE FROM employees WHERE id = ?', (employee_id,))
    conn.commit()
    print("deleted successfully!")

while True:
    print("1. Create Employee")
    print("2. Read Employees")
    print("3. Update Employee")
    print("4. Delete Employee")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        name = input("Enter employee name: ")
        telephone = input("Enter employee telephone number: ")
        address = input("Enter employee address: ")
        gender = input("Enter employee gender: ")

        Tk().withdraw() 
        photo_path = askopenfilename(title="Select Employee Photo")

        create_employee(name, telephone, address, gender, photo_path)
    elif choice == '2':
        read_employees()
    elif choice == '3':
        employee_id = input("Enter employee ID: ")
        name = input("Enter new employee name: ")
        telephone = input("Enter new employee telephone number: ")
        address = input("Enter new employee address: ")
        gender = input("Enter new employee gender: ")

        Tk().withdraw()  
