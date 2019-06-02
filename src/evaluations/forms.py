from django import forms
import pandas as pd

class RubricCriterionForm(forms.Form):
	'''
	Forma para elegir los niveles de logro de una rúbrica. Cada fila es una selección, donde se
	elige el nivel de logro.
	'''
	def __init__(self, *args, **kwargs):
		tabla_df = kwargs.pop('table') # Obtener la tabla

	    super(RubricCriterionForm, self).__init__(*args, **kwargs)

	    puntajes = tabla_df.columns.values[1:]
	    for rowindex, crit in tabla_df.iterrows()
	   		# Crear un campo de elección para cada fila de la rubrica
	   		fieldname = crit[0] # Primera columna es el nombre del criterio

	   		choices = []
	   		for index, nlogro in  enumerate(crit[1:]):
	   			choices.append((puntajes[index], nlogro)) # (puntaje, name)
	    	self.fields[fieldname] = ChoiceField(choices = choices, widget=forms.Select)