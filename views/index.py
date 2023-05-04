from flask import current_app as app, render_template
from models.tasks import Task


@app.route('/', methods=['GET'])
def index():
    tasks = Task.query.all()
    for task in tasks:
        if task.deadline != None:
            task.deadline_view = task.deadline.strftime('%d/%m/%y')
        else:
            task.deadline_view = None

    return render_template('index.html', tasks=tasks)