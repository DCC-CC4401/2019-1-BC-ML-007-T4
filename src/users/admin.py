from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import BaseUserCreationForm, BaseUserChangeForm
from .models import BaseUser

# Register your models here.

class BaseAdmin(UserAdmin):

    add_form = BaseUserCreationForm
    form = BaseUserChangeForm
    model = BaseUser
    list_display = ['email', 'username',]

admin.site.register(BaseUser, BaseAdmin)
