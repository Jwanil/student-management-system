# Student Management System

A Python Flask-based Student Management System with REST APIs and a CLI menu interface.

## Features

- **Authentication**: Register & login with bcrypt password hashing
- **Students**: Add, view, edit, delete students
- **Teachers**: Add and view teachers (with class assignment)
- **Classes**: Add and view classes (with teacher assignment)
- **Enrollments**: Enroll students into classes and view enrolled students

## Tech Stack

- **Backend**: Python + Flask (REST API)
- **Database**: SQLite (`sms_final.db`)
- **Password Hashing**: bcrypt
- **CLI**: Interactive terminal menu (`practice_sms.py`)

## Project Structure

```
Student_Mangement_System_Self/
├── app.py                  # Flask app entry point
├── db.py                   # Database connection & table creation
├── practice_sms.py         # CLI menu interface
├── Auth/
│   ├── auth_api.py         # /register and /login endpoints
│   └── auth_func.py        # CLI auth functions
├── Classes/
│   ├── class_api.py        # /classes endpoints
│   ├── class_func.py       # CLI class functions
│   └── class_menu.py       # CLI class menu
├── Teachers/
│   ├── teachers_api.py     # /teachers endpoints
│   ├── teachers_func.py    # CLI teacher functions
│   └── teachers_menu.py    # CLI teacher menu
└── Students/
    ├── students_api.py     # /students, /enrollstudents endpoints
    ├── students_func.py    # CLI student functions
    └── students_menu.py    # CLI student menu
```

## Setup & Run

### 1. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install dependencies
```bash
pip install flask bcrypt requests
```

### 3. Run the Flask API server
```bash
python app.py
```
Server runs on `http://127.0.0.1:5001`

### 4. Run the CLI interface (in a separate terminal)
```bash
python practice_sms.py
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/register` | Register a new user |
| POST | `/login` | Login with credentials |
| GET | `/students` | Get all students |
| POST | `/students` | Add a student |
| PUT | `/students/<roll_no>` | Update a student |
| DELETE | `/students/<roll_no>` | Delete a student |
| GET | `/teachers` | Get all teachers |
| POST | `/teachers` | Add a teacher |
| GET | `/classes` | Get all classes |
| POST | `/classes` | Add a class |
| POST | `/enrollstudents` | Enroll a student in a class |
| GET | `/view_enrolled_students` | View all enrollments |
