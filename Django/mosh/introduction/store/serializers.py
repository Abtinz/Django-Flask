from decimal import Decimal
from rest_framework import serializers
from .models import Product

class CollectionSerializer(serializers.Serializer):
    '''This is collection serializer for GET method(a simple test for getting a list of products in django-rest-framework)\n
    we will use this serializer aim to show relational collection object in products view! collection = {id and title}'''
    id = serializers.IntegerField()
    title = serializers.CharField(max_length = 255)

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