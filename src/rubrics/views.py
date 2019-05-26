from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic.edit import DeleteView, CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist

from .models import Rubric
from .forms import RubricEntryForm, RubricAchForm, RubricNameForm

import pandas as pd
import numpy as np


def rubrics_page(request, *args):
	return render(request, "rubrics.html", {})

def newRubricView(request):
	try:
		old_id = Rubric.objects.latest('id').id
	except ObjectDoesNotExist:
		old_id = 0
	new_id = old_id +  1
	rubrica = Rubric(id=new_id, name = "Rubrica {}".format(new_id), table=",1.0\nCriterio 1,nlogro1\n")
	rubrica.save()
	return redirect("rubrics:edit", rubric_id=new_id)

class RubricView(View):

	def get(self, request, rubric_id):
		rubrica = get_object_or_404(Rubric, pk=rubric_id)
		rubrica_df = rubrica.to_df()
		name_form = RubricNameForm({'name' : rubrica.get_name()});

		nlogro_forms = []
		for index, points in enumerate(rubrica_df.columns.values):
			if index!=0: nlogro_forms.append(RubricAchForm({'col' : index, 'nlogro' : points}))

		rows_forms = []
		for row_index, row_forms in rubrica_df.iterrows():
			row = []
			for col_index, entry in enumerate(row_forms):
				row.append(RubricEntryForm({'row' : row_index, 'col' : col_index, 'text' :entry}))
			rows_forms.append(row)

		context = {	'rows_forms' : rows_forms,
					'nlogro_forms': nlogro_forms,
					'name_form' : name_form,
					'rubrica_id' : rubric_id}
		return render(request, 'editor/rubric_editor.html', context)

	def post(self, request, rubric_id):
		nlogros = np.array(request.POST.getlist('nlogro'))
		data = np.array(request.POST.getlist('text'))

		cols = np.append([''], nlogros)

		ncols = cols.size
		nrows = int(data.size/ncols)
		rows = [data[ncols*i:ncols*(i+1)] for i in range(0, nrows)]

		name_form = RubricNameForm(request.POST)

		if name_form.is_valid():
			new_name = name_form.cleaned_data['name']
			df = pd.DataFrame(rows, columns=cols)
			df_csv = df.to_csv(None, sep=',', index=False)
			Rubric.objects.filter(pk=rubric_id).update(table=df_csv)

			Rubric.objects.filter(pk=rubric_id).update(name=new_name)

		return HttpResponseRedirect("")

class DeleteRubricView(SuccessMessageMixin, DeleteView):
	model = Rubric
	success_url = reverse_lazy('Rubrics Page')
	success_message = "deleted..."
