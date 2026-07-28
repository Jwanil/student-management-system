from flask import Blueprint, request, jsonify
# pyrefly: ignore [missing-import]
from db import get_db_connection


classes = Blueprint('class_api', __name__)

@classes.route('/classes', methods=['GET'])
def get_classes():
    sqliteConnection = get_db_connection()
    cursor = sqliteConnection.cursor()

    check_classes_table = ("SELECT class_id, class_name, teacher_name FROM teacher_classes")
    cursor.execute(check_classes_table)
    classes = cursor.fetchall()
    sqliteConnection.commit()
    sqliteConnection.close()
    
    class_list = [dict(row) for row in classes]    
    return jsonify(class_list)

@classes.route('/classes', methods=['POST'])
def add_class():
    new_class = request.get_json()
    
    class_name = new_class['class_name']
    teacher_name = new_class['teacher_name']
    create_if_missing = new_class.get('create_if_missing', False)
    
    sqliteConnection = get_db_connection()
    cursor = sqliteConnection.cursor()

    try:
        cursor.execute("BEGIN TRANSACTION;")

        # 1. Check if teacher exists
        cursor.execute("SELECT teacher_id FROM teachers WHERE teacher_name = ? LIMIT 1", (teacher_name,))
        teacher = cursor.fetchone() 

        if teacher:
            teacher_id = teacher['teacher_id'] 
        elif create_if_missing:
            # Create the teacher
            cursor.execute("INSERT INTO teachers (teacher_name) VALUES (?)", (teacher_name,))
            teacher_id = cursor.lastrowid
        else:
            sqliteConnection.rollback()
            return jsonify({"error": f"Teacher '{teacher_name}' not found!", "teacher_not_found": True}), 404

        # 2. INSERT class details into the classes table
        cursor.execute("INSERT INTO classes (class_name) VALUES (?)", (class_name,))
        class_id = cursor.lastrowid

        # 3. INSERT the bridge relationship
        cursor.execute("""
            INSERT INTO teacher_classes (teacher_id, class_id, teacher_name, class_name) 
            VALUES (?, ?, ?, ?)
        """, (teacher_id, class_id, teacher_name, class_name))

        sqliteConnection.commit()
        return jsonify({"message": f"Success! Created Class '{class_name}' and assigned to {teacher_name}."}), 200
            
    except Exception as e:
        sqliteConnection.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        sqliteConnection.close()
