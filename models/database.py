from flask_sqlalchemy import SQLAlchemy
from flask import Flask

db: SQLAlchemy = SQLAlchemy()

def create_database(app: Flask) -> None:
    db.init_app(app)
    app.db = db

    with app.app_context():
        db.drop_all()
        db.create_all()

