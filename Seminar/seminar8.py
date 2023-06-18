# Задача №49. Общее обсуждение
# Создать телефонный справочник с возможностью импорта и экспорта данных вформате .txt.
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи
# (Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных.

import os

def show_contacts(file_name):
    os.system('CLS')
    with open(file_name, 'r') as file:
        data = file.readlines()

        for contact in data:
            print(contact, end='')
    input('\nContact was successfully added! \nPress any key')


def add_contacts(file_name):
    os.system('CLS')
    with open(file_name, 'a') as file:
        res = ''
        res += input('Enter a surname of contact: ') + " "
        res += input('Enter a name of contact: ') + " "
        res += input('Enter a phonenumber of contact: ')

        file.write("\n" + res)
    input('Contact was successfully added! \nPress any key')


def search_contact(file_name):
    os.system('CLS')
    target = input('Input name of contact for searching: ')

    with open(file_name, 'r') as file:
        contacts = file.readlines()

        for contact in contacts:
            if target in contact:
                print(contact)
                break
            else:
                print('there is no contacts with ti name')
    input('\nPress any key')


def change_contact(file_name):
    os.system('CLS')
    target = input('Input name of contact for change: ') #Ищем что заменить
    chCont = ''
    with open(file_name, 'r') as file:
        contacts = file.readlines()

        for contact in contacts:
            if target in contact:
                chCont = contact #Поместили что заменить
                print(contact)
                break
        else:
            input('There is no contacts with ti name. \nPress any key')
            # print('There is no contacts with ti name')
            return
        newCont = ''
        newCont += input('Enter a surname of contact: ') + " "
        newCont += input('Enter a name of contact: ') + " "
        newCont += input('Enter a phonenumber of contact: ')
        for i in range(len(contacts)): ###
            if contacts[i] == chCont:
                contacts[i] = newCont + '\n'
                break
        # contacts = list(map(lambda x: x.replace(chCont, newCont + '\n'), contacts))#для замены всех похожих значеий
        
    with open(file_name, 'w') as file:
        for item in contacts:
            file.write(item)
    input('\nPress any key')


def delete_contact(file_name):
    os.system('CLS')
    target = input('Input name of contact for delete: ') #Ищем что удалить
    delCont = ''
    with open(file_name, 'r') as file:
        contacts = file.readlines()

        for contact in contacts:
            if target in contact:
                delCont = contact #Поместили что заменить
                print(contact)
                break
        else:
            input('There is no contacts with ti name. \nPress any key')
            # print('There is no contacts with ti name')
            return
        choice = input(f'Do you really want to delete a contact {delCont}? Press y or n: ')
        if choice == 'y':
            contacts.remove(delCont)
        else: return
        
    with open(file_name, 'w') as file:
        for item in contacts:
            file.write(item)
    input('\nPress any key')



def drawing():
    print('1 - show contacts')
    print('2 - add contacts')
    print('3 - search contacts')
    print('4 - change contacts')
    print('5 - delete contacts')
    print('6 - exit')


def main(file_name):
    while True:
        os.system('CLS')
        drawing()
        user_choice = int(input("Input a number from 1 to 6: "))

        if user_choice == 1:
            show_contacts(file_name)
        elif user_choice == 2:
            add_contacts(file_name)
        elif user_choice == 3:
            search_contact(file_name)
        elif user_choice == 4:
            change_contact(file_name)
        elif user_choice == 5:
            delete_contact(file_name)
        elif user_choice == 6:
            print('Have a nice day!')
            return


# show_contacts("d:/learning/GB_devops/Python/Seminar/test.txt")
# add_contacts("d:/learning/GB_devops/Python/Seminar/test.txt")
main("d:/learning/GB_devops/Python/Seminar/test.txt")
