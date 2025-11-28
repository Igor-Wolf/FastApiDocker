from repositories.user_repository import get_users_from_db

def fetch_users():
    users = get_users_from_db()
    return users
