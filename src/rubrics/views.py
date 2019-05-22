from django.shortcuts import get_object_or_404, render
from django.views import View


from .models import Rubric
from .forms import RubricEditForm

import pandas as pd
import numpy as np


class RubricaView(View):

	def get(self, request, rubrica_id, user_type):
		rubrica = get_object_or_404(Rubric, pk=rubrica_id)
		rubrica_df = rubrica.as_csv()
		form = RubricEditForm(instance=rubrica, rubrica_df = rubrica_df, id = rubrica_id)

		context = {'rubrica_id' : rubrica_id,
					'user_type' : user_type,
					'form'		: form}
		return render(request, 'rubrics/rubrica.html', context)

	def post(self, request, rubrica_id):
		form = RubricEditForm(request.POST)
		if form.is_valid():
			rubrica_df = form.to_df()
			return redirect("{}/admin", rubrica_id=rubrica_id, user_type="admin")
		return

class RubricaEditView(View):

	def post(self, request, rubrica_id, ):
		form = RubricEditForm(instance=rubrica, rubrica_df = rubrica_df, id = rubrica_id)
