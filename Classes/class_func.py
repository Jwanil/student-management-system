# pyrefly: ignore [missing-import]
from db import get_db_connection
# pyrefly: ignore [untyped-import]
import requests

BASE_URL = "http://127.0.0.1:5001"


def view_classes():
    response = requests.get(f"{BASE_URL}/classes")
    data = response.json()
    
    class_list = data    

    if not class_list:
        print("No classes found in the database.")
    else:
        print(f"{'Class ID':<10} | {'Class':<15} | {'Teacher':<10}")
        print("-" * 50)
        
        for c in class_list:
            class_id = str(c['class_id']) if c['class_id'] else 'N/A'
            class_name = str(c['class_name']) if c['class_name'] else 'N/A'
            teacher_name = str(c['teacher_name']) if c['teacher_name'] else 'N/A'
            
            print(f"{class_id:<10} | {class_name:<15} | {teacher_name:<10}")


def add_classes():
    print("\n--- Add Class ---")
    class_name = input("Enter class name: ")
    teacher_name = input("Teacher's Name: ")
    
    class_data = {
        "class_name": class_name,
        "teacher_name": teacher_name,
        "create_if_missing": False
    }
    
    response = requests.post(f"{BASE_URL}/classes", json=class_data)
    data = response.json()
    
    if response.status_code == 404 and data.get("teacher_not_found"):
        confirm = input(f"Teacher '{teacher_name}' not found. Do you want to create them? (y/n): ")
        if confirm.lower() == 'y':
            class_data["create_if_missing"] = True
            response = requests.post(f"{BASE_URL}/classes", json=class_data)
            data = response.json()
        else:
            print("Class addition cancelled.")
            return False

    if response.status_code == 200:
        print(data.get("message"))
        return True
    else:
        print(data.get("error", data.get("message")))
        return False
