# pyrefly: ignore [missing-import]
from Teachers.teachers_func import add_teachers, view_teachers

def teacher_menu():
    while True:
        print("\n--- Teacher Menu ---")
        print("1. View all teachers")
        print("2. Add teacher")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            view_teachers()
        elif choice == '2':
            add_teachers()
        elif choice == '3':
            break
        else:
            print("Invalid choice, please try again.")  
