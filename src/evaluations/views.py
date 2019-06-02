from django.shortcuts import render, get_object_or_404
from presentations.models import Grade
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

def evaluation_form_page(request, evaluation_id, *args):

    context = {
        "evaluation": get_object_or_404(Evaluation, course_id=evaluation_id),
    };

    return render(request, "evaluation_form.html", context);
