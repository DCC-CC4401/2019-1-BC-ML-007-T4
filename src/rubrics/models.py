from django.db import models
import pandas as pd
import io

# Create your models here.

class Rubric(models.Model):
    table = models.TextField(max_length=2000)

    def as_csv(self):
    	return pd.read_csv(io.StringIO(self.table), header=0, sep=',')

    def __str__(self):
    	return self.as_csv().to_string()


