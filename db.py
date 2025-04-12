import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="your_mysql_username",       # change this
        password="your_mysql_password",   # change this
        database="mystudylife_db"         # must match the database you created
    )
