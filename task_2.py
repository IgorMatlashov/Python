# 2. Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def data (name, surname, age, city, email, phone):
    print(f'{name} {surname}, {age}, lives in {city}, {email}, {phone}')

data(name = input('Enter name: '),
     surname = input('Enter surname: '),
     age = input('Enter age: '),
     city = input('Enter your city: '),
     email = input('Enter your email: '),
     phone = input('Enter your phone: '))