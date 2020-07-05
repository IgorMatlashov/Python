# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна
# корректно обработать эту ситуацию и не завершиться с ошибкой.


class Zero(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    dividend = int(input('Enter dividend: '))
    divisor = int(input('Enter divisor: '))
    if divisor == 0:
        raise Zero('Cannot divided by 0!')
    res = dividend / divisor
except Zero as err:
    print(err)
except ValueError:
    print('Enter digit!')
else:
    print(res)
finally:
    print('End')
