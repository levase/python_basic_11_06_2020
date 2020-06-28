"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""

while True:
    number_a = input('Введите первое число\n')
    number_b = input('Введите второе число\n')
    if not (number_a.isalpha() or number_b.isalpha()):
        number_a = float(number_a)
        number_b = float(number_b)
        break
    print('Введите числа\n')


def my_division(data_1: float, data_2: float) -> float:
    """
    Реализация функции деления двух чисел
    :param data_1: первое число
    :param data_2: второе чило
    :return: результат деления первого числа на второе
    """
    try:
        result = data_1 / data_2
        return result
    except ZeroDivisionError:
        print('\nДелить на ноль нельзя!')


print(f'\n{number_a} / {number_b} = ', my_division(number_a, number_b))
