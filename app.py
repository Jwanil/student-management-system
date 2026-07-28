from flask import Flask

# pyrefly: ignore [missing-import]
from Auth.auth_api import auth
# pyrefly: ignore [missing-import]
from Classes.class_api import classes
# pyrefly: ignore [missing-import]
from Teachers.teachers_api import teachers
# pyrefly: ignore [missing-import]
from Students.students_api import students

app = Flask(__name__)

app.register_blueprint(auth)
app.register_blueprint(classes)
app.register_blueprint(teachers)
app.register_blueprint(students)

@app.route('/')
def start():
    return("Server has started")


if __name__ == "__main__":
    app.run(debug=True, port=5001)
