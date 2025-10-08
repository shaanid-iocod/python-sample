import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345678",
        database="python_crud"
    )
def close_connection(conn):
    if conn.is_connected():
        conn.close()