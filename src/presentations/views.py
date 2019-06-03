from django.shortcuts import render, get_object_or_404

from .models import Presentation, Grade
from .forms import EvaluationCriterionForm

# Create your views here.

def evaluation_form_page(request, evaluation_id, group_id, *args):
    presentation: Presentation = get_object_or_404(Presentation, evaluation_id=evaluation_id, group_id=group_id)

    presentators = presentation.presentators.all()

    evaluation: Evaluation = presentation.evaluation

    all_presentations = evaluation.presentation_set.all()

    allowed_evaluators_set = presentation.allowed_evaluators.all()

    group_members = presentation.group.student_set.all()

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

    # Constructs the group members' info, including their presentation statuses
    group_member_statuses = []

    for group_member in group_members:
        
        group_member_status = "pending"

        for other_presentation in all_presentations:
            if other_presentation != presentation and grades.filter(presentation=other_presentation, student=group_member).count() != 0:
                group_member_status = "done"
                break

        group_member_statuses.append((group_member.name, group_member_status))

    # Obtener la tabla asociada a la rubrica
    rubrica = evaluation.rubric
    rubrica_df = rubrica.to_df()

    criterion_form = EvaluationCriterionForm(table=rubrica_df)

    context = {
        "allowed_evaluators": allowed_evaluators,
        "group_members": group_member_statuses,
        "presentation": presentation,
        "criterion_form" : criterion_form
    }

    return render(request, "evaluation_form.html", context);
