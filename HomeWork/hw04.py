from random import randint
# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

# n = int(input('Введите размер первого множества: '))
# m = int(input('Введите размер второго множества: '))
# nSet = []
# mSet = []

# for i in range(n):
#     print(f'Введите значение элемента {i+1} :', end=' ')
#     nSet.append(int(input()))
# for i in range(m):
#     print(f'Введите значение элемента {i+1} :', end=' ')
#     mSet.append(int(input()))

# nSet = set(nSet)
# mSet = set(mSet)
# print(f"Мноджество 1: {nSet}")
# print(f"Мноджество 2: {mSet}")
# resSet = nSet.intersection(mSet)
# print(f"Пересечение множеств: {resSet}")
# resSet = sorted(list(resSet))
# print(f"Отсортированные числа: {resSet}")

# Ввод чисел через пробел в список пока не нажмет Enter
# mol = [int(x) for x in input().split()]
# n = mol[0]  # Берется 1 число списка
# m = mol[1]  # 2 число списка
set_1 = set()
set_2 = set()
list_1 = list() # Лишнее
a = [int(x) for x in input().split()]  # Создается список под множество
k = set(a)  # список переводиться в множество
print(k)
# for i in k:
#     set_1.add(i) ## безсмысленное действие
b = [int(x) for x in input().split()]
k1 = set(b)
print(k1)
# for i in k1:
#     set_2.add(i) ###
# lok = set_1 & set_2
lok = k & k1 # объединение множеств
kool = list(lok)
kool.sort()
for i in kool:
    print(i, end=' ')


# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику.
# Она растёт на круглой грядке, причём кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном файле грядки.

gryadka = [4, 5, 3, 5, 7, 1, 2, 6, 7]
n = int(input('Введтите размер грядки: '))
gryadka = [randint(1, 10) for i in range(n)]

shema = {}
for i in range(len(gryadka)-1):
    shema[i] = gryadka[i-1]+gryadka[i]+gryadka[i+1]
shema[len(gryadka)-1] = gryadka[len(gryadka)-2] + gryadka[len(gryadka)-1] + gryadka[-len(gryadka)]
print(shema)
# # # shema = dict(sorted(shema.items(), key=lambda x: x[1], reverse=True))

print(f"Модуль соберет маскимальное количество ягоды с грядки № {max(shema, key=shema.get)} в количестве: {shema[max(shema, key=shema.get)]}")

n = int(input())
arr = list()
for i in range(n):
    x = int(input())
    arr.append(x)

arr_count = list()
for i in range(len(arr)-1):
    arr_count.append(arr[i -1] + arr[i] + arr[i+1])
arr_count.append(arr[-2]+ arr[-1]+arr[0])
print(max(arr_count))