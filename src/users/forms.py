from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import BaseUser

# Create your forms here.

class BaseUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = BaseUser
        fields = ('username', 'email')

class BaseUserChangeForm(UserChangeForm):

    class Meta:
        model = BaseUser
        fields = ('username', 'email')