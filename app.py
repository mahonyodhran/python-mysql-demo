from database.db_methods import selectQuery, insertQuery


if __name__ == "__main__":
    insertQuery('John', 'Doe', 'john@mail.com')
    selectQuery()