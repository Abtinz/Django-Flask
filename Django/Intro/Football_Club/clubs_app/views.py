from django.http import Http404
from django.shortcuts import render , HttpResponse

def home(request):
    return HttpResponse('welcom to football club app')

def clubs_table(request):
    raise Http404

def club_information(request,club_name):
        return render(request , 'clubs_app/football_club_profile.html'  context={'club_name':club_name})

    