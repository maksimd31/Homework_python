# ✔ Напишите программу, которая принимает две строки вида “a/b” — дробь с числителем и знаменателем.
# Программа должна возвращать сумму
# и *произведение дробей. Для проверки своего
# кода используйте модуль fractions.

#
# a_inp = input('Введите первую дробь: ')
# b_inp = input('Введите вторую дробь: ')

a_inp = '1 / 2'
b_inp = '4 / 4'


def calculate_fraction(arg1: str, arg2: str):
    a, b = arg1.split('/')
    c, d = arg2.split('/')
    a, b, c, d = int(a), int(b), int(c), int(d)
    sum_frac = str(a * d + b * c) + '/' + str(b * d)
    mul_frac = str(a * c) + '/' + str(b * d)
    return f"Сумма дробей: {sum_frac} \nПроизведение дробей: {mul_frac}"


print(calculate_fraction(a_inp, b_inp))

# готово
