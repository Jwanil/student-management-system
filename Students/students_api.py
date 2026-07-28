from flask import Blueprint, request, jsonify
# pyrefly: ignore [missing-import]
from db import get_db_connection
import sqlite3

students = Blueprint('students_api', __name__)

@students.route('/students', methods=['GET'])
def view_students():
    sqliteConnection = get_db_connection()
    cursor = sqliteConnection.cursor()

    check_students_table = ("SELECT * FROM students")
    cursor.execute(check_students_table)
    students = cursor.fetchall()
    sqliteConnection.commit()
    sqliteConnection.close()

    student_list = [dict(row) for row in students]
    return jsonify(student_list)

@students.route('/students', methods=['POST'])
def add_student():
    new_student = request.get_json()
    
    name = new_student['name']
    age = new_student['age']
    grade = new_student['grade']
    roll_no = new_student['roll_no']
    
    sqliteConnection = get_db_connection()
    cursor = sqliteConnection.cursor()

    try:
        cursor.execute("INSERT into students (student_name, age, grade, roll_no) VALUES (?, ?, ?, ?)", (name, age, grade, roll_no))
        sqliteConnection.commit()
        return jsonify({"message": "Student added successfully!"}), 200
    except sqlite3.IntegrityError:
        return jsonify({"error": "Student with this roll number already exists!"}), 400
    finally:
        sqliteConnection.close()

@students.route('/students/<int:roll_no>', methods=['PUT'])
def update_student(roll_no):
    student = request.get_json()
    name = student['name']
    age = student['age']
    grade = student['grade']
    sqliteConnection = get_db_connection()
    cursor = sqliteConnection.cursor()
    result =  cursor.execute("UPDATE students SET student_name = ?, age = ?, grade = ? WHERE roll_no = ?", (name, age, grade, roll_no))
    if result.rowcount == 0:
        sqliteConnection.close()
        return jsonify({"error": "Student not found!"}), 404
        
    sqliteConnection.commit()
    sqliteConnection.close()
    
    return jsonify({"message": f"Student {roll_no} updated successfully!"})

@students.route('/students/<int:roll_no>', methods=['DELETE'])
def delete_student(roll_no):
    sqliteConnection = get_db_connection()
    cursor = sqliteConnection.cursor()
    cursor.execute('DELETE FROM students WHERE roll_no = ?', (roll_no,))
    
    if cursor.rowcount == 0:
        sqliteConnection.close()
        return jsonify({"error": "Student not found!"}), 404
        
    sqliteConnection.commit()
    sqliteConnection.close()
    return jsonify({"message": f"Student {roll_no} deleted successfully!"}), 200

@students.route('/enrollstudents', methods=['POST'])
def enrollstudents():
    enrollment_data = request.get_json()
    student_name = enrollment_data['student_name']
    class_name = enrollment_data['class_name']
    
    sqliteConnection = get_db_connection()
    cursor = sqliteConnection.cursor()

    cursor.execute("""
        SELECT s.student_id, c.class_id 
        FROM students s 
        CROSS JOIN classes c 
        WHERE s.student_name = ? AND c.class_name = ?
    """, (student_name, class_name))
    result = cursor.fetchone()
    
    if result:
        student_id = result['student_id']
        class_id = result['class_id']
        
        cursor.execute("INSERT INTO enrolled_classes (student_id, class_id) VALUES (?, ?)", (student_id, class_id))
        sqliteConnection.commit()
        sqliteConnection.close()
        return jsonify({"message": f"Success! {student_name} has been enrolled in {class_name}."}), 200
    else:
        sqliteConnection.close()
        return jsonify({"error": "Error: Student or Class not found."}), 404


@students.route('/view_enrolled_students', methods=['GET'])
def view_enrolled_students():
    sqliteConnection = get_db_connection()
    cursor = sqliteConnection.cursor()
 
    cursor.execute('''SELECT 
            ec.enrollment_id, 
            s.student_id, 
            s.student_name, 
            s.roll_no, 
            tc.class_id, 
            tc.class_name, 
            tc.teacher_id, 
            tc.teacher_name 
        FROM enrolled_classes ec
        JOIN students s ON ec.student_id = s.student_id
        JOIN teacher_classes tc ON ec.class_id = tc.class_id''')
    enrolled_classes = cursor.fetchall()
    sqliteConnection.commit()
    sqliteConnection.close()
    
    enrolled_classes_list = [dict(row) for row in enrolled_classes]    
    return jsonify(enrolled_classes_list)
