from datetime import datetime

import pytest
from model_bakery import baker

from {{cookiecutter.main_app}}.models import {{cookiecutter.main_model}}
from {{cookiecutter.main_app}}.services import {{cookiecutter.main_model|lower}}_service


def test_should_get_{{cookiecutter.main_model|lower}}_as_pending(db):
    my_{{cookiecutter.main_model|lower}} = baker.make({{cookiecutter.main_model}}, description='Create an ansible deploy script', due_to=datetime.now())

    assert my_{{cookiecutter.main_model|lower}}.status == 'pending'


def test_should_get_{{cookiecutter.main_model|lower}}_as_done(db):
    my_{{cookiecutter.main_model|lower}} = baker.make({{cookiecutter.main_model}}, description='Create an ansible deploy script', due_to=datetime.now())

    {{cookiecutter.main_model|lower}}_updated = {{cookiecutter.main_model|lower}}_service.mark_as_done(my_{{cookiecutter.main_model|lower}}.id)

    assert {{cookiecutter.main_model|lower}}_updated.status == 'done'


def test_should_raise_an_erro_for_invalid_{{cookiecutter.main_model|lower}}_id(db):
    invalid_{{cookiecutter.main_model|lower}} = 0
    with pytest.raises(RuntimeError) as error:
        {{cookiecutter.main_model|lower}} = {{cookiecutter.main_model|lower}}_service.mark_as_done(invalid_{{cookiecutter.main_model|lower}})

    assert str(error.value) == f"{{cookiecutter.main_model}} ID: {invalid_{{cookiecutter.main_model|lower}}} invalida"


def test_should_mark_as_undone(db):
    my_{{cookiecutter.main_model|lower}} = baker.make(
        {{cookiecutter.main_model}},
        description='Create an ansible deploy script',
        due_to=datetime.now(),
        done=True)

    {{cookiecutter.main_model|lower}}_updated = {{cookiecutter.main_model|lower}}_service.mark_as_done(my_{{cookiecutter.main_model|lower}}.id)

    assert {{cookiecutter.main_model|lower}}_updated.status == 'pending'
