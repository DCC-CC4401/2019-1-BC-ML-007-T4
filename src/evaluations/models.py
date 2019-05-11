from django.db import models

# Create your models here.

class Evaluation(models.Model):

    rubric = models.ForeignKey("rubrics.Rubric", null=True, on_delete=models.SET_NULL)
    course = models.OneToOneField("courses.Course", primary_key=True, on_delete=models.CASCADE)
