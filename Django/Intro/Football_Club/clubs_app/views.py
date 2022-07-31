from django.http import Http404
from django.shortcuts import render , HttpResponse

def home(request):
    return HttpResponse('welcom to football club app')

def clubs_table(request):
    raise Http404

def club_information(request,club_name):
        return HttpResponse(f'{club_name} Club')

    