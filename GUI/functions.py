def get_todos(filepath="app1/files/todos.txt"):
    '''Read a txt file and return list of to-do items'''
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_args, filepath="app1/files.todos.txt"):
    '''
    Write the to-do list in the text file
    '''
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_args)