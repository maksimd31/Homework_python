# 3. Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
# Результаты
#    обхода сохраните в файлы json, csv и pickle. Для дочерних объектов указывайте родительскую директорию. Для каждого
#    объекта укажите файл это или директория. Для файлов сохраните его размер в байтах, а для директорий размер
#    файлов в ней с учётом всех вложенных файлов и директорий.


# Очень не простое задание, еле справился.
# Так ежим по темам я не успеваю все запоминать, и очень тяжело идет процесс. Темы сложные.
# У нас до этого пол года был курс java и все что с ним связанно, а курс питона был пол года назад.
# Поэтому мне и многим довольно сложно не запутаться, и долго соображать над задачками! Так как не все пришли с нуля))

import os
import json
import csv
import pickle


def get_file_size(file_path):
    """Возвращает размер файла в байтах"""
    return os.path.getsize(file_path)


def get_directory_size(dir_path):
    """Возвращает размер директории, включая все вложенные файлы и директории"""
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(dir_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += get_file_size(fp)
    return total_size


def get_files_and_directories(dir_path):
    """Возвращает список словарей, каждый из которых содержит информацию о файле или директории,
    включая размер (для файлов) и размер всех вложенных файлов и директорий (для директорий)"""
    result = []
    for item in os.listdir(dir_path):
        item_path = os.path.join(dir_path, item)
        if os.path.isfile(item_path):
            result.append({
                'path': item_path,
                'name': item,
                'type': 'file',
                'size': get_file_size(item_path),
                'parent': dir_path
            })
        elif os.path.isdir(item_path):
            result.append({
                'path': item_path,
                'name': item,
                'type': 'directory',
                'size': get_directory_size(item_path),
                'parent': dir_path
            })
            result.extend(get_files_and_directories(item_path))
    return result


def save_to_json(data, filename):
    """Сохраняет данные в файл json"""
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)


def save_to_csv(data, filename):
    """Сохраняет данные в файл csv"""
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['path', 'name', 'type', 'size', 'parent'])
        for item in data:
            writer.writerow([item['path'], item['name'], item['type'], item['size'], item['parent']])


def save_to_pickle(data, filename):
    """Сохраняет данные в файл pickle"""
    with open(filename, 'wb') as f:
        pickle.dump(data, f)


def process_directory(dir_path):
    """Обрабатывает директорию и сохраняет результаты в файлы json, csv и pickle"""
    data = get_files_and_directories(dir_path)
    save_to_json(data, 'result.json')
    save_to_csv(data, 'result.csv')
    save_to_pickle(data, 'result.pickle')


if __name__ == '__main__':
    process_directory('../..')
else:
    __add_ = ['process_directory']
