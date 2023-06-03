# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

rus_numbers = ['Один', 'Два', 'Три', 'Четыре']
i = 0
out_f = open('text_new_4.txt', 'w', encoding='utf-8')
with open('text_4.txt', encoding='utf-8') as f:
    for line in f:
        new_line = line.split('-')
        new_line[0] = rus_numbers[i]
        out_f.write(' -'.join(new_line))
        i += 1
out_f.close()