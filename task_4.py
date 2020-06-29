# 4. Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction)
# , которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.


class Car:
    def __init__(self, color, name, speed, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'The {self.color}, {self.name} went at {self.speed} km/h')

    def turn(self, direction):
        self.direction = direction
        print(f'The {self.color} {self.name} turned {self.direction}')

    def stop(self):
        print(f'The {self.color}, {self.name} stopped')

    def show_speed(self):
        print(f'The {self.color}, {self.name} rides at a speed {self.speed}')


class TownCar(Car):
    def __init__(self, color, name, speed, is_police=False):
        super().__init__(color, name, speed, is_police=False)

    def show_speed(self):
        if self.speed > 60:
            print(f'The {self.color}, {self.name} rides exceeds speed. Allowable speed no move then 60 km/h')
        else:
            print(f'The {self.color}, {self.name} rides at an acceptable speed')


class SportCar(Car):
    def __init__(self, color, name, speed, is_police=False):
        super().__init__(color, name, speed, is_police=False)

class WorkCar(Car):
    def __init__(self, color, name, speed, is_police=False):
        super().__init__(color, name, speed, is_police=False)

    def show_speed(self):
        if self.speed > 40:
            print(f'The {self.color} {self.name} exceeds speed. Allowable speed no move then 40 km/h')
        else:
            print(f'The {self.color}, {self.name} rides at an acceptable speed')


class PoliceCar(Car):
    def __init__(self, color, name, speed, is_police=False):
        super().__init__(color, name, speed, is_police=False)


audi = SportCar('Red', 'Audi', 100)
nissan = TownCar('White', 'Nissan', 30)
lada = WorkCar('Rose', 'Lada', 70, True)
ford = PoliceCar('Blue',  'Ford', 110, True)

audi.go()
nissan.turn('left')
lada.stop()
ford.show_speed()

# a = Car('Mazda', 'black', 60)
# a.go()
# a.turn('left')
# a.stop()
# a.show_speed()
#
# t = TownCar('nissan', 'rad', 60)
# t.show_speed()
#
# t_2 = TownCar('nissan', 'white', 70)
# t_2.show_speed()
#
# w = WorkCar('police', 'red', 40)
# w.show_speed()
#
# w_2 = WorkCar('police', 'green', 50)
# w_2.show_speed()