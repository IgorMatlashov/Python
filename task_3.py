# 3. Создать текстовый файл (не программно),
# построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

with open('text_3.txt', 'r', encoding='utf-8') as f:
    my_list = f.readlines()
    data = {}
    for i in my_list:
        i = i.split()
        i[1] = float(i[1])
        data.update({i[1]: i[0]})
    for i in data.keys():
        if i < 20000:
            print(f'{data.get(i)}, has salary of less than 20,000')
    print(f'Average employee income: {(sum(data.keys())/ len(data))}')