# lib/manager.py

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
            
    def delete_task(self, task_id):
        try:
            task = session.query(Task).filter(Task.id == task_id).first()
            if task:
                session.delete(task)
                session.commit()
                print(f'Task with ID {task_id} deleted successfully.')
            else:
                print(f'Task with ID {task_id} not found.')
        except Exception as e:
            session.rollback()
            print(f'Error deleting task: {e}')

def main():
    manager = TaskManager()
    while True:
        print("\n1. Add Task\n2. List Tasks\n3. Delete Task\n4. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            description = input("Enter task description: ")
            priority = input("Enter task priority: ")
            username = input("Enter username: ")
            manager.add_task(description, priority, username)
        elif choice == "2":
            manager.list_tasks()
        elif choice == "3":
            task_id = int(input("Enter task ID to delete: "))
            manager.delete_task(task_id)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
