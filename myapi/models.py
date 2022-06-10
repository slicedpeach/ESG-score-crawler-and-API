from pickle import NONE
from django.db import models

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=200)
    ric = models.CharField(max_length=200)
    rank = models.CharField(max_length=200)
    esgscore = models.IntegerField(max_length=100)
    environmental = models.IntegerField(max_length=100)
    social = models.IntegerField(max_length=100)
    governance = models.IntegerField(max_length=100)
    
    def __str__(self):
        return self.name

