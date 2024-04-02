from django.urls import path 
from .views import MusicRequestView , RegisterApiMainView, GetSongRequestsView

urlpatterns = [

    path("song/", MusicRequestView.as_view(), name='song'),
    path("",RegisterApiMainView.as_view(), name='register'),
    path("song/requests/<int:id>", GetSongRequestsView.as_view(), name='get-song-requests'),

]