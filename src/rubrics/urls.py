from django.urls import path
from rubrics.views import RubricaView, newRubricaView, DelRubricaView

from . import views

app_name = 'rubrica'
urlpatterns = [
    path('<int:rubrica_id>', RubricaView.as_view(), name='rubrica'),
    path('new', newRubricaView, name='new_rubrica'),
    path('<int:pk>/delete', DelRubricaView.as_view(), name='del_rubrica')
]