# На семинаре 13 был создан проект по работе с пользователями (имя, id, уровень).
# Напишите 3-7 тестов pytest для данного проекта.
# Используйте фикстуры.
# Все в одном месте
import json
import pytest


class User:
    def __init__(self, name, id, access_level):
        self.name = name
        self.id = id
        self.access_level = access_level

    def to_dict(self):
        return {"name": self.name, "id": self.id, "access_level": self.access_level}

class Project:
    def __init__(self):
        self.users = set()

    def load_data(self, file_path):
        with open(file_path) as f:
            data = json.load(f)
            for user_data in data:
                user = User(user_data["name"], user_data["id"], user_data["access_level"])
                self.users.add(user)

    def login(self, name, id):
        user = User(name, id, 0)
        if user in self.users:
            return user.access_level
        else:
            raise Exception("Access Denied")

    def add_user(self, user):
        if user.access_level < self.login(user.name, user.id):
            raise Exception("Access Denied")
        self.users.add(user)


def serialize_data():
    while True:
        name = input("Введите имя: ")
        id = input("Введите личный идентификатор: ")
        access_level = int(input("Введите уровень доступа (от 1 до 7): "))
        user = User(name, id, access_level)
        with open("data.json", "a") as f:
            json.dump(user.to_dict(), f)
        if input("Продолжить? (y/n): ").lower() != "y":
            break


def test_login(project):
    assert project.login("John", "1234") == 5
    with pytest.raises(Exception):
        project.login("Bob", "5678")


def test_add_user(project):
    user = User("Sarah", "9012", 3)
    with pytest.raises(Exception):
        project.add_user(user)
    user = User("Chris", "3456", 6)
    project.add_user(user)
    assert user in project.users


def test_load_data():
    project = Project()
    project.load_data("test_data.json")
    assert len(project.users) == 2
    assert User("John", "1234", 5) in project.users
    assert User("Jane", "5678", 3) in project.users


@pytest.fixture
def project():
    project = Project()
    project.load_data("test_data.json")
    return project
