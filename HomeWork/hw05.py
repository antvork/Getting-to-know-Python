# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# # A = 3; B = 5 -> 243 (3⁵)
# #     A = 2; B = 3 -> 8
# def degree(num, deg):
#     if deg == 1:
#         return num
#     if deg != 1:
#         return num * degree(num, deg - 1)

# a = int(input("Введите число A: "))
# b = int(input("Введите степень B: "))

# print(f"Число А в степени В равно: {degree(a, b)}")

# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# *Пример:*
# 2 2
#     4

def summa(a, b):
    if a == 0:
        return b
    return summa(a-1, b+1)

a = int(input("Введите число A: "))
b = int(input("Введите степень B: "))

print(summa(a, b))
