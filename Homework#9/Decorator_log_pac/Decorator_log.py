# # Соберите пакет с играми из тех файлов, что уже были созданы в рамках курса
# from functools import wraps
# from venv import logger
#
#
# # import logger
# # import logging
#
#
# def log_call(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         logger.info(f"Вызов функции {func.__name__} с аргументами {args} и {kwargs}")
#         return func(*args, **kwargs)
#
#     return wrapper
#
#
# @log_call
# def my_function(x, y):
#     return x + y
#
#
# my_function(3, 4)
# # В этом примере мы используем модуль logging для логирования вызовов функций. Мы создаем декоратор log_call, который принимает функцию в качестве аргумента и оборачивает ее в новую функцию-обертку. Внутри функции-обертки мы вызываем функцию, которую декорировали, с помощью wraps(). Затем мы логируем вызов функции с помощью метода info() модуля logging.
# #
# # После этого мы возвращаем новую функцию-обертку, которая просто вызывает декорированную функцию.
# #
# # Когда мы вызываем декорированную функцию my_function, она будет автоматически логироваться.
#
#
# import json
#
#
# def write_to_file(filename, data):
#     with open(filename, 'w') as file:
#         json.dump(data, file)
#
#
# @write_to_file
# def my_decorated_function():
#     # Здесь находится код вашей функции
#     pass
#
#
# @write_to_file
# def my_decorated_function():
#     data = {
#         'key1': 'value1',
#         'key2': 2,
#         'key3': 'string'
#     }
#     return data
