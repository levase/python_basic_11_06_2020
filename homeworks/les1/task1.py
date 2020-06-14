a = 1
b = 2.1
c = 'Программа'
d = 'работает'

name = input('Ваше имя?\n')
surname = input('Ваша фамилия?\n')

while True:
    age = input('Сколько Вам лет?\n')
    if age.isdigit():
        age = int(age)
        break
    print('Введите возраст числом')

print(f'Вас зовут {name} {surname}, {2020-age} года рождения\n')
print(c, d)
