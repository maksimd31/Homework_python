"""
 Задание No2
📌 Дорабатываем задачу 1.
📌 Превратите внешнюю функцию в декоратор.
📌 Он должен проверять входят ли переданные в функцию- угадайку числа в диапазоны [1, 100] и [1, 10].
📌 Если не входят, вызывать функцию со случайными числами из диапазонов.

"""

from typing import Callable
from random import randint
from task4 import counter_wrap
from jas import to_json_wrapper

__all__ = ['binary_search_game_wrap']


def binary_search_game_wrap(func) -> Callable[[], None]:
    def wrapper(num: int, count: int, *args, **kwargs):
        if 1 > num or num > 100:
            num = randint(1, 100)
        if 1 > count or num > 10:
            count = randint(1, 10)
        result = func(num, count, *args, **kwargs)
        return result

    return wrapper


@counter_wrap(3)
@binary_search_game_wrap
@to_json_wrapper
def game(num: int, count: int):
    for i in range(1, count + 1):
        print(f"Попытка номер {i} ")
        user_num = int(input("Введите число от 1 до 100: \n >>> "))
        if user_num == num:
            print("Угадал!!!")
            break
        elif user_num < num:
            print("Ваше число меньше")
        else:
            print("Ваше число больше")


if __name__ == '__main__':
    game(101, -15)
