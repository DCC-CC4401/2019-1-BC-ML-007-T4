from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest
from presentations.models import Grade
from .models import Evaluation
from courses.models import Course
from rubrics.models import Rubric
from presentations.models import Presentation
from django.db.models.query import QuerySet
from .forms import EvaluationsForm

from django.views import View

# Create your views here.


def evaluations_page(request: HttpRequest, *args):
    
    if request.user.is_staff:
        evaluaciones=  Evaluation.objects.all()
        if(request.method == "POST"):
            form = EvaluationsForm(request.POST)
            if form.is_valid():
                post = form.save(commit=True)
                post.save()
                course: Course = Evaluation.objects.get(id=post.id).course
                for group in course.group_set.all():
                    Presentation.objects.create(evaluation=Evaluation.objects.get(id=post.id), group=group)
            
        else:
            form = EvaluationsForm()
        return render(request, "evaluations.html",{'evaluaciones': evaluaciones, 'form' : form})
    else:
        userid = request.user.id  
        grades = Grade.objects.filter(evaluator_id = userid)[:10] #All grades for the evaluator     
        context = {
            'obj' : grades
        }
        return render(request, "evaluations.html", context)

