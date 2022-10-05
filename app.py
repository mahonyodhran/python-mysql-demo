from db_connection import my_sql_conn

# result = my_sql_conn.execute("INSERT INTO instructor VALUES (ID,first_name, last_name, email, NULL)")

query = my_sql_conn.execute('SELECT * FROM instructor;')
for row in query:
    print(row)
    
query.close()