from env_vars import USER, PWD, DB, HOST, PORT
from sqlalchemy import create_engine

my_sql_conn = create_engine("mysql://"+USER+":"+PWD+"@"+ HOST+":"+str(PORT)+"/"+DB)
