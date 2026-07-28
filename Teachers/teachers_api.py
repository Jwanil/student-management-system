from flask import Blueprint, request, jsonify
# pyrefly: ignore [missing-import]
from db import get_db_connection


teachers = Blueprint('teachers_api', __name__)

@teachers.route('/teachers', methods=['GET'])
def get_teachers():
    sqliteConnection = get_db_connection()
    cursor = sqliteConnection.cursor()

    check_teachers_table = ("SELECT class_id, class_name, teacher_name FROM teacher_classes")
    cursor.execute(check_teachers_table)
    teachers = cursor.fetchall()
    sqliteConnection.commit()
    sqliteConnection.close()
    
    teacher_list = [dict(row) for row in teachers]    
    return jsonify(teacher_list)

@teachers.route('/teachers', methods=['POST'])
def add_teacher():
    new_teacher = request.get_json()
    
    teacher_name = new_teacher['teacher_name']
    class_name = new_teacher['class_name']
    create_if_missing = new_teacher.get('create_if_missing', False)
    
    sqliteConnection = get_db_connection()
    cursor = sqliteConnection.cursor()

    try:
        cursor.execute("BEGIN TRANSACTION;")

        # 1. Check if teacher exists
        cursor.execute("SELECT class_id FROM classes WHERE class_name = ? LIMIT 1", (class_name,))
        classes = cursor.fetchone() 

        if classes:
            class_id = classes['class_id'] 
        elif create_if_missing:
            # Create the classes
            cursor.execute("INSERT INTO classes (class_name) VALUES (?)", (class_name,))
            class_id = cursor.lastrowid
        else:
            sqliteConnection.rollback()
            return jsonify({"error": f"Class '{class_name}' not found!", "class_not_found": True}), 404

        # 2. INSERT teacher details into the teacher table
        cursor.execute("INSERT INTO teachers (teacher_name) VALUES (?)", (teacher_name,))
        teacher_id = cursor.lastrowid

        # 3. INSERT the bridge relationship
        cursor.execute("""
            INSERT INTO teacher_classes (teacher_id, class_id, teacher_name, class_name) 
            VALUES (?, ?, ?, ?)
        """, (teacher_id, class_id, teacher_name, class_name))

        sqliteConnection.commit()
        return jsonify({"message": f"Success! Created Teacher '{teacher_name}' and assigned to {class_name}."}), 200
            
    except Exception as e:
        sqliteConnection.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        sqliteConnection.close()
