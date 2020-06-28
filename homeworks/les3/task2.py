"""
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.

Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""

name = 'Иван'
surname = 'Иванов'
year = 1964
town = 'Москва'
email = '1@2.net'
mobile = 8745212656


def user_info(name: str, surname: str, year: int, town: str, email: str, mobile: int, ) -> str:
    """
    вывод данных о пользователе одной строкой
    :param name: имя
    :param surname: фамилия
    :param year: год рождения
    :param town: город проживания
    :param email: email
    :param mobile: телефон
    :return: инфо о пользователе одной строкой
    """
    result = f'{name} {surname}, {year} год рождения. Проживает в {town}. Телефон {mobile}, эл. почта {email}'
    return result


print(user_info(name, surname, year, town, email, mobile))
