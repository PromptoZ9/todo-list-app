def intro():
    print("###############################")
    print("---Welcome to TO_DO_LIST_APP---")
    print("###############################")
    print("_______________________________")

def nama_input():
    front_name = input ('Input your first name: ')
    last_name =  input ('Input your last name: ')
    return f"{front_name} {last_name}"


def menu_list():
    print("Type 1 to add todo, ")
    print("Type 2 to see all todos, ")
    print("Type 3 to erase todos, ")
    print("Type 4 to erase all todos, ")
    print("Type 5 to end the program, ")
    
    
    
def get_user_input():
    while True:
        try:
            user_input = int(input("Input the number based on the list above: "))
            if user_input in [1,2,3,4,5]:
                return user_input
            else: 
                print("Input not valid, please input the number based on the list")
        except ValueError:
            print("Error pls input the number based on the list: ")
            

        
def show_username(full_name):
    print(f"Welcome {full_name}")
    
def add_todos(todos): 
    while True:
        todo_name = input ('Input your todo, type "exit" to save your todos: ') 
        if todo_name == 'exit':
            return todos
        else:
            todos.append(todo_name)    
    
    
def exit_program(todos):
    exit_ = input('Do you want to exit ?, y or n : ')
    if exit_ == 'y':
        print('exiting program')
        print(f"your todos are {todos}")
        exit()
    elif exit_ == 'n':
        print('restarting program (WIP)')
    else: 
        print('invalid input')

def show_todos(todos):
    if len(todos) > 0:
        print("Here's the list of your todos : ")
        for i, todo in enumerate(todos, start=1):
            print (f"{i}. {todo}")
    else: 
        print("Your todo list is empty")
        
        
def delete_todos(todos):
    while True:
        todo_delete = int(input ('Input todos that need to be erased, type 0 to cancel: ')) - 1
        if todo_delete == -1:
            return todos
        elif todo_delete >= 0:    
            todos.pop(todo_delete)
        else:
            print ("Input is not valid, please input based on the list above")

   
def delete_all_todos(todos):
    sure = input('are you sure to erase all of your todos? y or n: ')
    if sure == 'y':
        todos.clear()
        return todos
    else:
        return todos

        
intro()
full_name = nama_input()
show_username(full_name)


todos = []

while True:
    menu_list()
    user_input = get_user_input()
    #print(f"your user input is {user_input}")
    if user_input == 1:
        todos = add_todos(todos)
        print("Returning to main menu")
    elif user_input == 2:
        show_todos(todos)
    elif user_input == 3:
        show_todos(todos)
        todos = delete_todos(todos)
        print("Returning to main menu")
    elif user_input == 4:
        todos = delete_all_todos(todos)
        print("Returning to main menu")
    elif user_input == 5:
        exit_program(todos)
    else:
        print("Input is not valid")



