from django.shortcuts import render

from django.http import HttpResponse
from rubrics.models import Rubric
# Create your views here.

def landing_page(request, *args):
    queryset = Rubric.objects.all()[::-1]
    context = {
        "my_rubrics" : queryset
    }
    return render(request, 'landing_page.html',context)
