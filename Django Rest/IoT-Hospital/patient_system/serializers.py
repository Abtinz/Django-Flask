from rest_framework import serializers
from .models import PatientsModel, HospitalBedsModels

#serializers are needed to using integrated relational models in database
class HospitalBedsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HospitalBedsModels
        fields = ('__all__')

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientsModel
        fields = ('__all__')