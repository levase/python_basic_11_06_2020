my_number = input('Введите целое положительное число: \n')
my_number = int(my_number)
max_number = my_number % 10
my_number = my_number // 10
while my_number > 0:
    if my_number % 10 > max_number:
        max_number = my_number % 10
    my_number = my_number // 10
print('Максимальное число в цифре -', max_number)

