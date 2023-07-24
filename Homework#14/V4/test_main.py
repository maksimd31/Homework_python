import pytest
from main import Project, User, ExceptionAccess, ExceptionLevel
import json
from pathlib import Path


@pytest.fixture
def project():
    yield Project.from_json_file('file.json')


def test_project(project):
    assert len(project.users) == 7


def test_enter(project):
    project.enter('John', 111)
    assert str(project.admin) == '1 111 John'


def test_enter_exception(project):
    with pytest.raises(ExceptionAccess):
        project.enter('Sara', 789)


def test_add_user(project):
    project.enter('John', 111)
    project.add_user('Alex', 999, 1)
    assert len(project.users) == 8


def test_add_user_exception(project):
    project.enter('John', 111)
    with pytest.raises(ExceptionLevel):
        project.add_user('Alex', 999, 2)


def test_remove_user(project):
    project.enter('John', 111)
    project.remove_user(753)
    assert len(project.users) == 6


def test_exit(project):
    project.enter('John', 111)
    with project:
        pass
    with open('users.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    assert len(data['1']) == 2

