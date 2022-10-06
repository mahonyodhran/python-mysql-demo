'''Module for any database related methods
'''
from database.db_connection import my_sql_conn


def insert_query(first_name, last_name, email):
    '''insert record into table
    '''
    values = [first_name, last_name, email]
    my_sql_conn.execute(
        "insert into user (first_name,last_name, email) values(%s,%s, %s)", values
    )


def select_query():
    '''retrieve records from table
    '''
    query = my_sql_conn.execute("SELECT * FROM user;")
    for row in query:
        print(row)
    query.close()
