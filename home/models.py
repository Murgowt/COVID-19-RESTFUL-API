from django.db import models

# Create your models here.

class world(models.Model):
    total_cases=models.IntegerField()
    deaths=models.IntegerField()
    recovered=models.IntegerField()
    active=models.IntegerField()

    