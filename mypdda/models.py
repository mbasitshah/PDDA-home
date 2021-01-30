from django.db import models

# Create your models here.

class Results(models.Model):
    PlantName = models.CharField(max_length=200, null=True)
    Condition = models.CharField(max_length=200, null=True)
    DiseaseName = models.CharField(max_length=200, null=True)
    Medicines = models.CharField(max_length=200, null=True)
    Precautions = models.CharField(max_length=200, null=True)
