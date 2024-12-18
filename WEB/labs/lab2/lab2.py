from labs.lab2.function import *

list = [0, 2, 4, 2, 5, 9, 8, 3, 1, 7, 10]
menu = [quick_sort.__doc__, min_5.__doc__, max_5.__doc__, average.__doc__]

for index, item in enumerate(menu):
                        item = item.strip("\n")
                        row = f"{index+1} - {item}"
                        print(row)

user = input('Ведіть цифру функції: ')
match user:
    case '1':
        print('Результат: ', quick_sort(list))
        print('Лабораторна робота виконана успішно!')
    case '2':
        print('Результат: ', min_5(list))
        print('Лабораторна робота виконана успішно!')
    case '3':
        print('Результат: ', max_5(list))
        print('Лабораторна робота виконана успішно!')
    case '4':
        print('Результат: ', average(list))
        print('Лабораторна робота виконана успішно!')
    case _:
        print('Невірне значення!')