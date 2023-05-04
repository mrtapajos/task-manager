from flask import Flask
from models.database import create_database


app = Flask(__name__, template_folder= './views/templates', static_folder='./views/static')
with app.app_context():
    from controllers import task_controller
    from views import index
    
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'

create_database(app)

if __name__ == '__main__':
    app.run(debug=True)
