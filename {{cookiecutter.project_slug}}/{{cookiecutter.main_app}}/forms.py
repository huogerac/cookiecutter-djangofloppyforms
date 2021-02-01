# -*- coding: utf-8 -*-

from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm

import floppyforms.__future__ as forms
from floppyforms import widgets


from .models import {{ cookiecutter.main_model }}


class {{ cookiecutter.main_app|capitalize }}Form(forms.Form):
    description = forms.CharField()


class {{ cookiecutter.main_model }}ModelForm(forms.ModelForm):
    class Meta:
        model = {{ cookiecutter.main_model }}
        fields = ('description', 'due_to',)


class BasicForm(forms.Form):
    """
    TODO:--------------------------
    input           TextInput               OK
    inputN          NumberInput             OK
    inputEmail      EmailInput
    textarea        TextInput               OK
    drowpdown       Select                  OK
    drowpdown       SelectMultiple          OK
    checkbox        CheckboxInput
    checkbox2       MultiCheckbox?
    radiobox        RadioSelect
    date            DateInput
    time            TimeInput
    datetime        DateTimeInput
    """

    COLORS_CHOICES = [
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('black', 'Black'),
    ]

    name = forms.CharField(max_length=32, widget=widgets.TextInput())
    year = forms.IntegerField(widget=widgets.NumberInput())
    description = forms.CharField(max_length=32, widget=widgets.Textarea(attrs={'rows': '4'}))
    color = forms.ChoiceField(widget=widgets.Select(), choices=COLORS_CHOICES)
    colors = forms.MultipleChoiceField(widget=widgets.Select(attrs={'multiple': True}), choices=COLORS_CHOICES)
    is_boolean = forms.CharField(max_length=32, widget=widgets.CheckboxInput())
    option = forms.ChoiceField(widget=widgets.RadioSelect(), choices=COLORS_CHOICES)
    is_not_boolean = forms.CharField(max_length=32, widget=widgets.CheckboxInput())
    option_again = forms.CharField(max_length=32, widget=widgets.CheckboxInput())

    def __init__(self, *args, **kwargs):
        super(BasicForm, self).__init__(*args, **kwargs)
        self.fields["year"].initial = 2021


class LoginForm(AuthenticationForm, forms.Form):
    """
    Override the default authentication
    """
    message_incorrect_password = "Usuário ou senha inválida"
    message_inactive = "Usuário está inativo"

    username = forms.CharField(max_length=76, 
                    widget=widgets.TextInput(attrs={'placeholder': 'Email or Username'}))
    password = forms.CharField(widget=widgets.PasswordInput(attrs={'placeholder': 'Password'}))

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            self.user_cache = authenticate(username=username, password=password)
            if (self.user_cache is None):
                raise forms.ValidationError(self.message_incorrect_password)
            if not self.user_cache.is_active:
                raise forms.ValidationError(self.message_inactive)
        return self.cleaned_data
