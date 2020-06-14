# Пересчет секунд в чч:мм:сс
print('Программа преобразования количества секунд в формат чч:мм:сс\n')
my_time = input('Введите количество секунд числом: \n')
my_time = int(my_time)
my_hour = my_time // 3600
my_minute = (my_time % 3600) // 60
my_second = (my_time % 3600) % 60

print(f'После преобразования {my_hour:>002}:{my_minute:>002}:{my_second:>002}')