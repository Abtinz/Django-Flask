from django.shortcuts import render,HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializers

# Create your views here.

class ProductViews(APIView):
    def get(self , request):
        queryset = Product.objects.all()
        serializer = ProductSerializers(queryset , many = True)
        return Response(serializer.data)
    
class SingleProductViews(APIView):

    def is_exist(self , id):
        try:
            queryset = Product.objects.get(id = id)
            return queryset
        except Product.DoesNotExist:
            pass
    
    def get(self , request, id):
        queryset = self.is_exist(id= id)
        if queryset:
            serializer = ProductSerializers(queryset)
            return Response(serializer.data)
        else:
            return Response({"message":"no items with this id ..."})