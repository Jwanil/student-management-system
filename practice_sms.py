# pyrefly: ignore [missing-import]
from db import createtableifnotexists
# pyrefly: ignore [missing-import]
from Auth.auth_func import login, register
# pyrefly: ignore [missing-import]
from Classes.class_menu import class_menu
# pyrefly: ignore [missing-import]
from Teachers.teachers_menu import teacher_menu
# pyrefly: ignore [missing-import]
from Students.students_menu import student_menu


def menu():
    while True:
        print("\n--- Main Menu ---")
        print("1. Student Menu")
        print("2. Teacher Menu")
        print("3. Class Menu")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            student_menu()
        elif choice == '2':
            teacher_menu()
        elif choice == '3':
            class_menu()
        elif choice == '4':
            break
        else:
            print("Invalid choice, please try again.")  



def main():
    while True:
        print("Welcome to the Student Management System!")
        print("Auth")
        print("1. login")
        print("2. register")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")
        if choice == '1':
            if login():
                print("Login successfull")
                menu()
        elif choice == '2':

            if register():
                print("Login successfull")
                menu()

            
        elif choice == '3':
            break

        else:
            print("Invalid choice, please try again.")

createtableifnotexists()

if __name__ == "__main__":
    main()
