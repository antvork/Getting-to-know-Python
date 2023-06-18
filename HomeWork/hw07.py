# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, 
# Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) 
# в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. 
# Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры. 
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

# *Пример:*

# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
#     **Вывод:** Парам пам-пам  
# list_1 = [input().split()]


# def ditties_pooh(list_1):
#     list_2 = list_1.split()
#     letter_1 = ['а','у','о','ы','и','э','я','ю','е','ё']
#     countList = list()

#     for item in list_2:
#         k = 0
#         for letter in item:
#             if letter in letter_1:
#                 k += 1
#         countList.append(k)
    
#     if len(set(countList)) == 1:
#         print('Парам пам-пам')
#     else:
#         print('Пам парам')

        
# list_1 ='пара-ра-рам рам-пам-папам па-ра-па-да'
# list_2 ='пара-ра-рам рам-пум-пупам па-ре-по-дам'
# list_3 ='Трам-пара-папам-парам-па-пам-пам-па Пум-пурум-пу-пурум-трам-пам-па'
# list_4 ='Пам-парам-пурум Пум-пурум-карам'

# ditties_pooh(list_2)

# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и
# столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте,
# почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой
# ровно два аргумента, как, например, у операции умножения.
# Ввод: Вывод:
# print_operation_table(lambda x, y: x * y) 
#  1  2  3  4  5  6
#  2  4  6  8 10 12
#  3  6  9 12 15 18
#  4  8 12 16 20 24
#  5 10 15 20 25 30
#  6 12 18 24 30 36 

def print_operation_table(operation, num_rows, num_columns):
    string_1 = ""
    for i in range(1, num_columns+1):
        for j in range(1, num_rows+1):
            string_1 += f"{operation(i, j):4d}"
        print(string_1)
        string_1 = ""
    return ''

print(print_operation_table(lambda x,y: x*y, 6, 6))