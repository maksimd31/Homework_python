#
# ✔ Напишите программу, которая принимает две строки вида “a/b” — дробь с числителем и знаменателем.
# Программа должна возвращать сумму
# и *произведение дробей. Для проверки своего
# кода используйте модуль fractions.

from fractions import Fraction

a = input('Введите первую дробь: ')
b = input('Введите вторую дробь: ')


def calculate_fraction(arg1: str, arg2: str):
    fraction1 = Fraction(arg1)
    fraction2 = Fraction(arg2)
    sum_fractions = fraction1 + fraction2
    product_fractions = fraction1 * fraction2
    return f"Сумма дробей: {sum_fractions} \nПроизведение дробей: {product_fractions}"


print(calculate_fraction(a, b))
