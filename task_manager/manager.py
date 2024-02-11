from models import Task
from database import Session

session = Session()

class TaskManager:
    def add_task(self, description, priority, username): 
        try:
            new_task = Task(description=description, priority=priority, username=username)  
            session.add(new_task)
            session.commit()
            print(f'Task added: {description} (Priority: {priority}, Assigned to: {username})')  
        except Exception as e:
            session.rollback()
            print(f'Error adding task: {e}')

    def list_tasks(self):
        try:
            tasks = session.query(Task).all()
            if not tasks:
                print('No tasks found.')
            else:
                print('Tasks:')
                for task in tasks:
                    print(f'{task.id}. {task.description} (Priority: {task.priority}, Assigned to: {task.username})')  
        except Exception as e:
            print(f'Error listing tasks: {e}')

def main():
    manager = TaskManager()
    while True:
        print("\n1. Add Task\n2. List Tasks\n3. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            description = input("Enter task description: ")
            priority = input("Enter task priority: ")
            username = input("Enter username: ")  # Prompt for username input
            manager.add_task(description, priority, username)  # Pass username to add_task method
        elif choice == "2":
            manager.list_tasks()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
