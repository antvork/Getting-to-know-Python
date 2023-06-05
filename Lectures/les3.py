# Функции
# def sumNumbers(n):
#     summa = 0
#     for i in range(1, n+1):
#         summa += i
#     return summa

# # a = sumNumbers(5)
# # print(sumNumbers(5))
# # print(a)

# def sumNumbers2(n, y = 'Hello'): # Передача со сзначением по умолчанию
#     print(y)
#     summa = 0
#     for i in range(1, n+1):
#         summa += i
#     return summa

# print(sumNumbers2(5, 'qwerty')) # Передача с заменой значения по умочанию

# def sum_str(*args): #Вариант с неизвестным количеством агрументов
#     res = ''
#     for i in args:
#         res += i
#     return res

# # print(sum_str('q', 'r', 'l'))
# # print(sum_str('q', 'r', 'l', 'qwe'))
# print(sum_str(1, 3, 5)) # Будет ошибка типа, т.к. res = string

# Модульность
# Модуль это файл в котором есть функции и мы их можем использовать

# import modul1 # Подключение модуля
# print(modul1.max1(5, 9)) # вызов модуля

# from modul1 import max1 # Импорт определенной функции
# from modul1 import * # Импорт всех функции из модуля
# print(max1(5, 9))
# import modul1 as m1 #Присвоение другого названия для модуля для удобства
# print(m1.max1(10, 9))

# Рекурсия

# def fib(n):
#     if n in [1,2]: #Условие выхода из рекурсии ОБЯЗАТЕЛЬНО!!!
#         return 1 #Условие выхода из рекурсии ОБЯЗАТЕЛЬНО!!!
#     return fib(n-1) + fib(n-2)

# list_1 = []
# for i in range(1, 10):
#     list_1.append(fib(i))
# print(list_1)

# Алгоритмы
# Набор инструкций для выполнения задачи
# Быстрая сортировка

# def quick_sort(array):
#     if len(array) <= 1:
#         return array
#     else:
#         pivot = array[0]
#     less = [i for i in array[1:] if i <= pivot]
#     greater = [i for i in array[1:] if i > pivot]
#     return quick_sort(less) + [pivot] + quick_sort(greater)


# print(quick_sort([10, 5, 2]))

# Сортировка слиянием


def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1


list1 = [1, 5, 9, 3, 83]
merge_sort(list1)
print(list1)
