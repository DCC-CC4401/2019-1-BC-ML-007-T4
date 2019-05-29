from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Presentation(models.Model):
    
    evaluation = models.ForeignKey("evaluations.Evaluation", on_delete=models.CASCADE)
    group = models.ForeignKey("courses.Group",on_delete=models.CASCADE)

    class Meta:

        unique_together = (("evaluation", "group"),)

class Grade(models.Model):   
    evaluator = models.ForeignKey("users.BaseUser", on_delete=models.CASCADE)
    presentation = models.ForeignKey("presentations.Presentation", on_delete=models.CASCADE)
    student = models.ForeignKey("courses.Student", on_delete=models.CASCADE)
    value = models.FloatField(validators=[
        MinValueValidator(1.0),
        MaxValueValidator(7.0)
    ])
    state = models.BooleanField(default=False)

    class Meta:
        unique_together = (("evaluator", "presentation", "student"),)
