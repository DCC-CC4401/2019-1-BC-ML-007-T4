from django.shortcuts import render, get_object_or_404

from .models import Evaluation

# Create your views here.


def evaluations_page(request, *args):
    
    return render(request, "evaluations.html");

def evaluation_form_page(request, evaluation_id, *args):

    context = {
        "evaluation": get_object_or_404(Evaluation, course_id=evaluation_id),
    };

    return render(request, "evaluation_form.html", context);
