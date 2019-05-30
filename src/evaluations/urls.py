from django.urls import path
from .views import evaluation_form_page

from . import views

app_name = 'evaluations'
urlpatterns = [
    path('evaluar/<int:evaluation_id>', evaluation_form_page, name='form'),
]