import sys

while True:
        user_action = input()
        user_action = user_action.strip()

        if user_action.startswith('list'):
                print("Доступні лабораторні роботи:")
                labs = ['lab1 - Лабораторна робота №1', 'lab2 - Лабораторна робота №2',
                        'lab3 - Лабораторна робота №3', 'lab4 - Лабораторна робота №4',
                        'lab5 - Лабораторна робота №5', 'lab6 - Лабораторна робота №6', 
                        'lab7 - Лабораторна робота №7']
                for index, item in enumerate(labs):
                        item = item.strip("\n")
                        row = f"{index+1}. {item}"
                        print(row)

        #elif user_action.startswith('run'):


        elif user_action.startswith('exit'):
                break
        else:
                print("Command is not valid")