from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic.edit import DeleteView, CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required, permission_required

from .models import Rubric
from evaluations.models import Evaluation
from .forms import RubricEntryForm, RubricAchForm, RubricNameForm, RubricDurationForm

import pandas as pd
import numpy as np


@login_required
def rubrics_page(request, *args):

	# TODO: Permitir ver solo si el usuario tiene el derecho
	rubric_ids = map(lambda x: x.get('id'), Rubric.objects.all().values('id'))
	rubric_names = map(lambda x: x.get('name'), Rubric.objects.all().values('name'))
	rubric_htmls = map(lambda x: x.to_df().to_html(index=False, classes="rubric_table", justify="left"), Rubric.objects.all())

	context = {
		"rubrics": zip(rubric_ids, rubric_names, rubric_htmls),
	}
	return render(request, "rubrics.html", context)

@login_required
@permission_required('rubrics.add_rubric')
def newRubricView(request):
	try:
		old_id = Rubric.objects.latest('id').id
	except ObjectDoesNotExist:
		old_id = 0
	new_id = old_id +  1
	rubrica = Rubric(id=new_id, name = "Rubrica {}".format(new_id),
				table="Criterio,6.0\nCriterio 1,nlogro1\n",
				duration_min=5., duration_max=10.)
	rubrica.save()
	return redirect("rubrics:view", rubric_id=new_id)

class RubricCopyView(PermissionRequiredMixin, LoginRequiredMixin, View):
	'''
	Vista responsable de crear una copia para la edición de una rúbrica asociada a una
	evaluación dada
	'''
	permission_required = 'rubrics.add_rubric'
	def post(self, request, rubric_id, eval_id):
		rubrica = get_object_or_404(Rubric, pk=rubric_id)
		name = "Rubrica {} de evaluacion {}".format(rubric_id, eval_id)
		# Si ya hice esto antes, solo ver la rubrica
		print(name, rubrica.name)
		if name==rubrica.name:
			return redirect("rubrics:view", rubric_id=rubric_id)
		# Crear una copia con el nombre nuevo
		rubrica_new = Rubric(name = name,
					table=rubrica.table,
					duration_min=rubrica.duration_min, duration_max=rubrica.duration_max)
		rubrica_new.save()
		# Reasignar la rubrica de esta evaluación a la neuva rubrica
		Evaluation.objects.filter(pk=eval_id).update(rubric=rubrica_new)

		return redirect("rubrics:view", rubric_id=rubrica_new.id)

class RubricView(LoginRequiredMixin, View):

	def get(self, request, rubric_id):
		rubrica = get_object_or_404(Rubric, pk=rubric_id)
		rubrica_df = rubrica.to_df()
		name_form = RubricNameForm({'name' : rubrica.get_name()})
		time_form = RubricDurationForm(
			{'duration_min' : rubrica.duration_min,
			'duration_max' : rubrica.duration_max})

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
					'time_form' : time_form,
					'rubrica_id' : rubric_id,
					'duration_min' : rubrica.duration_min,
					'duration_max' : rubrica.duration_max}

		if request.user.has_perm('rubrics.change_rubric'):
			return render(request, 'rubrics/rubric_editor.html', context)
			
		# TODO: Permitir ver solo si el usuario tiene el derecho
		return render(request, 'rubrics/rubric_view.html', context)

	def post(self, request, rubric_id):
		if not request.user.has_perm('rubrics.edit_rubric'):
			return HttpResponseForbidden()
		nlogros = np.array(request.POST.getlist('nlogro'))
		data = np.array(request.POST.getlist('text'))

		cols = np.append(['Criterio'], nlogros)

		ncols = cols.size
		nrows = int(data.size/ncols)
		rows = [data[ncols*i:ncols*(i+1)] for i in range(0, nrows)]

		name_form = RubricNameForm(request.POST)
		time_form = RubricDurationForm(request.POST)

		if name_form.is_valid() and time_form.is_valid():
			new_name = name_form.cleaned_data['name']
			dmin = time_form.cleaned_data['duration_min']
			dmax = time_form.cleaned_data['duration_max']
			df = pd.DataFrame(rows, columns=cols)
			df_csv = df.to_csv(None, sep=',', index=False)

			Rubric.objects.filter(pk=rubric_id).update(table=df_csv)
			Rubric.objects.filter(pk=rubric_id).update(name=new_name)
			Rubric.objects.filter(pk=rubric_id).update(duration_min=dmin, duration_max=dmax)


		return HttpResponseRedirect("")



class DeleteRubricView(PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
	model = Rubric
	success_url = reverse_lazy('Rubrics Page')
	success_message = "Rubrica Borrada"
	permission_required = 'rubrics.del_rubric'
