# Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class ComplexNumber:
    def __init__(self, a, b, z = 'j'):
        self.a = a
        self.b = b
        self.z = z

    def __add__(self, other):
        r1 = self.a + other.a
        r2 = self.b + other.b
        return f'Sum: {r1} {"+" if r2 > 0 else "-"} {abs(r2)} * {self.z}'

    def __mul__(self, other):
        r1 = (self.a * other.a) - (self.b * other.b)
        r2 = (self.b * other.a) + (self.a * other.b)
        return f'Mul: {r1} {"+" if r2 > 0 else "-"} {abs(r2)} * {self.z}'

    def __str__(self):
        return f'result operation:'


z_1 = ComplexNumber(2, 6)
z_2 = ComplexNumber(2, -12)
print(z_1)
print(z_1 + z_2)
print(z_1 * z_2)
