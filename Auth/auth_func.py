
# pyrefly: ignore [untyped-import]
import requests


BASE_URL = "http://127.0.0.1:5001"

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    user_data = {
        "username": username,
        "password": password
    }
    
    response = requests.post(f"{BASE_URL}/login", json=user_data)
    data = response.json()
    
    if response.status_code == 200:
        print(data.get("message"))
        return True
    else:
        print(data.get("error", data.get("message")))
        return False
      
def register():
    print("\n--- Register ---")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    user_data = {
        "username": username,
        "password": password
    }
    
    response = requests.post(f"{BASE_URL}/register", json=user_data)
    data = response.json()
    
    if response.status_code == 200:
        print(data.get("message"))
        return True
    else:
        print(data.get("error", data.get("message")))
        return False

