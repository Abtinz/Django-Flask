from django.shortcuts import render,HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from .models import Product
from .serializers import ProductSerializers

# Create your views here.

class ProductViews(APIView):
    def get(self , request):
        queryset = Product.objects.all()
        serializer = ProductSerializers(queryset , many = True)
        return Response(serializer.data)
    
    def post(self , request):
        serializer = ProductSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status= status.HTTP_201_CREATED)
        else:
            return Response({"message":"please follow true json passing ..."},status=status.HTTP_400_BAD_REQUEST)

    
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
            return Response(
                {"message":"no items with this id ..."},
                status=status.HTTP_400_BAD_REQUEST
                )