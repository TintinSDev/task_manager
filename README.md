# TASK_MANAGER CLI

## Author: Martin Maina
https://wakatime.com/projects/task_manager

```
TASK_MANAGER/
├── lib
│   ├── alembic.ini
│   ├── database.py
│   ├── __init__.py
│   ├── manager.py
│   ├── migrations
│   │   ├── env.py
│   │   └── versions
│   │       └── __pycache__
│   ├── models.py
│   ├── notes
│   ├── __pycache__
│   ├── seed.py
│   ├── task_manager.db
│   └── users.py
├── Pipfile
├── Pipfile.lock
└── README.md

```

# How to run the project.
* Git clone into git@github.com:TintinSDev/task_manager.git
* cd into task_manager
* Run $python manager.py add_task --description "Your task description" --priority "Your priority" --name "name of user" --enrollment_date "date of enrollment" --category_id "" --user_id ""
* Run your sqlite database and viola, all your tasks added
* Used faker library to generate random category descriptions,tasks and users by running python seed.py.

### manager.py
Running the manager.py command gives options for CRUD operations for all tasks

### models.py
Running models.py command creates the database table for the projects which contains three tables; Tasks,Categories and Users

### seed.py
Running seed.py command promps the faker library to generate random category descriptions,tasks and users 

## Code Structure & Libraries
* sqlalchemy.orm.joinedload is used to eagerly load the related Category and User objects along with the Task objects in a single query.
* The relationships (category and user) defined in the Task model are used to access the associated objects.
* By utilizing SQLAlchemy relationships, you abstract away the need to explicitly perform JOIN operations in your queries. 
* SQLAlchemy will take care of generating the appropriate SQL queries based on the relationships you defined in your models.
* from sqlalchemy import create_engine
* from sqlalchemy.orm import sessionmaker
* from your_module import Task, Categories, Users  # Replace 'your_module' with the actual module name where your models are defined

### Create an SQLite in-memory database for demonstration purposes
```
engine = create_engine('sqlite:///:memory:', echo=True)
```

### Create the tables in the database
```
Base.metadata.create_all(engine)
```

### Create a session
```
Session = sessionmaker(bind=engine)
session = Session()
```

### Add sample data to the database
```
category = Categories(name='Sample Category')
user = Users(username='sample_user', password='password', email='user@example.com', name='John', surname='Doe')
task = Task(description='Sample Task', priority='High', name='Task 1', category=category, user=user)
session.add(category)
session.add(user)
session.add(task)
session.commit()
```
### Query tasks with associated category and user
```
tasks_with_details = session.query(Task).options(
    # Specify the relationships to load eagerly
    sqlalchemy.orm.joinedload(Task.category),
    sqlalchemy.orm.joinedload(Task.user)
).all()
```
### Access the details
for task in tasks_with_details:
    print(f'Task: {task.description}, Category: {task.category.name}, User: {task.user.username}')

## Fire Library Code for tasks

```
import fire
from models import Task, session

class TaskManager:
    def add_task(self, description, priority,username):
        new_task = Task(description=description, priority=priority, username=username)
        session.add(new_task)
        session.commit()
        print(f'Task added: {description} (Priority: {priority}, Assigned to: {username})')

    def list_tasks(self):
        tasks = session.query(Task).all()
        if not tasks:
            print('No tasks found.')
        else:
            print('Tasks:')
            for task in tasks:
                print(f'{task.id}. {task.description} (Priority: {task.priority} Assigned to: {username})')

if __name__ == '__main__':
    fire.Fire(TaskManager) ```
```
## Faker generation

* Generate descriptions for categories using Faker's fake.text() method.
* Create categories with the generated descriptions and add them to the session.
* Iterate over the categories to create tasks with descriptions matching those of the categories. These tasks are then added to the session.
* Finally, create users and add them to the session as before.
* Generate new usernames using the fake.unique.user_name() method to ensure uniqueness.
* Check if each new username already exists in the Users table. If not, create a new user with that username and a random password.
* Proceed to create tasks using the newly generated and verified usernames.



