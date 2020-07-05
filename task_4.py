# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.


class Equipment:
    def __init__(self, name, surname, count, price):
        self.name = name
        self.surname = surname
        self.count = count
        self.price = price
    def __str__(self):
        return f"{self.name} {self.surname} left {self.count} by price {self.price}"

class Printer(Equipment):
    def __init__(self, name, surname, count, price):
        super().__init__(name, surname, count, price)
        self.data = []
    def chars(self, *chars):
        self.data = list(chars)


class Stock:
    place = []
    def stores(self, *eqs):
        for eq in eqs:
            self.place.append(eq)

s = Stock()

printer = Printer('samsung', '1x', 5, 1300)
printer.chars('color', 'B&W', 'Bluetooth')
print(printer.data)

s.stores(printer)
print(s.place)
