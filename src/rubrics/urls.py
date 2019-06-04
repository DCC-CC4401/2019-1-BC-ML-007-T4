from django.urls import path
from .views import RubricView, newRubricView, DeleteRubricView, RubricCopyView

from . import views

app_name = 'rubrics'
urlpatterns = [
    path('new', newRubricView, name='new'),
    path('<int:rubric_id>', RubricView.as_view(), name='view'),
    path('<int:pk>/delete', DeleteRubricView.as_view(), name='delete'),
    path('<int:rubric_id>/<int:eval_id>/copy', RubricCopyView.as_view(), name='copy')
]