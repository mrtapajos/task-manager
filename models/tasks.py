from sqlalchemy import Column, Integer, String, DateTime
from models.database import db


class Task(db.Model):
    __tablename__ = 'tasks'
    
    name: str = Column(String(50), primary_key=True, unique=True)
    deadline: DateTime = Column(DateTime)
    importance: int = Column(Integer)

    def to_json(self):
        return {'name': self.name,
                'deadline': self.deadline,
                'importance': self.importance}
    
    def __repr__(self):
        return f'NAME: {self.name} -- IMPORTANCE: {self.importance}'