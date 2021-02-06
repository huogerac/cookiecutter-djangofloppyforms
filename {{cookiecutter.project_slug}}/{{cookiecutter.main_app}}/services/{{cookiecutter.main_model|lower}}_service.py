from {{ cookiecutter.main_app }}.models import {{ cookiecutter.main_model }}


def mark_as_done({{ cookiecutter.main_model|lower }}_id):
    {{ cookiecutter.main_model|lower }} = {{ cookiecutter.main_model }}.objects.filter(id={{ cookiecutter.main_model|lower }}_id).first()
    if not {{ cookiecutter.main_model|lower }}:
        raise RuntimeError(f"{{ cookiecutter.main_model }} ID: {% raw %}{{% endraw %}{{ cookiecutter.main_model|lower }}_id{% raw %}}{% endraw %} invalida")

    {{ cookiecutter.main_model|lower }}.done = not {{ cookiecutter.main_model|lower }}.done
    {{ cookiecutter.main_model|lower }}.save()
    return {{ cookiecutter.main_model|lower }}
