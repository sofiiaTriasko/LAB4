import MySQLdb

def get_connection():
    url = "localhost"
    database_name = "store"
    user = "root"
    password = "password"
    return MySQLdb.connect(url, user, password, database_name)
