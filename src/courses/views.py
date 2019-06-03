from django.shortcuts import render
from .models import Course

# Create your views here.

def courses_page(request, *args):
    if request.user.is_staff==True:
        queryset = Course.objects.filter(owner = request.user)
        return render(request, 'courses.html', {'Courses':queryset})
    else:
        return render(request, 'landing_page.html')
