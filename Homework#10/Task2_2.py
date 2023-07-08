import os
import json
import csv
import pickle


class File:  # родительский класс
    def __init__(self, path, name, size, parent):
        self.path = path
        self.name = name
        self.size = size
        self.parent = parent

    def get_file_size(self):
        """Возвращает размер файла в байтах"""
        return os.path.getsize(self.path)


class Directory(File):  # Наследуемся от класса File
    def __init__(self, path, name, size, parent):
        super().__init__(path, name, size, parent)
        self.type = 'directory'
        self.children = []

    def get_directory_size(self):
        """Возвращает размер каталога, включая все вложенные файлы и каталоги."""
        total_size = 0
        for child in self.children:
            if isinstance(child, Directory):
                total_size += child.get_directory_size()
            else:
                total_size += child.get_file_size()
        return total_size

    def add_child(self, child):
        """Добавляет дочерний файл в каталог"""
        self.children.append(child)


class Processor:
    def __init__(self, dir_path):
        self.dir_path = dir_path

    def get_files_and_directories(self):
        """Возвращает список словарей, каждый из которых содержит информацию о файле или каталоге, включая размер
         (для файлов) и размер всех вложенных файлов и каталогов (для каталогов)."""
        result = []
        for item in os.listdir(self.dir_path):
            item_path = os.path.join(self.dir_path, item)
            if os.path.isfile(item_path):
                file = File(item_path, item, 0, self.dir_path)
                file.size = file.get_file_size()
                result.append(file)
            elif os.path.isdir(item_path):
                directory = Directory(item_path, item, 0, self.dir_path)
                directory.size = directory.get_directory_size()
                directory.children = Processor(item_path).get_files_and_directories()
                result.append(directory)
        return result

    @staticmethod
    def save_to_json(data, filename):
        """Сохраняет файл в json"""
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

    @staticmethod
    def save_to_csv(data, filename):
        """Сохраняет файл в csv"""
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['path', 'name', 'type', 'size', 'parent'])
            for item in data:
                writer.writerow([item.path, item.name, item.type, item.size, item.parent])

    @staticmethod
    def save_to_pickle(data, filename):
        """Сохраняет файл в pickle"""
        with open(filename, 'wb') as f:
            pickle.dump(data, f)

    def process_directory(self):
        """Обрабатывает каталог и сохраняет результаты в файлы json, csv и pickle"""
        data = self.get_files_and_directories()
        self.save_to_json(data, 'result.json')
        self.save_to_csv(data, 'result.csv')
        self.save_to_pickle(data, 'result.pickle')


if __name__ == '__main__':
    processor = Processor('../..')
    processor.process_directory()
else:
    __add_ = ['Processor']
