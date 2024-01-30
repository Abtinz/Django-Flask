from django.db import models

# Create your models here.


class BloodBank(models.Model):
    group = models.CharField(max_length=2, unique=True)
    quantity = models.IntegerField()

class BloodBankPatient(models.Model):
    name = models.CharField(max_length=100)
    blood_group = models.CharField(max_length=2)
    daily_requirement = models.IntegerField()
    days_in_hospital = models.IntegerField()
