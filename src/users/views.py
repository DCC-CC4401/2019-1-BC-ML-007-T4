from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def landing_page(request, *args):

    return render(request, 'landing_page.html')

def evaluators_page(request, *args):

    return render(request, 'evaluators.html')
