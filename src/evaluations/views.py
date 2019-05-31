from django.shortcuts import render
from presentations.models import *
from .models import Evaluation
from django.db.models.query import QuerySet

# Create your views here.


def evaluations_page(request, *args):
    if request.user.is_staff:
        return render(request, "evaluations.html")
    else:
        userid = request.user.id
        grades = Grade.objects.filter(evaluator_id = userid)[:10] #All grades for the evaluator
        context = {
            'obj' : grades
        }
        return render(request, "evaluations.html", context)
