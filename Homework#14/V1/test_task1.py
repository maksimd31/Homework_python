import json
import pytest
from task1 import User, Project


@pytest.fixture
def project():
    proj = Project()
    user1 = User("Alice", "123", 2)
    user2 = User("Bob", "456", 1)
    proj.add_user(user1)
    proj.add_user(user2)
    return proj


def test_login(project):
    assert project.login("Alice", "123") == 2
    assert project.login("Bob", "456") == 1
    with pytest.raises(Exception):
        project.login("Charlie", "789")


def test_add_user(project):
    user3 = User("Charlie", "789", 0)
    with pytest.raises(Exception):
        project.add_user(user3)
    user4 = User("David", "101112", 1)
    project.add_user(user4)
    assert user4 in project.users
