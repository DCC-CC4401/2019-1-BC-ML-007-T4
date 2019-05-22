from django.db import models
import pandas as pd
import io

# Create your models here.

class Rubric(models.Model):
    name = models.TextField(max_length=50)
    table = models.TextField(max_length=2000)

    def to_df(self):
    	return pd.read_csv(io.StringIO(self.table), header=0, sep=',')

    def get_name(self):
    	return self.name

    def __str__(self):
    	return self.to_df().to_string()


