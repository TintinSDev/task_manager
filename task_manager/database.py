# task_manager/database.py
from sqlalchemy.orm import sessionmaker

from task_manager.models import engine

Session = sessionmaker(bind=engine)
session = Session()
