from models import Task, session
import ipdb

class TaskManager:
    def add_task(self, description, priority):
        new_task = Task(description=description, priority=priority)
        session.add(new_task)
        session.commit()
        print(f'Task added: {description} (Priority: {priority})')

    def list_tasks(self):
        tasks = session.query(Task).all()
        if not tasks:
            print('No tasks found.')
        else:
            print('Tasks:')
            for task in tasks:
                print(f'{task.id}. {task.description} (Priority: {task.priority})')

def main():
    manager = TaskManager()
    while True:
        print("\n1. Add Task\n2. List Tasks\n3. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            description = input("Enter task description: ")
            priority = input("Enter task priority: ")
            manager.add_task(description, priority)
        elif choice == "2":
            manager.list_tasks()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()