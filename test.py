class Num1:
    def __init__(self, a):
        self.a = a

    def draw(self):
        print(f'Num1 {self.a}')

class Num2:
    def __init__(self, b):
        self.b = b

    def drw(self):
        print(f'Num2 {self.b}')

class Num3(Num1, Num2):
    def __init__(self, a, b):
        super().__init__(a, b)

    def draw(self):
        print(f'Pencil {self.a}, {self.b}')

s = Num1(1)
s.draw()

pan = Num2(2)
pan.drw()

p = Num3()
p.draw()
