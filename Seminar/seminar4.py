# Задача №25. Решение в группах
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.

# sp = input().split()
# print(sp)
# result = {}
# for i in sp:
#     if i in result:
#         print(f'{i}_{result[i]}', end=' ')
#     else:
#         print(i, end=' ')
#     result[i] = result.get(i, 0) + 1
# print()
# print(result)

# sp = input().split()
# my_dict = {}

# count = str()

# for letter in sp:
#     if letter in my_dict:
#         my_dict[letter] += 1
#         count += f'{letter}_{my_dict[letter]} '
#     else:
#         my_dict[letter] = 0
#         count += f'{letter} '
# print(count)


# a = {'a': 4, 'b': 6, 'c': 1}
# print(a['a'])
# a.get('d', 7) +1
# print(a)

# Задача №27. Решение в группах
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13
text = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure. So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"
text = text.upper().split()
print(len(set(text)))
print(set(text))

# Задача №29. Решение в группах
# Ваня и Петя поспорили, кто быстрее решит
# следующую задачу: “Задана последовательность
# неотрицательных целых чисел. Требуется определить
# значение наибольшего элемента
# последовательности, которая завершается первым
# встретившимся нулем (число 0 не входит в
# последовательность)”. Однако 2 друга оказались не
# такими смышлеными. Никто из ребят не смог до
# конца сделать это задание. Они решили так: у кого
# будет меньше ошибок в коде, тот и выиграл спор. За
# помощью товарищи обратились к Вам, студентам.
# Примечание: Программные коды на следующих
# слайдах

# n = int(input()) не верный код
# max_number = -1
# while n < 0: #>
#     n = int(input()) #второй раз 
#     if max_number < n: # > 
#         n = max_number
# print(n)
