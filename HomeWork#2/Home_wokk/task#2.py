#
# ✔ Напишите программу, которая принимает две строки вида “a/b” — дробь с числителем и знаменателем.
# Программа должна возвращать сумму
# и *произведение дробей. Для проверки своего
# кода используйте модуль fractions.

# Напишите программу, которая принимает две строки вида
# “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль
# fractions.


from fractions import Fraction

# Ввод дробей
fraction1 = input("Введите первую дробь: ")
per = list(fraction1)
fraction_one = per[0]
fraction_two = per[-1]

# fraction2 = input("Введите вторую дробь: ")

# a, b = map(int, input('Введите дроби через пробел').split())


def convert_fraction(fraction_one_arg, fraction_two_arg):
    one = Fraction(fraction_one_arg)
    tow = Fraction(fraction_two_arg)
    sum_fraction = one + tow
    multiply_fraction = one * tow
    return f'Сумма дробей: {sum_fraction}\n Произведение дробей: {multiply_fraction}'


print(convert_fraction(int(fraction_one),int(fraction_two)))
