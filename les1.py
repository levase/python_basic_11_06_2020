# PEP8

"""
int - Это целое число
float - Это дробное число
str - это строка
bool - boolean
"""

catalog_id_1 = 14 # Это комментарий
catalog_id_2 = 15
my_float = 12.134
my_str1 = 'Это строка 1'
my_str2 = "Это тоже строка 2"
my_str3 = """Это строка из
множества
строк"""

my_str4 = 'Нужно выделить "ТЕРМИН"'
my_str5 = "Нужно выделить \"ТЕРМИН\""

# age = 33
#
# if age >= 18:
#    print('Доступ разрешен')
# elif age >= 16:
#    print('Ограниченный доступ')
# else:
#    print('Доступ запрещен')

while True:
    age = input('Введите возраст\n')
    if age.isdigit():
        age = int(age)
        break
    print('Возраст должен быть числом')

if age >= 18:
    print('Доступ разрешен во все разделы включая ХХХ')
elif age >= 16:
    print('Доступ разрешен во все разделы')
elif age >= 8:
    print('Доступ разрешен в раздел \"Мультики\"')
else:
    print('Доступ запрещен')




