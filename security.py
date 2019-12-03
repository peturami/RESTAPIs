from resources.user import UserModel

def authenticate(username, password):
    user = UserModel.find_by_username(username)
    if user and user.password == password:
        return user

def identity(payload): # payload - content of JWT token
    user_id = payload['identity']
    print(user_id)
    print(payload)
    return UserModel.find_by_id(user_id)

