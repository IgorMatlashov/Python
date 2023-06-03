# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

my_list = ['Hello\n', 'How are u?\n', 'I see u\n', 'Good\n']
with open("text_2.txt", 'w', encoding='utf-8') as file_obj:
    file_obj.writelines(my_list)
with open("text_2.txt") as f:
    lines = 0
    letters = 0
    for line in f:
        lines += line.count("\n")
        letters = len(line)-1
        print(f"{letters} letters in line")
    print(f"String count is {lines}")