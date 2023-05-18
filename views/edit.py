from flask import current_app as app, render_template, request, redirect, url_for, make_response
from http import HTTPStatus
from datetime import datetime
from models.tasks import Task
from models.database import db_update

# UPDATE
@app.route('/tasks/edit/<int:edit_id>', methods=['GET', 'POST'])
def edit_task(edit_id):
    task: dict = Task.query.get(edit_id)


    if request.method == 'POST':
        task.id = request.form['task-id']
        task.name = request.form['task-name']
        task.deadline = datetime.strptime(request.form['task-deadline'], '%Y-%m-%d').date()
        task.importance = request.form['task-importance']

        # PUSH TO DATABASE
        db_update(task)
        if db_update:
            return redirect(url_for('index'))
        else:
            return make_response({"message": "Couldn't edit task!"}, HTTPStatus.BAD_REQUEST)


    return render_template('edit.html', task=task)
        