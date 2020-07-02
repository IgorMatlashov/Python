# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, name, size):
        self.name = name
        self.size = size

    @abstractmethod
    def expense(self):
        pass


class Coat(Clothes):
    @property
    def expense(self):
        return self.size / 6.5 + 0.5


class Suit(Clothes):
    @property
    def expense(self):
        return self.size * 2 + 0.3


coat = Coat('Nike', 52)
suit = Suit('Puma', 180)
print(f"{coat.expense} meters of fabric are spent on {coat.name}")
print(f"{suit.expense} meters of fabric are spent on {suit.name}")
common = coat.expense + suit.expense
print(f"Total spent {common} fabrics")
