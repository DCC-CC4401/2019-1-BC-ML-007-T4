from django.urls import path

from .views import evaluation_form_page

app_name = 'presentations'
urlpatterns = [
    path('evaluar/<int:evaluation_id>/<int:group_id>', evaluation_form_page, name='form'),
]
