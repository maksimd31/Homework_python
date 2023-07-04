"""
Создайте функцию-замыкание, которая запрашивает два целых числа:
○ от 1 до 100 для загадывания,
○ от 1 до 10 для количества попыток
📌 Функция возвращает функцию, которая через консоль
просит угадать загаданное число за указанное число попыток.
"""
from typing import Callable

__all__ = ['binary_search_game']


def binary_search_game(num: int, count: int) -> Callable[[], None]:
    def wrapper():
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

    return wrapper


if __name__ == '__main__':

    code = binary_search_game(10, 5)
    code()
