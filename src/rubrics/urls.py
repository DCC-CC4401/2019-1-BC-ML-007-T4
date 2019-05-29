from django.urls import path
from .views import RubricView, newRubricView, DeleteRubricView

from . import views

app_name = 'rubrics'
urlpatterns = [
    path('new', newRubricView, name='new'),
    path('<int:rubric_id>', RubricView.as_view(), name='edit'),
    path('<int:pk>/delete', DeleteRubricView.as_view(), name='delete')
]