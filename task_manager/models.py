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
    name = Column(String(), index=True)
    enrollment_date = Column(DateTime(), default=datetime.utcnow)
    
    # Relationship with Categories table
    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship('Categories', back_populates='tasks')

    # Relationship with Users table
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('Users', back_populates='tasks')

class Categories(Base):
    __tablename__ = 'categories'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(), index=True)
    description = Column(String(), index=True)
    
    # Relationship with Task table
    tasks = relationship('Task', back_populates='category')

    def __repr__(self):
        return f'<Categories {self.name}>'

    def __str__(self):
        return self.name

    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

class Users(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(), index=True)
    password = Column(String(), nullable=False)
    email = Column(String(55))
    name = Column(String(), index=True)
    surname = Column(String(), index=True)
    enrollment_date = Column(DateTime(), default=datetime.utcnow)

    # Relationship with Task table
    tasks = relationship('Task', back_populates='user')

    def __repr__(self):
        return f'<Users {self.username}>'

    def __str__(self):
        return self.username

    def __init__(self, username, password, email, name, surname):
        self.username = username
        self.password = password
        self.email = email
        self.name = name
        self.surname = surname

    def __eq__(self, other):
        return self.username == other.username

    
    
    
engine = create_engine('sqlite:///task_manager.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)