# 5. Создать (программно) текстовый файл,
# записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

with open('text_5,txt', 'w+', encoding='utf-8') as f:
    try:
        numbers = input('Enter numbers: ')
        f.writelines(numbers)
        my_list = numbers.split()
        print(sum(map(int, my_list)))
    except ValueError:
        print('Enter numbers!')