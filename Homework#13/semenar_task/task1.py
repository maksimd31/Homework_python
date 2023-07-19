#
# # task1
# ''
# """
# 📌 Создайте функцию, которая запрашивает числовые данные от пользователя до тех пор,
#  пока он не введёт целое или вещественное число.
# 📌 Обрабатывайте не числовые данные как исключения.
# """
#
#
# # def get():
# #     while True:
# #         num = (input('Введите: '))
# #         if not isinstance(num, (int, float)):
# #             raise ValueError('ERROR Вводи int and float')
# #         break
# #     return num
# #
# #
# # def get2():
# #     while True:
# #         num = input('Введите: ')
# #         if not isinstance(num, (int | float)):
# #             raise ValueError('ERROR Вводи int and float')
# #         else:
# #             break
# def get_number():
#     """
#
#     >>> get_number(2)
#     2
#     >>> get_number(2.3)
#     2.3
#     >>> get_number('eeeeee')
#
#     """
#     while True:
#         try:
#             arg = float(input("Введите число: "))
#             return arg
#         except ValueError:
#             print("Ошибка: введите целое или вещественное число.")
#
#
# # number = get_number()
# # print("Вы ввели число:", number)
#
# if __name__ == '__main__':
#     import doctest
#     doctest.testmod()
#     # get_number()
#     # print(get())

import unittest
import doctest


def get_number():
    while True:
        try:
            arg = float(input("Введите число: "))
            return arg
        except ValueError:
            print("Ошибка: введите целое или вещественное число.")


class TestGetNumber(unittest.TestCase):
    def test_integer(self):
        self.assertEqual(get_number(), 42)

    def test_float(self):
        self.assertAlmostEqual(get_number(), 3.14159, delta=0.00001)

    def test_negative(self):
        self.assertEqual(get_number(), -7)

    def test_zero(self):
        self.assertEqual(get_number(), 0)


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite())
    return tests


if __name__ == '__main__':
    unittest.main()
