import os
import sys
sys.path.append(os.getcwd)

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, create_engine
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime




Base = declarative_base()
class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
    priority = Column(String, nullable=False)
    username = Column(String())
    enrollment_date = Column(DateTime(), default=datetime.utcnow)
    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship('Categories', back_populates='tasks')
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('Users', back_populates='tasks')

class Categories(Base):
    __tablename__ = 'categories'
    
    id = Column(Integer, primary_key=True)

    description = Column(String(), index=True)
    
    # Relationship with Task table
    tasks = relationship('Task', back_populates='category')

    def __repr__(self):
        return f'<Categories {self.description}>'
    def __str__(self):
        return self.description
    def __init__(self, description):
        self.description = description
    def __eq__(self, other):
        return self.description == other.description

class Users(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(), index=True)
    password = Column(String(), nullable=False)
    enrollment_date = Column(DateTime(), default=datetime.utcnow)
    

    # Relationship with Task table
    tasks = relationship('Task', back_populates='user')

    def __repr__(self):
        return f'<Users {self.username}>'

    def __str__(self):
        return self.username

    def __init__(self, username, password):
        self.username = username
        self.password = password
        

    def __eq__(self, other):
        return self.username == other.username

    
DATABASE_URL = "sqlite:///task_manager.db" 
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()
Base.metadata.create_all(bind=engine)

