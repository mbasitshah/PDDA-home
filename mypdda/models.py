from django.db import models


# Create your models here.

class Results(models.Model):
    PlantName = models.CharField(max_length=200, null=True)
    Condition = models.CharField(max_length=200, null=True)
    DiseaseName = models.CharField(max_length=200, null=True)
    Medicines = models.CharField(max_length=200, null=True)
    Precautions = models.CharField(max_length=200, null=True)


class Medicines(models.Model):
    Id = models.integer(max_length=20, null=True)
    Name = models.charField(max_length=200, null=True)
    condition = models.charField(max_length=20, null=True)


class Precautions(models.Model):
    Id = models.integerField(max_length=20, null=True)
    Name = models.charField(max_length=200, null=True)
