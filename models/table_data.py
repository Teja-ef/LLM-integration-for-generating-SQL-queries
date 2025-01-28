from sqlalchemy import Column, Integer, String, DateTime, Boolean, func, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Table = declarative_base()

class Person(Table):
    __tablename__ = "USERS"
    
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    # Relationship to the Task table
    tasks = relationship("Task", back_populates="user")

class Task(Table):
    __tablename__ = "TASK"

    id = Column(Integer, primary_key=True, autoincrement=True)
    ToDo = Column(String(255), nullable=False)
    CreatedAt = Column(DateTime, default = func.now(),nullable=False)
    Status = Column(String(255), nullable=False)
    isExist = Column(Boolean, nullable=False)
    user_id = Column(Integer, ForeignKey("USERS.user_id"))
    # Relationship to the Person table
    user = relationship("Person", back_populates="tasks")

    



