'''Module for any database related methods
'''
from sqlalchemy import select
from database.db_connection import Session
from models.user import User


session = Session()

def insert_user(user):
    '''insert user record into table
    '''
    session.add(user)
    session.commit()
    session.close()


def select_all_users():
    '''retrieve all records from user table
    '''
    stmt = select(User)
    for user in session.scalars(stmt):
        print(user)
