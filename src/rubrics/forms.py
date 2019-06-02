from django import forms
from .models import Rubric
import pandas as pd


class RubricEntryForm(forms.Form):
	'''
	Forma para una entrada de la rubrica, para la interfaz de edicion.
	'''
	text = forms.CharField(max_length=50, widget=forms.Textarea())
	col = forms.IntegerField()
	row = forms.IntegerField()

class RubricAchForm(forms.Form):
	'''
	Forma para una celda de puntaje de algún nivel de logro, para la interfaz de edicion.
	'''
	nlogro = forms.FloatField()
	col = forms.IntegerField()

class RubricNameForm(forms.Form):
	'''
	Forma para el nombre de la rúbrica.
	'''
	name = forms.CharField(max_length=50, required=True)

