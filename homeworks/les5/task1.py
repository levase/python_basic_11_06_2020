"""
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

with open('task1.txt', 'w', encoding='UTF-8') as file:
    while True:
        string = input()
        if string != '':
            file.write(f'{string}\n')
        else:
            break





