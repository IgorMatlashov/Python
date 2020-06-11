# 1. Поработайте с переменными, создайте несколько,
# выведите на экран, запросите у пользователя несколько чисел и строк и сохраните в переменные,
# выведите на экран.

name = input('Enter name: ')
age = int(input('Enter age: '))
hobby = input('Enter your hobby: ')

result = f'{name}, {age} age, my hobby is {hobby}'
print(result)