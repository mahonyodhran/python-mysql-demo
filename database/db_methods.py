from database.db_connection import my_sql_conn


def insertQuery(first_name, last_name, email):
    values = [first_name, last_name, email]
    my_sql_conn.execute(
        "insert into user (first_name,last_name, email) values(%s,%s, %s)", values
    )


def selectQuery():
    query = my_sql_conn.execute("SELECT * FROM user;")
    for row in query:
        print(row)
    query.close()
