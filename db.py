
import sqlite3

def get_db_connection():
    sqliteConnection = sqlite3.connect('sms_final.db')
    sqliteConnection.row_factory = sqlite3.Row  # This lets us access columns by name
    return sqliteConnection


def createtableifnotexists():
    sqliteConnection = get_db_connection()
    cursor = sqliteConnection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users 
                        (user_id INTEGER PRIMARY KEY AUTOINCREMENT , 
                        username TEXT NOT NULL UNIQUE, 
                        password TEXT NOT NULL)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS students 
                    (student_id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    roll_no INTEGER NOT NULL UNIQUE, 
                    student_name TEXT NOT NULL, 
                    age INTEGER, 
                    grade TEXT)''')

    # Core tables keep text metadata for quick rendering
    cursor.execute('''CREATE TABLE IF NOT EXISTS teachers (
        teacher_id INTEGER PRIMARY KEY AUTOINCREMENT, 
        teacher_name TEXT NOT NULL
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS classes (
        class_id INTEGER PRIMARY KEY AUTOINCREMENT, 
        class_name TEXT NOT NULL
    )''')

    # The Junction Table links them together
    cursor.execute('''CREATE TABLE IF NOT EXISTS teacher_classes (
        teacher_id INTEGER NOT NULL,
        class_id INTEGER NOT NULL,
        teacher_name TEXT NOT NULL,
        class_name TEXT NOT NULL,
        PRIMARY KEY (teacher_id, class_id),
        FOREIGN KEY(teacher_id) REFERENCES teachers(teacher_id),
        FOREIGN KEY(class_id) REFERENCES classes(class_id)
    )''')


    cursor.execute('''CREATE TABLE IF NOT EXISTS enrolled_classes
                    (enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    student_id INTEGER NOT NULL,
                    class_id INTEGER NOT NULL,
                    FOREIGN KEY(student_id) REFERENCES students(student_id),
                    FOREIGN KEY(class_id) REFERENCES classes(class_id)
                    )
                    ''')


    sqliteConnection.commit()
    sqliteConnection.close()

