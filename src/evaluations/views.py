from django.shortcuts import render

# Create your views here.

def evaluations_page(request, *args):
    
    return render(request, "evaluations.html");
