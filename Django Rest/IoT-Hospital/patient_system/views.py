from django.shortcuts import render
from .models import PatientsModel, HospitalBedsModels
from .serializers import PatientSerializer, HospitalBedsSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['POST'])
def SetBedsCount(request,num):
    number = int(num)
    success = "Ture"

    for i in range(number):
        bed = {
            "bedId": str(i),
            "totalCapacity": "1"
        }
        ser = HospitalBedsSerializer(data=bed)
        if ser.is_valid():
            ser.save()
        else:
            success = "False"
            print(ser.errors)

    return Response({"completion": f"{success}"})


@api_view(['GET'])
def BedsCounts(request):
    beds = HospitalBedsModels.objects.all()
    beds = beds.filter(totalCapacity='1')
    ser = HospitalBedsSerializer(beds, many=True)
    return Response(ser.data)


@api_view(['POST'])
def AddPatient(request,name):
    beds = HospitalBedsModels.objects.all()
    beds = beds.filter(totalCapacity='1')
    if not beds:
        return Response({"completion": "Failed"})

    assignedBed = beds.first()
    bedId = assignedBed.id
    assignedBed.totalCapacity = '0'
    patient = {
        "name": name,
        "bed": bedId
    }
    ser = PatientSerializer(data=patient)
    if ser.is_valid():
        ser.save()
        return Response({"completion": "Success"})
    else:
        print(ser.errors)
        return Response({"completion": "Failed"})

@api_view(['DELETE'])
def DeletePatient(request, name):
    print(name)
    patients = PatientsModel.objects.all()
    patient = patients.filter(name=name)
    if not patient:
        return Response({"completion": "Failed"})
    beds = HospitalBedsModels.objects.all()
    bed = beds.filter(bedId=str(patient.first().bed))
    bed = bed.first()
    bed.totalCapacity = '1'
    bed.save()
    patient.delete()
    return Response({"completion": "Successful"})
