# 2. Пользователь вводит время в секундах. Переведите время в часы,
# минуты и секунды и выведите в формате чч:мм:сс.
# Испоьзуйте форматирование строк.

sec = int(input('Enter second: '))
h = sec // 3600
m = (sec // 60) % 60
s = sec % 60

h = str(h)
m = str(m)
s = str(s)

if len(h) < 2:
    h = '0' + h
else:
    h
if len(m) < 2:
    m = '0' + m
else:
    m
if len(s) < 2:
    s = '0' + s
else:
    s

print(f'{h}:{m}:{s}')