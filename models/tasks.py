from sqlalchemy import Column, Integer, String, Date
from models.database import db


class Task(db.Model):
    __tablename__ = 'tasks'
    
    id: int = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    name: str = Column(String(50))
    deadline: Date = Column(Date, nullable=True)
    importance: int = Column(Integer)

    def to_json(self):
        return {'name': self.name,
                'deadline': self.deadline,
                'importance': self.importance}
    
    def __repr__(self):
        return f'Task: {self.name} // Importance: {self.importance}'
    