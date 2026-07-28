# pyrefly: ignore [missing-import]
from db import get_db_connection

# pyrefly: ignore [untyped-import]
import requests

BASE_URL = "http://127.0.0.1:5001"

def view_teachers():
    response = requests.get(f"{BASE_URL}/teachers")
    data = response.json()
    
    teacher_list = data    

    if not teacher_list:
        print("No teachers found in the database.")
    else:
        print(f"{'Teacher':<15} | {'Class Name'}")
        print("-" * 50)
        
        for t in teacher_list:
            print(f"{t['teacher_name']:<15} | {t['class_name']}")



def add_teachers():
    print("\n--- Add Teacher ---")
    teacher_name = input("Enter new teacher name: ")
    class_name = input("Assign to which class name: ")

    teacher_data = {
        'teacher_name': teacher_name,
        'class_name': class_name,
        'create_if_missing': False
    }
    
    response = requests.post(f'{BASE_URL}/teachers', json=teacher_data)
    data = response.json()
    if response.status_code == 404 and data.get("class_not_found"):
        confirm = input(f"Class '{class_name}' not found. Do you want to create them? (y/n): ")
        if confirm.lower() == 'y':
            teacher_data["create_if_missing"] = True
            response = requests.post(f"{BASE_URL}/teachers", json=teacher_data)
            data = response.json()
        else:
            print("Teacher addition cancelled.")
            return False
    if response.status_code == 200:
        print(data.get("message"))
        return True
    else:
        print(data.get("error", data.get("message")))
        return False
