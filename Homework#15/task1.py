# Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК. Соберите информацию о содержимом в виде объектов namedtuple.
# Каждый объект хранит:
# * имя файла без расширения или название каталога,
# * расширение, если это файл,
# * флаг каталога,
# * название родительского каталога.
# В процессе сбора сохраните данные в текстовый файл используя логирование.

import os
import logging
import argparse
from collections import namedtuple

logging.basicConfig(filename='log.txt', filemode='w', format='%(asctime)s - %(message)s', level=logging.INFO)


def get_dir_info(path):
    for item in os.scandir(path):
        if item.is_dir():
            flag = 'Directory'
            ext = ''
        elif item.is_file():
            flag = 'File'
            ext = os.path.splitext(item.name)[1]
        else:
            flag = ''
            ext = ''
        parent = os.path.basename(os.path.dirname(item))
        name = os.path.splitext(item.name)[0]
        dir_info = namedtuple('dir_info', ['name', 'ext', 'flag', 'parent'])
        info = dir_info(name, ext, flag, parent)
        logging.info(info)
        print(info)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="path to directory")
    args = parser.parse_args()
    path = args.path
    get_dir_info(path)
