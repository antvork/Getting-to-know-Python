# Списки
# list_1 = []  # Создание пустого списка
# List_2 = list()  #  Создание пустого списка через функцию List
# list_1 = [1, 9, 11, 13, 14, 17]
# print(list_1)
# print(*list_1) #выводит список без []

# for i in list_1:
#     print(i, end =' ')
# print()

# print(len(list_1)) # вывод длинны списка

# print(list_1[-1])

# list_1.append(8) #Добавление элемента в список
# print(list_1)

# list_3 = []
# for i in range(5): #Дополнение списка поочередноо из функции range
#     list_3.append(i)
#     print(list_3)

# Удаление последнего элемента списка:
# list_1 = [1, 9, 11, 13, 14, 17]
# print(list_1)
# print(list_1.pop()) # Удаление последнего элмента из списка и возвращение его для вывода на экран
# print(list_1)

# Удаление конкретного элемента списка
# list_1 = [1, 9, 11, 13, 14, 17]
# print(list_1)
# print(list_1.pop(0)) #Удаление первого элемента
# print(list_1)

# Добавление элемента на нужную позицию
# list_1 = [1, 2, 3, 13, 14, 17]
# print(list_1)
# print(list_1.insert(2, 15)) #Добвление на 2 позицию  нужного элемента
# Срезы
# list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(list_1[0])
# print(list_1[1])
# print(list_1[len(list_1)-1])  # вывод последнего элемента списка
# print(list_1[-1])  # Вывод последнего элемента списка
# print(list_1[-5])   # 5
# print(list_1[:])  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(list_1[:2])  # [1, 2]
# print(list_1[len(list_1)-2:])  # [8, 9]
# print(list_1[2:9]) #[3, 4, 5, 6, 7, 8, 9]
# print(list_1[6:-18]) #[]
# print(list_1[0:len(list_1):6]) #[1, 7] # Вывод сначала до конца с шагом 6
# print(list_1[::6]) #[1, 7] # Вывод сначала до конца с шагом 6

# ### Кортеж ###
# t = ()  # Создание пустого кортежа
# print(type(t))  # <class 'tuple'> класс кортеж
# t = (1,)  # способ заполненеия кортежа ВАЖНА ЗАПЯТАЯ в конце
# print(type(t))

# v = [1, 6, 9]
# print(v)
# print(type(v))

# v = tuple(v)  # Изменение списка в кортеж
# print(v)  # (1, 6, 9)
# print(type(v))

# # a, b = 1, 2  # Множественное присваивание
# a, b, c = v # получение данных в переменные через множественнное присваивание
# print(a, b, c)

###

# t = (5, 6, 3, 4, 5)
# for i in t:
#     print(i)

# for i in range(len(t)):
#     print(t[i])

# Словари

# d = {} #Создание пустого словаря
# d = dict() #Создание пустого словаря

# d['q'] = 'qwerty'  #создали ключ и присвоили к нему значение
# print(d) # {'q': 'qwerty'}

# d['w'] = 'werty'
# print(d)# {'q': 'qwerty', 'w': 'werty'}
# print(d['q']) # qwerty

# dictionary = {}
# dictionary = {'up': '^', 'left': '<', 'down': 'v',
#               'right': '>'}  # Заполнение словаря
# print(dictionary) # {'up': '^', 'left': '<', 'down': 'v', 'right': '>'}
# print(dictionary['left']) # <
# dictionary['left'] = '<=' #Замена значения элемента
# print(dictionary['left'])

# dictionary[998] = 98772 #Добавление ключа и значения в словарь
# print(dictionary['tupe']) # KeyError: 'tupe'
# del (dictionary['left'])  # Удаление элемента из словаря

# for item in dictionary:  # вывод только ключей
#     print(item)

# for item in dictionary:  # Вывод ключа и значения через .format
#     print('{} : {}'.format(item, dictionary[item]))

# print(dictionary.items()) #Выводит список из кортежей dict_items([('up', '^'), ('left', '<'), ('down', 'v'), ('right', '>')])

# for (k, v) in dictionary.items(): # выводит ключ и значение
#     print(k, v)

# # МНОЖЕСТВА
# q = set()  # создание множества
# colors = {'red', 'green', 'blue'} #Создание и запись значений в множество
# print(colors)  # {'green', 'red', 'blue'}
# colors.add('red')  # Попытка добавить неуникальное значение
# print(colors)  # {'green', 'red', 'blue'}
# colors.add('gray')  # Добавление значения в множество
# print(colors)  # {'red', 'blue', 'green', 'gray'}
# colors.remove('red')  # Удаление значения
# print(colors)  # {'green', 'gray', 'blue'}
# colors.discard('red')  # Удаление с проверкой
# colors.clear()  # Удаление всех элементов Множества
# print(colors)  # set()


# Операции с множествами в Python
# a = {1, 2, 3, 4, 8}
# b = {2, 6, 3, 14, 33}
# c = a.copy()  # Копирование значений множества {1, 2, 3, 4, 8}
# u = a.union(b)  # Ообъединение множеств {1, 2, 3, 4, 33, 6, 8, 14}
# i = a.intersection(b)  # Поиск пересечения множеств {2, 3}
# dl = a.difference(b)  # Нахождение разности множества {8, 1, 4}
# dr = b.difference(a)  # {33, 6, 14}
# # Находим пересечения множеств, далее объединяем два множества без этих элементов  {1, 33, 4, 6, 8, 14}
# q = a.union(b).difference(a.intersection(b))
# print(q)

# # Замороженные множества
# a = {1, 8, 6}
# # Заморозка множества, для того чтобы его нельзя было изменять
# b = frozenset(a) # создание неизменяемого множества
# print(b)

### List Comprehension - Генератор списка
list_1 = [i for i in range(1, 101)] #Создание списка от 1 до 100
print(list_1)
list_2 = [i for i in range(1, 101) if i % 2 == 0]  #Создание списка от 1 до 100 только четные числа
print(list_2)
list_2 = [(i, i) for i in range(1, 101) if i % 2 == 0] #Создание кортежей 
print(list_2)
list_3 = [i*2 for i in range(10) if i % 2 == 0]
print(list_3)

list_4 = [0]*7
print(len(list_4))