"""
Создайте класс прямоугольник.
📌 Класс должен принимать длину и ширину при создании
экземпляра.
📌 У класса должно быть два метода, возвращающие периметр и площадь.
📌 Если при создании экземпляра передаётся только одна сторона, считаем что у нас квадрат.

"""


class Pectangle:
    def __init__(self, length, width=None):
        if width is None:
            self.length = self.width = length
            print('Это квадрат')
        else:
            self.length = length
            self.width = width

    def perimetr(self):
        return 2 * (self.length + self.width)

    def square(self):
        return self.length * self.width

    def print_p(self):
        return print(self)

    def __add__(self, other):
        p = self.perimetr() + other.perimetr()
        return Pectangle(p // 2 / 2)

    def __sub__(self, other):
        p = self.perimetr() - other.perimetr()
        return Pectangle(abs(p // 2 / 2))

    def __eq__(self, other):
        return self.square() == other.square()

    def __gt__(self, other):
        return self.square() > other.square()

    def __lt__(self, other):
        return self.square() < other.square()

    def __ge__(self, other):
        return self.square() >= other.square()

    def __le__(self, other):
        return self.square() <= other.square()
        # a = Pectangle(10)
        # b = Pectangle(10, 5)
        # print(a.perimetr(), a.square())
        # print(b.perimetr(), b.square())


rec_1 = Pectangle(5, 5)
rec_2 = Pectangle(7, 7)
print(f'{rec_1.perimetr() = } {rec_2.perimetr() =}')
rec_3 = rec_1 + rec_2
rec_4 = rec_1 - rec_2
print(f'{rec_3.length = } {rec_4.width =}')

print(rec_1 == rec_2)
print(rec_3 <= rec_4)
