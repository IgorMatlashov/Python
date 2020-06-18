# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def division(num_1, num_2):
    try:
        result = int(num_1) / int(num_2)
    except ZeroDivisionError:
        return ('Division by zero')
    except ValueError:
        return ('Enter numbers')
    return f'result: {result:.2f}'

print(division((input('Enter dividend: ')), (input('Enter divisor: '))))
