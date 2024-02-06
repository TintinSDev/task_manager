from models import Task, session

class TaskManager:
    def add_task(self, description, priority, username):  # Updated method signature
        new_task = Task(description=description, priority=priority, username=username)  # Pass username to Task creation
        session.add(new_task)
        session.commit()
        print(f'Task added: {description} (Priority: {priority}, Assigned to: {username})')  # Print the assigned username along with the task details

    def list_tasks(self):
        tasks = session.query(Task).all()
        if not tasks:
            print('No tasks found.')
        else:
            print('Tasks:')
            for task in tasks:
                print(f'{task.id}. {task.description} (Priority: {task.priority}, Assigned to: {task.username})')  

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