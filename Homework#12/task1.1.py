import csv

"""
Создайте класс студента. Используя дескрипторы проверяйте ФИО на первую заглавную букву
 и наличие только букв. Названия предметов должны загружаться из файла CSV
 при создании экземпляра. Другие предметы в экземпляре недопустимы.
 Для каждого предмета можно хранить оценки (от 2 до 5)
 и результаты тестов (от 0 до 100). Также экземпляр должен сообщать средний балл
 по тестам для каждого предмета и по оценкам всех предметов вместе взятых.
"""


class Student:
    class Name:
        def __init__(self, value):
            self.value = value.capitalize()

        def __get__(self, obj, objtype):
            return self.value

        def __set__(self, obj, value):
            if not isinstance(value, str):
                raise TypeError('Имя должно быть строкой')
            if not value.isalpha():
                raise ValueError('Имя должно содержать только буквы')
            self.value = value.capitalize()

    def __init__(self, name, surname, patronymic, subjects_csv):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.subjects = {}

        with open(subjects_csv, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=';', quotechar='|')
            for row in reader:
                self.subjects[row[0]] = {'marks': [], 'tests': []}

    name = Name('')
    surname = Name('')
    patronymic = Name('')

    def add_mark(self, subject, mark):
        if subject not in self.subjects:
            raise ValueError('Недопустимая тема')
        if mark < 2 or mark > 5:
            raise ValueError('Недопустимая оценка')
        self.subjects[subject]['marks'].append(mark)

    def add_test_result(self, subject, result):
        if subject not in self.subjects:
            raise ValueError('Недопустимая тема')
        if result < 0 or result > 100:
            raise ValueError('Неверный результат теста')
        self.subjects[subject]['tests'].append(result)

    def get_average_test_result(self, subject):
        if subject not in self.subjects:
            raise ValueError('Недопустимая тема')
        results = self.subjects[subject]['tests']
        if len(results) == 0:
            return None
        return sum(results) / len(results)

    def get_average_mark(self, subject):
        if subject not in self.subjects:
            raise ValueError('Недопустимая тема')
        marks = self.subjects[subject]['marks']
        if len(marks) == 0:
            return None
        return sum(marks) / len(marks)

    def get_total_average_mark(self):
        marks = []
        for subject_marks in self.subjects.values():
            marks += subject_marks['marks']
        if len(marks) == 0:
            return None
        return sum(marks) / len(marks)


if __name__ == '__main__':
    student = Student("Иван", "Иванов", "Иванович", "subjects.csv")
    student.add_mark("Математика", 4)
    student.add_mark("Математика", 5)
    student.add_test_result("Математика", 78)
    student.add_test_result("Математика", 89)

    print(student.get_average_test_result("Математика"))
    print(student.get_average_mark("Математика"))
    print(student.get_total_average_mark())
