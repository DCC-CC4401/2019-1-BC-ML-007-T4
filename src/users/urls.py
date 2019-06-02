from django.urls import path
from .views import registro_usuario, DeleteUserView, EditUserView

from . import views

app_name = 'users'
urlpatterns = [
    path('<int:pk>', EditUserView.as_view(), name='edit'),
    path('<int:pk>/delete', DeleteUserView.as_view(), name='delete')
]