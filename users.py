from db import get_connection

def get_all_users(limit=None, offset=None):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM users"
    params = []
    if limit is not None and offset is not None:
        query += " LIMIT %s OFFSET %s"
        params = [limit, offset]
    cursor.execute(query, params)
    users = cursor.fetchall()
    cursor.close()
    conn.close() 
    return users

def create_user(name, email):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
    conn.commit()
    cursor.close()
    conn.close()
