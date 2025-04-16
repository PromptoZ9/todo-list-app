import json

def read_json(filename):
    with open(filename,'r') as file:
        data = json.load(file)
    return data

def save_json(filename, db):
    with open(filename,'w') as file:
       json.dump(db, file)

def login(db):
    username = input('username: ')
    password = input('password: ')
    if username in db and db[username]['password'] == password:
        print(f'login success!, welcome {username}')
        return db[username]
    else: 
        raise ValueError('login failed, username/password is incorrect')

def register(db):
    username = input('username: ')
    password1 = input('password: ')
    password2 = input('confirm password: ')
    if password1 == password2 and username not in db:
        print('register success')
        db[username] = {"name": username, "password": password1, 'todos': [] }
        save_json("db.json", db)
    else:
        raise Exception('username/password did not match, or username already been used')


if __name__ == "__main__":
    db = read_json("db.json")
    register(db)
    #user = login(db)
    #print(user)