from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import BaseUser

# Create your forms here.

class BaseUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = BaseUser
        fields = ['first_name', 'last_name', 'email', 'username']
        labels = {
            'first_name': 'nombre',
            'last_name': 'apellido',
            'email': 'email',
            'username': 'username'
        }

class BaseUserChangeForm(UserChangeForm):

    class Meta:
        model = BaseUser
        fields = ('username', 'email')
