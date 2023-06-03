# 6. Необходимо создать (не программно) текстовый файл,
# где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

with open("text_6.txt", "r", encoding="utf-8") as f:
    plan = {}
    my_list = []
    for el in f:
        les_name, time_1, time_2, time_3 = el.split()
        les_name = les_name[:-1]
        try:
            if time_1 != '-':
                time_1 = int(time_1[:-3])
            else:
                time_1 = 0
            if time_2 != '-':
                time_2 = int(time_2[:-4])
            else:
                time_2 = 0
            if time_3 != '-':
                time_3 = int(time_3[:-5])
            else:
                time_3 = 0
            result = time_1 + time_2 + time_3
            my_list.append(les_name)
            my_list.append(result)
            plan[les_name] = result
        except:
            print('err')
    for key, value in plan.items():
        print(f'{key} hours: {value}')
