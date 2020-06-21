# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

salary = 0


def sal(*data):
    global salary
    name, time, rate, bonus = data
    try:
        salary = int(time) * int(rate) + int(bonus)
    except ValueError:
        print('Enter number')
    print(f'Employee salary {name} = {salary}')


if __name__ == '__main__':
    name, time, rate, bonus = argv
    try:
        salary = int(time) * int(rate) + int(bonus)
    except ValueError:
        print('Enter number')
    print(f'Employee salary {name} = {salary}')
