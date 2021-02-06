from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic import TemplateView, ListView, View
from django.http import HttpResponse

from .models import {{ cookiecutter.main_model }}
from .forms import {{ cookiecutter.main_model }}ModelForm, BasicForm
from .services import {{ cookiecutter.main_model|lower }}_service


def index(request):
    return HttpResponse("Hello, world. You're at the index.")


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



class {{ cookiecutter.main_model }}DoneView(View):

    def get(self, request, *args, **kwargs):
        {{ cookiecutter.main_model|lower }}_service.mark_as_done(self.kwargs.get('pk'))
        return redirect(reverse("{{ cookiecutter.main_app }}.{{ cookiecutter.main_model|lower }}.list"))
