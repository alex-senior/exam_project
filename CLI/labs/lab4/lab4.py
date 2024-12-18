import runpy
from termcolor import colored
print(colored("Task1", "yellow"))
runpy.run_path(path_name='CLI/labs/lab4/task1.py')

print('\n' + colored("Task2", "yellow"))
runpy.run_path(path_name='CLI/labs/lab4/task2.py')

print('\n' + colored("Task3", "yellow"))
runpy.run_path(path_name='CLI/labs/lab4/task3.py')