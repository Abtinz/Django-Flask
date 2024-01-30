from django.db import models

# Create your models here.

from django.db import models

class HospitalBedsModels(models.Model):
    bedId = models.CharField(max_length=100)
    totalCapacity = models.CharField(max_length=100)

    def __str__(self):
        return self.bedId


class PatientsModel(models.Model):
    name = models.CharField(max_length=50)
    bed = models.ForeignKey(HospitalBedsModels, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
        
