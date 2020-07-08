"""1. Реализовать класс Matrix (матрица).
Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать данные (список списков)
для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц)
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:
    def __init__(self, user_list):
        self.user_list = user_list

    def __str__(self):
        return '\n'.join([' '.join([str(y) for y in i]) for i in self.user_list])

    def __add__(self, other):
        my_list = []
        for idx, el_1 in enumerate(self.user_list, 0):
            el_3 = []
            for idx2, el_2 in enumerate(el_1, 0):
                numbers = el_2 + other.user_list[idx][idx2]
                el_3.append(numbers)
            my_list.append(el_3)
        return Matrix(my_list)


user_list_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
user_list_2 = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
print(user_list_1)
print('#' * 30)
print(user_list_2)
print('#' * 30)
user_list_3 = user_list_1 + user_list_2
print(user_list_3)
