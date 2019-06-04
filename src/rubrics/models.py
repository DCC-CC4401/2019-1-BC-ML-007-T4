from django.db import models
import pandas as pd
import io

# Create your models here.

class Rubric(models.Model):
    name = models.TextField(max_length=50)
    table = models.TextField(max_length=2000)
    duration_min = models.FloatField()
    duration_max = models.FloatField()

    def to_df(self):
    	return pd.read_csv(io.StringIO(self.table), header=0, sep=',')

    def get_name(self):
    	return self.name

    def __str__(self):
    	return self.name

    def get_absolute_url(self):
        return reverse('rubric:view', kwargs={'rubrica_id': self.pk})
