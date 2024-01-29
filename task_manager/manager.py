# task_manager/manager.py
import fire
from task_manager.models import Task, session

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

if __name__ == '__main__':
    fire.Fire(TaskManager)
