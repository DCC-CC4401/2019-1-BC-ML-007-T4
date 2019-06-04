from django import forms
from .models import Evaluation

class EvaluationsForm(forms.ModelForm):

    class Meta:
        model = Evaluation
        fields = [
            "course",
            "rubric"
        ]        