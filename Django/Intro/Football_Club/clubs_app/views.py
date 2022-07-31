from django.http import Http404
from django.shortcuts import render , HttpResponse

def home(request):
    return HttpResponse('welcom to football club app')

def clubs_information(request):
    raise Http404