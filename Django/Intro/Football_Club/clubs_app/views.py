from django.http import Http404
from django.shortcuts import render , HttpResponse
from .models import Clube
def home(request):
    return HttpResponse('welcom to football club app')

def clubs_table(request):
    clubs = Clube.objects.all()
    return render(request , 'clubs_app/football_club_tables.html' ,  context={'clubs':clubs})
def club_information(request,club_name):
        club = Clube.objects.get(name = club_name)
        return render(request , 'clubs_app/football_club_profile.html' ,  context={'club':club})
        

    