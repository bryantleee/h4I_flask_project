import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
 
Base = declarative_base()
 
class Tasks(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, nullable=False, primary_key = True)
    task_name = Column(String(64), nullable=False)
    description = Column(String(64), nullable = False)
    date=Column(String(64), nullable=False)
    completed=Column(Integer, nullable =False)
    
@property
def serialize(self):
    return {
        'task_name' : self.name,
        'description' : self.description,
        'date' : self.date,
        'completed' : self.completed,
        'id' : self.id
    }

engine = create_engine('sqlite:///tasks.db')
 

Base.metadata.create_all(engine)