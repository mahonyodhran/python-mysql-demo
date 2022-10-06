"""Module to connect to database
"""
from sqlalchemy import create_engine
from env_vars import USER, PWD, DB, HOST, PORT


my_sql_conn = create_engine(
    "mysql://" + USER + ":" + PWD + "@" + HOST + ":" + str(PORT) + "/" + DB
)
