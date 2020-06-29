# 3. Реализовать базовый класс Worker (работник),
# в котором определить атрибуты:
# name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь,
# содержащий элементы: оклад и премия, например,
# {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника
# (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).


class Worker:

    def __init__(self, name, surname, position, _income, _bonus=0):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': _income, 'bonus': _bonus}


class Position(Worker):
    def __init__(self, name, surname, position, income, _bonus=0):
        super().__init__(name, surname, position, income, _bonus=0)

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')


a = Position('Igor', 'Mat.', 'Director', 5000)
print(a.get_full_name())
print(a.position)
print(a.get_total_income())
