# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
import os

from pathlib import Path

fpath = Path('task2.py').absolute()


# print(fpath)


def get_file_info(path: str) -> tuple:  # очень прикольная констркуция функции когда сразу можно прописывать return
    """
    Функция для получения пути, имени и расширения файла
    """
    file_path, file_ext = os.path.splitext(path)
    dir_path, file_name = os.path.split(file_path)

    return dir_path, file_name, file_ext


print(get_file_info(str(fpath)))
