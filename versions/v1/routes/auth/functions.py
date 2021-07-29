from fakeData import fakeUsers
import jwt
import os
from models import Client, Admin
from app import db
from email_validator import validate_email, EmailNotValidError

jwt_secret_key = os.getenv("JWT_SECRET_KEY")

def getUser(user_id):
    user = None

    for u in fakeUsers.users:
        if(u['id'] == user_id):
            return u
    
    return user

def login_with_credentials(username, password):

    # Verificar se é admin
    admin = Admin.query.filter_by(adminname=username).first()

    if admin != None:
        if admin.password == password:
            return {
                "code": 0,
                "name": admin.adminname,
                "password": admin.password,
                "email": admin.email,
                "id": admin.id,
                "admin": True,
            }
        else:
            return {
            "code": 2
        } # Password incorreto



    user = Client.query.filter_by(username=username).first()

    if user == None:
        return {
            "code": 1, 
        }# Usuário não existe
    if user.password != password:
        return {
            "code": 2
        } # Password incorreto
    
    return {
        "code": 0,
        "name": user.username,
        "password": user.password,
        "email": user.email,
        "id": user.id,
        "admin": False,
    }

def generate_token(name, is_admin, user_id):
    print(f"Secret {jwt_secret_key}")
    token = jwt.encode({
            "name": name,
            "admin": is_admin, 
            "user_id": user_id}, 
            jwt_secret_key, 
            algorithm="HS256",
        )
    return token

def password_check(passwd):
    SpecialSym =['$', '@', '#', '%']
    val = True
      
    if len(passwd) < 6:
        print('length should be at least 6')
        val = False
          
    if not any(char.isdigit() for char in passwd):
        print('Password should have at least one numeral')
        val = False
          
    if not any(char.isupper() for char in passwd):
        print('Password should have at least one uppercase letter')
        val = False
          
    if not any(char.islower() for char in passwd):
        print('Password should have at least one lowercase letter')
        val = False
          
    if not any(char in SpecialSym for char in passwd):
        print('Password should have at least one of the symbols $@#')
        val = False
    if val:
        return val

def email_check(email):
    try:
        validate_email(email)
        return True
    except EmailNotValidError as e:
        print(e)
        return False

def create_user(name, password, email):
    user = Client(name, password, email)
    db.session.add(user)
    db.session.commit()
    return user

def is_username_available(name):
    user = Client.query.filter_by(username=name).first()
    return user == None