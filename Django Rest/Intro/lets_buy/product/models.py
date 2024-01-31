from django.db import models
from django.core.validators import MaxValueValidator , MinValueValidator

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length = "200", unique = True)
    original_price = models.FloatField()
    discount = models.IntegerField(
        default  = 0,
        validators = [MinValueValidator(0), MaxValueValidator(100)]
    )

