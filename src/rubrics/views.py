from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.views import View


from .models import Rubric
from .forms import RubricEntryForm, RubricAchForm, RubricNameForm

import pandas as pd
import numpy as np


class RubricaView(View):

	def get(self, request, rubrica_id, user_type):
		rubrica = get_object_or_404(Rubric, pk=rubrica_id)
		rubrica_df = rubrica.to_df()
		name_form = RubricNameForm({'name' : rubrica.get_name()});

		print(rubrica_df)

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
					'rubrica_id' : rubrica_id,
					'user_type' : user_type}
		return render(request, 'rubrics/rubrica.html', context)

	def post(self, request, rubrica_id, user_type):
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
			Rubric.objects.filter(pk=rubrica_id).update(table=df_csv)
			Rubric.objects.filter(pk=rubrica_id).update(name=new_name)
		
		return HttpResponseRedirect("") 
