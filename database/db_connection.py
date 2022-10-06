"""Module to connect to database
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from env_vars import USER, PWD, DB, HOST, PORT


my_sql_conn = create_engine(
    "mysql://" + USER + ":" + PWD + "@" + HOST + ":" + str(PORT) + "/" + DB
)

Session = sessionmaker(bind=my_sql_conn)
Base = declarative_base()