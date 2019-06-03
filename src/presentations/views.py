from django.shortcuts import render, get_object_or_404

from .models import Presentation, Grade

# Create your views here.

def evaluation_form_page(request, evaluation_id, group_id, *args):

    presentation: Presentation = get_object_or_404(Presentation, evaluation_id=evaluation_id, group_id=group_id)

    presentators = presentation.presentators

    evaluation: Evaluation = presentation.evaluation

    allowed_evaluators_set = presentation.allowed_evaluators.all()

    allowed_evaluators = []

    group_members = presentation.group.student_set.all()

    group_member_statuses = []

    grades = presentation.grade_set.all()

    answered = grades.filter(state=True, evaluator=request.user).count() == grades.filter(evaluator=request.user).count()

    for evaluator in allowed_evaluators_set:

        evaluator_answered_grades = grades.filter(state=True, evaluator=evaluator, presentation=presentation).count()

        evaluator_total_grades = grades.filter(evaluator=evaluator, presentation=presentation).count()

        evaluator_expected_grades = presentators.all().count()

        if evaluator_total_grades != evaluator_expected_grades:
            evaluator_status = "pending"
        elif evaluator_answered_grades != evaluator_expected_grades:
            evaluator_status = "evaluating"
        else:
            evaluator_status = "done"

        allowed_evaluators.append((evaluator.username, evaluator_status))

    context = {
        "allowed_evaluators": allowed_evaluators,
        "group_members": group_members,
        "presentation": presentation,
        "answered": answered,
    };

    return render(request, "evaluation_form.html", context);
