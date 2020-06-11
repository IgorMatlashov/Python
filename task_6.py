# 6. Спортсмен занимается ежедневными пробежками.
# В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.

start = int(input('Enter the results of the first day in km: '))
finish = int(input('Enter the total desired result in km: '))

day = 1

while start < finish:
    print(f'{day} days: {start:.2f}')
    start = start + (start / 100 * 10)
    day += 1
print(f'{day} days: {start:.2f}, need for your purpose')


