# 1. Реализовать класс «Дата»,
# функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Data:
    def __init__(self, data):
        self.data = data

    @classmethod
    def get_data(cls, data):
        my_data = []
        for i in data.split():
            if i != '-':
                my_data.append(int(i))
        return my_data

    @staticmethod
    def validation(my_data):
        if 1 <= my_data[0] <= 31:
            if 1 <= my_data[1] <= 12:
                if my_data[2] < 0:
                    return f'BC'
                else:
                    return 'If this date is your birthday, then Happy holiday!:)'
            else:
                return f'Wrong month'
        else:
            return f'Wrong day'


    def __str__(self):
        result = Data.validation(Data.get_data(self.data))
        return result

while True:
    data = input('Enter data: ')
    if data == 'stop':
        break
    d = Data(data)
    print(d)
