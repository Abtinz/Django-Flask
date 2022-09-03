from django.http import Http404
from django.shortcuts import render , HttpResponse
from .models import Clube

def home(request): return render(request , 'clubs_app/home.html' )

def clubs_table(request):
    clubs = Clube.objects.all()
    return render(request , 'clubs_app/football_club_tables.html' ,  context={'clubs':clubs})

def club_information(request,club_name):
        club = Clube.objects.get(name = club_name)
        return render(request , 'clubs_app/football_club_profile.html' ,  context={'club':club})


def new_football_club(request): 
    club_name = request.GET.get('clubs_name')
    foundation_date = request.GET.get('foundation_date')
    clubs_league = request.GET.get('clubs_league')
    clubs_rank = request.GET.get('clubs_rank')
    clubs_country = request.GET.get('clubs_country')

    if club_name and foundation_date and clubs_league and clubs_rank and clubs_country: 
        Clube.objects.create( name = club_name ,
            foundation_date = foundation_date ,
            league_title = clubs_league ,
             rank = clubs_rank ,
            country = clubs_country
        )
    return render(request , 'clubs_app/add_club.html')

        

    