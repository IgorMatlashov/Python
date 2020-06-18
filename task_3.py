# 3. Реализовать функцию my_func(),
# которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def sum (num_1, num_2, num_3):
    try:
        numbers = sorted([int(num_1), int(num_2), int(num_3)])
    except ValueError:
        return 'Enter numbers'
    return numbers[1:]

print(sum((input('Enter first number: ')),
          (input('Enter second number: ')),
          (input('Enter third number: '))))