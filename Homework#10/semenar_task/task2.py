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


a = Pectangle(10)
b = Pectangle(10, 5)
print(a.perimetr(), a.square())
print(b.perimetr(), b.square())
