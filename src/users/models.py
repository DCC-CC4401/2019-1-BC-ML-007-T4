from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class BaseUser(AbstractUser):

    allowed_as_evaluator_in = models.ForeignKey("evaluations.Evaluation", null=True, on_delete=models.SET_NULL)

    def __str__(self):

        return self.get_username()
