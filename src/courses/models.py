from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator

# Create your models here.

class Course(models.Model):
    
    owner = models.ForeignKey("users.BaseUser", null=True, on_delete=models.SET_NULL)
    code = models.CharField(max_length=7, validators=[
        RegexValidator(regex=r'^[A-Z]{1,2}[0-9]{1,4}[A-Z]{0,1}$')
    ])
    year = models.PositiveSmallIntegerField(validators=[
        MaxValueValidator(3000),
        MinValueValidator(1999)
    ])
    semester = models.PositiveSmallIntegerField(validators=[
        MaxValueValidator(2),
        MinValueValidator(1)
    ])
    section = models.PositiveSmallIntegerField(validators=[
        MinValueValidator(1)
    ])
    name = models.CharField(max_length=60)

    def __str__(self):
        string_semester = ""
        if self.semester == 1:
            string_semester = "Primavera"
        else:
            string_semester = "Otoño"
        return self.code + "-" + str(self.section) + " " + string_semester + "-" + str(self.year)

    class Meta:

        unique_together = (("code", "year", "semester", "section"),)

class Group(models.Model):

    course = models.ForeignKey("courses.Course", on_delete=models.CASCADE)
    number = models.PositiveSmallIntegerField(validators=[
        MinValueValidator(1)
    ])
    name = models.CharField(max_length=60)

    def __str__(self):
        return str(self.course) + ": " + str(self.number)

    class Meta:

        unique_together = (("course", "number"),)

class Student(models.Model):

    courses = models.ManyToManyField("courses.Course")
    groups = models.ManyToManyField("courses.Group")
    name = models.CharField(max_length=100)
    rut = models.CharField(max_length=10, validators=[
        RegexValidator(regex=r'^[0-9]{1,8}-[0-9,K]{1}$')
    ])

    def __str__(self):
        return self.name
