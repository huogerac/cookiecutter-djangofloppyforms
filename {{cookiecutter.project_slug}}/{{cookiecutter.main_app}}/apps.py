from django.apps import AppConfig


class {{ cookiecutter.main_app|capitalize }}Config(AppConfig):
    name = '{{ cookiecutter.main_app }}'
