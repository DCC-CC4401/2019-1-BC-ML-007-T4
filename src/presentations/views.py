from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpRequest

from .models import Presentation, Grade
from .forms import EvaluationCriterionForm, EvaluationDurationForm, EvaluatorsListForm

# Create your views here.

def evaluation_form_page(request: HttpRequest, evaluation_id: int, group_id: int, *args):
    presentation: Presentation = get_object_or_404(Presentation, evaluation_id=evaluation_id, group_id=group_id)

    presentators = presentation.presentators.all()

    evaluation: Evaluation = presentation.evaluation

    all_evaluations = evaluation.course.evaluation_set.all()
    all_presentations = []

    for other_evaluation in all_evaluations:
        for other_presentation in other_evaluation.presentation_set.all():
            all_presentations.append(other_presentation)

    allowed_evaluators_set = presentation.allowed_evaluators.all()

    group_members = presentation.group.student_set.all()

    grades = presentation.grade_set.all()

    all_grades = Grade.objects.filter(presentation__evaluation__course=evaluation.course)

    # Constructs the allowed evaluators' info, including their evaluation status
    allowed_evaluators = []

    for evaluator in allowed_evaluators_set:

        evaluator_answered_grades = 0
        evaluator_total_grades = 0

        for presentator in presentators:

            evaluator_answered_grades += grades.filter(state=True, evaluator=evaluator, presentation=presentation, student=presentator).count()

            evaluator_total_grades += grades.filter(evaluator=evaluator, presentation=presentation, student=presentator).count()

        evaluator_expected_grades = presentators.all().count()

        if evaluator_total_grades != evaluator_expected_grades:
            evaluator_status = "pending"
        elif evaluator_answered_grades != evaluator_expected_grades:
            evaluator_status = "evaluating"
        else:
            evaluator_status = "done"

        allowed_evaluators.append((evaluator.username, evaluator_status))

    # Constructs the group members' info, including their presentation statuses
    group_member_statuses = []

    for group_member in group_members:
        
        group_member_status = "pending"

        for other_presentation in all_presentations:
            if ((other_presentation.presentators.filter(name=group_member.name, rut=group_member.rut).count() != 0) and 
                (all_grades.filter(presentation=other_presentation, student=group_member, state=True).count() == other_presentation.allowed_evaluators.all().count())):
                group_member_status = "done"
                break

        group_member_statuses.append((group_member.name, group_member_status))

    current_presentators = []

    for presentator in presentators:

        current_presentators.append(presentator.name)

    
    # Obtener la tabla asociada a la rubrica, y sus datos
    rubrica = evaluation.rubric
    rubrica_df = rubrica.to_df()
    dmin = rubrica.duration_min
    dmax = rubrica.duration_max

    # forma para los criterios
    criterion_form = EvaluationCriterionForm(table=rubrica_df)

    # forma para el tiempo
    duration_form = EvaluationDurationForm()

    edit_evaluators_form = EvaluatorsListForm(instance=presentation)

    context = {
        "evaluation_status": evaluation.is_open,
        "group_name": presentation.group.name,
        "presentation_number": evaluation.id,
        "course": str(evaluation.course),
        "allowed_evaluators": allowed_evaluators,
        "group_members": group_member_statuses,
        "current_presentators": current_presentators,
        "criterion_form" : criterion_form,
        "duration_min" : dmin,
        "duration_max" : dmax,
        "duration_form" : duration_form,
        "edit_evaluators_form": edit_evaluators_form,
    }

    return render(request, "evaluation_form.html", context);

def update_context_view(request: HttpRequest, evaluation_id: int, group_id: int):
    
    context = {}

    if request.method == "POST":

        presentation: Presentation = get_object_or_404(Presentation, evaluation_id=evaluation_id, group_id=group_id)

        allowed_evaluators_set = presentation.allowed_evaluators.all()

        presentators = presentation.presentators.all()

        grades = presentation.grade_set.all()

        # Constructs the allowed evaluators' info, including their evaluation status
        allowed_evaluators = []

        for evaluator in allowed_evaluators_set:

            evaluator_answered_grades = 0
            evaluator_total_grades = 0

            for presentator in presentators:

                evaluator_answered_grades += grades.filter(state=True, evaluator=evaluator, presentation=presentation, student=presentator).count()

                evaluator_total_grades += grades.filter(evaluator=evaluator, presentation=presentation, student=presentator).count()

            evaluator_expected_grades = presentators.all().count()

            if evaluator_total_grades != evaluator_expected_grades:
                evaluator_status = "pending"
            elif evaluator_answered_grades != evaluator_expected_grades:
                evaluator_status = "evaluating"
            else:
                evaluator_status = "done"

            allowed_evaluators.append((evaluator.username, evaluator_status))

        context["allowed_evaluators"] = allowed_evaluators

        group_members = presentation.group.student_set.all()

        evaluation: Evaluation = presentation.evaluation

        context["evaluation_status"] = evaluation.is_open

        all_evaluations = evaluation.course.evaluation_set.all()
        all_presentations = []

        for other_evaluation in all_evaluations:
            for other_presentation in other_evaluation.presentation_set.all():
                all_presentations.append(other_presentation)

        all_grades = Grade.objects.filter(presentation__evaluation__course=evaluation.course)

        # Constructs the group members' info, including their presentation statuses
        group_member_statuses = []

        for group_member in group_members:
            
            group_member_status = "pending"

            for other_presentation in all_presentations:
                if ((other_presentation.presentators.filter(name=group_member.name, rut=group_member.rut).count() != 0) and 
                    (all_grades.filter(presentation=other_presentation, student=group_member, state=True).count() == other_presentation.allowed_evaluators.all().count())):
                    group_member_status = "done"
                    break

            group_member_statuses.append((group_member.name, group_member_status))

        context["group_members"] = group_member_statuses

        current_presentators = []

        for presentator in presentators:

            current_presentators.append(presentator.name)

        context["current_presentators"] = current_presentators

    return JsonResponse(context)
