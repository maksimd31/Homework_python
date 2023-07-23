import json
import pytest
from io import StringIO

from main import User, Project, main


@pytest.fixture
def project():
    return Project()


@pytest.fixture
def users():
    return [
        User("Alice", 111, 2),
        User("Bob", 222, 1),
        User("Charlie", 333, 0),
        User("Eve", 444, 1)
    ]


@pytest.fixture
def data():
    return [
        {"name": "Alice", "id": 111, "access_level": 2},
        {"name": "Bob", "id": 222, "access_level": 1},
        {"name": "Charlie", "id": 333, "access_level": 0},
        {"name": "Eve", "id": 444, "access_level": 1}
    ]


def test_load_data(project, users, data):
    with StringIO(json.dumps(data)) as f:
        project.load_data(f)
    assert project.users == set(users)


def test_login(project, users):
    for user in users:
        project.users.add(user)
    assert project.login("Alice", 111) == 2
    assert project.login("Eve", 444) == 1
    with pytest.raises(Exception):
        project.login("Mallory", 555)


def test_add_user(project):
    project.add_user(User("Alice", 111, 2))
    with pytest.raises(Exception):
        project.add_user(User("Bob", 222, 1))
    with pytest.raises(Exception):
        project.add_user(User("Charlie", 333, 0))
    with pytest.raises(Exception):
        project.add_user(User("Eve", 444, 1))


def test_main(monkeypatch):
    inputs = ["Alice", "111", "2", "y", "Bob", "222", "1", "n"]
    monkeypatch.setattr("builtins.input", lambda: inputs.pop(0))
    with open("data.json", "w") as f:
        f.write("[]")
    main()
    with open("data.json") as f:
        data = json.load(f)
    assert len(data) == 2
    assert data[0]["name"] == "Alice"
    assert data[1]["name"] == "Bob"
