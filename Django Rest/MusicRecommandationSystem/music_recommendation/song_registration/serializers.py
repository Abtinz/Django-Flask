
from rest_framework import serializers
from .models import SongRequests

#this serializer will be used for building the request for data base storages
class SongRequestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SongRequests
        fields = '__all__'

#this serializer will help us to process requests
class AddSongRequestsSerializer(serializers.Serializer):
    email = serializers.EmailField()
    song_file = serializers.FileField()