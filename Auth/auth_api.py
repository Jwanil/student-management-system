
from flask import Blueprint, request, jsonify
import sqlite3
# pyrefly: ignore [missing-import]
from db import get_db_connection
import bcrypt

auth = Blueprint('auth_api', __name__)


@auth.route('/register', methods= ['POST'])
def register():
    data = request.get_json()
    username = data['username']
    password = data['password']

    # 1. bcrypt requires the password to be encoded as bytes
    password_bytes = password.encode('utf-8')
    
    # 2. Hash the password with a generated "salt"
    hashed_password_bytes = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
    
    # 3. Decode back to a normal string so we can save it in our SQLite database
    hashed_password_string = hashed_password_bytes.decode('utf-8')
    
    sqliteConnection = get_db_connection()
    cursor = sqliteConnection.cursor()
    try:
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', 
                     (username, hashed_password_string))
        sqliteConnection.commit()
    except sqlite3.IntegrityError:
        cursor.close()
        sqliteConnection.close()
        return jsonify({"error": "Username already exists!"}), 400

    cursor.close()
    sqliteConnection.close()
    return jsonify({"message": "User created successfully with bcrypt!"}), 200

@auth.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']
    
    sqliteConnection = get_db_connection()
    cursor = sqliteConnection.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    cursor.close()
    sqliteConnection.close()
    
    # If the user exists, we use bcrypt.checkpw() to compare the entered password with the database hash
    if user:
        # We have to encode both the entered password and the database hash back into bytes to compare them
        password_bytes = password.encode('utf-8')
        db_hash_bytes = user['password'].encode('utf-8')
        
        if bcrypt.checkpw(password_bytes, db_hash_bytes):
            return jsonify({"message": "Login successful!", "token": "secret-admin-token"}), 200
            
    return jsonify({"error": "Invalid username or password!"}), 401

