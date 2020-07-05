# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.


class Stock:
    department_printer = []
    department_scanner = []
    department_copier = []
    dict_data = {}


class Equipment:
    def __init__(self, name, model, price, count=1):
        self.name = name
        self.model = model
        self.count = count
        self.price = price

    def __str__(self):
        return f"{self.name} {self.model} left {self.count} by price {self.price}"


class Printer(Equipment):
    printer_count = 0

    def __init__(self, name, model, price, count=1):
        super().__init__(name, model, price, count)
        self.data = f'{name}, {model}, {price}, {count}'
        self.printer_count += 1
        self.list_char = []


class Copier(Equipment):
    copier_count = 0

    def __init__(self, name, model, price, count=1):
        super().__init__(name, model, price, count)
        self.data = f'{name}, {model}, {price}, {count}'
        self.copier_count += 1
        self.list_char = []


class Scanner(Equipment):
    scanner_count = 0

    def __init__(self, name, model, price, count=1):
        super().__init__(name, model, price, count)
        self.data = f'{name}, {model}, {price}, {count}'
        self.scanner_count += 1
        self.list_char = []


s = Stock()

while True:
    print('Enter "exit" to exit the program or "back" to step back')
    answer = input('Which stock department do you want to go to\n'
                   '"department printer" = 1, "department scanner" = 2, "department copier" = 3 : ')
    if answer == 'exit':
        print('Goodbye')
        exit()
    elif answer == 'department printer' or 'printer' or '1':
        print(s.department_printer)
        add_or_with = input('Do you want to add or leave?\n'
                            'Enter "+" for add or "back" to leave the department: ')
        if add_or_with == 'back':
            continue
        if add_or_with == '+':
            name = input('Please enter "name": ')
            model = input('Please enter "model": ')
            price = int(input('Please enter "price": '))
            count = int(input('Please enter "count": '))
            printer = Printer(name, model, price, count)
            add_feat = input('You want to add features?\n'
                             'Enter "yes" or "no": ')
            if add_feat == 'no':
                s.department_printer.append(s.dict_data.fromkeys([printer.data]))
                print(s.department_printer)
            elif add_feat == 'yes':
                char = input('Enter feature: ')
                printer.list_char.append(char)
                if char == 'back':
                    break
                else:
                    printer.list_char.append(char)
                    s.department_printer.append(s.dict_data.fromkeys([printer.data], char))
    elif answer == 'department scanner' or 'scanner' or '2':
        print(s.department_scanner)
        add_or_with = input('Do you want to add or leave?\n'
                            'Enter "+" for add or "back" to leave the department: ')
        if add_or_with == 'back':
            continue
        if add_or_with == '+':
            name = input('Please enter "name": ')
            model = input('Please enter "model": ')
            price = int(input('Please enter "price": '))
            count = int(input('Please enter "count": '))
            scanner = Scanner(name, model, price, count)
            add_feat = input('You want to add features?\n'
                             'Enter "yes" or "no": ')
            if add_feat == 'no':
                s.department_scanner.append(s.dict_data.fromkeys([scanner.data]))
                print(s.department_scanner)
            elif add_feat == 'yes':
                char = input('Enter feature: ')
                scanner.list_char.append(char)
                if char == 'back':
                    break
                else:
                    scanner.list_char.append(char)
                    s.department_scanner.append(s.dict_data.fromkeys([scanner.data], char))

    elif answer == 'department copier' or 'copier' or '3':
        print(s.department_copier)
        add_or_with = input('Do you want to add or leave?\n'
                            'Enter "+" for add or "back" to leave the department: ')
        if add_or_with == 'back':
            continue
        if add_or_with == '+':
            name = input('Please enter "name": ')
            model = input('Please enter "model": ')
            price = int(input('Please enter "price": '))
            count = int(input('Please enter "count": '))
            copier = Copier(name, model, price, count)
            add_feat = input('You want to add features?\n'
                             'Enter "yes" or "no": ')
            if add_feat == 'no':
                s.department_copier.append(s.dict_data.fromkeys([copier.data]))
                print(s.department_copier)
            elif add_feat == 'yes':
                char = input('Enter feature: ')
                copier.list_char.append(char)
                if char == 'back':
                    break
                else:
                    copier.list_char.append(char)
                    s.department_copier.append(s.dict_data.fromkeys([copier.data], char))
