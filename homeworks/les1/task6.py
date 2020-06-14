start_dist = input('Введите количество километров за первый день: \n')
finish_dist = input('Введите итоговое количество километров: \n')
day = 1
start_dist = int(start_dist)
finish_dist = int(finish_dist)

while start_dist < finish_dist:
    start_dist *= 1.1
    day += 1
print(day)

