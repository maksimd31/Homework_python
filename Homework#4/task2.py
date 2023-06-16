# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента. Если ключ не хешируем,
# используйте его строковое представление.

import hashlib


# items = {"палатка": 15, "нож": 0.6, "стол": 10, "стул": 5, "спальный мешок": 1.5, "Топор": 2, "продукты": 2}


# def tt(arg):  # возвращает ключи
#     return arg.keys()
#
#
# key = tt(items)
# print(key)
#

# def task_2(**kwargs):
#     for key, value in kwargs.items():
#         return f' ключ {key} значение {value}'
#

def task_2_2(**kwargs):
    result = {}
    for key, value in kwargs.items():
        if not hash(key):  # не знаю правильный ли подход
            key = str(key)
        result[key] = value
    return result


print(task_2_2(key=1, valie='hhghjj'))
