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
        fields = ['id','title', 'collection', 'price', 'price_with_tax','inventory', 'last_update']
    
    #source and renaming in serializers
    price = serializers.DecimalField(max_digits=6, decimal_places=2,source= 'unit_price')
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    collection = CollectionSerializer()

    def calculate_tax(self, product:Product):
        ''' This serializable method will implement taz calculation over serialized product's unit_price
        '''
        return product.unit_price * Decimal(1.15)