'''Main driver for app
'''
from database.db_methods import select_query, insert_query


if __name__ == "__main__":
    insert_query("Mike", "Hawk", "mike@mail.com")
    select_query()
