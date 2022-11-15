from django import forms
from django.db import models
from .models import Login


class LoginForm(forms.ModelForm):
   class Meta:
        model=Login
        fields="__all__"