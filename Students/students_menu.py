
# pyrefly: ignore [missing-import]
from Students.students_func import add_students,edit_students,delete_student,view_students,enrollstudents,view_enrolled_students

def student_menu():
    while True:
        print("\n--- Student Menu ---")
        print("1. View all students")
        print("2. Add student")
        print("3. Edit student")
        print("4. Delete student")
        print("5. Enroll student")
        print("6. View enrolled classes")
        print("7. Exit")
        
        # Get input from the user
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            view_students()
        elif choice == '2':
            add_students()
        elif choice == '3':
            edit_students()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            enrollstudents()
        elif choice == '6':
            view_enrolled_students()
        elif choice == '7':
            break
        else:
            print("Invalid choice, please try again.")
