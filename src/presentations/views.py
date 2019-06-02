from django.shortcuts import render, get_object_or_404

from .models import Presentation

# Create your views here.

def evaluation_form_page(request, evaluation_id, group_id, *args):

    context = {
        "evaluation": get_object_or_404(Presentation, evaluation_id=evaluation_id, group_id=group_id),
    };

    return render(request, "evaluation_form.html", context);
