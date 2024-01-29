# task_manager

task_manager/
├── alembic/
│   ├── versions/
│   │   └── ... (your migration scripts)
│   ├── env.py
│   └── script.py.mako
├── task_manager/
│   ├── __init__.py
│   ├── models.py
│   ├── database.py
│   └── ...
├── Pipfile
├── Pipfile.lock
└── alembic.ini


In this example below:

sqlalchemy.orm.joinedload is used to eagerly load the related Category and User objects along with the Task objects in a single query.
The relationships (category and user) defined in the Task model are used to access the associated objects.
By utilizing SQLAlchemy relationships, you abstract away the need to explicitly perform JOIN operations in your queries. 
SQLAlchemy will take care of generating the appropriate SQL queries based on the relationships you defined in your models.
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from your_module import Task, Categories, Users  # Replace 'your_module' with the actual module name where your models are defined

# Create an SQLite in-memory database for demonstration purposes
engine = create_engine('sqlite:///:memory:', echo=True)

# Create the tables in the database
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Add sample data to the database
category = Categories(name='Sample Category')
user = Users(username='sample_user', password='password', email='user@example.com', name='John', surname='Doe')
task = Task(description='Sample Task', priority='High', name='Task 1', category=category, user=user)
session.add(category)
session.add(user)
session.add(task)
session.commit()

# Query tasks with associated category and user
tasks_with_details = session.query(Task).options(
    # Specify the relationships to load eagerly
    sqlalchemy.orm.joinedload(Task.category),
    sqlalchemy.orm.joinedload(Task.user)
).all()

# Access the details
for task in tasks_with_details:
    print(f'Task: {task.description}, Category: {task.category.name}, User: {task.user.username}')

