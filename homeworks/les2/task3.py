"""
Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict
"""

print('Вариант решения через list \n')
while True:
    month = input('Введите месяц в виде целого числа от 1 до 12 \n')
    if month.isdigit():
        month = int(month)
        if month not in range (1, 13):
            print(f'{month} - не входит в диапазон от 1 до 12 \n')
            continue
        break
    print(f'{month} - не является числом \n')

winter, spring, summer, autumn = [12, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]

if month in winter:
    print(f'\n{month} месяц относится к зиме \n')
elif month in spring:
    print(f'\n{month} месяц относится к весне \n')
elif month in summer:
    print(f'\n{month} месяц относится к лету \n')
else:
    print(f'\n{month} месяц относится к осени \n')

print('\nВариант решения через dict \n')

year_time = {
    'winter': (12, 1, 2),
    'spring': (3, 4, 5),
    'summer': (6, 7, 8),
    'autumn': (9, 10, 11)
}

for key, value in year_time.items():
    if month in value:
        print(key)




