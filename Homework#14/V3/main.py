import json


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
            raise Exception("Доступ запрещен")

    def add_user(self, user):
        if user.access_level < self.login(user.name, user.id):
            raise Exception("Доступ запрещен")
        self.users.add(user)


def main():
    while True:
        name = input("Введите ваше имя: ")
        id = input("Введите ваш ID: ")
        access_level = input("Введите свой уровень доступа: ")
        user = User(name, id, access_level)
        with open("data.json", "a") as f:
            json.dump(user.to_dict(), f)
        if input("Продолжать? (y/n): ").lower() != "y":
            break


def add_user_info(name, id, access_level):
    with open("data.json", "r") as f:
        data = json.load(f)
    user = User(name, id, access_level)
    data.append(user.to_dict())
    with open("data.json", "w") as f:
        json.dump(data, f)


if __name__ == "__main__":
    add_user_info("Dave", 555, 1)
    add_user_info("Alice", 111, 2),
    add_user_info("Bob", 222, 1),
    add_user_info("Charlie", 333, 0),
    add_user_info("Eve", 444, 1)
    # main()
