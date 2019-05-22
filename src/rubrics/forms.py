from django import forms
from .models import Rubric

class RubricEditForm(forms.ModelForm):

	class Meta:
		model = Rubric
		fields = ['table']

	def __init__(self, *args, **kwargs):
		self.rubrica_df = kwargs.pop('rubrica_df')
		self.rubrica_id = kwargs.pop('id')
		super(RubricEditForm, self).__init__(*args, **kwargs)
		
		self.id = forms.CharField(max_length=100, widget=forms.HiddenInput(), initial=self.rubrica_id)
		self.fields['table'].widget = forms.HiddenInput()

		for col_index, points in enumerate(self.rubrica_df.columns.values):
			if col_index!=0:
				self.fields['nlogro_{}'.format(col_index)] = forms.FloatField(label=points, initial=points)

		for row_index, row in self.rubrica_df.iterrows():
			for col_index, entry in enumerate(row.array):
				self.fields['descripcion_{}_{}'.format(row_index,
													col_index)] = forms.CharField(max_length=50,
																	initial=entry, label=entry,
																	widget=	forms.Textarea())

	def get_nlogro(self):
	    return [self[name] for name in filter(lambda x: x.startswith('nlogro_'), self.fields)]

	def get_rows(self):
	    for row_index, row in self.rubrica_df.iterrows():
	    	row = [self[name] for name in filter(lambda x: x.startswith('descripcion_{}'.format(row_index)),
	    										self.fields)]
	    	yield row

	def to_df(self):
		datadir = self.cleaned_data()
		cols = ['-'] + [datadir[name] for name in filter(lambda x: x.startswith('nlogro_'), self.fields)]
		row_data = [data[name] for name in filter(lambda x: x.startswith('descripcion_'), self.fields)]
		
		df = DataFrame()