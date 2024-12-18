import runpy

while True:
        user_action = input('list, run or exit: ')
        user_action_start = user_action.strip()

        """if user_action_start.startswith('list'):
                print("Доступні лабораторні роботи:")
                labs = ['lab1 - Лабораторна робота №1', 'lab2 - Лабораторна робота №2',
                        'lab3 - Лабораторна робота №3', 'lab4 - Лабораторна робота №4',
                        'lab5 - Лабораторна робота №5', 'lab6 - Лабораторна робота №6', 
                        'lab7 - Лабораторна робота №7']
                for index, item in enumerate(labs):
                        item = item.strip("\n")
                        row = f"{index+1}. {item}"
                        print(row)
        elif user_action_start.startswith('exit'):
                break"""

        match user_action:
                case 'list':
                        print("Доступні лабораторні роботи:")
                        labs = ['lab1 - Лабораторна робота №1', 'lab2 - Лабораторна робота №2',
                                'lab3 - Лабораторна робота №3', 'lab4 - Лабораторна робота №4',
                                'lab5 - Лабораторна робота №5', 'lab6 - Лабораторна робота №6', 
                                'lab7 - Лабораторна робота №7']
                        for index, item in enumerate(labs):
                                item = item.strip("\n")
                                row = f"{index+1}. {item}"
                                print(row)
                case 'run 1':
                        runpy.run_path(path_name='CLI/labs/lab1/lab1.py')
                case 'run 2':
                        from labs.lab2 import *
                        runpy.run_path(path_name='CLI/labs/lab2/lab2.py')
                case 'run 3':
                        runpy.run_path(path_name='CLI/labs/lab3/lab3.py')
                case 'run 4':
                        runpy.run_path(path_name='CLI/labs/lab4/lab4.py')
                case 'run 5':
                        runpy.run_path(path_name='CLI/labs/lab5/lab5.py')
                case 'run 6':
                        runpy.run_path(path_name='CLI/labs/lab6/lab6.py')
                case 'run 7':
                        runpy.run_path(path_name='CLI/labs/lab7/lab7.py')
                case 'exit':
                        break
                case _:
                        print('Невірне значення!')

print("Завершено!")