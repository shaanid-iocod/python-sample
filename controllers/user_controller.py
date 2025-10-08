from users import get_all_users, create_user
from views import render_template

def list_users():
    users = get_all_users()
    return render_template("index.html", {"user": users})

def store_user(data):
    create_user(data['name'], data['email'])
