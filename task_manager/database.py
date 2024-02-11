# task_manager/database.py
from sqlalchemy.orm import sessionmaker

from models import engine

Session = sessionmaker(bind=engine)
session = Session()

# DATABASE_URL = 'mysql+pymysql://root:-Martin6553@localhost:3306/task_manager'



