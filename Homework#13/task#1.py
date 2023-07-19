"""
Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях.
Напишите к ним классы исключения с выводом подробной информации. Поднимайте исключения внутри основного кода.
Например нельзя создавать прямоугольник со сторонами отрицательной длины.
"""
import csv


class BadName(Exception):
    def __init__(self, name):
        super().__init__(f"Имя {name} некорректно, оно должно содержать только буквы")


class BadMark(Exception):
    def __init__(self, mark):
        super().__init__(f"Оценка {mark} недопустима, оценка должна быть целым числом от 2 до 5")


class BadTestResult(Exception):
    def __init__(self, result):
        super().__init__(f"Результат {result} недопустим, результат должен быть целым числом от 0 до 100")


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
                raise BadName(value)
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
            raise BadMark(mark)
        self.subjects[subject]['marks'].append(mark)

    def add_test_result(self, subject, result):
        if subject not in self.subjects:
            raise ValueError('Недопустимая тема')
        if result < 0 or result > 100:
            raise BadTestResult(result)
        self.subjects[subject]['tests'].append(result)

    def get_average_test_result(self, subject):
        if subject not in self.subjects:
            raise ValueError('Недопустимая тема')
        test_results = self.subjects[subject]['tests']
        if not test_results:
            return None
        return sum(test_results) / len(test_results)

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

