from rest_framework import serializers
from .models import BloodBank, BloodBankPatient

#serializers are needed to using integrated relational models in database

class BloodBankSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodBank
        fields = ('__all__')

        
class BloodBankPatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodBankPatient
        fields = ('__all__')