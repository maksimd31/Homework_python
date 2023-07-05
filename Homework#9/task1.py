"""Урок 9. Декораторы
Напишите следующие функции:

1. Нахождение корней квадратного уравнения

2. Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.

3. Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.

4. Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл."""
import csv
import json
import math
from functools import wraps
from pprint import pprint
from random import randint


def square_roots(a_arg, b_arg, c_arg):
    """Функция 1. Нахождение корней квадратного уравнения"""
    d_arg = b_arg ** 2 - 4 * a_arg * c_arg
    if d_arg > 0:
        x1 = (-b_arg + d_arg ** 0.5) / (2 * a_arg)
        x2 = (-b_arg - d_arg ** 0.5) / (2 * a_arg)
        return x1, x2
        # return f'x1 = {x1}', f'x1 = {x2}'
    elif d_arg == 0:
        x1 = -b_arg / (2 * a_arg)
        return x1
        # return f'x = {-b_arg / (2 * a_arg)}'
    else:
        return None


def square_roots_math(a_arg, b_arg, c_arg):
    d = b_arg ** 2 - 4 * a_arg * c_arg
    if d < 0:
        return None, None
    x1 = (-b_arg + math.sqrt(d)) / (2 * a_arg)
    x2 = (-b_arg - math.sqrt(d)) / (2 * a_arg)
    return x1, x2


# x - эксклюзивное создание, бросается исключение FileExistsError, если файл уже существует.
def csv_generator(filename, rows):
    """Функция Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк."""
    with open(filename, mode='w+', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        for i in range(rows):
            writer.writerow([randint(1, 100), randint(1, 100), randint(1, 100)])


def decorator_csv(func):
    """3. Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла."""

    @wraps(func)
    def wrapper(filename):
        with open(filename, newline='', encoding='utf-8') as csv_file:
            listt = []
            dictt = {}
            reader = csv.reader(csv_file)
            for i in reader:
                a_arg, b_arg, c_arg = map(int, i)
                x1, x2 = func(a_arg, b_arg, c_arg)
                # тут что-то я долго не мог сообразить как закинуть все результаты, а не по последнему,
                # так и не понял как время поджимает, сдаю как есть )) Смог через лист
                dct = {'a': a_arg, 'b': b_arg, 'c': c_arg, 'x1': x1, 'x2': x2}
                dictt.update(dct)
                listt.append(dct)
                pprint(f'a = : {a_arg}, b = : {b_arg}, c = : {c_arg}, x1 = : {x1}, x2 = : {x2}')
        # return f'a = : {a_arg}, b = : {b_arg}, c = : {c_arg}, x1 = : {x1}, x2 = : {x2}'
        # write_to_json('data2.json', dct)
        # return f'a = : {a_arg}, b = : {b_arg}, c = : {c_arg}, x1 = : {x1}, x2 = : {x2}'
        return listt, a_arg, b_arg, c_arg, x1, x2

    return wrapper


def json_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        with open('log2.json', mode='a', newline='', encoding='utf-8') as json_f:
            # data = {'res': res}
            data = {
                'F_name': func.__name__,
                'args': args,
                # 'kwargs': kwargs,
                'result': res
            }
            json_f.write('\n')
            json.dump(data, json_f, indent=2, sort_keys=True)

    return wrapper


# @decorator_csv
# def decorator_csv_input(a, b, c):
#     return square_roots(a, b, c)
@json_decorator
@decorator_csv
def decorator_csv_input_math(a, b, c):
    return square_roots_math(a, b, c)


@json_decorator
def decorator_csv_input_log(a, b, c):
    return square_roots_math(a, b, c)


if __name__ == '__main__':
    # """Функция 1. Нахождение корней квадратного уравнения"""
    # a, b, c = map(int, input().split())
    # square_roots(a, b, c)
    # """Функция Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк."""
    csv_generator('data.csv', 500)
    decorator_csv_input_math('data.csv')

    # decorator_csv_input_log(1, 2, 1)

    # decorator_csv_input_log(1, 2, 1)
    # decorator_csv_input('data.csv')

# тут я что-то не сообразил как записать все в логированние все данные, записывает по последнему
