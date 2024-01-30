# task_manager/database.py
from sqlalchemy.orm import sessionmaker

from models import engine

Session = sessionmaker(bind=engine)
session = Session()
