import sqlite3

# pyrefly: ignore [missing-import]
from db import get_db_connection
# pyrefly: ignore [untyped-import]
import requests

BASE_URL = "http://127.0.0.1:5001"

def view_students():

    response = requests.get(f"{BASE_URL}/students")
    data = response.json()
    
    student_list = data   
    if not student_list:
        print("No students found in the database.")
    else:

        print(f"{'Name':<15} | {'Roll No:':<10} | {'Age:':<6} | {'Grade:'}")
        print("-" * 50)
        
        for s in student_list:
            print(f"{s['student_name']:<15} | {str(s['roll_no']):<10} | {str(s['age']):<6} | {s['grade']}")


def add_students():

    print("\n--- Add Student ---")
    try:
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        grade = input("Enter student grade: ")
        roll_no = int(input("Enter student roll number: "))
    except ValueError as e:
        print("Error: Invalid input. Please try again.")
        return False
    
    student_data = {
        "name": name,
        "age": age,
        "grade": grade,
        "roll_no": roll_no
    }

    response = requests.post(f"{BASE_URL}/students", json = student_data)
    data = response.json()
    
    if response.status_code == 200:
        print(data.get("message"))
        return True
    else:
        print(data.get("error", data.get("message")))
        return False

def delete_student():
    print("\n--- Delete Student ---")
    try:
        roll_no = int(input("Enter student roll number: "))
    except ValueError as e:
        print("Error: Invalid input. Please try again.")
        return False

    response = requests.delete(f"{BASE_URL}/students/{roll_no}")
    data = response.json()
    
    if response.status_code == 200:
        print(data.get("message"))
        return True
    else:
        print(data.get("error", data.get("message")))
        return False


def edit_students():
    print("\n--- Edit Student ---")
    try:
        roll_no = int(input("Enter student roll number whose data you want to edit: "))
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        grade = input("Enter student grade: ")
    except ValueError as e:
        print("Error: Invalid input. Please try again.")
        return False
    
    student_data = {
        "name": name,
        "age": age,
        "grade": grade
        }


    response = requests.put(f"{BASE_URL}/students/{roll_no}", json = student_data)
    data = response.json()

    if response.status_code == 200:
        print(data.get("message"))
        return True
    else:
        print(data.get("error", data.get("message")))
        return False


def enrollstudents():
    print("\n--- Enroll Student in Class ---")
    student_name = input("Enter student name: ")
    class_name = input("Enter class name: ")
    
    enrollment_data = {
        "student_name": student_name,
        "class_name": class_name
    }
    
    response = requests.post(f"{BASE_URL}/enrollstudents", json=enrollment_data)
    data = response.json()
    
    if response.status_code == 200:
        print(data.get("message"))
        return True
    else:
        print(data.get("error", data.get("message")))
        return False
   

def view_enrolled_students():
    response = requests.get(f"{BASE_URL}/view_enrolled_students")
    data = response.json()
    enrolled_classes_list = data

    if not enrolled_classes_list:
        print("No enrolled classes found in the database.")
    else:
        print(f"{'Student Name':<15} | {'Roll No':<10} | {'Class Name':<10} | {'Teacher Name':<10}")
        print("-" * 50)
        for e in enrolled_classes_list:
            print(f"{e['student_name']:<15} | {e['roll_no']:<10} | {str(e['class_name']):<10} | {str(e['teacher_name']):<10}")
