from django.db import models
from django.forms import DateField

# Create your models here.

class familiares(models.Model):

    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    dni=models.IntegerField(max_length=8)
    nacimiento=models.DateField()