from models import Users, session
from datetime import datetime

class UserManager:
    def add_user(self, username, password, email, name, surname):
        new_user = Users(username=username, password=password, email=email, name=name, surname=surname)
        session.add(new_user)
        session.commit()
        print(f'User added: {username}')

    def list_users(self):
        users = session.query(Users).all()
        if not users:
            print('No users found.')
        else:
            print('Users:')
            for user in users:
                print(f'{user.id}. {user.username} ({user.email})')

def main():
    manager = UserManager()
    while True:
        print("\n1. Add User\n2. List Users\n3. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            email = input("Enter email: ")
            name = input("Enter name: ")
            surname = input("Enter surname: ")
            manager.add_user(username, password, email, name, surname)
        elif choice == "2":
            manager.list_users()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()