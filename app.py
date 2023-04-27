from flask import Flask
from models.database import create_database


app = Flask(__name__)
with app.app_context():
    from controllers import task_controller
    
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'

create_database(app)

if __name__ == '__main__':
    app.run(debug=True)
