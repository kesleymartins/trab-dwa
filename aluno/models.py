from django.db import models
from .enums import Situation

class Student(models.Model):
    name = models.CharField(max_length=100)
    entryPeriod = models.CharField(max_length=6)
    email = models.EmailField(max_length=100)
    grade = models.FloatField()

    situation = models.CharField(
        choices=[(tag.value, tag.value) for tag in Situation], 
        default=Situation.APROVADO, 
        max_length=100
    )
