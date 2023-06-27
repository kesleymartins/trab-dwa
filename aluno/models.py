from django.db import models

class Student(models.Model):
    situations = (
        (1, 'Cursando'),
        (2, 'Aprovado'),
        (3, 'Reprovado'),
    )

    name = models.CharField(max_length=100)
    entryPeriod = models.CharField(max_length=6)
    email = models.EmailField(max_length=100)
    frade = models.FloatField()
    situation = models.IntegerField(choices=situations, default=1)
