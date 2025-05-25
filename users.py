# users.py
users = []

def add_user(username, password):
    users.append({
        'username': username,
        'password': password
    })

def get_all_users():
    return users
