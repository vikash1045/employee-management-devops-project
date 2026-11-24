
from flask import Flask, jsonify

app = Flask(__name__)

employees = [
    {"id": 1, "name": "Vikash", "role": "DevOps Engineer"},
    {"id": 2, "name": "Arun", "role": "Cloud Engineer"}
]

@app.route("/")
def home():
    return "Welcome to AWS DevOps Employee Management System!"

@app.route("/employees")
def get_employees():
    return jsonify(employees)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
