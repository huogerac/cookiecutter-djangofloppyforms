from django.views.generic import TemplateView
from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from . import forms


urlpatterns = [
    path('', TemplateView.as_view(template_name="{{ cookiecutter.main_app }}/index.html"), name='{{ cookiecutter.main_app }}.index'),

    # LOGIN
    path(
        'login', auth_views.LoginView.as_view(
            template_name='{{ cookiecutter.main_app }}/login.html',
            authentication_form=forms.LoginForm,
        ), name='{{ cookiecutter.main_app }}.login'),
    path(
        'login/success', TemplateView.as_view(
            template_name='{{ cookiecutter.main_app }}/login_success.html',
        ), name='{{ cookiecutter.main_app }}.login_success'),

    # GET STARTED
    path('getstarted', TemplateView.as_view(template_name="{{ cookiecutter.main_app }}/getstarted.html"), name='{{ cookiecutter.main_app }}.getstarted'),
    path('basic_form', views.BasicFormView.as_view(), name='{{ cookiecutter.main_app }}.basic_form'),

    # CRUD
    path('{{ cookiecutter.main_model|lower }}/list', views.{{ cookiecutter.main_model }}ListView.as_view(), name="{{ cookiecutter.main_app }}.{{ cookiecutter.main_model|lower }}.list"),
    path('{{ cookiecutter.main_model|lower }}/create', views.{{ cookiecutter.main_model }}CreateView.as_view(), name="{{ cookiecutter.main_app }}.{{ cookiecutter.main_model|lower }}.create"),
    path('{{ cookiecutter.main_model|lower }}/update/<pk>', views.{{ cookiecutter.main_model }}UpdateView.as_view(), name='{{ cookiecutter.main_app }}.{{ cookiecutter.main_model|lower }}.update'),
    path('{{ cookiecutter.main_model|lower }}/delete/<pk>', views.{{ cookiecutter.main_model }}DeleteView.as_view(), name='{{ cookiecutter.main_app }}.{{ cookiecutter.main_model|lower }}.delete'),

    path('new/', views.New{{ cookiecutter.main_app|capitalize }}.as_view(), name='{{ cookiecutter.main_app }}.new'),
    path('update/<pk>', views.New{{ cookiecutter.main_app|capitalize }}Model.as_view(), name='{{ cookiecutter.main_app }}.update'),
]
