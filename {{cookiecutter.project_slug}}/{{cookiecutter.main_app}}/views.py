from django.shortcuts import render
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic import TemplateView, ListView
from django.http import HttpResponse

from .models import {{ cookiecutter.main_model }}
from .forms import {{ cookiecutter.main_app|capitalize }}Form, {{ cookiecutter.main_model }}ModelForm, BasicForm


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class New{{ cookiecutter.main_app|capitalize }}(FormView):
    template_name = '{{ cookiecutter.main_app }}/new_{{ cookiecutter.main_app }}.html'
    form_class = {{ cookiecutter.main_app|capitalize }}Form


class BasicFormView(FormView):
    template_name = '{{ cookiecutter.main_app }}/basic_form.html'
    form_class = BasicForm


class {{ cookiecutter.main_model }}ListView(ListView):

    model = {{ cookiecutter.main_model }}
    paginate_by = '100'
    context_object_name = '{{ cookiecutter.main_model|lower }}_list'
    template_name = '{{ cookiecutter.main_app }}/{{ cookiecutter.main_model|lower }}_list.html'

    def get_context_data(self, **kwargs):
        context = super({{ cookiecutter.main_model }}ListView, self).get_context_data(**kwargs)
        project = self.request.GET.get('project')
        context['project'] = project
        return context

    def get_queryset(self):
        project = self.request.GET.get('project')
        if not project:
            return {{ cookiecutter.main_model }}.objects.all()
        return {{ cookiecutter.main_model }}.objects.filter(project=project)


class {{ cookiecutter.main_model }}UpdateView(UpdateView):
    model = {{ cookiecutter.main_model }}
    form_class = {{ cookiecutter.main_model }}ModelForm
    context_object_name = '{{ cookiecutter.main_model|lower }}'
    template_name = '{{ cookiecutter.main_app }}/{{ cookiecutter.main_model|lower }}_form.html'

    def get_success_url(self):
        return reverse("{{ cookiecutter.main_app }}.{{ cookiecutter.main_model|lower }}.list")


class {{ cookiecutter.main_model }}CreateView(CreateView):
    model = {{ cookiecutter.main_model }}
    form_class = {{ cookiecutter.main_model }}ModelForm
    context_object_name = '{{ cookiecutter.main_model|lower }}'
    template_name = '{{ cookiecutter.main_app }}/{{ cookiecutter.main_model|lower }}_form.html'

    def get_success_url(self):
        return reverse("{{ cookiecutter.main_app }}.{{ cookiecutter.main_model|lower }}.list")

class {{ cookiecutter.main_model }}DeleteView(DeleteView):
    model = {{ cookiecutter.main_model }}
    form_class = {{ cookiecutter.main_model }}ModelForm
    context_object_name = '{{ cookiecutter.main_model|lower }}'
    template_name = '{{ cookiecutter.main_app }}/{{ cookiecutter.main_model|lower }}_delete_form.html'

    def get_success_url(self):
        return reverse("{{ cookiecutter.main_app }}.{{ cookiecutter.main_model|lower }}.list")



class New{{ cookiecutter.main_app|capitalize }}Model(UpdateView):
    model = {{ cookiecutter.main_model }}
    form_class = {{ cookiecutter.main_model }}ModelForm
    template_name = '{{ cookiecutter.main_app }}/new_{{ cookiecutter.main_app }}_model.html'
    context_object_name = '{{ cookiecutter.main_model|lower }}'
