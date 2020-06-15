# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

number = int(input("Enter month number: "))
if number in range(1, 13):
    month_dict = {1: 'January',
                  2: 'February',
                  3: 'March',
                  4: 'April',
                  5: 'May',
                  6: 'June',
                  7: 'Jule',
                  8: 'August',
                  9: 'September',
                  10: 'October',
                  11: 'November',
                  12: 'December'}
    seasons_dict = {1: 'winter',
                    2: 'winter',
                    3: 'spring',
                    4: 'spring',
                    5: 'spring',
                    6: 'summer',
                    7: 'summer',
                    8: 'summer',
                    9: 'autumn',
                    10: 'autumn',
                    11: 'autumn',
                    12: 'winter'}
    month_list = list(month_dict.values())
    seasons_list = list(seasons_dict.values())
    for i, el in enumerate(month_dict):
        if i == number-1:
            print(f"Month from list is {month_list[i]} and this is {seasons_list[i]}")
            break
    print(f"Month from dict is {month_dict[number]} and this is {seasons_dict[number]}")
else:
    print("there is no such season")