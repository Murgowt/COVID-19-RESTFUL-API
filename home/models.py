from django.db import models

# Create your models here.

class world(models.Model):
    total_cases = models.IntegerField()
    deaths = models.IntegerField()
    recovered = models.IntegerField()
    active = models.IntegerField()

class countries(models.Model):
    country=models.CharField(max_length=20)
    total_cases = models.IntegerField()
    deaths = models.IntegerField()
    recovered = models.IntegerField()
    active = models.IntegerField()
    new_cases=models.IntegerField()
    new_deaths=models.IntegerField()

class states(models.Model):
    state = models.CharField(max_length=30)
    total_cases = models.IntegerField()
    deaths = models.IntegerField()
    recovered = models.IntegerField()

    
