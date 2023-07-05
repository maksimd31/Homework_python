# Дорабатываем функции из предыдущих задач.

# * Генерируйте файлы в указанную директорию — отдельный параметр функции.
#
# * Отсутствие/наличие директории не должно вызывать ошибок в работе функции (добавьте проверки).
#
# * Существующие файлы не должны удаляться/изменяться в случае совпадения имён.
# Напишите функцию группового переименования файлов. Она должна:
# * принимать в качестве аргумента желаемое конечное имя файлов.
#
# * При переименовании в конце имени добавляется порядковый номер.
#
# * принимать в качестве аргумента расширение исходного файла.
# Переименование должно работать только для этих файлов внутри каталога.
#
# * принимать в качестве аргумента расширение конечного файла.
# Шаблон переименованного файла: <original_name>_<new_name>_<position>.<new_extention>
# 3. Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.

import os
import webbrowser

__all__ = ["batch_rename_files"]  # Работает


def batch_rename_files(dir_path, new_name, old_ext, new_ext):
    """
    Параметры
    :param dir_path : Путь к каталогу (str)
    :param new_name : Новое имя (str)
    :param old_ext : Расширение файлов, которые будут переименованы (str)
    :param new_ext : Новое расширение (str)
    """
    counter = 1
    for file in os.listdir(dir_path):
        if file.endswith(old_ext):
            # Получить старое имя файла без расширения
            old_name = os.path.splitext(file)[0]
            # Создаем новое имя файла со счетчиком, новым именем и новым расширением
            new_file_name = f"{old_name}_{new_name}_{counter}.{new_ext}"
            # Если новое имя файла уже существует, увеличьте счетчик
            while os.path.exists(os.path.join(dir_path, new_file_name)):
                counter += 1
                new_file_name = f"{old_name}_{new_name}_{counter}.{new_ext}"
                # Переименуйте файл
            os.rename(os.path.join(dir_path, file), os.path.join(dir_path, new_file_name))
            counter += 1


def zac():
    link = "https://www.meme-arsenal.com/assets/img/not-found.jpg"
    webbrowser.open(link)


def main():
    batch_rename_files('..', 'test2', 'md', 'txt')


if __name__ == '__main__':
    main()

# else: # Этим исключением я хотел заблокировать использования модуля в роле библиотеки,
# если вернуть это условие то вылезет прикольная картина.
# Выдаст ошибка в консоле что это не библиотека
# zac()
# raise SystemExit('Это не библиотека')
