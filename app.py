
from flask import Flask, jsonify, render_template, request
import sqlite3

app = Flask(__name__)

DATABASE = "employees.db"

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def initialize_database():
    conn = get_db()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            role TEXT NOT NULL,
            photo TEXT
        )
    """)

    count = conn.execute(
        "SELECT COUNT(*) FROM employees"
    ).fetchone()[0]

    if count == 0:
        employees = [
            ("Vikash", "DevOps Engineer", "https://randomuser.me/api/portraits/men/1.jpg"),
            ("Arun", "Cloud Engineer", "https://randomuser.me/api/portraits/men/2.jpg"),
            ("Karthik", "Python Developer", "https://randomuser.me/api/portraits/men/3.jpg"),
            ("Praveen", "Software Engineer", "https://randomuser.me/api/portraits/men/4.jpg"),
            ("Suresh", "System Administrator", "https://randomuser.me/api/portraits/men/5.jpg"),
            ("Manoj", "AWS Engineer", "https://randomuser.me/api/portraits/men/6.jpg"),
            ("Dinesh", "Network Engineer", "https://randomuser.me/api/portraits/men/7.jpg"),
            ("Surya", "Frontend Developer", "https://randomuser.me/api/portraits/men/8.jpg"),
            ("Rahul", "Backend Developer", "https://randomuser.me/api/portraits/men/9.jpg"),
            ("Ajith", "Database Administrator", "https://randomuser.me/api/portraits/men/10.jpg")
        ]

        conn.executemany(
            "INSERT INTO employees (name, role, photo) VALUES (?, ?, ?)",
            employees
        )

    conn.commit()
    conn.close()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/employees", methods=["GET"])
def get_employees():
    conn = get_db()
    employees = conn.execute(
        "SELECT * FROM employees ORDER BY id"
    ).fetchall()
    conn.close()

    return jsonify([dict(e) for e in employees])

@app.route("/employees", methods=["POST"])
def add_employee():
    data = request.get_json()

    if not data or not data.get("name") or not data.get("role"):
        return jsonify({"error": "Name and role are required"}), 400

    conn = get_db()
    cursor = conn.execute(
        "INSERT INTO employees (name, role, photo) VALUES (?, ?, ?)",
        (data["name"].strip(), data["role"].strip(),
         "https://randomuser.me/api/portraits/men/11.jpg")
    )

    conn.commit()
    employee_id = cursor.lastrowid
    conn.close()

    return jsonify({"message": "Employee added", "id": employee_id}), 201

@app.route("/employees/<int:employee_id>", methods=["DELETE"])
def delete_employee(employee_id):
    conn = get_db()
    cursor = conn.execute(
        "DELETE FROM employees WHERE id = ?", (employee_id,)
    )
    conn.commit()
    conn.close()

    if cursor.rowcount == 0:
        return jsonify({"error": "Employee not found"}), 404

    return jsonify({"message": "Employee deleted"})

initialize_database()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
