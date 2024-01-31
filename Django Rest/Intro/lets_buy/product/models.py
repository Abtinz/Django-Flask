from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length = "200", unique = True)
    original_price = models.FloatField()
    discount = models.FloatField()
    
