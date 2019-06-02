from django.db import models

# Create your models here.

class Evaluation(models.Model):

    rubric = models.ForeignKey("rubrics.Rubric", null=True, on_delete=models.SET_NULL)
    course = models.ForeignKey("courses.Course", null=False, on_delete=models.CASCADE)
