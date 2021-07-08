from fakeData import fakeUsers

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