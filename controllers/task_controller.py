from flask import jsonify, make_response, current_app as app
from http import HTTPStatus
from models.tasks import Task




@app.route('/tasks', methods=['GET'])
def all_tasks():
    tasks = Task.query.all()
    list_tasks = jsonify([task.name for task in tasks])
    response = make_response(list_tasks, HTTPStatus.OK)
    return response



""" @app.route('/tasks', methods=['POST'])
def add_task():
     """