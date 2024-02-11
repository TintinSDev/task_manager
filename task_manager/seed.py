from models import Task, Categories, Users
from faker import Faker
from database import session

fake = Faker()

# # Create and add users
users = [Users(username=fake.name(), password=fake.password()) for _ in range(4)]
session.add_all(users)
session.commit()


# user_ids connecte to the usernames
user_ids = {user.username: user.id for user in users}
# print("User IDs:", user_ids) 
# we now new usernames for tasks
new_usernames = [fake.unique.name() for _ in range(1)]

# Create and add users with the new usernames
users = []
for username in users:
        password = fake.password()
        user = Users(username=username, password=password)
        users.append(user)
   
session.add_all(users)
session.commit()

# Generate descriptions for categories
category_descriptions = [fake.text() for _ in range(4)]

# Create and add categories with the same descriptions
categories = [Categories(description=description) for description in category_descriptions]
session.add_all(categories)
session.commit()

# connect category descriptions to category ids
category_ids = {category.description: category.id for category in categories}

# Create and add tasks with corresponding category descriptions and usernames
tasks = []
for category in categories:
    username = fake.random_element(elements=new_usernames)
    task = Task(description=category.description, 
                priority=fake.random_element(elements=('Low', 'Medium', 'High')), 
                username=username, 
                category_id=category.id,
                user_id = user.id
                ) 
    tasks.append(task)

    if len(tasks) == 4:
         break
session.add_all(tasks)
session.commit()






# # Create and add tasks with connected usernames
# tasks = [
#     Task(description=fake.text(), priority='Low', username=fake.name(), user_id=user_ids[username])
#     for username in user_ids
# ]

# # Extend the tasks list with tasks having connected category IDs
# tasks.extend([
#     Task(description=fake.text(), priority='Low', username=fake.name(), category_id=category_ids[category_desc])
#     for category_desc in category_descriptions
# ])
# session.add_all(tasks)
# session.commit()
# tasks = []
# categories = []
# users = []

# for _ in range(3):
#     task = Task(description=fake.text(), priority='Low', username=fake.name(), category_id=1, user_id=1)
#     tasks.append(task)

# for _ in range(3):
#     category = Categories(description=f'Description {_+1}')
#     categories.append(category)

# for _ in range(3):
#     user = Users(username=f'User {_+1}', password=f'Password {_+1}')
#     users.append(user)

# session.add_all(tasks)
# session.add_all(categories)
# session.add_all(users)
# session.commit()
