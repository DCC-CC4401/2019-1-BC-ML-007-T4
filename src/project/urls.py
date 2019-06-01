"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views

from users.views import landing_page, evaluators_page, registro_usuario
from courses.views import courses_page
from evaluations.views import evaluations_page
from rubrics.views import rubrics_page

urlpatterns = [
    path('', landing_page, name="Landing Page"),
    path('cursos/', courses_page, name="Courses Page"),
    #path('evaluadores/', evaluators_page, name="Evaluators Page"),
    path('evaluadores/', registro_usuario.as_view(), name="Evaluators Page"),
    path('evaluadores/', include('users.urls'), name="Edit Users"),
    path('rubricas/', rubrics_page, name="Rubrics Page"),
    path('rubricas/', include('rubrics.urls'), name="Rubrics Editor"),
    path('evaluaciones/', evaluations_page, name="Evaluations Page"),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('admin/', admin.site.urls),
]
