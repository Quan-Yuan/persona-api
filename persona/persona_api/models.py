from django.db import models
from django.contrib.postgres.fields import ArrayField
from itertools import product

BLOOD_TYPES = [(t + p, t + p) for t, p in product(['A', 'B', 'AB', 'O'], '+-')]
SEX = [('M', 'Male'), ('F', 'Female')]


class Persona(models.Model):
    job = models.TextField(null=True)
    company = models.TextField(null=True)
    ssn = models.TextField(null=True)
    residence = models.TextField(null=True)
    current_location = ArrayField(
        models.FloatField(),
        size=2,
        null=True
    ),
    blood_type = models.TextField(choices=BLOOD_TYPES, null=True)
    website = ArrayField(models.TextField(), null=True)
    username = models.TextField(primary_key=True)
    name = models.TextField(null=True)
    sex = models.CharField(null=True, max_length=1, choices=SEX)
    address = models.TextField(null=True)
    mail = models.EmailField(null=True)
    birthdate = models.DateField(null=True)

    class Meta:
        ordering = ["username"]
