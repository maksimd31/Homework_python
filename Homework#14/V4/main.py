import json


# Создайте класс с базовым исключением и дочерние классыисключения:
# ○ ошибка уровня,
# ○ ошибка доступа.

class MyException(Exception):
    pass


class ExceptionLevel(MyException):
    pass


class ExceptionAccess(MyException):
    pass


# Вспомните задачу из семинара 8 про сериализацию данных, где в бесконечном цикле запрашивали имя, личный идентификатор и уровень доступа (от 1 до 7).
# Напишите класс пользователя, который хранит эти данные в свойствах экземпляра.
# Реализуйте магический метод проверки на равенство пользователей

class User:
    def __init__(self, id_, name, access=None):
        self.id_ = id_
        self.name = name
        self.access = access

    def __eq__(self, other):
        return self.id_ == other.id_ and self.name == other.name

    def __str__(self):
        return f'{self.access} {self.id_} {self.name}'


class Project:
    file_name = 'users.json'

    def __init__(self, users: list[User]):
        self.users = users
        self.admin: User = None

    @classmethod
    def from_json_file(cls, json_file):
        with open(json_file, 'r', encoding='utf-8') as f:
            dct = json.load(f)
        my_list = []
        for access, item in dct.items():
            for id_, name in item.items():
                my_list.append(User(id_, name, access))
        return Project(my_list)

    def enter(self, name, id_):
        user_1 = User(id_, name)
        for user in self.users:
            if user_1 == user:
                self.admin = user
                break
        else:
            raise ExceptionAccess

    def add_user(self, name, id_, access):
        if self.admin.access > access:
            raise ExceptionLevel
        self.users.append(User(id_, name, access))

    def remove_user(self, id_):
        for user in self.users:
            if user.id_ == id_:
                self.users.remove(user)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        my_dict = {str(i): {} for i in range(1, 7 + 1)}
        for user in self.users:
            my_dict[user.access] = {str(user.id_): str(user.name)}
        with open(self.file_name, 'w', encoding='utf-8') as f:
            json.dump(my_dict, f)


if __name__ == '__main__':
    project = Project.from_json_file('file.json')
    print(project.users)
