from flask import jsonify, make_response, current_app as app, request
from http import HTTPStatus
from models.tasks import Task
from models.database import db_commit, db, db_delete
from datetime import datetime


# READ
@app.route('/tasks', methods=['GET'])
def all_tasks():
    tasks = Task.query.all()
    list_tasks = jsonify([task.name for task in tasks])
    response = make_response(list_tasks, HTTPStatus.OK)
    return response


# CREATE
@app.route('/tasks', methods=['POST'])
def add_task():
    task: dict = request.get_json()

    # GETTING TASK VALUES
    task_id: int = task.get('id')
    task_name: str = task.get('name')
    task_importance: str = task.get('importance')
    task_deadline_str: str = task.get('deadline')
    # CONVERSION (STRING TO DATE)
    task_deadline_date = datetime.strptime(task_deadline_str, '%d/%m/%Y').date()

    # CREATING NEW TASK OBJECT
    task: Task = Task(id=task_id, name=task_name, deadline=task_deadline_date, importance=task_importance)
    task: dict = {'name': task_name, 'deadline': task_deadline_date, 'importance': task_importance}

    db_commit(Task(**task))
    
    return make_response('FEITO!', HTTPStatus.OK)
    
# UPDATE
# PRECISO COLOCAR ID NA TABELA
@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    task = Task.query.get(id)

    if not task:
        return make_response('ID não encontrado!', HTTPStatus.NOT_FOUND)
    
    task.name: str = request.json.get('name', task.name)

    task_deadline_str: str = request.json.get('deadline', task.deadline)
    task_deadline_date = datetime.strptime(task_deadline_str, '%d/%m/%Y').date()
    task.deadline = task_deadline_date

    task.importance: str = request.json.get('importance', task.importance)
    
    db.session.merge(task)
    db.session.commit()

    return make_response('A tarefa foi modificada com sucesso!', HTTPStatus.OK)


# DELETE 
@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = Task.query.get(id)

    if not task:
        return make_response('ID não encontrado!', HTTPStatus.NOT_FOUND)
    
    db_delete(task)
    return make_response('Tarefa deletada com sucesso!', HTTPStatus.OK)