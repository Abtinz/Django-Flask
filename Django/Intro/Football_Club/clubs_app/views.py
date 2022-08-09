from django.http import Http404
from django.shortcuts import render , HttpResponse
from .models import Clube
def home(request):
    return HttpResponse('welcom to football club app')

def clubes_table(request):
    raise Http404

def clube_information(request,club_name):
        clubes = Clube.objects.all()
        if club_name in clubes:
            return render(request , 'clubs_app/football_club_profile.html' ,  context={'club':Clube.objects.get(name = club_name)})
        #else :

    