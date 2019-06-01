from django.urls import path
from .views import registro_usuario, DeleteUserView

from . import views

app_name = 'users'
urlpatterns = [
    #path('<int:rubric_id>', RubricView.as_view(), name='edit'),
    path('<int:pk>/delete', DeleteUserView.as_view(), name='delete')
]