# Решение д/з
# Тут я хотел показать, что сделал модуль, а не библиотеку
from Hm7_package.task1 import batch_rename_files
batch_rename_files('.', 'test2', 'mb', 'txt')

# 3. Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.
from Seminar_project.sem_task1 import task_1
from Seminar_project.sem_task2 import task_2
from Seminar_project.sem_task3 import task_3
from Seminar_project.sem_task4 import task_4

task_1(5, './numbers_main.txt')
task_2(10, './names_main.txt')
task_3('./names_main.txt', './numbers_main.txt')
task_4('txt', 5)
