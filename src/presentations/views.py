from django.shortcuts import render, get_object_or_404

from .models import Presentation, Grade

# Create your views here.

def evaluation_form_page(request, evaluation_id, group_id, *args):

    presentation = get_object_or_404(Presentation, evaluation_id=evaluation_id, group_id=group_id)

    evaluation = presentation.evaluation

    allowed_evaluators = presentation.allowed_evaluators.all()

    grades = presentation.grade_set.all()

    context = {
        "evaluation": presentation,
        "answered": grades,
    };

    return render(request, "evaluation_form.html", context);
