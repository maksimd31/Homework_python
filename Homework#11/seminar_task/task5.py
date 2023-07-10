# task 5-6
''
"""
📌 Дорабатываем класс прямоугольник из прошлого семинара.
📌 Добавьте возможность сложения и вычитания.
📌 При этом должен создаваться новый экземпляр прямоугольника.
📌 Складываем и вычитаем периметры, а не длинну и ширину.
📌 При вычитании не допускайте отрицательных значений.
"""

"""
Задание No6
📌 Доработайте прошлую задачу.
📌 Добавьте сравнение прямоугольников по площади
📌 Должны работать все шесть операций сравнения
          
"""


class Pectangle:
    def __init__(self, length, width=None):
        """
        Method init
        :param length: Длина
        :param width: Ширина
        """
        if width is None:
            self.length = self.width = length
            print('Это квадрат')
        else:
            self.length = length
            self.width = width

    def perimetr(self):
        """
        :return: возвращает периметр
        """
        return 2 * (self.length + self.width)

    def square(self):
        """
        :return: возвращает площадь
        """
        return self.length * self.width

    def __str__(self):
        """
        :return: возвращает print для пользователя
        """
        return f'List int {self.length = }\nList str {self.width = }'

    def __repr__(self):
        """
        :return: возвращает инфо для программиста
        """
        return f'{self.length = } {self.width = }'

    def __add__(self, other):
        """
        Переопределение сложение периметра
        :param other:
        :return:
        """
        p = self.perimetr() + other.perimetr()
        return Pectangle(p // 2 / 2)

    def __sub__(self, other):
        """
        Вычитание
        :param other:
        :return:
        """
        p = self.perimetr() - other.perimetr()
        return Pectangle(abs(p // 2 / 2))

    def __eq__(self, other):
        """
        Сравнение
        :param other:
        :return:
        """
        return self.square() == other.square()

    def __gt__(self, other):
        """
        Сравнение больше
        :param other:
        :return:
        """
        return self.square() > other.square()

    def __lt__(self, other):
        """
        Сравнение меньше
        :param other:
        :return:
        """
        return self.square() < other.square()

    def __ge__(self, other):
        """
        Сравнение больше или равно
        :param other:
        :return:
        """
        return self.square() >= other.square()

    def __le__(self, other):
        """
        Сравнение меньше или равно
        :param other:
        :return:
        """
        return self.square() <= other.square()
        # a = Pectangle(10)
        # b = Pectangle(10, 5)
        # print(a.perimetr(), a.square())
        # print(b.perimetr(), b.square())


if __name__ == '__main__':
    # Создание экземпляра класса
    rec_1 = Pectangle(5, 5)
    rec_2 = Pectangle(7, 7)

    # Сложение
    print(f'{rec_1.perimetr() = } {rec_2.perimetr() =}')
    rec_3 = rec_1 + rec_2

    # Вычитание
    rec_4 = rec_1 - rec_2
    print(f'{rec_3.length = } {rec_4.width =}')

    # Сравнение
    print(rec_1 == rec_2)

    # Сравнение меньше или равно
    print(rec_3 <= rec_4)
