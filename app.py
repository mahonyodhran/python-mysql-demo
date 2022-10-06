'''Main driver for app
'''
from database.db_methods import select_all_users, insert_user
from models.user import User


if __name__ == "__main__":
    newUser = User("Tom", "Hanks", "tanks@mail.com")
    insert_user(newUser)
    select_all_users()