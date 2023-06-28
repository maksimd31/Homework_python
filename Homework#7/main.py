# Решение д/з
# Тут я хотел показать, что сделал модуль, а не библиотеку
# from Hm7_package.task1 import batch_rename_files
# batch_rename_files('.', 'test2', 'mb', 'txt')

import Hm7_package

Hm7_package.batch_rename_files('.', 'test2', 'mb', 'txt')

# 3. Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.
import Seminar_project

Seminar_project.task_1(5, './numbers_main.txt')
Seminar_project.task_2(10, './names_main.txt')
Seminar_project.task_3('./names_main.txt', './numbers_main.txt')
Seminar_project.task_4('txt', 5)
