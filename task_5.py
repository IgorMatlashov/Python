# 5. Программа запрашивает у пользователя строку чисел,
# разделенных пробелом. При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

result = 0
while True:
    line = input("Enter number or special token q fo exite or + fo sum: ")
    tokens = line.split(" ")
    for token in tokens:
        try:
            number = float(token)
            result += number
        except:
            if token == '+':
                print(f"You sum is {result}. Program is terminated")
            if token == 'q':
                print(f"You sum is {result}. Program is terminated")
                exit()