from django.shortcuts import render
from presentations.models import *
# Create your views here.


def evaluations_page(request, *args):
    return render(request, "evaluations.html")
