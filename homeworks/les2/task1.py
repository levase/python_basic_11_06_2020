"""
Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента.
Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя,
а указать явно, в программе.
"""

my_list = [1, 2, 15.0, 'qwerty', [1, 2, 3], None, True]

for my_class in my_list:
    print(type(my_class))
quit()
