""" Forms definitions for users app """
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """ docstring """
    class Meta(UserCreationForm):
        """ docstring """
        model = CustomUser
        fields = ('username', 'email', 'age',)


class CustomUserChangeForm(UserChangeForm):
    """ docstring """
    class Meta:
        """ docstring """
        model = CustomUser
        fields = ('username', 'email', 'age',)
