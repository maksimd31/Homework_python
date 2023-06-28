# Задание №4
# ✔ Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# ✔ расширение
# ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
# ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
# ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
# ✔ количество файлов, по умолчанию 42
# ✔ Имя файла и его размер должны быть в рамках переданного диапазона.

from random import choice, choices, randint

LETTERS = 'qwertyuiopasdfghjklzxcvbnm'

__all__ = ['task_4']


def task_4(ext, min_length=6, max_length=30, min_byte=256, max_byte=4096, count_files=42):
    '''
    Генератор файлов
    :param ext:
    :param min_length:
    :param max_length:
    :param min_byte:
    :param max_byte:
    :param count_files:
    :return:
    '''
    for _ in range(count_files):
        # собираем имя файла. choices - случайный выбор k элементов из итерируемого объекта
        filename = '7_4/' + ''.join(choices(LETTERS, k=randint(min_length, max_length))) + '.' + ext
        content = ''
        # формируем содержимое файла для последующей записи в файл (чтобы не дёргать файл по каждому байту)
        for _ in range(randint(min_byte, max_byte)):
            content += choice(LETTERS)
        # content.append(bytes(choice(LETTERS).encode('utf-8')))
        with open(filename, 'wb') as f:
            # запись в файл строки, преобразованной в bytes
            f.write(bytes(content, 'utf-8'))


if __name__ == '__main__':
    ext = 'txt'
    task_4(ext, count_files=5)