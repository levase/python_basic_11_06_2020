"""3. Реализовать базовый класс Worker (работник),
в котором определить атрибуты: name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь,
содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
 и дохода с учетом премии (get_total_income).
 Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
 проверить значения атрибутов, вызвать методы экземпляров).
 """


class Worker:
    def __init__(self, name, surname, position, _income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = _income


class Position(Worker):
    def get_full_name(self):
        print(self.name, self.surname)

    def get_total_income(self):
        print(f'Зарплата: {sum([self._income["wage"], self._income["bonus"]])}')


a = Position("Ivan", "Ivanov", "Engineer", {"wage": 45000, "bonus": 2000})
print(a.name)
print(a.surname)
print(a.position)
print(a._income)
a.get_full_name()
a.get_total_income()
print()
a = Position("Petr", "Petrov", "Expert", {"wage": 90000, "bonus": 12000})
print(a.name)
print(a.surname)
print(a.position)
print(a._income)
a.get_full_name()
a.get_total_income()
