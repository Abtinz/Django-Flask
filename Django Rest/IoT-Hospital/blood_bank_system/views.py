from django.shortcuts import render
from .models import BloodBank, BloodBankPatient
from .serializers import  BloodBankSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['POST'])
def setBank(request):
    supply = request.data
    ser = BloodBankSerializer(data=supply)
    if ser.is_valid():
        ser.save()
        return Response({"completion": "Success"})
    else:
        print(ser.errors)
        return Response({"completion": "Failed"})
    
@api_view(['PUT'])
def AddPatient(request):
    type = request.data["group"]
    count = request.data["count"]
    bloods = BloodBank.objects.all()
    blood = bloods.filter(group=type).first()
    blood.supply = str(int(blood.quantity) + int(count))
    blood.save()
    ser = BloodBankSerializer(bloods, many=True)
    return Response(ser.data)

    
@api_view(['GET'])
def IsInCriticalMode(request):
    
    bloods = BloodBank.objects.all()
   
    for item in bloods:
        if item.quantity < 2:
            return Response({"critical": "True"})
    return Response({"critical": "False"})
