from django.contrib import admin
from .models import {{ cookiecutter.main_model }}

class {{ cookiecutter.main_model }}Admin(admin.ModelAdmin):
    pass

admin.site.register({{ cookiecutter.main_model }}, {{ cookiecutter.main_model }}Admin)