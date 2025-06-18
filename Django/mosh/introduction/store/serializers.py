from decimal import Decimal
from rest_framework import serializers
from .models import Cart, CartItem, Collection, OrderItem, Product, Review

class CollectionSerializer(serializers.ModelSerializer):
    '''This is collection serializer for GET method(a simple test for getting a list of products in django-rest-framework)\n
    we will use this serializer aim to show relational collection object in products view! collection = {id and title}\n
    Also, this model serializer class will be defined for Generic view of collection's list and apis
    '''

    # annotate() will put product_count into each instance, so we expose it read-only
    product_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Collection
        fields = ['id', 'title', 'product_count']

    def create(self, validated_data):
        return super().create(validated_data)

class OrderSerializer(serializers.Serializer):
    '''This is order's serializer for GET method(a simple test for getting a list of ordered products in django-rest-framework)'''
    placed_at = serializers.DateTimeField()
    payment_status = serializers.CharField()

class ProductsCollectionSerializer(serializers.Serializer):
    '''This is collection serializer for GET method(a simple test for getting a list of products in django-rest-framework)\n
    we will use this serializer aim to show relational collection object in products view! collection = {id and title}'''
    collection = CollectionSerializer()

class ProductSerializer(serializers.Serializer):
    '''This is products serializer for GET method(a simple test for getting a list of products in django-rest-framework)'''
    id = serializers.IntegerField()
    title = serializers.CharField(max_length = 255)
    #source and renaming in serializers
    price = serializers.DecimalField(max_digits=6, decimal_places=2,source= 'unit_price')
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    collection = CollectionSerializer()

    def calculate_tax(self, product:Product):
        ''' This serializable method will implement taz calculation over serialized product's unit_price
        '''
        return product.unit_price * Decimal(1.15)
    
class ProductModelSerializer(serializers.ModelSerializer):
    '''This is a product's model serializer class for GET method(a simple test for getting a list of products in django-rest-framework)'''

    class Meta:
        model = Product
        fields = ['id','title', 'collection', 'unit_price', 'price_with_tax','inventory', 'last_update']
    
    #source and renaming in serializers
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    collection = CollectionSerializer()

    def calculate_tax(self, product:Product):
        ''' This serializable method will implement taz calculation over serialized product's unit_price
        '''
        return product.unit_price * Decimal(1.15)
    
    def create(self, validated_data):
        return super().create(validated_data)

class OrderedItemModelSerializer(serializers.Serializer):
    '''This is an ordered item's model serializer class for GET method(a simple test for getting a list of ordered products in django-rest-framework)'''
    
    order = OrderSerializer()
    product = ProductSerializer()
    price = serializers.DecimalField(max_digits=6, decimal_places=2,source= 'unit_price')
    ordered_count = serializers.DecimalField(max_digits=6, decimal_places=2,source= 'quantity')
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    final_price = serializers.SerializerMethodField(method_name='calculate_final_price')

    def calculate_tax(self, order:OrderItem):
        ''' This serializable method will implement taz calculation over serialized product's unit_price
        '''
        return order.unit_price * Decimal(1.15) 
    
    def calculate_final_price(self, order:OrderItem):
        ''' This serializable method will implement taz calculation over serialized product's unit_price
        '''
        return self.calculate_tax(order=order) * Decimal(order.quantity)
    
class ProductPostModelSerializer(serializers.ModelSerializer):
    """
    Serializer used exclusively for POST requests to
    `./store/products/all/`.

    * Accepts all writeable Product fields plus an optional list of
      promotion IDs.
    * Adds a read-only `price_with_tax` that returns the unit price
      with a flat 10 % tax applied.  Change the multiplier if your
      local tax rate differs.
    """
    
    class Meta:
        model = Product
        fields = ['id','title','slug','description','unit_price','inventory','collection','price_with_tax']
    
    price_with_tax = serializers.SerializerMethodField(
        method_name='calculate_tax'
    )

    def calculate_tax(self, product: Product) -> Decimal:
        """
        Return unit_price * 1.10  (i.e. add 10 % tax).
        """
        return product.unit_price * Decimal('1.10')
    
class ProductUpdateModelSerializer(serializers.ModelSerializer):
    """
    Used for PUT / PATCH requests on a single product.
    Mirrors the writable fields of ProductPostModelSerializer but
    overrides update() so we can replace the many-to-many
    promotions relation cleanly. (in future ...)
    """
    
    class Meta:
        model = Product
        fields = ['id','title','slug','description','unit_price','inventory','collection']

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        return instance

class ReviewModelSerializer(serializers.ModelSerializer):
    '''This is a product's reviews model serializer class for GET method(a simple test for getting a list of products in django-rest-framework)'''

    class Meta:
        model = Review
        fields = ['id','name', 'description', 'product', 'date']
    
class CartItemSerializer(serializers.ModelSerializer):
    '''This is a cart items model serializer class for GET method'''
    product = ProductModelSerializer()
    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity']

class CartModelSerializer(serializers.ModelSerializer):
    '''This is a cart's model serializer class for POST, GET method'''
    id = serializers.UUIDField(read_only = True)
    items = CartItemSerializer(many = True, read_only = True)
    class Meta:
        model = Cart
        fields = ['id', 'items']

