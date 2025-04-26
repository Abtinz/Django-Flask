from django.db import models

# Create your models here.

class Product(models):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits= 6,decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)

class Customer(models):

    MEMBERSHIP_DEFAULT = "B"
    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_DEFAULT, "Bronze"),
        ("S", "Silver"),
        ("G","Gold")
    ]

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique = True)
    phone = models.CharField(max_length=25)
    birth_date = models.DateField(null=True)
    membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES, default= MEMBERSHIP_DEFAULT)

class Order(models):

    ORDER_STATUS_DEFAULT = "p"
    ORDER_STATUS_POSSIBLE_STATES = [
        (ORDER_STATUS_DEFAULT, "Pending"),
        ("C", "Completed"),
        ("F","Failed")
    ]

    placed_at = models.DateTimeField(auto_now_add=True)
    membership = models.CharField(max_length=1, choices=ORDER_STATUS_POSSIBLE_STATES, default= ORDER_STATUS_DEFAULT)

