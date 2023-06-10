# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# a1 = int(input('Enter first element: '))
# d = int(input('Enter differens: '))
# n = int(input('Enter quantity: '))
# res = [a1 + (i - 1) * d for i in range(1, n+1)]
# print(res)

# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

data = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
dataIndex = []
print(data)

nmin = int(input('Enter min: '))
nmax = int(input('Enter max: '))
dataIndex =[i for i in range(0, len(data)) if data[i] >= nmin and data[i] <= nmax]
print(dataIndex)