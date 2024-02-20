from seed import Faker
from models import Task, Categories, Users, DATABASE_URL, create_engine
from database import sessionmaker
from manager import TaskManager
import ipdb



fake = Faker()

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)


ipdb.set_trace()