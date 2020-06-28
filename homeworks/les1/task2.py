# Пересчет секунд в чч:мм:сс
print('Программа преобразования количества секунд в формат чч:мм:сс\n')

while True:
    my_time = input('Введите количество секунд числом: \n')
    if my_time.isdigit():
        my_time = int(my_time)
        break
    else:
        print('Ошибка ввода, это не число')

my_hour = my_time // 3600
my_minute = (my_time % 3600) // 60
my_second = (my_time % 3600) % 60

print(f'После преобразования {my_hour:>002}:{my_minute:>002}:{my_second:>002}')
