from flask_sqlalchemy import SQLAlchemy
from flask import Flask

db: SQLAlchemy = SQLAlchemy()

def create_database(app: Flask) -> None:
    db.init_app(app)
    app.db = db

    with app.app_context():
        # db.drop_all()
        db.create_all()


def db_commit(model: db.Model) -> bool:
    try:
        db.session.add(model)
        db.session.commit()
        return True
    except:
        db.session.rollback()
        return False

def db_update(model: db.Model) -> bool:
    try:
        print('Tentando atualização!')
        db.session.commit()
        return True
    except Exception as error:
        db.session.rollback()
        print(error)
        return False

def db_delete(model: db.Model) -> bool:
    try:
        db.session.delete(model)
        db.session.commit()
        return True
    except:
        db.session.rollback()
        return False