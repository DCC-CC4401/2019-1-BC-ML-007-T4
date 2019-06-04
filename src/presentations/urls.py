from django.urls import path

from .views import evaluation_form_page, update_context_view, upload_grade

app_name = 'presentations'
urlpatterns = [
    path('evaluar/<int:evaluation_id>/<int:group_id>', evaluation_form_page, name='form'),
    path('evaluar/<int:evaluation_id>/<int:group_id>/subir_nota', upload_grade, name='upload_grade'),
    path('evaluar/<int:evaluation_id>/<int:group_id>/update_context', update_context_view, name='ajax_update'),
]
