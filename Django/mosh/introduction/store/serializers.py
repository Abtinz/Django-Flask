from rest_framework import serializers


class ProductSerializer(serializers.Serializer):
    '''This is products serializer for GET method(a simple test for getting a list of products in django-rest-framework)'''
    id = serializers.IntegerField()
    title = serializers.CharField(max_length = 255)
    unit_price = serializers.DecimalField(max_digits=6, decimal_places=2)