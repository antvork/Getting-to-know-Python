# a = 5
# b = 5.58
# c ='hello'

# # print (f"{a} - {b} - {c}") интерполяция  строк
# print ("{} - {} - {}".format(a,b,c)) # интерполяция  строк через функцию

# print('Введите первое число')
# a = int(input())
# # print(a)
# b = int(input('Введите второе число'))

# print(a, ' + ', b, ' = ', a + b)

# c = 5.89
# print(c)
# print(type(c))
# c = int(c) #Производим приведение типов из float в int
# print(c)
# print(type(c))


# c = 1
# print(c)
# print(type(c))
# c = bool(c)
# print(c)
# print(type(c))
###

# a = 5.8945
# b = 6.3453
# print(round(a*b, 3)) #Функция ограничения количества знаков после запятой
###

# iter = 2
# iter += 3  # iter = iter + 3
# iter -= 4  # iter =iter - 4
# iter *= 5  # iter = iter * 5
# iter /= 5 # iter = iter / 5
# iter //= 5 # iter = iter // 5 # Целочисленное деление
# iter %= 5 # iter = iter % 5
# iter **= 5 # iter = iter **5
###

# username = input('Введите имя: ') # IF - IFELSE - ELSE
# if username == 'Маша':
#     print('Ура, это же Маша!')
# elif username == 'Марина':
#     print('Я так ждала тебя, Марина')
# elif username == 'Ильнар':
#     print('Ильнар - топ')
# else:
#     print('Привет, ', username)
###

# i = 0
# while i < 5: # цикл while - else
#     # if i == 3: # Не рекомендуется использовать, есть метод флажка
#     #     break
#     i += 1
# else:
#     print('Пожалуй')
#     print('Хватит )')
# print(i)
###

# n =int(input()) # Метод флажка
# flag = True
# i = 2
# while flag: #
#     if n % i == 0: #если остаток при делении числа n на i равен 0
#         flag = False
#         print(i)
#     elif i > n // 2: # делить числа не может превышать введенное число, делимое на 2
#         print(n)
#         flag = False
#     i += 1
###

#r = range(5) # Функция range()
# r = range(1, 10, 2) # Функция range()
# for i in r: # цикл for
#     print(i)
###

# a = 'qwerty' # проходим по строке и выводим посимвольно
# for i in a:
#     print(i)
###
# line = "" # Вложенные циклы
# for i in range(5): # ???
#     line = ""
#     for j in range(5):
#         line += "*"
#     print(line)
### РАБОТА СО СТРОКАМИ

# text = "СъЕШЬ еще этих МяГкИх французских булок"
# print(len(text)) # выводит количество символов
# print("еще" in text) # проверяет есть ли в строке данный текст
# print(text.lower()) # переводит весь текст в верхний регистр
# print(text.upper()) # переводит весь текст в нижний регистр
# print (text.replace('еще', 'ЕЩЕ')) # функция замены слова еще на ЕЩЕ
### СРЕЗЫ

# text = "СъЕШЬ еще этих МяГкИх французских булок"
# print(text[0])
# print(text[1])
# print(text[len(text)-1]) # вывод последнего символа
# print(text[-1]) # вывод последнего символа ОТРИЦАТЕЛЬНОЕ ИНДЕКСИРОВАНИЕ
# print(text[-5])
# print(text[:]) # вывод всех символов
# print(text[:2]) # вывод первых 2 символов
# print(text[len(text)-2:]) #вывод последних 2 символов
# print(text[20:]) # вывод с 20 символа до конца
# print(text[2:9]) # вывод со 2 элемента до 9 не включая
# print(text[6:-18]) # вывод с 6 до -18 (обратная индексация)
# print(text[0:len(text):6]) # вывод от 0 до конца с шагом в 6 символов
# print(text[::6]) #вывод от 0 до конца с шагом в 6 символов
# text = text[2:9] + text[-5] + text[:2] # сложение частей строк
# print(text)



