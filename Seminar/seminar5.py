import customFunct as cf

# print(cf.LastFib(7))

# Задача №33. Решение в группах
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

# journal = [1, 2, 3, 4, 5, 1, 5, 5]
# # n = int(input("Введите размер журнала: "))
# # for i in range(n):
# #     journal.append(int(input('Введите оценку: ')))
# print(journal)

# estMax = max(journal)
# estMin = min(journal)
# print(estMax)
# print(estMin)

# for i in range(len(journal)):
#     if journal[i] == estMax:
#         journal[i]= estMin

# print(journal)

# Задача №35. Решение в группах
# Напишите функцию, которая принимает о число и проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

# number = int(input('Введите число: '))
# def is_simple(number):
#     if number > 2 and number %2 !=0:
#         for i in range( 3, number //2):
#             if number % i == 0:
#                 return False
#         return True
#     return False

# print(is_simple(number))

# def is_prime(number): #ИИ
#     if number < 2:
#         return False
#     for i in range(2, int(number ** 0.5) + 1):
#         if number % i == 0:
#             return False
#     return True
# ```
# Пример использования:
# ```
# print(is_prime(7))  # True
# print(is_prime(10))  # False

def reverse_range(num):
    print(num, end=' ')
    if num > 1:
        reverse_range(num -1)
    
number = int(input('Введите число: '))
             
reverse_range(number)