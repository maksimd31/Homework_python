"""
Напишите функцию, которая ищет json файлы в указанной директории и сохраняет их содержимое в виде одноимённых pickle файлов.
"""

import os
import json
import pickle

__add__ = ['process_json_files']


def process_json_files(directory):
    """
    Ищет json файлы в указанной директории и сохраняет их содержимое в виде одноименных pickle файлов
    """
    for file in os.listdir(directory):
        if file.endswith('.json'):
            with open(os.path.join(directory, file)) as f:
                data = json.load(f)
                with open(os.path.join(directory, os.path.splitext(file)[0] + '.pickle'), 'wb') as p:
                    pickle.dump(data, p)


if __name__ == '__main__':
    process_json_files('.')
