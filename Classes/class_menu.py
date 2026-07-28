# pyrefly: ignore [missing-import]
from Classes.class_func import add_classes, view_classes

def class_menu():
    while True:
        print("\n--- Class Menu ---")
        print("1. View all classes")
        print("2. Add class")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            view_classes()
        elif choice == '2':
            add_classes()
        elif choice == '3':
            break
        else:
            print("Invalid choice, please try again.")
