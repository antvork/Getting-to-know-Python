# def calc1(a, b):
#     return a+b

# def calc2(a, b):
#     return a*b

# def f(x):
#     return x*x

# print(type(f))

# def math(op, x, y):
#     print(op(x, y))

# math(calc2, 5, 8) #Возможность передавать функцию в функцию
# ЛЯМБДА ФУНКЦИИ
# math(lambda a, b: a + b, 5, 45)

# calc = lambda a, b: a+b  - лямбда функция
# def calc(a, b): return a + b - тоже само что и наверху
# print(calc(1, 9))

# Пример
# 1. В списке хранятся числа. Нужно выбрать только чётные числа и составить список пар
# (число; квадрат числа).
# Пример: 1 2 3 5 8 15 23 38
# Получить: [(2, 4), (8, 64), (38, 1444)]

# list1 = [1, 2, 3, 5, 8, 15, 23, 48]
# resList = []
# for i in list1:
#     if i % 2 == 0:
#         resList.append((i, i**2)) ### добавление  в виде кортежа

# print(resList)

# def select(f, col):   ### Пересмотреть и разобрать!!!
#     return [f(x) for x in col] # в переменную f мы ложим фкнкцию и для всех элементов x из col мы применяем функцию


# def where(f, col):
#     return [x for x in col if f(x)] # функция возвращает список если они прошли провеку f(x) функции


# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = select(int, data)  # переводим все к целочисленному типу
# print(res)

# res = where(lambda x: x % 2 == 0, res) # возвращяем список только с четными значениями
# print(res)

# res = list(select(lambda x: (x, x**2), res)) # возвращаем список кортежей x и x**2
# # res = select(lambda x: (x, x**2), res) # возвращаем список кортежей x и x**2
# print(res)

# Функция MAP

###
# map  =  # def select(f, col):   ### Пересмотреть и разобрать!!!
# return [f(x) for x in col]
###

# list_1 = [x for x in range(1, 20)]
# print(list_1)

# list_1 = list(map(lambda x: x + 10, list_1))
# print(list_1)
###
###
# C клавиатуры вводится некий набор чисел, в качестве разделителя используется
# пробел. Этот набор чисел будет считан в качестве строки. Как превратить list строк в list чисел?

# data = '15 16 33 45 78'
# # print(data)

# # data = data.split()
# # print(data)
# data = list(map(int, data.split())) #Разделяек элементы >  преобразуем в число > заносим в список
# print(data)

# def where(f, col):# функция возвращает список если они прошли провеку f(x) функции
#     return [x for x in col if f(x)]


# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = map(int, data)  # переводим все к целочисленному типу
# print(res)

 
# res = where(lambda x: x % 2 == 0, res) # возвращяем список только с четными значениями
# print(res)


# res = list(map(lambda x: (x, x**2), res)) # возвращаем список кортежей x и x**2
# res = map(lambda x: (x, x**2), res) # возвращаем список кортежей x и x**2
# print(res)

# /////////////////////////////////////////////////////
# Функция filter
## функция where тоже самое что и filter

# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = list(filter(lambda x: x % 10 == 5, data))
# print(res)

# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = map(int, data)  # переводим все к целочисленному типу
# res = filter(lambda x: x % 2 == 0, res) # возвращяем список только с четными значениями
# res = list(map(lambda x: (x, x**2), res)) # возвращаем список кортежей x и x**2
# print(res)

### Функция zip????
#Функция zip() применяется к набору итерируемых объектов и возвращает итератор с кортежами
# # из элементов входных данны

# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# data = list(zip(users, ids)) 
# print(data) # [('user1', 4), ('user2', 5), ('user3', 9), ('user4', 14), ('user5', 7)]

# Функция zip () пробегает по минимальному входящему набору:
# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111, 222, 333]
# data = list(zip(users, ids, salary))
# print(data) # [('user1', 4, 111), ('user2', 5, 222), ('user3', 333)]

### Функция enumerate
# Функция enumerate() применяется к итерируемому объекту и возвращает новый итератор с
# кортежами из индекса и элементов входных данных.
# users = ['user1', 'user2', 'user3']
# data = list(enumerate(users))
# print(data) # [(0, 'user1'), (1, 'user2'), (2, 'user3')]

# ### Работа с файлами

# a - добавление
# colors = ['red', '88856', 'blue']
# data = open('file.txt', 'a', encoding='utf-8') # здесь указываем режим, в котором будем работать: a - режим добавления в файл
# data.writelines(colors) # разделителей не будет
# data.close() # закрыли файл

# w - перезаписи
# with open('file.txt', 'w') as data: # для того чтоб постоянно не открывать и закрывать файл, файл автоматический закроется w - режим замены в файле
#     data.write('line 1\n') # Внесем в файл значение line и сделаем перенос строки
#     data.write('line 2\n')

# print(56)

# r - Режим чтения
# path = 'file.txt'
# data = open('file.txt', 'r')
# for line in data:
#     print(line)
# data.close()

### Модуль os
# import os
### Модуль shutil
#import shutil