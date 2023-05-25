from flask import make_response, current_app as app, request, redirect, url_for
from http import HTTPStatus
from models.tasks import Task
from models.database import db_commit, db_delete
from datetime import datetime, date



# CREATE
@app.route('/tasks', methods=['POST'])
def add_task():
    task: dict = request.get_json()

    # GETTING TASK VALUES
    # task_id: int = task.get('id')
    task_name: str = task.get('name')
    task_importance: int = task.get('importance')
    task_deadline_str: str = task.get('deadline')

    # VALIDATING NAME & IMPORTANCE
    if not task_name or not task_importance or task_importance <= 0:
        return make_response({"message": "INVALID TASK!"}, HTTPStatus.BAD_REQUEST)
    
    
    # DATE CONDITIONS
    today: date = date.today()

    if task_deadline_str != '': # CAN'T BE NONE
        task_deadline_date = datetime.strptime(task_deadline_str, '%Y-%m-%d').date()
        if task_deadline_date < today:
            return make_response({"message": "Date must be after today or today!"}, HTTPStatus.BAD_REQUEST)
    else:
        task_deadline_date = None


    # CREATING NEW TASK OBJECT
    task: Task = Task(name=task_name, deadline=task_deadline_date, importance=task_importance)
    task: dict = {'name': task_name, 'deadline': task_deadline_date, 'importance': task_importance}

    db_action = db_commit(Task(**task)) # (name: task_name, deadline: task_deadline_date, importance: task_importance)

    if db_action:
        return make_response({'message': "Task successfully added!"}, HTTPStatus.OK)
    else:
        return make_response({'message': "Error adding task!"}, HTTPStatus.BAD_REQUEST)
    
    


# DELETE 
@app.route('/tasks/delete/<int:id>', methods=['POST'])
def delete_task(id):
    task = Task.query.get(id)      
    db_action = db_delete(task)

    if db_action:
        return redirect(url_for('index'))
    
    else:
        return make_response({"message": 'ID não encontrado!'}, HTTPStatus.NOT_FOUND)
    