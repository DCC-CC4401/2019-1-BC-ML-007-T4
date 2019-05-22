from django.urls import path
from rubrics.views import RubricaView

from . import views

app_name = 'rubrica'
urlpatterns = [
    path('<int:rubrica_id>/<str:user_type>', RubricaView.as_view(), name='rubrica'),
]