# lib/users.py

from models import Users
from database import Session

session = Session()

class UserManager:
    def add_user(self, username, password):
        try:
            new_user = Users(username=username, password=password)
            session.add(new_user)
            session.commit()
            print(f'User added: {username}')
        except Exception as e:
            session.rollback()
            print(f'Error adding user: {e}')

    def list_users(self):
        try:
            users = session.query(Users).all()
            if not users:
                print('No users found.')
            else:
                print('Users:')
                for user in users:
                    print(f'{user.id}. {user.username}')
        except Exception as e:
            print(f'Error listing users: {e}')

    def delete_user(self, user_id):
        try:
            user = session.query(Users).filter(Users.id == user_id).first()
            if user:
                session.delete(user)
                session.commit()
                print(f'User with ID {user_id} deleted successfully.')
            else:
                print(f'User with ID {user_id} not found.')
        except Exception as e:
            session.rollback()
            print(f'Error deleting user: {e}')

def main():
    manager = UserManager()
    while True:
        print("\n1. Add User\n2. List Users\n3. Delete User\n4. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            manager.add_user(username, password)
        elif choice == "2":
            manager.list_users()
        elif choice == "3":
            user_id = int(input("Enter user ID to delete: "))
            manager.delete_user(user_id)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
