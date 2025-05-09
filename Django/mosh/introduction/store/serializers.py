from decimal import Decimal
from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.Serializer):
    '''This is products serializer for GET method(a simple test for getting a list of products in django-rest-framework)'''
    id = serializers.IntegerField()
    title = serializers.CharField(max_length = 255)
    #source and renaming in serializers
    price = serializers.DecimalField(max_digits=6, decimal_places=2,source= 'unit_price')
    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')

    def calculate_tax(self, product:Product):
        ''' This serializable method will implement taz calculation over serialized product's unit_price
        '''
        return product.unit_price * Decimal(1.15)