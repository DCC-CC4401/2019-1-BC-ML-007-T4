from django.urls import path
from .views import newEvaluationView

from . import views

app_name = 'evaluations'
urlpatterns = [
    path('new', newEvaluationView, name='new'),
]