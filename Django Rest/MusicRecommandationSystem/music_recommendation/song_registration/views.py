from django.shortcuts import render
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView

from song_registration.tasks import music_recognition, process_music_recognition
from .models import SongRequests
from .serializers import SongRequestsSerializer,AddSongRequestsSerializer
from music_recommendation.S3_helper import upload_to_server ,create_song_url
import requests
from rest_framework import generics , status
from music_recommendation.mailgun import mailgun_service

class MusicRequestView(generics.CreateAPIView):
    serializer_class=AddSongRequestsSerializer
    queryset=SongRequests.objects.all()
    def post(self,request):

        #receiving the email of user from json form
        request_data={
            "email":request.data["email"]
        }

        serializer=SongRequestsSerializer(data=request_data)
        #check if the data is valid
        if(serializer.is_valid()):

            #now we need to save and upload our data to Dbas and S3 cloud services
            
            serializer.save()
            song_request=serializer.data

            #uploading the request and song to the server
            request_id =song_request['id']
            song_file=request.data['song_file']

            print(request_id)
            print(song_file)
            
            #saving the music file and request id in s3 cloud
            url = upload_to_server(music_file = song_file,song_id = request_id)

            if(url):
                #saving the s3 file url
                add=SongRequests.objects.get(id=request_id)
                add.song_url =f"https://music-recommander.storage.iran.liara.space/{request_id}"
                add.save()
                
                #process_music_recognition.delay(request_id)
                music_recognition(request_id)
                #sending confirmation email
                mailgun_service(email = "abtinzandi@gmail.com" , message= "hi, your request is registered successfully")

                return Response({"message": "your request is registered successfully"}, status=200)
                
            else:
                return Response({"message": "some errors from cloud systems"}, status=500)
        else:
            return Response({"message": "please complete the fields"}, status=400)


#this api vie will help user to find specific url of song request api
class RegisterApiMainView(APIView):
    
    def get(self,request):
       
        return Response({"warning": "song register system url: https://music-recommender-cloud.liara.run/register/song/"}, status=300)
    
class GetSongRequestsView(generics.RetrieveAPIView):

    serializer_class=SongRequestsSerializer
    queryset=SongRequests.objects.all()
    
    '''
    this method will show our song requests status and their data
        args -> id is needed for finding the song trough the database query
    '''
    def get(self,request,id):
       
        add=get_object_or_404(SongRequests,id=id)
        serializer=SongRequestsSerializer(add)
        data=serializer.data
        if(data['status']=="done"):
            return Response(data,status=status.HTTP_200_OK)
        elif (data['status']=="pending"):
            return Response({"message":"song recognition is pending"},status=status.HTTP_202_ACCEPTED)
        elif (data['status']=="ready"):
            return Response({"message":"song ID is ready, recommendation system started!"},status=status.HTTP_202_ACCEPTED)
        
        return Response({"message":"your song recognition is rejected"},status=status.HTTP_403_FORBIDDEN)
