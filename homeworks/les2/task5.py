"""
Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2]
"""

my_list = [7, 5, 3, 3, 2]

# for item in enumerate(my_list):
#     print(item)

while True:
    user_number = input('Введите новый элемент рейтинга\n')
    if user_number.isdigit():
        user_number = int(user_number)
        break
    else:
        print(f'{user_number} - не является натуральным числом\n')

user_number_count = my_list.count(user_number)

if user_number_count == 0:
    if my_list[0] < user_number:
        my_list.insert(0, user_number)
    elif my_list[-1] > user_number:
        my_list.append(user_number)
    else:
        for item, value in enumerate(my_list[:]):
            if value < user_number:
                my_list.insert(item, user_number)
                break
else:
    item_2 = my_list.index(user_number) + user_number_count
    my_list.insert(item_2, user_number)
print(my_list)
quit()