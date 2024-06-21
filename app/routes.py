from flask import Blueprint, request, jsonify
from .models import Task
from . import db

main = Blueprint('main', __name__)

@main.route('/api/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    task_list = []
    for task in tasks:
        task_list.append({'id': task.id, 'title': task.title, 'description': task.description, 'dueDate': task.due_date})
    return jsonify(task_list)

@main.route('/api/tasks', methods=['POST'])
def add_task():
    task_data = request.get_json()
    new_task = Task(title=task_data['title'], description=task_data['description'], due_date=task_data['dueDate'])
    db.session.add(new_task)
    db.session.commit()
    return jsonify({'id': new_task.id, 'title': new_task.title, 'description': new_task.description, 'dueDate': new_task.due_date})

@main.route('/api/tasks/<int:id>', methods=['GET'])
def get_task(id):
    task = Task.query.get(id)
    if not task:
        return jsonify({'error': 'Task not found'}), 404
    return jsonify({'id': task.id, 'title': task.title, 'description': task.description, 'dueDate': task.due_date})

@main.route('/api/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    task_data = request.get_json()
    task = Task.query.get(id)
    if not task:
        return jsonify({'error': 'Task not found'}), 404
    task.title = task_data['title']
    task.description = task_data['description']
    task.due_date = task_data['dueDate']
    db.session.commit()
    return jsonify({'id': task.id, 'title': task.title, 'description': task.description, 'dueDate': task.due_date})

@main.route('/api/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = Task.query.get(id)
    if not task:
        return jsonify({'error': 'Task not found'}), 404
    db.session.delete(task)
    db.session.commit()
    return '', 204
