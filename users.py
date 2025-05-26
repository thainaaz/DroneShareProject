# users.py
users = []

def add_user(username, password):
    users.append({
        'username': username,
        'password': password
    })

def get_all_users():
    return users

def find_user_by_username(username):
    for user in users:
        if user['username'] == username:
            return user
    return None
