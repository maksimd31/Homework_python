# Добавьте в пакет, созданный на семинаре шахматный модуль.
# Внутри него напишите код, решающий задачу о 8 ферзях. Известно,
# что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
import random

__add__ = ['queen_8']  # не работает


# Это очень сложная задача


def check_queens(queens):
    """Реализация по заданию"""
    for i in range(len(queens)):
        for j in range(i + 1, len(queens)):
            if queens[i][0] == queens[j][0] or queens[i][1] == queens[j][1] or \
                    abs(queens[i][0] - queens[j][0]) == abs(queens[i][1] - queens[j][1]):  # abs меняет полюс на минус
                return False
    return True


# Напишите функцию в шахматный модуль.
# Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
# Проверяйте различные случайные варианты и выведите 4 успешных расстановки.
# *Выведите все успешные варианты расстановок

def generate_random_queens(arg_pole):
    """Рандомное поле, где arg_pole размер поля, если всегда использовать поле 8х8 очень долго ищет - грузит"""
    queens = []
    for i in range(arg_pole):
        queen = (random.randint(1, arg_pole), random.randint(1, arg_pole))
        queens.append(queen)
    return queens


def queen_8(arg_pole):
    successful_queens = []
    while len(successful_queens) < 1:
        queens = generate_random_queens(arg_pole)
        if check_queens(queens):
            successful_queens.append(queens)
            return f"Ферзи не бьют друг друга и стоят на координат : {queens}"


if __name__ == '__main__':
    print(queen_8(6))  # а вот на поле 6х6 находит достаточно быстро
