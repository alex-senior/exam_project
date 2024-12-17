from math import *
from termcolor import colored

print(colored('Завдання 1', 'blue')) # task1
a = float(input('Ведіть число: '))
z = cos(a) + cos(2*a) + cos(6*a) + cos(7*a)
print('Результат: ', z)

print(colored('Завдання 2', 'blue')) # task2
n = int(input("Ведіть натуральне число: "))
f = 1
for i in range (n):
    y = (2*n)-1
    n = n-1
    f = f*y
print('Результат: ', f)

print(colored('Завдання 3', 'blue')) # task3
list = [2, 4, -3, 0, 9, 54, -2, -6]
print('Результат: ', max(list))
k = 0
for i in range(len(list)):
    if(list[i]%2==0 and list[i]>0):
        k+=list[i]
print('Результат: ', k)

list.reverse()
for m in range(len(list)):
    if(list[m]<0):
        print(list[m])