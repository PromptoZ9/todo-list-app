import json


def intro():
    print("###############################")
    print("---Welcome to TO_DO_LIST_APP---")
    print("###############################")
    print("_______________________________")

def menu_list():
    main_menu = ("add todo", "see all todos", "edit todo", "erase todo", "erase all todos", 
    "end the program")
    for i, m in enumerate(main_menu, start = 1):
        print(f"{i}. {m}")
     
def get_user_input():
    while True:
        try:
            user_input = int(input(" Input the number based on the list above: "))
            if user_input in [1,2,3,4,5,6]:
                return user_input
            else: 
                print("Input not valid, please input the number based on the list")
        except ValueError:
            print("Error pls input the number based on the list: ")
            
def show_username(full_name):
    print(f"Welcome {full_name}")
    
def add_todos(todos): 
    todo_name = input ('Input your todo: ') 
    description = input('Describe your activity:  ')
    isImportant = bool(input('is it important? 1 or 0:  '))
    notes = []
    while True:
        note = input('add your notes, type "exit" to leave:  ')
        if note == "exit":
            break
        else:
            notes.append(note)
    todo = {
        "name" : todo_name, 
        "description" : description, 
        "isImportant" : isImportant, 
        "notes" : notes
     }
    todos.append(todo) 
    return todos
            
def exit_program(db):
    print('exiting program')
    save_json("db.json",db)
    exit()
    
def show_todos(todos):
    if len(todos) < 1:
        print("Your todo list is empty")
    else: 
        print("Here's the list of your todos : ")
        for i, todo in enumerate(todos, start=1):
            print (f"{i}. {todo['name']} - {todo['description']}")
        user_input = int(input('type the number of your todo on the list to see the detail: '))
        if user_input > 0 and user_input <= len(todos):
            todo = todos[user_input - 1]
            print("--------------------------------")
            for key in todo:
                if isinstance(todo[key],bool):
                    match todo[key]:
                        case True:
                            print(f"{key.upper()} = IMPORTANT")
                        case False:
                            print(f"{key.upper()} = UNIMPORTANT")
                elif isinstance(todo[key], list):
                    print("EXTRA NOTE(s)= ")
                    for i, note in enumerate(todo[key], start = 1):
                        print(f"{i}. {note}")
                else:
                    print(f"{key.upper()} = {todo[key]}")
            print("--------------------------------")
        else:
            raise ValueError("Input is not valid, please input the number from the list above") 
        
def show_todos_simpler(todos):
    if len(todos) < 1:
        print("Your todo list is empty")
    else: 
        print("Here's the list of your todos : ")
        for i, todo in enumerate(todos, start=1):
            print (f"{i}. {todo['name']} - {todo['description']}")
            
def delete_todos(todos):
    while True:
        todo_delete = int(input ('Input todos that need to be erased, type 0 to cancel: ')) - 1
        if todo_delete == -1:
            return todos
        elif todo_delete >= 0 and todo_delete < len(todos):    
            deleted_todo = todos.pop(todo_delete)
            print(f"your {deleted_todo['name']} activity from your todo list has been deleted")
           
        else:
            print ("Input is not valid, please input based on the list above")

   
def delete_all_todos(todos, username):
    sure = input('are you sure to erase all of your todos? y or n: ')
    if sure == 'y':
        todos.clear()
        print(f"All of {username} activities from the todo list has been deleted")
        return todos
    else:
        return todos

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
        db[username] = {"name": username, "password": password1, 'todos': [] }
        save_json("db.json", db)
        exit("Register success")
    else:
        raise Exception('username/password did not match, or username already been used')

         
if __name__ == '__main__':
    db = read_json("db.json")
    intro() 
    
    login_or_register = input('login or register: ')
    match login_or_register:
        case 'login':
            user = login(db)
        case 'register':
            register(db)
        case _:
            raise ValueError('Invalid input, please input login or register')    

while True:
    menu_list()
    user_input = get_user_input()
    match user_input: 
        case 1:
            while True: 
                user['todos'] = add_todos(user['todos'])
                exit_ = bool(input('Are you sure you want to exit? 1-> yes, 0-> no:  '))
                if exit_:
                    save_json('db.json', db)
                    print("Returning to main menu")
                    break
        case 2:
            show_todos(user['todos'])
        case 3:
            print("Edit your todo list")
            show_todos_simpler(user['todos'])
            todo_input = int(input("choose the number of your todo that needs to be edited: ")) - 1
            if todo_input < 0:
                raise ValueError('Input is not valid,please input the number based on the list above')
            print(user['todos'][todo_input])
            for i, key in enumerate(user['todos'][todo_input], start=1): 
                print(f"{i}. {key}")
            user_input = int(input("choose the number based on the list to edit your todo: "))
            match user_input:
                case 1:
                    user['todos'][todo_input]['name'] = input('enter updated todo name: ')
                case 2:
                    user['todos'][todo_input]['description'] = input('enter todo updated description: ')
                case 3:
                    user['todos'][todo_input]['isImportant'] = int(input('enter new important status, 1 -> Important, 0-> Not Important: '))                    
                case 4:
                    print("Extra notes: ")
                    for i, k in enumerate(user['todos'][todo_input]['notes'], start=1):
                        print(f"{i}. {k}")
                    indeks_input = int(input('Choose a number from the list above to edit the extra notes: ')) - 1
                    if indeks_input < 0:
                        raise ValueError('Input is not valid, please input the number based from above')
                    user['todos'][todo_input]['notes'][indeks_input] = input("Add extra note here: ")
        case 4:
            show_todos_simpler(user['todos'])
            user["todos"] = delete_todos(user["todos"])
            print("Returning to main menu")
        case 5:
            todos = delete_all_todos(user['todos'], user['name'])
            print("Returning to main menu")
        case 6:
            exit_program(db)
        case _:
            print("Input is not valid")

