# 2. Для списка реализовать обмен значений соседних элементов,
# т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

count = int(input('Enter the length of the list: '))
my_list = []
for num in range(count):
    my_list.append(int(input('Enter next number: ')))

for element in range(0, len(my_list) - 1, 2):
    my_list[element], my_list[element + 1] = my_list[element + 1], my_list[element]

print(my_list)