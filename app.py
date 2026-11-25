
import os
from urllib.parse import urlparse, unquote
from flask import Flask, jsonify, render_template, request
from dotenv import load_dotenv
import pg8000.dbapi

load_dotenv()

app = Flask(__name__)

DATABASE_URL = os.getenv("DATABASE_URL")


def get_db():
    if not DATABASE_URL:
        raise RuntimeError("DATABASE_URL is missing. Check your .env file.")

    url = urlparse(DATABASE_URL)

    return pg8000.dbapi.connect(
        user=unquote(url.username),
        password=unquote(url.password),
        host=url.hostname,
        port=url.port or 5432,
        database=url.path.lstrip("/"),
        ssl_context=True
    )


def initialize_database():
    conn = get_db()
    try:
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS employees (
                id BIGSERIAL PRIMARY KEY,
                name TEXT NOT NULL,
                role TEXT NOT NULL,
                photo TEXT
            )
        """)

        cursor.execute("SELECT COUNT(*) FROM employees")
        count = cursor.fetchone()[0]

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

            cursor.executemany(
                "INSERT INTO employees (name, role, photo) VALUES (%s, %s, %s)",
                employees
            )

        conn.commit()
    finally:
        conn.close()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/employees", methods=["GET"])
def get_employees():
    conn = get_db()
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM employees ORDER BY id")
        rows = cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        employees = [dict(zip(columns, row)) for row in rows]
        return jsonify(employees)
    finally:
        conn.close()


@app.route("/employees", methods=["POST"])
def add_employee():
    data = request.get_json()

    if not data or not data.get("name") or not data.get("role"):
        return jsonify({"error": "Name and role are required"}), 400

    conn = get_db()
    try:
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO employees (name, role, photo)
            VALUES (%s, %s, %s)
            RETURNING id
            """,
            (
                data["name"].strip(),
                data["role"].strip(),
                "https://randomuser.me/api/portraits/men/11.jpg"
            )
        )
        employee_id = cursor.fetchone()[0]
        conn.commit()

        return jsonify({
            "message": "Employee added",
            "id": employee_id
        }), 201
    finally:
        conn.close()


@app.route("/employees/<int:employee_id>", methods=["DELETE"])
def delete_employee(employee_id):
    conn = get_db()
    try:
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM employees WHERE id = %s",
            (employee_id,)
        )

        if cursor.rowcount == 0:
            conn.rollback()
            return jsonify({"error": "Employee not found"}), 404

        conn.commit()
        return jsonify({"message": "Employee deleted"})
    finally:
        conn.close()


initialize_database()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
