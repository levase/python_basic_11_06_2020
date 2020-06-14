a = 1
b = 2.1
my_str1 = 'Программа'
my_str2 = 'работает'

name = input('Ваше имя?\n')
surname = input('Ваша фамилия?\n')

while True:
    age = input('Сколько Вам лет?\n')
    if age.isdigit():
        age = int(age)
        break
    print('Введите возраст числом')

print(f'Вас зовут {name} {surname}, {2020-age} года рождения\n')
print(my_str1, my_str2)
