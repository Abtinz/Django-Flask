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