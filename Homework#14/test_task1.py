import pytest

from task1 import User, Project


@pytest.fixture
def project():
    project = Project()
    project.load_data("data.json")
    return project


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
