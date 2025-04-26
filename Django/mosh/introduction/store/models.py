from django.db import models


class Promotion(models.Model):
    """
    A marketing offer that can be applied to one or many products.

    Fields
    -------
    description : str  
        Short human-readable label, e.g. “Holiday Sale – 15 % off”.

    discount : float  
        Discount value (percentage or fixed amount, depending on
        how your business logic interprets it).  Validation such as
        “0 ≤ discount ≤ 1” should be enforced higher up (form /
        serializer level).
    """
    description = models.CharField(max_length=255)
    discount = models.FloatField()


class Collection(models.Model):
    """
    A logical group of products (e.g. “Winter Jackets”).

    `featured_product` is optional and uses `related_name='+'` so
    Django will **not** create a reverse relation on `Product`,
    avoiding any naming conflicts there.
    """
    title = models.CharField(max_length=255)
    featured_product = models.ForeignKey(
        'Product',
        on_delete=models.SET_NULL,
        null=True,
        related_name='+'
    )  # note: related_name='+' -> will help us to avoid from conflicts ...


class Product(models.Model):
    """
    A sellable item that appears in your store’s catalogue.

    Important design notes
    ----------------------
    * `unit_price` is the *current* price; historical prices are
      snap-shotted onto `OrderItem.unit_price` at checkout time.
    * `last_update` auto-refreshes on each save, allowing cheap
      cache-invalidation checks.
    * Many-to-many `promotions` lets one product participate in
      several active sales without extra join tables.
    """
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)
    promotions = models.ManyToManyField(Promotion)


class Customer(models.Model):
    """
    End-user profile.

    `Meta` customisations  
    * `db_table` points to an existing legacy table.  
    * Composite index on (`last_name`, `first_name`) speeds up
      directory-like queries and admin search.
    """
    MEMBERSHIP_DEFAULT = "B"
    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_DEFAULT, "Bronze"),
        ("S", "Silver"),
        ("G", "Gold")
    ]

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=25)
    birth_date = models.DateField(null=True)
    membership = models.CharField(
        max_length=1,
        choices=MEMBERSHIP_CHOICES,
        default=MEMBERSHIP_DEFAULT
    )

    class Meta:
        db_table = "store_customer"
        indexes = [
            models.Index(fields=['last_name', 'first_name'])
        ]


class Order(models.Model):
    """
    Order header; individual products live in `OrderItem`.

    The `membership` field here actually stores the order *status*
    (Pending / Completed / Failed).  Keeping the existing field
    name avoids touching migrations you may already have.
    """
    ORDER_STATUS_DEFAULT = "p"
    ORDER_STATUS_POSSIBLE_STATES = [
        (ORDER_STATUS_DEFAULT, "Pending"),
        ("C", "Completed"),
        ("F", "Failed")
    ]

    placed_at = models.DateTimeField(auto_now_add=True)
    membership = models.CharField(
        max_length=1,
        choices=ORDER_STATUS_POSSIBLE_STATES,
        default=ORDER_STATUS_DEFAULT
    )
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)


class OrderItem(models.Model):
    """
    One line item inside an order.

    `unit_price` duplicates the product’s price at the moment of
    checkout, ensuring later price changes do not affect past
    orders.
    """
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    # Why we have a repetitive price of product for each order item? ...
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)


class Address(models.Model):
    """
    Shipping or billing address.  A customer can have many.

    `CASCADE` ensures addresses are deleted automatically when a
    customer gets removed.
    """
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    # one to many relationship by declaring customer as a foreign key ...
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)


class Cart(models.Model):
    """
    Shopping cart for anonymous or logged-in users.
    """
    created_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    """
    Product held in a cart prior to checkout.
    """
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
