# Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class ComplexNumber:
    def __init__(self, a):
        self.a = a

    def __add__(self, other):
        return f'Sum: {self.a + other.a}'

    def __mul__(self, other):
        return f'Mul: {self.a * other.a}'

    def __str__(self):
        return f'result operation:'


z_1 = ComplexNumber(2+2j)
z_2 = ComplexNumber(3+2j)
print(z_1)
print(z_1 + z_2)
print(z_1 * z_2)
