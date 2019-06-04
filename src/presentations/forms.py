from django import forms
import pandas as pd

from .models import Presentation

class EvaluationDurationForm(forms.Form):
  duracion = forms.DecimalField(max_digits=3, widget=forms.NumberInput(attrs={
                        'class' : "w3-input w3-border w3-round",
                        'size'  : "1",
                        'style' : "width:20%; display:inline; margin-left: 5%",
                        'id'  : 'duration-input',
                        'required' : 'true'
    }))

class EvaluationCriterionForm(forms.Form):
    '''
    Forma para elegir los niveles de logro de una rúbrica. Cada fila es una selección, donde se
    elige el niveltext = forms.CharField(max_length=50, widget=forms.Textarea())
  col = forms.IntegerField()
  row = forms.IntegerField() de logro.
    '''
    def __init__(self, *args, **kwargs):
        tabla_df = kwargs.pop('table') # Obtener la tabla

        super(EvaluationCriterionForm, self).__init__(*args, **kwargs)

        puntajes = tabla_df.columns.values[1:]
        for rowindex, crit in tabla_df.iterrows():
            # Crear un campo de elección para cada fila de la rubrica
           fieldname = crit[0] # Primera columna es el nombre del criterio
           choices = []
           for index, nlogro in  enumerate(crit[1:]):
               choices.append((puntajes[index], nlogro)) # (puntaje, name)
           self.fields[fieldname] = forms.ChoiceField(label=fieldname, choices = choices,
                                                     widget=CriterionWidg)
           self.fields[fieldname].widget.attrs.update({'label' : fieldname})

class CriterionWidg(forms.RadioSelect):
    '''
    Widget para mostrar un criterio y sus niveles de logro
    '''
    template_name = 'criterions/select_criterion.html'
    option_template_name = 'criterions/select_criterion_option.html'

class EvaluatorsListForm(forms.ModelForm):

    class Meta:
        model = Presentation
        fields = ["allowed_evaluators"]

class PresentatorsListForm(forms.ModelForm):

    class Meta:
        model = Presentation
        fields = ["presentators"]
