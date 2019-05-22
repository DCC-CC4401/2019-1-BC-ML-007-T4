from django import forms
from .models import Rubric


class RubricEntryForm(forms.Form):
	text = forms.CharField(max_length=50, widget=forms.Textarea())
	col = forms.IntegerField()
	row = forms.IntegerField()



class RubricAchForm(forms.Form):
	nlogro = forms.FloatField()
	col = forms.IntegerField()

class RubricNameForm(forms.Form):
	name = forms.CharField(max_length=50, required=True)
