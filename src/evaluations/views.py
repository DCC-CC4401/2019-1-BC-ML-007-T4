from django.shortcuts import render, get_object_or_404
from presentations.models import Grade
from .models import Evaluation
from django.db.models.query import QuerySet

from django.views import View

# Create your views here.


def evaluations_page(request, *args):
    
    if request.user.is_staff:
        evaluaciones=  Evaluation.objects.all()
        return render(request, "evaluations.html",{'evaluaciones':evaluaciones})
    else:
        userid = request.user.id
        grades = Grade.objects.filter(evaluator_id = userid)[:10] #All grades for the evaluator
        context = {
            'obj' : grades
        }
        return render(request, "evaluations.html", context)

def newEvaluationView(request):
	try:
		old_id = Evaluation.objects.latest('id').id
	except ObjectDoesNotExist:
		old_id = 0
	new_id = old_id +  1
	evaluation = Evaluation(id=new_id)
	evaluation.save()
	return redirect("rubrics:view", rubric_id=new_id)