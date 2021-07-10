from fakeData import fakeUsers
import jwt
import os

jwt_secret_key = os.getenv("JWT_SECRET_KEY")

def getUser(user_id):
    user = None

    for u in fakeUsers.users:
        if(u['id'] == user_id):
            return u
    
    return user

def login_with_credentials(username, password):
    user = None

    for u in fakeUsers.users:
        if(u['name'] == username and u['password'] == password):
            return u
    
    return user

def generate_token(name, is_admin, user_id):
    token = jwt.encode({"name": name, "admin": is_admin, "user_id": user_id}, jwt_secret_key, algorithm="HS256")
    return token