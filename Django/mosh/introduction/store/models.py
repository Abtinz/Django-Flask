from django.db import models

class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()

class Collection(models.Model):
    title = models.CharField(max_length=255)
    featured_product = models.ForeignKey(
        'Product', on_delete=models.SET_NULL, null=True, related_name='+')
    #note :  related_name='+' -> will help us to avoid from conflicts after building reverse relation in products class

class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)
    promotions = models.ManyToManyField(Promotion)

class Customer(models.Model):

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

    class Meta:
        db_table = "store_customers"
        indexes = [
            models.Index(fields= ['last_name', 'first_name'])
        ]

class Order(models.Model):

    ORDER_STATUS_DEFAULT = "p"
    ORDER_STATUS_POSSIBLE_STATES = [
        (ORDER_STATUS_DEFAULT, "Pending"),
        ("C", "Completed"),
        ("F","Failed")
    ]

    placed_at = models.DateTimeField(auto_now_add=True)
    membership = models.CharField(max_length=1, choices=ORDER_STATUS_POSSIBLE_STATES, default= ORDER_STATUS_DEFAULT)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    #Why we have a repetitive price of product for each order item? because product's prices can get changed by the time, we need to keep a constant value for user 
    #who had added the product before its getting alternations
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)

class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    #one to many relationship by declaring customer as a foreign key for address entity to the Django(we have multiple addresses for one user)
    customer = models.ForeignKey( Customer, on_delete=models.CASCADE)

class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
