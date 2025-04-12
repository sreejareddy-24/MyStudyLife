from flask import Blueprint, request, jsonify
from db import get_connection

task_bp = Blueprint('task_bp', __name__)

@task_bp.route('/tasks', methods=['POST'])
def add_task():
    data = request.json
    title = data['title']
    due_date = data['due_date']
    priority = data['priority']

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO tasks (title, due_date, priority) VALUES (%s, %s, %s)",
        (title, due_date, priority)
    )
    conn.commit()
    conn.close()
    return jsonify({"message": "Task added successfully"})

@task_bp.route('/tasks', methods=['GET'])
def get_tasks():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    conn.close()
    return jsonify(tasks)
